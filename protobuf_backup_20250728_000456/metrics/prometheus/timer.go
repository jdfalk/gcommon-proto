package prometheus

import (
	"sync"
	"sync/atomic"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
)

// timer implements the metrics.Timer interface for Prometheus.
// It provides a specialized metric for measuring durations, typically
// used for tracking the execution time of operations.
type timer struct {
	histogram metrics.Histogram
	mutex     sync.RWMutex

	// Track metrics for snapshot capability
	count     atomic.Int64
	totalTime atomic.Int64 // stored in nanoseconds
}

// stopwatch implements the metrics.Stopwatch interface.
// It provides a way to measure elapsed time for operations.
type stopwatch struct {
	timer     *timer
	startTime time.Time
	stopped   bool
	mutex     sync.Mutex
}

// newTimer creates a new Prometheus timer.
//
// Parameters:
//   - registry: The Prometheus registry to register the timer with
//   - name: The name of the timer metric
//   - globalTags: Global tags to apply to all metrics in the registry
//   - options: Optional configurations for the timer
//
// Returns:
//   - metrics.Timer: A new timer instance
func newTimer(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Timer {
	// Ensure the name ends with _seconds if it doesn't already
	if len(name) < 8 || name[len(name)-8:] != "_seconds" {
		name = name + "_seconds"
	}

	// Define reasonable default buckets for a timer if none are provided
	opts := parseOptions(options...)
	if len(opts.Buckets) == 0 {
		// Default buckets optimized for typical API response times
		// from 1ms to 10s
		opts.Buckets = []float64{
			0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1,
			0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0,
		}

		// Update the options
		options = append(options, metrics.WithBuckets(opts.Buckets))
	}

	// Create a histogram for the timer
	// Timers use histograms under the hood in Prometheus
	hist := newHistogram(registry, name, globalTags, options...)

	t := &timer{
		histogram: hist,
	}

	// Register the timer in the registry for tracking
	registry.Register(name, t, options...)

	return t
}

// Record records a duration in the timer.
//
// Parameters:
//   - duration: The duration to record
func (t *timer) Record(duration time.Duration) {
	// Convert duration to seconds for Prometheus
	seconds := float64(duration) / float64(time.Second)
	t.histogram.Observe(seconds)

	// Update our tracking for snapshot capability
	t.count.Add(1)
	t.totalTime.Add(int64(duration))
}

// Time executes the given function and records its duration.
// This is a convenience method for timing code blocks.
//
// Parameters:
//   - f: The function to time
func (t *timer) Time(f func()) {
	startTime := time.Now()
	f()
	t.Record(time.Since(startTime))
}

// Start returns a stopwatch that can be used to measure elapsed time.
// Call Stop() on the returned stopwatch to record the duration.
//
// Returns:
//   - metrics.Stopwatch: A new stopwatch instance
func (t *timer) Start() metrics.Stopwatch {
	return &stopwatch{
		timer:     t,
		startTime: time.Now(),
		stopped:   false,
	}
}

// WithTags returns a new timer with the given tags.
// This allows for dimensional metrics where the same timer can be tracked
// across different dimensions (e.g., endpoint, method, status).
//
// Parameters:
//   - tags: The tags to apply to the timer
//
// Returns:
//   - metrics.Timer: A new timer instance with the combined tags
func (t *timer) WithTags(tags ...metrics.Tag) metrics.Timer {
	// Create a new timer with the updated histogram
	return &timer{
		histogram: t.histogram.WithTags(tags...),
	}
}

// Snapshot returns the current state of the timer.
// This provides a point-in-time view of all measurements recorded in the timer.
//
// Returns:
//   - metrics.HistogramSnapshot: A snapshot of the timer's current state
func (t *timer) Snapshot() metrics.HistogramSnapshot {
	// Delegate to the underlying histogram for snapshots
	return t.histogram.Snapshot()
}

// NewStopwatch returns a new stopwatch that can be used to measure elapsed time.
// Call Stop() on the returned stopwatch to record the duration.
//
// Returns:
//   - metrics.Stopwatch: A new stopwatch instance
func (t *timer) NewStopwatch() metrics.Stopwatch {
	return &stopwatch{
		timer:     t,
		startTime: time.Now(),
		stopped:   false,
	}
}

// Stop stops the stopwatch and records the elapsed duration in the timer.
// After stopping, the stopwatch cannot be used again.
func (s *stopwatch) Stop() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	if s.stopped {
		// Already stopped, do nothing
		return
	}

	s.stopped = true
	elapsed := time.Since(s.startTime)
	s.timer.Record(elapsed)
}

// Reset resets the stopwatch to the current time.
// This allows reusing a stopwatch instance for multiple measurements.
func (s *stopwatch) Reset() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	s.startTime = time.Now()
	s.stopped = false
}
