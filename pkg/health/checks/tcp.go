// file: pkg/health/checks/tcp.go
package checks

import (
	"context"
	"fmt"
	"net"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// TCPCheck monitors the health of a TCP endpoint.
// It attempts to establish a TCP connection to the specified address
// to determine if the endpoint is accessible.
type TCPCheck struct {
	// Embed the BaseCheck to inherit its functionality
	health.BaseCheck

	// Address to connect to in the format "host:port"
	address string

	// Timeout for connection attempts
	timeout time.Duration
}

// TCPCheckOption is a functional option type for configuring TCPCheck.
type TCPCheckOption func(*TCPCheck)

// WithInterval sets the check interval.
func WithInterval(interval time.Duration) TCPCheckOption {
	return func(c *TCPCheck) {
		c.SetInterval(interval)
	}
}

// WithType sets the check type.
func WithType(checkType health.CheckType) TCPCheckOption {
	return func(c *TCPCheck) {
		c.SetType(checkType)
	}
}

// WithEnabled sets whether the check is initially enabled.
func WithEnabled(enabled bool) TCPCheckOption {
	return func(c *TCPCheck) {
		c.SetEnabled(enabled)
	}
}

// NewTCPCheck creates a new TCPCheck to monitor the health of a TCP endpoint.
//
// Parameters:
//   - name: Unique name for this check
//   - address: The TCP address to connect to in the format "host:port"
//   - timeout: Maximum duration to wait for a connection
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured TCPCheck instance
func NewTCPCheck(name, address string, timeout time.Duration, options ...TCPCheckOption) *TCPCheck {
	check := &TCPCheck{
		address: address,
		timeout: timeout,
	}

	// Initialize the BaseCheck
	check.BaseCheck = health.NewBaseCheck(name)

	// Default configuration
	check.SetType(health.TypeReadiness) // TCP checks are typically used for dependency readiness
	check.SetInterval(time.Minute)      // Default 1 minute interval
	check.SetEnabled(true)              // Enabled by default

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Address returns the TCP address this check connects to.
//
// Returns:
//   - The TCP address in the format "host:port"
func (c *TCPCheck) Address() string {
	return c.address
}

// Timeout returns the connection timeout duration.
//
// Returns:
//   - The maximum duration to wait for a connection
func (c *TCPCheck) Timeout() time.Duration {
	return c.timeout
}

// Execute performs the TCP health check by attempting to establish a connection.
//
// The check performs these steps:
// 1. Create a dialer with the configured timeout
// 2. Attempt to establish a TCP connection to the configured address
// 3. Close the connection if successful
// 4. Return appropriate health result based on connection success/failure
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *TCPCheck) Execute(ctx context.Context) (health.Result, error) {
	startTime := time.Now()

	// Create result with details
	result := health.NewResult(health.StatusUnknown).
		WithDetails(map[string]interface{}{
			"address": c.address,
		})

	// Create a dialer with timeout
	dialer := &net.Dialer{
		Timeout: c.timeout,
	}

	// Try to establish a connection
	conn, err := dialer.DialContext(ctx, "tcp", c.address)

	// Calculate connection time
	connectionTime := time.Since(startTime)
	result = result.WithDetails(map[string]interface{}{
		"connectionTime": connectionTime.String(),
	})

	// Handle connection result
	if err != nil {
		// Connection failed
		result = result.
			WithStatus(health.StatusDown).
			WithError(err).
			WithDuration(connectionTime)

		return result, nil
	}

	// Connection succeeded, close it
	defer conn.Close()

	// Return success result
	return result.
		WithStatus(health.StatusUp).
		WithDuration(connectionTime), nil
}

// String returns a string representation of the TCP check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *TCPCheck) String() string {
	return fmt.Sprintf("TCPCheck{name=%s, address=%s, timeout=%s, type=%s, enabled=%t}",
		c.Name(), c.address, c.timeout, c.Type(), c.Enabled())
}
