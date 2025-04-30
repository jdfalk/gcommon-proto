// file: pkg/health/checks/redis.go
package checks

import (
	"context"
	"fmt"
	"strconv"
	"strings"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/health"
)

// RedisCheck is a health check that verifies connectivity to a Redis instance.
// It can optionally validate specific key patterns or perform custom commands.
type RedisCheck struct {
	*health.BaseCheck
	client          redis.UniversalClient // Redis client
	timeout         time.Duration         // Timeout for the Redis operations
	usePing         bool                  // Whether to use PING command for basic connectivity
	validateKeys    []string              // Optional keys to validate existence
	customCommands  []redisCommand        // Optional custom commands to execute
	threshold       time.Duration         // Threshold for slow operation warning
	maxMemoryUsage  float64               // Maximum memory usage in percentage (0-100)
	connectOnDemand bool                  // Whether to create a new connection for each check
	redisOptions    *redis.UniversalOptions // Redis connection options (for on-demand connection)
}

// redisCommand represents a custom Redis command to execute during the health check
type redisCommand struct {
	name  string            // Command name for reporting
	cmd   string            // The Redis command to execute
	args  []interface{}     // Command arguments
	check func(result interface{}, err error) error // Function to validate the result
}

// RedisCheckOption represents an option for a Redis health check.
type RedisCheckOption func(*RedisCheck)

