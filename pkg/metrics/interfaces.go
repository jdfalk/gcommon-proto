// Package metrics provides a unified interface for metrics collection.
package metrics

import (
	"context"
	"net/http"
	"time"
)

// Provider is a metrics provider.
type Provider interface {
	// Counter creates or retrieves a counter.
	Counter(name string, options ...Option) Counter

	// Gauge creates or retrieves a gauge.
	Gauge(name string, options ...Option) Gauge

	// Histogram creates or retrieves a histogram.
	Histogram(name string, options ...Option) Histogram

	// Summary creates or retrieves a summary.
	Summary(name string, options ...Option) Summary

	// Timer creates or retrieves a timer.
	Timer(name string, options ...Option) Timer

	// Registry returns the provider's registry.
	Registry() Registry

	// Handler returns an HTTP handler for metrics.
	Handler() http.Handler

	// Start starts the provider.
	Start(ctx context.Context) error

	// Stop stops the provider.
	Stop(ctx context.Context) error

	// WithTags returns a new provider with the given tags.
	WithTags(tags ...Tag) Provider
}

// Counter is a metric that represents a cumulative value.
type Counter interface {
	// Inc increments the counter by 1.
	Inc()

	// Add adds the given value to the counter.
	Add(value float64)

	// WithTags returns a new counter with the given tags.
	WithTags(tags ...Tag) Counter

	// Value returns the current value of the counter.
	Value() float64
}

// Gauge is a metric that represents a single numerical value.
type Gauge interface {
	// Set sets the gauge to the given value.
	Set(value float64)

	// Inc increments the gauge by 1.
	Inc()

	// Dec decrements the gauge by 1.
	Dec()

	// Add adds the given value to the gauge.
	Add(value float64)

	// Sub subtracts the given value from the gauge.
	Sub(value float64)

	// WithTags returns a new gauge with the given tags.
	WithTags(tags ...Tag) Gauge

	// Value returns the current value of the gauge.
	Value() float64
}

// Histogram is a metric that samples observations and counts them in configurable buckets.
type Histogram interface {
	// Observe adds a single observation to the histogram.
	Observe(value float64)

	// WithTags returns a new histogram with the given tags.
	WithTags(tags ...Tag) Histogram

	// Snapshot returns a snapshot of the histogram.
	Snapshot() HistogramSnapshot
}

// HistogramSnapshot is a snapshot of a histogram.
type HistogramSnapshot interface {
	// Count returns the number of observations.
	Count() int64

	// Sum returns the sum of all observations.
	Sum() float64

	// Quantile returns the value at the given quantile.
	Quantile(q float64) float64

	// Buckets returns the bucket counts.
	Buckets() map[float64]int64
}

// Summary is a metric that samples observations and provides a summary of their distribution.
type Summary interface {
	// Observe adds a single observation to the summary.
	Observe(value float64)

	// WithTags returns a new summary with the given tags.
	WithTags(tags ...Tag) Summary

	// Snapshot returns a snapshot of the summary.
	Snapshot() SummarySnapshot
}

// SummarySnapshot is a snapshot of a summary.
type SummarySnapshot interface {
	// Count returns the number of observations.
	Count() int64

	// Sum returns the sum of all observations.
	Sum() float64

	// Quantile returns the value at the given quantile.
	Quantile(q float64) float64

	// Quantiles returns all quantiles.
	Quantiles() map[float64]float64
}

// Timer is a metric that measures the duration of events.
type Timer interface {
	// Record records the given duration.
	Record(duration time.Duration)

	// Time executes the given function and records its duration.
	Time(f func())

	// WithTags returns a new timer with the given tags.
	WithTags(tags ...Tag) Timer

	// Snapshot returns a snapshot of the timer.
	Snapshot() HistogramSnapshot

	// NewStopwatch returns a new stopwatch.
	NewStopwatch() Stopwatch
}

// Stopwatch is a timer that can be stopped.
type Stopwatch interface {
	// Stop stops the timer and records its duration.
	Stop()

	// Reset resets the timer.
	Reset()
}

// Registry is a registry of metrics.
type Registry interface {
	// Get retrieves a metric.
	Get(name string, typ MetricType) (interface{}, bool)

	// GetOrCreate retrieves a metric or creates it if it doesn't exist.
	GetOrCreate(name string, typ MetricType, options ...Option) interface{}

	// Register registers a metric.
	Register(name string, metric interface{}, options ...Option) error

	// Unregister removes a metric from the registry.
	Unregister(name string) bool

	// Visit visits all metrics in the registry.
	Visit(visitor MetricVisitor)

	// WithTags returns a new registry with the given tags.
	WithTags(tags ...Tag) Registry

	// Snapshot returns a snapshot of all metrics in the registry.
	Snapshot() Snapshot
}

// Snapshot is a snapshot of all metrics in a registry.
type Snapshot interface {
	// Counters returns all counters in the snapshot.
	Counters() map[string]float64

	// Gauges returns all gauges in the snapshot.
	Gauges() map[string]float64

	// Histograms returns all histograms in the snapshot.
	Histograms() map[string]HistogramSnapshot

	// Summaries returns all summaries in the snapshot.
	Summaries() map[string]SummarySnapshot
}

// MetricVisitor is a function that visits a metric.
type MetricVisitor func(name string, typ MetricType, metric interface{})

// MetricType is the type of a metric.
type MetricType int

// Metric types.
const (
	TypeCounter MetricType = iota
	TypeGauge
	TypeHistogram
	TypeSummary
	TypeTimer
)

// Tag is a key-value pair that can be attached to a metric.
type Tag struct {
	Key   string
	Value string
}

// Options are options for creating a metric.
type Options struct {
	// Namespace is the metrics namespace.
	Namespace string

	// Subsystem is the metrics subsystem.
	Subsystem string

	// Help is the metric help text.
	Help string

	// Tags are additional tags to attach to the metric.
	Tags []Tag

	// Buckets are the histogram buckets.
	Buckets []float64

	// Quantiles are the summary quantiles.
	Quantiles []float64

	// MaxAge is the maximum age of observations in a summary.
	MaxAge time.Duration

	// AgeBuckets is the number of age buckets in a summary.
	AgeBuckets int

	// BufCap is the buffer capacity for observations in a summary.
	BufCap int

	// ObjectiveMap is a map of quantiles to objectives.
	ObjectiveMap map[float64]float64
}

// Option is a function that configures options.
type Option func(*Options)

// Config is the configuration for a metrics provider.
type Config struct {
	// Enabled specifies whether metrics collection is enabled.
	Enabled bool

	// Provider is the metrics provider to use.
	Provider string

	// Namespace is the metrics namespace.
	Namespace string

	// Subsystem is the metrics subsystem.
	Subsystem string

	// Tags are global tags to apply to all metrics.
	Tags []Tag

	// HTTPPath is the HTTP path for exposing metrics.
	HTTPPath string

	// ProviderConfig is provider-specific configuration.
	ProviderConfig map[string]interface{}

	// Registry is an optional existing registry to use.
	Registry Registry
}
