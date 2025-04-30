// file: pkg/health/checks/system.go
package checks

import (
	"context"
	"fmt"
	"runtime"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// SystemCheck monitors system resources like memory and CPU.
type SystemCheck struct {
	*health.BaseCheck
	memoryThresholdPct float64 // Memory threshold in percentage (0-100)
	gcPauseThreshold   time.Duration // Threshold for GC pause time warnings
}

// SystemCheckOption represents an option for a system health check.
type SystemCheckOption func(*SystemCheck)

// NewSystemCheck creates a new system health check.
func NewSystemCheck(options ...SystemCheckOption) *SystemCheck {
	c := &SystemCheck{
		memoryThresholdPct: 90.0, // Default to 90% memory threshold
		gcPauseThreshold:   100 * time.Millisecond, // Default to 100ms GC pause threshold
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("system", health.TypeComponent, 5*time.Second, 30*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the system health check.
func (c *SystemCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Collect memory statistics
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)

	// Calculate memory usage percentage
	memoryUsagePct := float64(memStats.HeapAlloc) / float64(memStats.HeapSys) * 100.0

	// Basic details that will be included in every result
	details := map[string]interface{}{
		"memory": map[string]interface{}{
			"heapAlloc":      formatBytes(memStats.HeapAlloc),
			"heapSys":        formatBytes(memStats.HeapSys),
			"heapInuse":      formatBytes(memStats.HeapInuse),
			"heapIdle":       formatBytes(memStats.HeapIdle),
			"usagePercent":   fmt.Sprintf("%.1f%%", memoryUsagePct),
			"threshold":      fmt.Sprintf("%.1f%%", c.memoryThresholdPct),
		},
		"gc": map[string]interface{}{
			"numGC":         memStats.NumGC,
			"lastPauseTime": time.Duration(memStats.PauseNs[(memStats.NumGC+255)%256]).String(),
			"totalPauseMs":  memStats.PauseTotalNs / 1000000,
			"threshold":     c.gcPauseThreshold.String(),
		},
		"goroutines": runtime.NumGoroutine(),
	}

	// Check memory usage
	if memoryUsagePct > c.memoryThresholdPct {
		return health.NewResult(health.StatusDegraded).
			WithError(fmt.Errorf("memory usage %.1f%% exceeds threshold %.1f%%", 
				memoryUsagePct, c.memoryThresholdPct)).
			WithDuration(time.Since(startTime)).
			WithDetails(details), nil
	}

	// Check GC pause time
	lastGCPause := time.Duration(memStats.PauseNs[(memStats.NumGC+255)%256])
	if lastGCPause > c.gcPauseThreshold {
		return health.NewResult(health.StatusDegraded).
			WithError(fmt.Errorf("GC pause %s exceeds threshold %s", 
				lastGCPause, c.gcPauseThreshold)).
			WithDuration(time.Since(startTime)).
			WithDetails(details), nil
	}

	// All checks passed
	return health.NewResult(health.StatusUp).
		WithDuration(time.Since(startTime)).
		WithDetails(details), nil
}

// WithMemoryThreshold sets the memory usage threshold.
// When memory usage exceeds this percentage, the check will return a degraded status.
// Value should be between 0 and 100.
func WithMemoryThreshold(thresholdPercent float64) SystemCheckOption {
	return func(c *SystemCheck) {
		if thresholdPercent > 0 && thresholdPercent <= 100 {
			c.memoryThresholdPct = thresholdPercent
		}
	}
}

// WithGCPauseThreshold sets the garbage collection pause time threshold.
// When GC pause time exceeds this duration, the check will return a degraded status.
func WithGCPauseThreshold(threshold time.Duration) SystemCheckOption {
	return func(c *SystemCheck) {
		if threshold > 0 {
			c.gcPauseThreshold = threshold
		}
	}
}

// formatBytes formats bytes into a human-readable string (KB, MB, GB).
func formatBytes(bytes uint64) string {
	const (
		KB = 1024
		MB = KB * 1024
		GB = MB * 1024
	)

	switch {
	case bytes >= GB:
		return fmt.Sprintf("%.2f GB", float64(bytes)/float64(GB))
	case bytes >= MB:
		return fmt.Sprintf("%.2f MB", float64(bytes)/float64(MB))
	case bytes >= KB:
		return fmt.Sprintf("%.2f KB", float64(bytes)/float64(KB))
	default:
		return fmt.Sprintf("%d B", bytes)
	}
}