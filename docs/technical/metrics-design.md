# Metrics Module Technical Design

## Overview

The metrics module provides a unified interface for collecting and exporting metrics across various backends, with primary support for OpenTelemetry and Prometheus. This design document outlines the architecture, interfaces, and implementation details for the metrics module.

## Goals

- Provide a consistent API across different metrics backends
- Support both OpenTelemetry and Prometheus metrics
- Enable easy integration with HTTP servers and middleware
- Support custom metric collection for application-specific metrics
- Allow for runtime configuration of metrics collection
- Provide efficient metrics collection with minimal overhead
- Enable integration with other modules (e.g., database, logging)

## Architecture

### Core Components

```text
                  +----------------+
                  |   Provider     |
                  +-------+--------+
                          |
        +----------------++-----------------+
        |                |                  |
+-------+------+  +------+-------+  +-------+------+
|  Collector   |  |  Exporter    |  | Registration |
+-------+------+  +------+-------+  +-------+------+
        |                |                  |
        |                |                  |
+-------+------+  +------+-------+  +-------+------+
| Counter/Gauge |  | HTTP/gRPC   |  | Global/Local |
| /Histogram    |  | Exporters   |  | Metrics      |
+--------------+   +-------------+   +--------------+
```

### Component Design

#### Provider Interface

The core of the module is the `Provider` interface, which defines the common operations for metrics collection and export.

#### Metrics Types

The module supports the following metric types:

- **Counters**: For values that only increase (e.g., request count)
- **Gauges**: For values that can increase and decrease (e.g., active connections)
- **Histograms**: For measuring distributions of values (e.g., request durations)

#### Collectors

Collectors are responsible for gathering metrics from various parts of the application.

#### Exporters

Exporters send metrics to monitoring systems (Prometheus, OTLP, etc.).

#### Registration System

The registration system allows for dynamic registration and management of metrics.

## Interface Design

### Provider

```go
// Provider represents a metrics provider.
type Provider interface {
    // Counter creates or gets a counter metric.
    Counter(name, description string, labels ...string) Counter

    // Gauge creates or gets a gauge metric.
    Gauge(name, description string, labels ...string) Gauge

    // Histogram creates or gets a histogram metric.
    Histogram(name, description string, buckets []float64, labels ...string) Histogram

    // Middleware returns HTTP middleware for collecting request metrics.
    Middleware() interface{}

    // Start starts the metrics collection.
    Start(ctx context.Context) error

    // Stop stops the metrics collection.
    Stop(ctx context.Context) error

    // Registry returns the metrics registry.
    Registry() interface{}

    // Expose metrics to a specific endpoint.
    ExposeHTTP(handler http.Handler, path string)
}
```

### Counter

```go
// Counter represents a counter metric.
type Counter interface {
    // Inc increments the counter by 1.
    Inc(labels ...string)

    // Add adds the given value to the counter.
    Add(value float64, labels ...string)

    // WithLabels returns a new counter with pre-set labels.
    WithLabels(labels map[string]string) Counter
}
```

### Gauge

```go
// Gauge represents a gauge metric.
type Gauge interface {
    // Set sets the gauge to the given value.
    Set(value float64, labels ...string)

    // Inc increments the gauge by 1.
    Inc(labels ...string)

    // Dec decrements the gauge by 1.
    Dec(labels ...string)

    // Add adds the given value to the gauge.
    Add(value float64, labels ...string)

    // Sub subtracts the given value from the gauge.
    Sub(value float64, labels ...string)

    // WithLabels returns a new gauge with pre-set labels.
    WithLabels(labels map[string]string) Gauge
}
```

### Histogram

```go
// Histogram represents a histogram metric.
type Histogram interface {
    // Observe records a value in the histogram.
    Observe(value float64, labels ...string)

    // WithLabels returns a new histogram with pre-set labels.
    WithLabels(labels map[string]string) Histogram
}
```

## Configuration

### Config Structure

