// file: pkg/health/checks/redis.go
package checks

import (
	"context"
	"fmt"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/health"
)

// RedisCheck is a health check that verifies Redis connectivity and functionality.
type RedisCheck struct {
	baseCheck *health.BaseCheck
	client    redis.UniversalClient
	command   string
	timeout   time.Duration
}

// RedisCheckOption is a functional option type for configuring RedisCheck.
type RedisCheckOption func(*RedisCheck)

// WithRedisCheckInterval sets the check interval.
func WithRedisCheckInterval(interval time.Duration) RedisCheckOption {
	return func(c *RedisCheck) {
		if interval > 0 {
			c.baseCheck.SetInterval(interval)
		}
	}
}

// WithRedisCheckType sets the check type.
func WithRedisCheckType(checkType health.CheckType) RedisCheckOption {
	return func(c *RedisCheck) {
		c.baseCheck.SetType(checkType)
	}
}

// WithRedisCheckEnabled sets whether the check is initially enabled.
func WithRedisCheckEnabled(enabled bool) RedisCheckOption {
	return func(c *RedisCheck) {
		c.baseCheck.SetEnabled(enabled)
	}
}

// WithRedisCommand sets the Redis command to execute for the health check.
func WithRedisCommand(command string) RedisCheckOption {
	return func(c *RedisCheck) {
		if command != "" {
			c.command = command
		}
	}
}

// WithRedisTimeout sets the Redis command timeout.
func WithRedisTimeout(timeout time.Duration) RedisCheckOption {
	return func(c *RedisCheck) {
		if timeout > 0 {
			c.timeout = timeout
		}
	}
}

// NewRedisCheck creates a new Redis service health check.
//
// Parameters:
//   - name: Unique name for this check
//   - client: Redis client to use for the check
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured RedisCheck instance
func NewRedisCheck(name string, client redis.UniversalClient, options ...RedisCheckOption) *RedisCheck {
	check := &RedisCheck{
		client:  client,
		command: "PING", // Default command is PING
		timeout: 5 * time.Second,
	}

	// Initialize the base check
	check.baseCheck = health.NewBaseCheck(name, health.TypeDependency, check.timeout, 30*time.Second)

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Name returns the check name.
func (c *RedisCheck) Name() string {
	return c.baseCheck.Name()
}

// Type returns the check type.
func (c *RedisCheck) Type() health.CheckType {
	return c.baseCheck.Type()
}

// Timeout returns the check timeout.
func (c *RedisCheck) Timeout() time.Duration {
	return c.timeout
}

// Interval returns the check interval.
func (c *RedisCheck) Interval() time.Duration {
	return c.baseCheck.Interval()
}

// Enabled returns whether the check is enabled.
func (c *RedisCheck) Enabled() bool {
	return c.baseCheck.Enabled()
}

// SetEnabled enables or disables the check.
func (c *RedisCheck) SetEnabled(enabled bool) {
	c.baseCheck.SetEnabled(enabled)
}

// Execute performs the Redis health check by executing the configured command.
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *RedisCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Create a context with timeout
	ctxTimeout, cancel := context.WithTimeout(ctx, c.timeout)
	defer cancel()

	// Execute command based on what was configured
	var cmdResult interface{}
	var err error

	switch c.command {
	case "PING":
		cmdResult, err = c.client.Ping(ctxTimeout).Result()
	case "INFO":
		cmdResult, err = c.client.Info(ctxTimeout).Result()
	default:
		// For any other command, execute it as a generic command
		cmdResult, err = c.client.Do(ctxTimeout, c.command).Result()
	}

	// Check for errors
	if err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("Redis command '%s' failed: %w", c.command, err)).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"command": c.command,
				"timeout": c.timeout.String(),
			}), nil
	}

	// Command executed successfully
	return health.NewResult(health.StatusUp).
		WithDuration(time.Since(startTime)).
		WithDetails(map[string]interface{}{
			"command":  c.command,
			"response": fmt.Sprintf("%v", cmdResult),
		}), nil
}

// String returns a string representation of the Redis check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *RedisCheck) String() string {
	redisOptions := ""
	if universal, ok := c.client.(*redis.UniversalClient); ok && universal != nil {
		redisOptions = fmt.Sprintf("%v", universal.Options())
	}

	return fmt.Sprintf("RedisCheck{name=%s, command=%s, timeout=%s, redis=%s}",
		c.Name(), c.command, c.timeout, redisOptions)
}
