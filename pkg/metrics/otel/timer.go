package otel

import (
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
)

// timer implements the metrics.Timer interface for OpenTelemetry.
type timer struct {
	histogram metrics.Histogram
	mutex     sync.RWMutex
}

// stopwatch implements the metrics.Stopwatch interface.
type stopwatch struct {
	timer     *timer
	startTime time.Time
	stopped   bool
	mutex     sync.Mutex
}

// newTimer creates a new OpenTelemetry timer.
func newTimer(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Timer {
	// Ensure the name ends with _seconds if it doesn't already
	if len(name) < 8 || name[len(name)-8:] != "_seconds" {
		name = name + "_seconds"
	}

	// Create a histogram for the timer
	// Timers use histograms under the hood in OpenTelemetry
	hist := newHistogram(registry, name, globalTags, options...)

	return &timer{
		histogram: hist,
	}
}

// Record records a duration.
func (t *timer) Record(duration time.Duration) {
	// Convert duration to seconds for OpenTelemetry
	seconds := float64(duration) / float64(time.Second)
	t.histogram.Observe(seconds)
}

// Time executes the given function and records its duration.
func (t *timer) Time(f func()) {
	startTime := time.Now()
	f()
	t.Record(time.Since(startTime))
}

// WithTags returns a new timer with the given tags.
func (t *timer) WithTags(tags ...metrics.Tag) metrics.Timer {
	// Delegate to the underlying histogram for tag handling
	return &timer{
		histogram: t.histogram.WithTags(tags...),
	}
}

// Snapshot returns the current snapshot.
func (t *timer) Snapshot() metrics.HistogramSnapshot {
	// Delegate to the underlying histogram for snapshots
	return t.histogram.Snapshot()
}

// NewStopwatch starts a new stopwatch.
func (t *timer) NewStopwatch() metrics.Stopwatch {
	return &stopwatch{
		timer:     t,
		startTime: time.Now(),
		stopped:   false,
	}
}

// Stop stops the timer and records the duration.
func (s *stopwatch) Stop() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	if !s.stopped {
		s.timer.Record(time.Since(s.startTime))
		s.stopped = true
	}
}

// Reset resets the timer.
func (s *stopwatch) Reset() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	s.startTime = time.Now()
	s.stopped = false
}
