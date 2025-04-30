// file: pkg/health/checks/tcp.go
package checks

import (
	"context"
	"fmt"
	"net"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// TCPCheck is a health check that verifies TCP connectivity to a dependency.
type TCPCheck struct {
	*health.BaseCheck
	address    string        // Address of the TCP server (host:port)
	timeout    time.Duration // Timeout for the connection attempt
	retryCount int           // Number of connection attempts before failing
	retryDelay time.Duration // Delay between retry attempts
}

// TCPCheckOption represents an option for a TCP health check.
type TCPCheckOption func(*TCPCheck)

// NewTCPCheck creates a new TCP dependency health check.
// The address parameter should be in the format "host:port".
func NewTCPCheck(address string, options ...TCPCheckOption) *TCPCheck {
	c := &TCPCheck{
		address:    address,
		timeout:    5 * time.Second,
		retryCount: 1,
		retryDelay: 1 * time.Second,
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("tcp-"+address, health.TypeDependency, c.timeout, 60*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the TCP health check by attempting to establish a connection.
func (c *TCPCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()
	details := map[string]interface{}{
		"address": c.address,
	}

	// Try to establish a TCP connection with retries if configured
	var err error
	var conn net.Conn

	for attempt := 0; attempt <= c.retryCount; attempt++ {
		// If this is a retry, add a delay
		if attempt > 0 {
			select {
			case <-time.After(c.retryDelay):
				// Continue with retry
			case <-ctx.Done():
				// Context cancelled during wait
				return health.NewResult(health.StatusDown).
					WithError(fmt.Errorf("context cancelled during retry: %w", ctx.Err())).
					WithDuration(time.Since(startTime)).
					WithDetails(details), nil
			}
		}

		// Create a dialer with timeout
		dialer := &net.Dialer{
			Timeout: c.timeout,
		}

		// Try to connect
		conn, err = dialer.DialContext(ctx, "tcp", c.address)
		if err == nil {
			// Connection successful
			_ = conn.Close()
			break
		}

		// Check if context is done before retrying
		if ctx.Err() != nil {
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("context cancelled: %w", ctx.Err())).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}

		// If this was the last attempt, keep the error for the result
		if attempt == c.retryCount {
			details["error"] = err.Error()
			details["attemptsMade"] = attempt + 1
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("connection failed after %d attempts: %w", attempt+1, err)).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}
	}

	// If we got here, the connection was successful
	duration := time.Since(startTime)
	return health.NewResult(health.StatusUp).
		WithDuration(duration).
		WithDetails(map[string]interface{}{
			"address":     c.address,
			"connectedIn": duration.String(),
		}), nil
}

// WithTCPTimeout sets the timeout for the TCP connection attempt.
func WithTCPTimeout(timeout time.Duration) TCPCheckOption {
	return func(c *TCPCheck) {
		c.timeout = timeout
	}
}

// WithRetries configures the number of connection retries.
func WithRetries(count int, delay time.Duration) TCPCheckOption {
	return func(c *TCPCheck) {
		c.retryCount = count
		c.retryDelay = delay
	}
}
