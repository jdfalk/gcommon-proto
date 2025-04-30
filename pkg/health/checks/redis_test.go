// file: pkg/health/checks/redis_test.go
package checks

import (
	"context"
	"fmt"
	"testing"
	"time"

	"github.com/alicebob/miniredis/v2"
	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

// TestRedisCheck tests the Redis health check functionality
func TestRedisCheck(t *testing.T) {
	// Start a mock Redis server
	mr, err := miniredis.Run()
	require.NoError(t, err)
	defer mr.Close()

	// Create Redis client connected to the mock server
	redisClient := redis.NewClient(&redis.Options{
		Addr: mr.Addr(),
	})
	defer redisClient.Close()

	// Test basic connectivity with default options
	t.Run("Basic connectivity", func(t *testing.T) {
		check := NewRedisCheck(redisClient)
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())

		details := result.Details()
		assert.Contains(t, details, "ping")
		pingDetails, ok := details["ping"].(map[string]interface{})
		assert.True(t, ok)
		assert.Equal(t, "PONG", pingDetails["response"])
	})

	// Test with custom name
	t.Run("Custom name", func(t *testing.T) {
		check := NewRedisCheck(redisClient, WithRedisName("custom-redis"))
		assert.Equal(t, "custom-redis", check.Name())

		result, err := check.Execute(context.Background())
		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())
	})

	// Test with key validation - existing key
	t.Run("Key validation - existing key", func(t *testing.T) {
		// Set a test key
		err := redisClient.Set(context.Background(), "test-key", "value", 0).Err()
		require.NoError(t, err)

		check := NewRedisCheck(redisClient, WithRedisKeyValidation("test-key"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())

		details := result.Details()
		assert.Contains(t, details, "keys")
		keyDetails, ok := details["keys"].(map[string]interface{})
		assert.True(t, ok)
		assert.Contains(t, keyDetails, "test-key")

		testKeyInfo, ok := keyDetails["test-key"].(map[string]interface{})
		assert.True(t, ok)
		assert.Equal(t, true, testKeyInfo["found"])
	})

	// Test with key validation - non-existent key
	t.Run("Key validation - non-existent key", func(t *testing.T) {
		check := NewRedisCheck(redisClient, WithRedisKeyValidation("non-existent-key"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusDegraded, result.Status()) // Degraded because key wasn't found

		details := result.Details()
		assert.Contains(t, details, "keys")
		keyDetails, ok := details["keys"].(map[string]interface{})
		assert.True(t, ok)
		assert.Contains(t, keyDetails, "non-existent-key")

		keyInfo, ok := keyDetails["non-existent-key"].(map[string]interface{})
		assert.True(t, ok)
		assert.Equal(t, false, keyInfo["found"])
	})

	// Test with key validation - pattern matching
	t.Run("Key validation - pattern matching", func(t *testing.T) {
		// Set multiple keys with a pattern
		for i := 1; i <= 5; i++ {
			key := fmt.Sprintf("pattern-key-%d", i)
			err := redisClient.Set(context.Background(), key, fmt.Sprintf("value-%d", i), 0).Err()
			require.NoError(t, err)
		}

		check := NewRedisCheck(redisClient, WithRedisKeyValidation("pattern-key-*"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())

		details := result.Details()
		assert.Contains(t, details, "keys")
		keyDetails, ok := details["keys"].(map[string]interface{})
		assert.True(t, ok)
		assert.Contains(t, keyDetails, "pattern-key-*")

		patternInfo, ok := keyDetails["pattern-key-*"].(map[string]interface{})
		assert.True(t, ok)
		assert.Equal(t, true, patternInfo["found"])
		assert.Greater(t, patternInfo["count"], float64(0))
	})

	// Test with custom command
	t.Run("Custom command", func(t *testing.T) {
		// Set a test key for the custom command
		err := redisClient.Set(context.Background(), "cmd-test-key", "test-value", 0).Err()
		require.NoError(t, err)

		check := NewRedisCheck(redisClient, WithRedisCommand("get-key", "GET", "cmd-test-key"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())

		details := result.Details()
		assert.Contains(t, details, "commands")
		cmdDetails, ok := details["commands"].(map[string]interface{})
		assert.True(t, ok)
		assert.Contains(t, cmdDetails, "get-key")

		cmdInfo, ok := cmdDetails["get-key"].(map[string]interface{})
		assert.True(t, ok)
		assert.Equal(t, "test-value", cmdInfo["result"])
	})

	// Test with custom command and validation
	t.Run("Custom command with validation", func(t *testing.T) {
		// Set a test key for the custom command
		err := redisClient.Set(context.Background(), "validation-key", "expected-value", 0).Err()
		require.NoError(t, err)

		// Create a validator that checks if the result matches the expected value
		validator := func(result interface{}, err error) error {
			if err != nil {
				return err
			}

			strResult, ok := result.(string)
			if !ok {
				return fmt.Errorf("expected string result, got %T", result)
			}

			if strResult != "expected-value" {
				return fmt.Errorf("expected 'expected-value', got '%s'", strResult)
			}

			return nil
		}

		check := NewRedisCheck(redisClient,
			WithRedisCommandAndCheck("validate-value", "GET", validator, "validation-key"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusUp, result.Status())
	})

	// Test with custom command and failing validation
	t.Run("Custom command with failing validation", func(t *testing.T) {
		// Set a test key with wrong value
		err := redisClient.Set(context.Background(), "failing-key", "wrong-value", 0).Err()
		require.NoError(t, err)

		// Create a validator that will fail because the value doesn't match
		validator := func(result interface{}, err error) error {
			return fmt.Errorf("validation failed intentionally")
		}

		check := NewRedisCheck(redisClient,
			WithRedisCommandAndCheck("failing-check", "GET", validator, "failing-key"))
		result, err := check.Execute(context.Background())

		assert.NoError(t, err)
		assert.Equal(t, health.StatusDown, result.Status())
		assert.Contains(t, result.Error().Error(), "validation failed intentionally")
	})

	// Test with context timeout
	t.Run("Context timeout", func(t *testing.T) {
		// Create a check with a custom command that will be slow
		check := NewRedisCheck(redisClient, WithRedisCommand("slow-command", "DBSIZE"))

		// Create a context with a very short timeout
		ctx, cancel := context.WithTimeout(context.Background(), 1*time.Nanosecond)
		defer cancel()

		// Execute should fail because the context times out
		_, err := check.Execute(ctx)
		assert.Error(t, err)
		assert.Contains(t, err.Error(), "context deadline exceeded")
	})
}

// TestRedisCheckWithoutClient tests the behavior when no Redis client is available
func TestRedisCheckWithoutClient(t *testing.T) {
	check := NewRedisCheck(nil)
	result, err := check.Execute(context.Background())

	assert.NoError(t, err)
	assert.Equal(t, health.StatusDown, result.Status())
	assert.Contains(t, result.Error().Error(), "no Redis client available")
}

// TestRedisCheckWithOnDemandConnection tests connecting on demand using options
func TestRedisCheckWithOnDemandConnection(t *testing.T) {
	// Start a mock Redis server
	mr, err := miniredis.Run()
	require.NoError(t, err)
	defer mr.Close()

	// Create Redis options for on-demand connection
	redisOpts := &redis.UniversalOptions{
		Addrs: []string{mr.Addr()},
	}

	// Create the check with on-demand connection options
	check := NewRedisCheck(nil, WithRedisOptions(redisOpts))
	result, err := check.Execute(context.Background())

	assert.NoError(t, err)
	assert.Equal(t, health.StatusUp, result.Status())
}
