// file: pkg/health/checks/tcp.go
package checks

import (
	"context"
	"fmt"
	"net"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// TCPCheck is a health check that verifies TCP connectivity to a specified address.
type TCPCheck struct {
	baseCheck *health.BaseCheck
	address   string
	timeout   time.Duration
}

// TCPCheckOption is a functional option type for configuring TCPCheck.
type TCPCheckOption func(*TCPCheck)

// WithTCPCheckInterval sets the check interval.
func WithTCPCheckInterval(interval time.Duration) TCPCheckOption {
	return func(c *TCPCheck) {
		if interval > 0 {
			c.baseCheck.SetInterval(interval)
		}
	}
}

// WithTCPCheckType sets the check type.
func WithTCPCheckType(checkType health.CheckType) TCPCheckOption {
	return func(c *TCPCheck) {
		c.baseCheck.SetType(checkType)
	}
}

// WithTCPCheckEnabled sets whether the check is initially enabled.
func WithTCPCheckEnabled(enabled bool) TCPCheckOption {
	return func(c *TCPCheck) {
		c.baseCheck.SetEnabled(enabled)
	}
}

// WithTCPTimeout sets the connection timeout.
func WithTCPTimeout(timeout time.Duration) TCPCheckOption {
	return func(c *TCPCheck) {
		if timeout > 0 {
			c.timeout = timeout
		}
	}
}

// NewTCPCheck creates a new TCP connectivity health check.
//
// Parameters:
//   - name: Unique name for this check
//   - address: The TCP address to connect to in the format "host:port"
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured TCPCheck instance
func NewTCPCheck(name string, address string, options ...TCPCheckOption) *TCPCheck {
	check := &TCPCheck{
		address: address,
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
func (c *TCPCheck) Name() string {
	return c.baseCheck.Name()
}

// Type returns the check type.
func (c *TCPCheck) Type() health.CheckType {
	return c.baseCheck.Type()
}

// Timeout returns the check timeout.
func (c *TCPCheck) Timeout() time.Duration {
	return c.timeout
}

// Interval returns the check interval.
func (c *TCPCheck) Interval() time.Duration {
	return c.baseCheck.Interval()
}

// Enabled returns whether the check is enabled.
func (c *TCPCheck) Enabled() bool {
	return c.baseCheck.Enabled()
}

// SetEnabled enables or disables the check.
func (c *TCPCheck) SetEnabled(enabled bool) {
	c.baseCheck.SetEnabled(enabled)
}

// Execute performs the TCP health check by attempting to establish a connection.
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *TCPCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Create a dialer with timeout
	dialer := &net.Dialer{
		Timeout: c.timeout,
	}

	// Try to establish a TCP connection
	conn, err := dialer.DialContext(ctx, "tcp", c.address)
	if err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("failed to connect to %s: %w", c.address, err)).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"address": c.address,
				"timeout": c.timeout.String(),
			}), nil
	}
	defer conn.Close()

	// Connection was successful
	connectTime := time.Since(startTime)
	return health.NewResult(health.StatusUp).
		WithDuration(connectTime).
		WithDetails(map[string]interface{}{
			"address":      c.address,
			"connect_time": connectTime.String(),
		}), nil
}

// String returns a string representation of the TCP check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *TCPCheck) String() string {
	return fmt.Sprintf("TCPCheck{name=%s, address=%s, timeout=%s}",
		c.Name(), c.address, c.timeout)
}
