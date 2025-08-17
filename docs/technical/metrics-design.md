# Metrics Module Technical Design

## Overview

The metrics module provides a unified interface for application metrics collection, aggregation, and export with support for multiple metrics backends. This design document outlines the architecture, interfaces, and implementation details
for the metrics module.

## Goals

- Provide a consistent API for metrics collection
- Support multiple metrics backends (Prometheus, OpenTelemetry, etc.)
- Enable dimensional metrics with tags/labels
- Support standard metric types (counters, gauges, histograms, etc.)
- Allow for custom metric definitions
- Enable integration with other modules (e.g., HTTP middleware)
- Support high-performance metrics collection
- Enable metrics aggregation and preprocessing
- Provide automatic runtime and system metrics

## Architecture

### Core Components

```plaintext
              +-----------------+
              |     Provider    |
              +--------+--------+
                       |
   +------------------+-------------------+
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Metrics |    | Exporters   |     |  Registry  |
+---------+    +-------------+     +-------------+
   |                  |                   |
   |                  |                   |
+--+------+    +------+------+     +------+------+
| Counter/|    |Prometheus/ |     | Dimensions  |
| Gauge/  |    |OTEL/Other  |     | & Labels    |
| etc     |    |            |     |             |
+---------+    +-------------+     +-------------+
```

### Component Design

#### Provider Interface

The core of the module is the `Provider` interface, which defines the common operations for metrics management.

#### Metric Types

The module supports standard metric types:

- **Counter**: Monotonically increasing value
- **Gauge**: Value that can go up and down
- **Histogram**: Distribution of values
- **Summary**: Sliding window of observations
- **Timer**: Convenience for measuring durations

#### Exporters

Exporters handle sending metrics to various backends:

- **Prometheus**: Push or pull model for Prometheus
- **OpenTelemetry**: Compatible with OpenTelemetry collectors
- **Statsd**: Export to StatsD protocol
- **Logger**: Output metrics to logs
- **Multi**: Send to multiple exporters

#### Registry

The registry manages metrics creation, retrieval, and organization.

## Interface Design

### Provider

```go
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
```

### Counter

```go
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
```

### Gauge

```go
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
```

### Histogram

```go
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
```

### Summary

```go
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
```

### Timer

```go
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
```

### Registry

```go
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
```

### Tag

```go
// Tag represents a metric tag/label.
type Tag struct {
    // Key is the tag key.
    Key string

    // Value is the tag value.
    Value string
}
```

## Configuration

### Config Structure

```go
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
```

## Implementation Details

### Prometheus Implementation

The Prometheus implementation uses the `prometheus/client_golang` package and supports both pull and push models for metrics exposition.

### OpenTelemetry Implementation

The OpenTelemetry implementation uses the OpenTelemetry SDK and supports exporting to various backends through the OpenTelemetry collector.

### In-memory Implementation

The in-memory implementation provides metrics for testing and development, with support for snapshots and introspection.

### Adapter Pattern

The module uses adapters to transform between the common interface and backend-specific implementations, allowing for easier integration of new backends.

## Usage Examples

### Basic Usage

```go
config := metrics.Config{
    Provider:             "prometheus",
    Enabled:              true,
    Namespace:            "myapp",
    Subsystem:            "api",
    EnableRuntimeMetrics: true,
    Endpoint:             "/metrics",
}

provider, err := metrics.NewProvider(config)
if err != nil {
    log.Fatal(err)
}
defer provider.Stop(context.Background())

// Create and use a counter
requestCounter := provider.Counter("requests_total",
    metrics.WithDescription("Total number of requests"),
    metrics.WithTags(metrics.Tag{Key: "service", Value: "api"}),
)

requestCounter.Inc()
```

### Working with Tags/Labels