// NewRedisCheck creates a new Redis health check.
// It verifies connectivity to a Redis instance and optionally performs additional checks.
func NewRedisCheck(client redis.UniversalClient, options ...RedisCheckOption) *RedisCheck {
	c := &RedisCheck{
		client:          client,
		timeout:         5 * time.Second,
		usePing:         true,
		validateKeys:    []string{},
		customCommands:  []redisCommand{},
		threshold:       1 * time.Second,
		maxMemoryUsage:  90.0,
		connectOnDemand: false,
		redisOptions:    nil,
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("redis", health.TypeDependency, c.timeout, 60*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the Redis health check.
func (c *RedisCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	// Create a context with timeout
	checkCtx, cancel := context.WithTimeout(ctx, c.timeout)
	defer cancel()

	startTime := time.Now()
	var client redis.UniversalClient

	// Determine which Redis client to use
	if c.connectOnDemand && c.redisOptions != nil {
		client = redis.NewUniversalClient(c.redisOptions)
		defer client.Close()
	} else if c.client != nil {
		client = c.client
	} else {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("no Redis client available")), nil
	}

	// Details for the check result
	details := map[string]interface{}{}

	// Check 1: Basic connectivity (PING)
	if c.usePing {
		pingStart := time.Now()
		pong, err := client.Ping(checkCtx).Result()
		pingDuration := time.Since(pingStart)

		details["ping"] = map[string]interface{}{
			"duration": pingDuration.String(),
		}

		if err != nil {
			details["ping"].(map[string]interface{})["error"] = err.Error()
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("Redis PING failed: %w", err)).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}

		if pong != "PONG" {
			details["ping"].(map[string]interface{})["response"] = pong
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("Redis PING returned unexpected response: %s", pong)).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}

		details["ping"].(map[string]interface{})["response"] = pong

		// Check for slow response
		if pingDuration > c.threshold {
			details["warning"] = fmt.Sprintf("Redis PING took longer than threshold (%s)", c.threshold)
			return health.NewResult(health.StatusDegraded).
				WithError(fmt.Errorf("Redis PING is slow: %s > %s", pingDuration, c.threshold)).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}
	}

	// Check 2: Validate keys if specified
	if len(c.validateKeys) > 0 {
		keyResults := make(map[string]interface{})
		keysFound := 0

		for _, keyPattern := range c.validateKeys {
			keysStart := time.Now()
			var keys []string

			// If the key contains wildcards, use SCAN to find matching keys
			if strings.ContainsAny(keyPattern, "*?[]") {
				iter := client.Scan(checkCtx, 0, keyPattern, 10).Iterator()
				for iter.Next(checkCtx) {
					keys = append(keys, iter.Val())
					if len(keys) >= 10 { // Limit the number of matched keys for performance
						break
					}
				}
				if err := iter.Err(); err != nil {
					keyResults[keyPattern] = map[string]interface{}{
						"error":    err.Error(),
						"duration": time.Since(keysStart).String(),
					}
					continue
				}
			} else {
				// For a specific key, just check if it exists
				exists, err := client.Exists(checkCtx, keyPattern).Result()
				if err != nil {
					keyResults[keyPattern] = map[string]interface{}{
						"error":    err.Error(),
						"duration": time.Since(keysStart).String(),
					}
					continue
				}
				if exists > 0 {
					keys = []string{keyPattern}
				}
			}

			keyResults[keyPattern] = map[string]interface{}{
				"found":    len(keys) > 0,
				"count":    len(keys),
				"duration": time.Since(keysStart).String(),
			}

			if len(keys) > 0 {
				keysFound++
			}
		}

		details["keys"] = keyResults

		// If no keys were found at all, consider the check degraded
		if keysFound == 0 && len(c.validateKeys) > 0 {
			return health.NewResult(health.StatusDegraded).
				WithError(fmt.Errorf("no required Redis keys found")).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}
	}

	// Check 3: Execute custom commands if specified
	if len(c.customCommands) > 0 {
		cmdResults := make(map[string]interface{})

		for _, cmd := range c.customCommands {
			cmdStart := time.Now()
			result, err := client.Do(checkCtx, cmd.cmd, cmd.args...).Result()
			cmdDuration := time.Since(cmdStart)

			cmdInfo := map[string]interface{}{
				"command":  fmt.Sprintf("%s %v", cmd.cmd, cmd.args),
				"duration": cmdDuration.String(),
			}

			if err != nil {
				cmdInfo["error"] = err.Error()
				cmdResults[cmd.name] = cmdInfo
				return health.NewResult(health.StatusDown).
					WithError(fmt.Errorf("Redis command '%s' failed: %w", cmd.name, err)).
					WithDuration(time.Since(startTime)).
					WithDetails(details), nil
			}

			// If a custom check function is provided, use it to validate the result
			if cmd.check != nil {
				if err := cmd.check(result, nil); err != nil {
					cmdInfo["error"] = err.Error()
					cmdInfo["result"] = fmt.Sprintf("%v", result)
					cmdResults[cmd.name] = cmdInfo
					return health.NewResult(health.StatusDown).
						WithError(fmt.Errorf("Redis command '%s' validation failed: %w", cmd.name, err)).
						WithDuration(time.Since(startTime)).
						WithDetails(details), nil
				}
			}

			cmdInfo["result"] = fmt.Sprintf("%v", result)
			cmdResults[cmd.name] = cmdInfo
		}

		details["commands"] = cmdResults
	}

	// Check 4: Memory usage if maxMemoryUsage is set
	if c.maxMemoryUsage > 0 {
		memStart := time.Now()
		info, err := client.Info(checkCtx, "memory").Result()
		memDuration := time.Since(memStart)

		if err != nil {
			details["memory"] = map[string]interface{}{
				"error":    err.Error(),
				"duration": memDuration.String(),
			}
		} else {
			memoryInfo := parseRedisMemoryInfo(info)
			details["memory"] = memoryInfo
			details["memory"].(map[string]interface{})["duration"] = memDuration.String()

			// Calculate memory usage percentage
			if memoryInfo["used_memory"] != nil && memoryInfo["maxmemory"] != nil {
				usedMemory, okUsed := memoryInfo["used_memory"].(int64)
				maxMemory, okMax := memoryInfo["maxmemory"].(int64)

				if okUsed && okMax && maxMemory > 0 {
					usagePercent := float64(usedMemory) / float64(maxMemory) * 100
					memoryInfo["usage_percent"] = usagePercent

					// Check if memory usage exceeds threshold
					if usagePercent > c.maxMemoryUsage {
						return health.NewResult(health.StatusDegraded).
							WithError(fmt.Errorf("Redis memory usage (%.1f%%) exceeds threshold (%.1f%%)",
								usagePercent, c.maxMemoryUsage)).
							WithDuration(time.Since(startTime)).
							WithDetails(details), nil
					}
				}
			}
		}
	}

	// All checks passed
	return health.NewResult(health.StatusUp).
		WithDuration(time.Since(startTime)).
		WithDetails(details), nil
}

