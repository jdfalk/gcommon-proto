// Package metrics provides a unified interface for metrics collection.
package metrics

import (
	"context"
	"net/http"
	"time"
)

// Context is an alias for context.Context to avoid imports in interfaces.
type Context = context.Context

// Duration is an alias for time.Duration to avoid imports in interfaces.
type Duration = time.Duration

// ResponseWriter is an alias for http.ResponseWriter to avoid imports in interfaces.
type ResponseWriter = http.ResponseWriter

// Request is an alias for http.Request to avoid imports in interfaces.
type Request = http.Request

// Handler is an alias for http.Handler to avoid imports in interfaces.
type Handler = http.Handler

// HandlerFunc is an alias for http.HandlerFunc to avoid imports in interfaces.
type HandlerFunc = http.HandlerFunc

// StatusOK is an alias for http.StatusOK to avoid imports in interfaces.
const StatusOK = http.StatusOK

// Provider is the interface for a metrics provider.
type Provider interface {
	// Counter creates or gets a counter.
	Counter(name string, options ...Option) Counter

	// Gauge creates or gets a gauge.
	Gauge(name string, options ...Option) Gauge

	// Histogram creates or gets a histogram.
	Histogram(name string, options ...Option) Histogram

	// Summary creates or gets a summary.
	Summary(name string, options ...Option) Summary

	// Timer creates or gets a timer.
	Timer(name string, options ...Option) Timer

	// Registry returns the metrics registry.
	Registry() Registry

	// Handler returns an HTTP handler for metrics exposition.
	Handler() Handler

	// Start initializes the metrics provider.
	Start(ctx Context) error

	// Stop stops the metrics provider.
	Stop(ctx Context) error

	// WithTags returns a new provider with the given tags.
	WithTags(tags ...Tag) Provider
}

// Counter is a metric that accumulates values.
type Counter interface {
	// Inc increments the counter by 1.
	Inc()

	// Add adds the given value to the counter.
	Add(value float64)

	// WithTags returns a new counter with the given tags.
	WithTags(tags ...Tag) Counter

	// Value returns the current value.
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

	// Value returns the current value.
	Value() float64
}

// Histogram is a metric that samples observations and counts them in configurable buckets.
type Histogram interface {
	// Observe records a value.
	Observe(value float64)

	// WithTags returns a new histogram with the given tags.
	WithTags(tags ...Tag) Histogram

	// Snapshot returns the current snapshot.
	Snapshot() HistogramSnapshot
}

// HistogramSnapshot represents a snapshot of a histogram.
type HistogramSnapshot interface {
	// Count returns the count of values.
	Count() int64

	// Sum returns the sum of values.
	Sum() float64

	// Quantile returns the value at the given quantile (0-1).
	Quantile(q float64) float64

	// Buckets returns the bucket counts.
	Buckets() map[float64]int64
}

// Summary is a metric that samples observations and provides quantile information.
type Summary interface {
	// Observe records a value.
	Observe(value float64)

	// WithTags returns a new summary with the given tags.
	WithTags(tags ...Tag) Summary

	// Snapshot returns the current snapshot.
	Snapshot() SummarySnapshot
}

// SummarySnapshot represents a snapshot of a summary.
type SummarySnapshot interface {
	// Count returns the count of values.
	Count() int64

	// Sum returns the sum of values.
	Sum() float64

	// Quantile returns the value at the given quantile (0-1).
	Quantile(q float64) float64

	// Quantiles returns the configured quantiles.
	Quantiles() map[float64]float64
}

// Timer is a specialized histogram that measures durations.
type Timer interface {
	// Record records a duration.
	Record(duration Duration)

	// Time executes the given function and records its duration.
	Time(f func())

	// WithTags returns a new timer with the given tags.
	WithTags(tags ...Tag) Timer

	// Snapshot returns the current snapshot.
	Snapshot() HistogramSnapshot

	// NewStopwatch starts a new stopwatch.
	NewStopwatch() Stopwatch
}

// Stopwatch is a timer that can be stopped.
type Stopwatch interface {
	// Stop stops the timer and records the duration.
	Stop()

	// Reset resets the timer.
	Reset()
}

// Registry is a collection of metrics.
type Registry interface {
	// Get gets a metric by name and type.
	Get(name string, typ MetricType) (interface{}, bool)

	// GetOrCreate gets or creates a metric.
	GetOrCreate(name string, typ MetricType, options ...Option) interface{}

	// Register registers a metric.
	Register(name string, metric interface{}, options ...Option) error

	// Unregister removes a metric.
	Unregister(name string) bool

	// Visit visits all metrics.
	Visit(visitor MetricVisitor)

	// WithTags returns a new registry with the given tags.
	WithTags(tags ...Tag) Registry

	// Snapshot returns a snapshot of all metrics.
	Snapshot() Snapshot
}

