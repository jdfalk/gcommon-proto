// file: pkg/health/checks/system.go
package checks

import (
	"context"
	"fmt"
	"math"
	"runtime"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/shirou/gopsutil/v3/cpu"
	"github.com/shirou/gopsutil/v3/mem"
)

// CPUCheck monitors the CPU usage of the system and reports health status
// based on a configurable threshold.
type CPUCheck struct {
	baseCheck *health.BaseCheck
	threshold float64       // CPU usage threshold percentage (0-100)
	duration  time.Duration // Duration over which to measure CPU usage
}

// CPUCheckOption is a functional option type for configuring CPUCheck.
type CPUCheckOption func(*CPUCheck)

// WithCPUCheckInterval sets the check interval.
func WithCPUCheckInterval(interval time.Duration) CPUCheckOption {
	return func(c *CPUCheck) {
		if interval > 0 {
			c.baseCheck.SetInterval(interval)
		}
	}
}

// WithCPUCheckType sets the check type.
func WithCPUCheckType(checkType health.CheckType) CPUCheckOption {
	return func(c *CPUCheck) {
		c.baseCheck.SetType(checkType)
	}
}

// WithCPUCheckEnabled sets whether the check is initially enabled.
func WithCPUCheckEnabled(enabled bool) CPUCheckOption {
	return func(c *CPUCheck) {
		c.baseCheck.SetEnabled(enabled)
	}
}

// WithCPUMeasurementDuration sets the duration over which to measure CPU usage.
func WithCPUMeasurementDuration(duration time.Duration) CPUCheckOption {
	return func(c *CPUCheck) {
		if duration > 0 {
			c.duration = duration
		}
	}
}

// NewCPUCheck creates a new CPU usage health check.
//
// Parameters:
//   - threshold: Maximum allowed CPU usage percentage (0-100)
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured CPUCheck instance
func NewCPUCheck(threshold float64, options ...CPUCheckOption) *CPUCheck {
	// Ensure threshold is within valid range
	threshold = math.Max(0, math.Min(100, threshold))

	check := &CPUCheck{
		threshold: threshold,
		duration:  3 * time.Second, // Default measurement duration
	}

	// Initialize the base check
	check.baseCheck = health.NewBaseCheck("cpu", health.TypeLiveness, 5*time.Second, 30*time.Second)

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Name returns the check name.
func (c *CPUCheck) Name() string {
	return c.baseCheck.Name()
}

// Type returns the check type.
func (c *CPUCheck) Type() health.CheckType {
	return c.baseCheck.Type()
}

// Timeout returns the check timeout.
func (c *CPUCheck) Timeout() time.Duration {
	return c.baseCheck.Timeout()
}

// Interval returns the check interval.
func (c *CPUCheck) Interval() time.Duration {
	return c.baseCheck.Interval()
}

// Enabled returns whether the check is enabled.
func (c *CPUCheck) Enabled() bool {
	return c.baseCheck.Enabled()
}

// SetEnabled enables or disables the check.
func (c *CPUCheck) SetEnabled(enabled bool) {
	c.baseCheck.SetEnabled(enabled)
}

// Execute performs the CPU health check by measuring CPU usage.
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *CPUCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Get CPU percentage over the configured duration
	percentages, err := cpu.Percent(c.duration, false)
	if err != nil {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("failed to get CPU usage: %w", err)).
			WithDuration(time.Since(startTime)), nil
	}

	// Check if we got valid data
	if len(percentages) == 0 {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("no CPU usage data available")).
			WithDuration(time.Since(startTime)), nil
	}

	// CPU percentage is the average across all cores
	cpuPercentage := percentages[0]

	// Create result with details
	result := health.NewResult(health.StatusUp).
		WithDetails(map[string]interface{}{
			"cpu_usage": cpuPercentage,
			"threshold": c.threshold,
			"cores":     runtime.NumCPU(),
			"duration":  c.duration.String(),
		}).
		WithDuration(time.Since(startTime))

	// Check if CPU usage exceeds threshold
	if cpuPercentage > c.threshold {
		return result.
			WithStatus(health.StatusDegraded).
			WithError(fmt.Errorf("CPU usage (%.2f%%) exceeds threshold (%.2f%%)",
				cpuPercentage, c.threshold)), nil
	}

	return result, nil
}