```go
// Create metrics with tags
requestLatency := provider.Histogram("request_latency_seconds",
    metrics.WithDescription("Request latency in seconds"),
    metrics.WithBuckets([]float64{0.001, 0.01, 0.1, 0.5, 1, 2, 5}),
)

// Add tags to specific measurements
requestLatency.WithTags(
    metrics.Tag{Key: "method", Value: "GET"},
    metrics.Tag{Key: "path", Value: "/users"},
    metrics.Tag{Key: "status", Value: "200"},
).Observe(0.042)

// Create a provider with default tags
apiProvider := provider.WithTags(
    metrics.Tag{Key: "service", Value: "api"},
    metrics.Tag{Key: "version", Value: "1.0"},
)

// All metrics created with this provider will have these tags
apiRequestCounter := apiProvider.Counter("requests_total")
```

### Timing Operations

```go
// Create a timer
requestTimer := provider.Timer("request_duration_seconds",
    metrics.WithDescription("Request duration in seconds"),
)

// Use timer directly
start := time.Now()
// ... do something ...
requestTimer.Record(time.Since(start))

// Or use the timing function
requestTimer.Time(func() {
    // ... do something ...
})

// Or use a stopwatch
stopwatch := requestTimer.NewStopwatch()
// ... do something ...
stopwatch.Stop()
```

### HTTP Middleware Integration

```go
// Create an HTTP middleware that records request metrics
func MetricsMiddleware(provider metrics.Provider) func(http.Handler) http.Handler {
    requestCounter := provider.Counter("http_requests_total",
        metrics.WithDescription("Total number of HTTP requests"),
    )

    requestDuration := provider.Histogram("http_request_duration_seconds",
        metrics.WithDescription("HTTP request duration in seconds"),
        metrics.WithBuckets([]float64{0.001, 0.01, 0.1, 0.5, 1, 2, 5}),
    )

    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            start := time.Now()

            // Use a response wrapper to capture status code
            ww := newWrappedResponseWriter(w)

            // Call the next handler
            next.ServeHTTP(ww, r)

            // Record metrics
            duration := time.Since(start).Seconds()

            method := r.Method
            path := r.URL.Path
            status := fmt.Sprintf("%d", ww.statusCode)

            requestCounter.WithTags(
                metrics.Tag{Key: "method", Value: method},
                metrics.Tag{Key: "path", Value: path},
                metrics.Tag{Key: "status", Value: status},
            ).Inc()

            requestDuration.WithTags(
                metrics.Tag{Key: "method", Value: method},
                metrics.Tag{Key: "path", Value: path},
                metrics.Tag{Key: "status", Value: status},
            ).Observe(duration)
        })
    }
}

// Use the middleware
http.Handle("/", MetricsMiddleware(provider)(myHandler))
```

### Custom Metric Registration

```go
// Create a custom metric
connectionGauge := provider.Gauge("active_connections",
    metrics.WithDescription("Number of active connections"),
)

// Update the gauge based on connection pool
connectionGauge.Set(float64(pool.ActiveConnections()))

// Or with a callback function
provider.Registry().(metrics.CallbackRegistry).RegisterCallback(
    "active_connections",
    func() float64 {
        return float64(pool.ActiveConnections())
    },
    metrics.WithDescription("Number of active connections"),
)
```

### Exposing Metrics

```go
// Get the metrics handler
http.Handle("/metrics", provider.Handler())

// For push-based systems, metrics are automatically pushed
// based on the configuration

// Or start a separate metrics server
metricsServer := &http.Server{
    Addr:    ":9091",
    Handler: provider.Handler(),
}

go metricsServer.ListenAndServe()
```

## Testing Strategy

- Unit tests for each metrics implementation
- Integration tests with actual metrics backends
- Mock implementations for higher-level tests
- Benchmarks for performance measurement
- Compatibility tests across different versions of backends

## Security Considerations

- Authentication for metrics endpoints
- Information disclosure in metrics
- Resource usage of metrics collection
- Rate limiting for metrics endpoints
- Sensitive data in metric names or labels

## Performance Considerations

- Efficient metric storage and retrieval
- Low-overhead instrumentation
- Batching of metrics emission
- Sampling for high-volume metrics
- Buffer management for network exports
- Concurrency control for thread safety
- Minimizing allocations in hot paths