// Snapshot is a snapshot of metrics.
type Snapshot interface {
	// Counters returns the counter snapshots.
	Counters() map[string]float64

	// Gauges returns the gauge snapshots.
	Gauges() map[string]float64

	// Histograms returns the histogram snapshots.
	Histograms() map[string]HistogramSnapshot

	// Summaries returns the summary snapshots.
	Summaries() map[string]SummarySnapshot
}

// MetricType represents a metric type.
type MetricType int

const (
	// TypeCounter is a counter metric.
	TypeCounter MetricType = iota

	// TypeGauge is a gauge metric.
	TypeGauge

	// TypeHistogram is a histogram metric.
	TypeHistogram

	// TypeSummary is a summary metric.
	TypeSummary

	// TypeTimer is a timer metric.
	TypeTimer
)

// MetricVisitor is a function that visits a metric.
type MetricVisitor func(name string, typ MetricType, metric interface{})

// Tag represents a metric tag.
type Tag struct {
	// Key is the tag key.
	Key string

	// Value is the tag value.
	Value string
}

// Options represents metric options.
type Options struct {
	// Description is the metric description.
	Description string

	// Tags are the metric tags.
	Tags []Tag

	// Buckets are the histogram buckets.
	Buckets []float64

	// Quantiles are the summary quantiles.
	Quantiles []float64

	// MaxAge is the maximum age of a summary.
	MaxAge Duration
}

// Option is a function that configures Options.
type Option func(*Options)

// WithDescription sets the metric description.
func WithDescription(description string) Option {
	return func(o *Options) {
		o.Description = description
	}
}

// WithTags sets the metric tags.
func WithTags(tags ...Tag) Option {
	return func(o *Options) {
		o.Tags = append(o.Tags, tags...)
	}
}

// WithBuckets sets the histogram buckets.
func WithBuckets(buckets []float64) Option {
	return func(o *Options) {
		o.Buckets = buckets
	}
}

// WithQuantiles sets the summary quantiles.
func WithQuantiles(quantiles []float64) Option {
	return func(o *Options) {
		o.Quantiles = quantiles
	}
}

// WithMaxAge sets the maximum age of a summary.
func WithMaxAge(maxAge Duration) Option {
	return func(o *Options) {
		o.MaxAge = maxAge
	}
}

// Config represents the metrics configuration.
type Config struct {
	// Enabled specifies whether metrics are enabled.
	Enabled bool

	// Provider specifies the metrics provider to use.
	// Supported values: "prometheus", "opentelemetry", "otel"
	Provider string

	// Namespace is the metrics namespace.
	Namespace string

	// Subsystem is the metrics subsystem.
	Subsystem string

	// Tags are the global tags to add to all metrics.
	Tags []Tag

	// EnableRuntimeMetrics enables runtime metrics.
	EnableRuntimeMetrics bool

	// PrometheusConfig contains Prometheus-specific configuration.
	PrometheusConfig *PrometheusConfig

	// OpenTelemetryConfig contains OpenTelemetry-specific configuration.
	OpenTelemetryConfig *OpenTelemetryConfig
}

// PrometheusConfig represents Prometheus-specific configuration.
type PrometheusConfig struct {
	// EnableGoCollector enables the Go collector.
	EnableGoCollector bool

	// EnableProcessCollector enables the process collector.
	EnableProcessCollector bool

	// PushGateway is the Prometheus push gateway URL.
	PushGateway string

	// PushJobName is the job name for the push gateway.
	PushJobName string

	// PushInterval is the push interval.
	PushInterval Duration

	// Registry is the Prometheus registry to use.
	// If nil, a new registry is created.
	Registry interface{}
}

// OpenTelemetryConfig represents OpenTelemetry-specific configuration.
type OpenTelemetryConfig struct {
	// CollectorURL is the OpenTelemetry collector URL.
	CollectorURL string

	// Insecure specifies whether to use insecure connections.
	Insecure bool

	// Headers are the headers to add to collector requests.
	Headers map[string]string

	// ResourceAttributes are the resource attributes to add.
	ResourceAttributes map[string]string

	// ExportInterval is the export interval.
	ExportInterval Duration

	// MeterProvider is the OpenTelemetry meter provider to use.
	// If nil, a new meter provider is created.
	MeterProvider interface{}
}
