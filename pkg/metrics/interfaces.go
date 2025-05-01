// Package metrics provides a unified interface for application metrics collection,
// aggregation, and export with support for multiple metrics backends.
package metrics

import (
	"context"
	"net/http"
	"time"
)

// MetricType represents a type of metric.
type MetricType int

const (
	// TypeCounter is a counter metric type.
	TypeCounter MetricType = iota

	// TypeGauge is a gauge metric type.
	TypeGauge

	// TypeHistogram is a histogram metric type.
	TypeHistogram

	// TypeSummary is a summary metric type.
	TypeSummary

	// TypeTimer is a timer metric type.
	TypeTimer
)

// Tag represents a metric tag/label.
type Tag struct {
	// Key is the tag key.
	Key string

	// Value is the tag value.
	Value string
}

// Option represents a metric creation option.
type Option func(options *Options)

// Options contains metric creation options.
type Options struct {
	// Description is the metric description.
	Description string

	// Unit is the metric unit.
	Unit string

	// Tags are the metric tags.
	Tags []Tag

	// Buckets are the histogram buckets.
	Buckets []float64

	// Objectives are the summary objectives.
	Objectives map[float64]float64

	// MaxAge is the maximum age of observations.
	MaxAge time.Duration

	// AgeBuckets is the number of age buckets.
	AgeBuckets uint32

	// BufCap is the buffer capacity.
	BufCap uint32
}

// Provider represents a metrics provider.
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
	Handler() http.Handler

	// Start initializes the metrics provider.
	Start(ctx context.Context) error

	// Stop stops the metrics provider.
	Stop(ctx context.Context) error

	// WithTags returns a new provider with the given tags.
	WithTags(tags ...Tag) Provider
}

// Counter represents a counter metric.
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

// Gauge represents a gauge metric.
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

// Histogram represents a histogram metric.
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

// Summary represents a summary metric.
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

// Timer represents a timer metric.
type Timer interface {
	// Record records a duration.
	Record(duration time.Duration)

	// Time executes the given function and records its duration.
	Time(f func())

	// WithTags returns a new timer with the given tags.
	WithTags(tags ...Tag) Timer

	// Snapshot returns the current snapshot.
	Snapshot() HistogramSnapshot

	// NewStopwatch starts a new stopwatch.
	NewStopwatch() Stopwatch
}

// Stopwatch represents a running timer.
type Stopwatch interface {
	// Stop stops the timer and records the duration.
	Stop()

	// Reset resets the timer.
	Reset()
}

// Registry represents a metrics registry.
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

// MetricVisitor is a function that visits a metric.
type MetricVisitor func(name string, typ MetricType, metric interface{})

// Snapshot represents a snapshot of all metrics.
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

// Common option functions

// WithDescription sets the metric description.
func WithDescription(description string) Option {
	return func(options *Options) {
		options.Description = description
	}
}

// WithUnit sets the metric unit.
func WithUnit(unit string) Option {
	return func(options *Options) {
		options.Unit = unit
	}
}

// WithTags sets the metric tags.
func WithTags(tags ...Tag) Option {
	return func(options *Options) {
		options.Tags = append(options.Tags, tags...)
	}
}

// WithBuckets sets the histogram buckets.
func WithBuckets(buckets []float64) Option {
	return func(options *Options) {
		options.Buckets = buckets
	}
}

// WithObjectives sets the summary objectives.
func WithObjectives(objectives map[float64]float64) Option {
	return func(options *Options) {
		options.Objectives = objectives
	}
}

// WithMaxAge sets the maximum age of observations.
func WithMaxAge(maxAge time.Duration) Option {
	return func(options *Options) {
		options.MaxAge = maxAge
	}
}

// WithAgeBuckets sets the number of age buckets.
func WithAgeBuckets(ageBuckets uint32) Option {
	return func(options *Options) {
		options.AgeBuckets = ageBuckets
	}
}

// WithBufCap sets the buffer capacity.
func WithBufCap(bufCap uint32) Option {
	return func(options *Options) {
		options.BufCap = bufCap
	}
}

// Config represents the metrics configuration.
type Config struct {
	// Provider specifies the metrics provider to use.
	// Supported values: "prometheus", "opentelemetry", "statsd", "noop"
	Provider string

	// Enabled specifies whether metrics collection is enabled.
	Enabled bool

	// Namespace is the namespace for all metrics.
	Namespace string

	// Subsystem is the subsystem for all metrics.
	Subsystem string

	// Tags are the global tags for all metrics.
	Tags []Tag

	// EnableRuntimeMetrics enables Go runtime metrics.
	EnableRuntimeMetrics bool

	// EnableSystemMetrics enables system metrics.
	EnableSystemMetrics bool

	// Endpoint is the HTTP endpoint for metrics exposition.
	Endpoint string

	// FlushInterval is the interval for flushing metrics.
	FlushInterval time.Duration

	// PrometheusConfig contains Prometheus-specific configuration.
	PrometheusConfig *PrometheusConfig

	// OpenTelemetryConfig contains OpenTelemetry-specific configuration.
	OpenTelemetryConfig *OpenTelemetryConfig

	// StatsdConfig contains StatsD-specific configuration.
	StatsdConfig *StatsdConfig
}

// PrometheusConfig represents Prometheus-specific configuration.
type PrometheusConfig struct {
	// Path is the HTTP path for metrics exposition.
	Path string

	// EnableGoCollector enables the Go collector.
	EnableGoCollector bool

	// EnableProcessCollector enables the process collector.
	EnableProcessCollector bool

	// PushGateway is the Prometheus push gateway URL.
	PushGateway string

	// PushInterval is the interval for pushing metrics to the gateway.
	PushInterval time.Duration

	// PushJobName is the job name for pushed metrics.
	PushJobName string
}

// OpenTelemetryConfig represents OpenTelemetry-specific configuration.
type OpenTelemetryConfig struct {
	// CollectorURL is the OpenTelemetry collector URL.
	CollectorURL string

	// ExportInterval is the interval for exporting metrics.
	ExportInterval time.Duration

	// ResourceAttributes are the resource attributes for all metrics.
	ResourceAttributes map[string]string

	// Headers are HTTP headers for the exporter.
	Headers map[string]string

	// Insecure specifies whether to use insecure connections.
	Insecure bool
}

// StatsdConfig represents StatsD-specific configuration.
type StatsdConfig struct {
	// Address is the StatsD server address.
	Address string

	// FlushPeriod is the flush period.
	FlushPeriod time.Duration

	// MaxPacketSize is the maximum packet size.
	MaxPacketSize int

	// SampleRate is the sample rate.
	SampleRate float64
}

// CallbackRegistry extends Registry with callback functions.
type CallbackRegistry interface {
	Registry

	// RegisterCallback registers a callback function for a gauge.
	RegisterCallback(name string, callback func() float64, options ...Option) error
}

// NewProvider creates a new metrics provider.
func NewProvider(config Config) (Provider, error) {
	// This is a placeholder that will be implemented in provider-specific packages
	// Each provider implementation should be in its own package (prometheus, otel, etc.)
	// and register with a factory pattern
	return nil, nil
}