// parseRedisMemoryInfo parses the Redis INFO MEMORY output into a structured map
func parseRedisMemoryInfo(info string) map[string]interface{} {
	result := make(map[string]interface{})

	// Split the INFO output into lines
	lines := strings.Split(info, "\r\n")

	for _, line := range lines {
		if strings.HasPrefix(line, "#") || line == "" {
			continue // Skip comments and empty lines
		}

		parts := strings.SplitN(line, ":", 2)
		if len(parts) != 2 {
			continue
		}

		key := strings.TrimSpace(parts[0])
		value := strings.TrimSpace(parts[1])

		// Try to convert numeric values
		if val, err := strconv.ParseInt(value, 10, 64); err == nil {
			result[key] = val
			continue
		}
		if val, err := strconv.ParseFloat(value, 64); err == nil {
			result[key] = val
			continue
		}

		// Otherwise keep as string
		result[key] = value
	}

	return result
}

// WithRedisTimeout sets the timeout for Redis operations.
func WithRedisTimeout(timeout time.Duration) RedisCheckOption {
	return func(c *RedisCheck) {
		if timeout > 0 {
			c.timeout = timeout
		}
	}
}

// WithRedisPing enables or disables the use of PING command for basic connectivity check.
func WithRedisPing(usePing bool) RedisCheckOption {
	return func(c *RedisCheck) {
		c.usePing = usePing
	}
}

// WithRedisKeyValidation adds keys or patterns to validate during the health check.
func WithRedisKeyValidation(keys ...string) RedisCheckOption {
	return func(c *RedisCheck) {
		c.validateKeys = append(c.validateKeys, keys...)
	}
}

// WithRedisCommand adds a custom command to execute during the health check.
func WithRedisCommand(name string, cmd string, args ...interface{}) RedisCheckOption {
	return func(c *RedisCheck) {
		c.customCommands = append(c.customCommands, redisCommand{
			name: name,
			cmd:  cmd,
			args: args,
		})
	}
}

// WithRedisCommandAndCheck adds a custom command with result validation.
func WithRedisCommandAndCheck(name string, cmd string, check func(result interface{}, err error) error, args ...interface{}) RedisCheckOption {
	return func(c *RedisCheck) {
		c.customCommands = append(c.customCommands, redisCommand{
			name:  name,
			cmd:   cmd,
			args:  args,
			check: check,
		})
	}
}

// WithRedisSlowThreshold sets the threshold for slow operation warnings.
func WithRedisSlowThreshold(threshold time.Duration) RedisCheckOption {
	return func(c *RedisCheck) {
		if threshold > 0 {
			c.threshold = threshold
		}
	}
}

// WithRedisMaxMemoryUsage sets the maximum memory usage threshold (percentage).
func WithRedisMaxMemoryUsage(percent float64) RedisCheckOption {
	return func(c *RedisCheck) {
		if percent > 0 && percent <= 100 {
			c.maxMemoryUsage = percent
		}
	}
}

// WithRedisOptions sets the Redis connection options for on-demand connections.
func WithRedisOptions(options *redis.UniversalOptions) RedisCheckOption {
	return func(c *RedisCheck) {
		c.redisOptions = options
		c.connectOnDemand = true
	}
}

// WithRedisName sets a custom name for the Redis check.
func WithRedisName(name string) RedisCheckOption {
	return func(c *RedisCheck) {
		c.BaseCheck = health.NewBaseCheck(name, health.TypeDependency, c.timeout, 60*time.Second)
	}
}