// String returns a string representation of the CPU check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *CPUCheck) String() string {
	return fmt.Sprintf("CPUCheck{name=%s, threshold=%.2f%%, duration=%s}",
		c.Name(), c.threshold, c.duration)
}

// MemoryCheck monitors the memory usage of the system and reports health status
// based on a configurable threshold.
type MemoryCheck struct {
	baseCheck *health.BaseCheck
	threshold float64 // Memory usage threshold percentage (0-100)
}

// MemoryCheckOption is a functional option type for configuring MemoryCheck.
type MemoryCheckOption func(*MemoryCheck)

// WithMemoryCheckInterval sets the check interval.
func WithMemoryCheckInterval(interval time.Duration) MemoryCheckOption {
	return func(c *MemoryCheck) {
		if interval > 0 {
			c.baseCheck.SetInterval(interval)
		}
	}
}

// WithMemoryCheckType sets the check type.
func WithMemoryCheckType(checkType health.CheckType) MemoryCheckOption {
	return func(c *MemoryCheck) {
		c.baseCheck.SetType(checkType)
	}
}

// WithMemoryCheckEnabled sets whether the check is initially enabled.
func WithMemoryCheckEnabled(enabled bool) MemoryCheckOption {
	return func(c *MemoryCheck) {
		c.baseCheck.SetEnabled(enabled)
	}
}

// NewMemoryCheck creates a new memory usage health check.
//
// Parameters:
//   - threshold: Maximum allowed memory usage percentage (0-100)
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured MemoryCheck instance
func NewMemoryCheck(threshold float64, options ...MemoryCheckOption) *MemoryCheck {
	// Ensure threshold is within valid range
	threshold = math.Max(0, math.Min(100, threshold))

	check := &MemoryCheck{
		threshold: threshold,
	}

	// Initialize the base check
	check.baseCheck = health.NewBaseCheck("memory", health.TypeLiveness, 5*time.Second, 30*time.Second)

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Name returns the check name.
func (c *MemoryCheck) Name() string {
	return c.baseCheck.Name()
}

// Type returns the check type.
func (c *MemoryCheck) Type() health.CheckType {
	return c.baseCheck.Type()
}

// Timeout returns the check timeout.
func (c *MemoryCheck) Timeout() time.Duration {
	return c.baseCheck.Timeout()
}

// Interval returns the check interval.
func (c *MemoryCheck) Interval() time.Duration {
	return c.baseCheck.Interval()
}

// Enabled returns whether the check is enabled.
func (c *MemoryCheck) Enabled() bool {
	return c.baseCheck.Enabled()
}

// SetEnabled enables or disables the check.
func (c *MemoryCheck) SetEnabled(enabled bool) {
	c.baseCheck.SetEnabled(enabled)
}

// Execute performs the memory health check by measuring memory usage.
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *MemoryCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Get memory statistics
	vmStat, err := mem.VirtualMemory()
	if err != nil {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("failed to get memory info: %w", err)).
			WithDuration(time.Since(startTime)), nil
	}

	// Create result with details
	result := health.NewResult(health.StatusUp).
		WithDetails(map[string]interface{}{
			"memory_usage":       vmStat.UsedPercent,
			"threshold":          c.threshold,
			"total_memory_bytes": vmStat.Total,
			"used_memory_bytes":  vmStat.Used,
			"free_memory_bytes":  vmStat.Free,
		}).
		WithDuration(time.Since(startTime))

	// Check if memory usage exceeds threshold
	if vmStat.UsedPercent > c.threshold {
		return result.
			WithStatus(health.StatusDegraded).
			WithError(fmt.Errorf("memory usage (%.2f%%) exceeds threshold (%.2f%%)",
				vmStat.UsedPercent, c.threshold)), nil
	}

	return result, nil
}

// String returns a string representation of the memory check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *MemoryCheck) String() string {
	return fmt.Sprintf("MemoryCheck{name=%s, threshold=%.2f%%}",
		c.Name(), c.threshold)
}