```go
// Config represents the metrics configuration.
type Config struct {
    // Enabled specifies whether metrics collection is enabled.
    Enabled bool

    // Provider specifies the metrics provider to use.
    // Supported values: "prometheus", "opentelemetry", "none"
    Provider string

    // Namespace is the metrics namespace, typically your application name.
    Namespace string

    // Subsystem is an optional subsystem name.
    Subsystem string

    // Labels are the global labels to apply to all metrics.
    Labels map[string]string

    // HTTPEndpoint is the endpoint to expose metrics on.
    HTTPEndpoint string

    // HTTPPath is the path to expose metrics on.
    HTTPPath string

    // ExportInterval is the interval for exporting metrics.
    ExportInterval time.Duration

    // OpenTelemetry specific configuration
    OpenTelemetry OpenTelemetryConfig

    // Prometheus specific configuration
    Prometheus PrometheusConfig
}

// OpenTelemetryConfig represents OpenTelemetry-specific configuration.
type OpenTelemetryConfig struct {
    // ExporterType specifies the exporter type.
    // Supported values: "otlp", "prometheus", "jaeger"
    ExporterType string

    // Endpoint is the exporter endpoint.
    Endpoint string

    // Insecure specifies whether to use insecure connections.
    Insecure bool

    // Headers are the headers to include in OTLP exports.
    Headers map[string]string

    // Compression specifies the compression method.
    Compression string

    // Timeout specifies the export timeout.
    Timeout time.Duration
}

// PrometheusConfig represents Prometheus-specific configuration.
type PrometheusConfig struct {
    // PushGateway is the address of the Prometheus pushgateway.
    PushGateway string

    // PushInterval is the interval for pushing metrics to the gateway.
    PushInterval time.Duration

    // JobName is the name of the job for pushed metrics.
    JobName string

    // DefaultBuckets are the default histogram buckets.
    DefaultBuckets []float64

    // DisableGoCollector disables the Go runtime collector.
    DisableGoCollector bool

    // DisableProcessCollector disables the process collector.
    DisableProcessCollector bool
}
```

## Implementation Details

### Prometheus Implementation

The Prometheus implementation uses the official Prometheus client library to collect and expose metrics. It includes:

- Auto-registration of metrics with the Prometheus registry
- HTTP endpoint for metrics scraping
- Support for pushing metrics to a Pushgateway
- Pre-configured histogram buckets for common scenarios

### OpenTelemetry Implementation

The OpenTelemetry implementation uses the OpenTelemetry Go SDK for metrics collection and export. It includes:

- Support for multiple export protocols (OTLP, Prometheus)
- Batch processing of metrics for efficient export
- Context propagation for distributed tracing integration
- Resource detection for automatic environment labeling

### Middleware Integration

The metrics module provides middleware for common web frameworks:

- HTTP middleware for standard library
- Integration with common routers and frameworks

### Database Integration

Integration with the database module allows for automatic collection of:

- Query execution times
- Connection pool metrics
- Transaction metrics
- Database errors

## Usage Examples

### Basic Setup

```go
config := metrics.Config{
    Enabled:      true,
    Provider:     "prometheus",
    Namespace:    "myapp",
    Subsystem:    "api",
    HTTPEndpoint: ":9090",
    HTTPPath:     "/metrics",
    Labels: map[string]string{
        "environment": "production",
    },
}

provider, err := metrics.New(config)
if err != nil {
    log.Fatal(err)
}

ctx := context.Background()
if err := provider.Start(ctx); err != nil {
    log.Fatal(err)
}
defer provider.Stop(ctx)
```

### Collecting Metrics

```go
// Create a counter
requestCounter := provider.Counter(
    "requests_total",
    "Total number of requests",
    "method", "path", "status",
)

// Increment counter
requestCounter.Inc("GET", "/api/users", "200")

// Create a gauge
activeConnections := provider.Gauge(
    "active_connections",
    "Number of active connections",
    "service",
)

// Set gauge value
activeConnections.Set(10, "database")

// Create a histogram
requestDuration := provider.Histogram(
    "request_duration_seconds",
    "Request duration in seconds",
    []float64{0.01, 0.05, 0.1, 0.5, 1, 5},
    "method", "path",
)

// Observe a value
requestDuration.Observe(0.23, "GET", "/api/users")
```

### Using Middleware

```go
// Create HTTP middleware
middleware := provider.Middleware()

// Use with standard library
http.Handle("/api/", middleware(apiHandler))
```

### Custom Metric Collection

```go
// Create a function to collect and report application metrics
func collectAppMetrics(ctx context.Context, provider metrics.Provider) {
    userGauge := provider.Gauge("active_users", "Number of active users")
    memoryGauge := provider.Gauge("memory_usage_bytes", "Memory usage in bytes")

    for {
        select {
        case <-ctx.Done():
            return
        case <-time.After(10 * time.Second):
            activeUsers := getActiveUsers()
            userGauge.Set(float64(activeUsers))

            memUsage := getMemoryUsage()
            memoryGauge.Set(float64(memUsage))
        }
    }
}
```

## Testing Strategy

- Unit tests for each provider implementation
- Integration tests with actual metrics systems
- Benchmarks for performance measurement
- Mock implementations for higher-level tests

## Security Considerations

- Authorization for metrics endpoints
- Sensitive information in metrics and labels
- Resource limitations to prevent DoS
- Network security for metric exports

## Performance Considerations

- Cardinality explosion from too many label combinations
- Efficient collection and batching
- Asynchronous exports
- Sampling for high-volume metrics
