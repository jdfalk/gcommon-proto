# Metrics Guide

This guide explains how to use the metrics module in your applications.

## Introduction

The metrics module provides a flexible and extensible way to collect and expose
metrics from your application. It supports multiple backend providers, including
Prometheus and OpenTelemetry, and offers a consistent API regardless of the
backend used.

## Features

- Multiple backend support (Prometheus, OpenTelemetry)
- Standard metric types: counter, gauge, histogram, summary, timer
- HTTP middleware for automatic request metrics
- Consistent API across backends
- Option-based configuration
- Tagging support
- Custom registry support

## Getting Started

### Basic Setup

To start using metrics in your application, you need to initialize a metrics
provider and then create metrics using that provider.

```go
package main

import (
	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/prometheus"
)

func main() {
	// Create a metrics config
	config := metrics.Config{
		Enabled:  true,
		Provider: "prometheus",
	}

	// Create a metrics provider
	provider, err := metrics.NewProvider(config)
	if err != nil {
		panic(err)
	}

	// Start the provider
	err = provider.Start(nil)
	if err != nil {
		panic(err)
	}

	// Create a counter
	counter := provider.Counter("my_counter",
		metrics.WithDescription("My counter description"),
		metrics.WithTags(metrics.Tag{Key: "label1", Value: "value1"}),
	)

	// Increment the counter
	counter.Inc()

	// Create a gauge
	gauge := provider.Gauge("my_gauge",
		metrics.WithDescription("My gauge description"),
	)

	// Set the gauge value
	gauge.Set(42.0)

	// Create a histogram
	histogram := provider.Histogram("my_histogram",
		metrics.WithDescription("My histogram description"),
		metrics.WithBuckets([]float64{1, 5, 10, 50, 100, 500, 1000}),
	)

	// Observe a value
	histogram.Observe(42.0)
}
```

### Using with HTTP

To automatically collect metrics for HTTP requests, you can use the middleware
provided:

```go
package main

import (
	"net/http"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/middleware"
)

func main() {
	// Create a metrics provider
	provider, err := metrics.NewProvider(metrics.Config{
		Enabled:  true,
		Provider: "prometheus",
	})
	if err != nil {
		panic(err)
	}

	// Create an HTTP handler
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, World!"))
	})

	// Wrap with metrics middleware
	handler := middleware.StandardMetrics(provider)(mux)

	// For more advanced configuration:
	// handler := middleware.RequestMetrics(middleware.RequestMetricsOptions{
	//     Provider:           provider,
	//     IncludeRequestSize: true,
	//     IncludeResponseSize: true,
	//     ExcludePaths:       []string{"/health", "/metrics"},
	// })(mux)

	// Start the HTTP server with the metrics handler
	http.ListenAndServe(":8080", handler)
}
```

## Exposing Metrics

### Prometheus

If you're using the Prometheus provider, you can expose the metrics via HTTP:

```go
package main

import (
	"net/http"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/prometheus"
)

func main() {
	// Create a metrics provider
	provider, err := metrics.NewProvider(metrics.Config{
		Enabled:  true,
		Provider: "prometheus",
	})
	if err != nil {
		panic(err)
	}

	// Expose the metrics handler
	http.Handle("/metrics", provider.Handler())
	http.ListenAndServe(":8080", nil)
}
```

### OpenTelemetry

If you're using OpenTelemetry, you'll need to configure an exporter:

```go
package main

import (
	"context"
	"log"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
	"go.opentelemetry.io/otel/sdk/resource"
	semconv "go.opentelemetry.io/otel/semconv/v1.21.0"
)

func main() {
	// Create an exporter
	exporter, err := otlpmetricgrpc.New(context.Background(),
		otlpmetricgrpc.WithEndpoint("localhost:4317"),
		otlpmetricgrpc.WithInsecure(),
	)
	if err != nil {
		log.Fatalf("Failed to create exporter: %v", err)
	}

	// Create a resource
	res := resource.NewWithAttributes(
		semconv.SchemaURL,
		semconv.ServiceName("my-service"),
		semconv.ServiceVersion("1.0.0"),
	)

	// Create a metrics config
	config := metrics.Config{
		Enabled:  true,
		Provider: "opentelemetry",
		OpenTelemetry: metrics.OpenTelemetryConfig{
			Exporter: exporter,
			Resource: res,
			Interval: metrics.Duration(time.Second * 10),
		},
	}

	// Create a metrics provider
	provider, err := metrics.NewProvider(config)
	if err != nil {
		log.Fatalf("Failed to create provider: %v", err)
	}

	// Start the provider
	err = provider.Start(context.Background())
	if err != nil {
		log.Fatalf("Failed to start provider: %v", err)
	}

	// Use the provider
	counter := provider.Counter("my_counter")
	counter.Inc()

	// Run forever
	select {}
}
```

## Advanced Usage

### Custom Tags

You can add tags to any metric:

```go
counter := provider.Counter("my_counter",
	metrics.WithTags(
		metrics.Tag{Key: "region", Value: "us-west"},
		metrics.Tag{Key: "environment", Value: "production"},
	),
)

counter.Inc()

// Later, you can add more tags
counter.WithTags(metrics.Tag{Key: "instance", Value: "i-12345"}).Inc()
```

### Provider with Default Tags

If you want to add the same tags to all metrics, you can create a provider with
default tags:

```go
taggedProvider := provider.WithTags(
	metrics.Tag{Key: "region", Value: "us-west"},
	metrics.Tag{Key: "environment", Value: "production"},
)

// All metrics created from this provider will have the default tags
counter := taggedProvider.Counter("my_counter")
```

### Custom Histograms

You can customize histograms with your own buckets:

```go
histogram := provider.Histogram("my_histogram",
	metrics.WithBuckets([]float64{0.001, 0.01, 0.1, 1, 10, 100, 1000}),
)
```

### Custom Summaries

Similarly, you can customize summaries with your own quantiles:

```go
summary := provider.Summary("my_summary",
	metrics.WithQuantiles([]float64{0.5, 0.9, 0.95, 0.99, 0.999}),
	metrics.WithMaxAge(metrics.Duration(time.Minute * 5)),
)
```

### Timers

Timers are a special metric type that measures the duration of operations:

```go
timer := provider.Timer("my_operation")

// Start the timer
stop := timer.Start()

// Later, stop the timer
stop()

// Or use the convenient Record method
timer.Record(func() {
	// Do some work
	time.Sleep(100 * time.Millisecond)
})
```

## Implementing a Custom Provider

If you need to implement a custom metrics provider, you need to implement the
`Provider` interface:

```go
type Provider interface {
	// Counter creates a new counter with the given name.
	Counter(name string, options ...Option) Counter

	// Gauge creates a new gauge with the given name.
	Gauge(name string, options ...Option) Gauge

	// Histogram creates a new histogram with the given name.
	Histogram(name string, options ...Option) Histogram

	// Summary creates a new summary with the given name.
	Summary(name string, options ...Option) Summary

	// Timer creates a new timer with the given name.
	Timer(name string, options ...Option) Timer

	// Registry returns the registry used by this provider.
	Registry() Registry

	// Handler returns an HTTP handler for the metrics endpoint.
	Handler() Handler

	// Start starts the provider.
	Start(ctx Context) error

	// Stop stops the provider.
	Stop(ctx Context) error

	// WithTags creates a new provider with the given tags.
	WithTags(tags ...Tag) Provider
}
```

Then register your provider:

```go
metrics.RegisterProvider("myprovider", func(config metrics.Config) (metrics.Provider, error) {
	return myCustomProvider{}, nil
})
```

## Best Practices

1. **Use descriptive names**: Choose clear, descriptive metric names that follow
   a consistent naming pattern.

2. **Add descriptions**: Always add descriptions to your metrics to help others
   understand what they measure.

3. **Use tags wisely**: Tags are powerful but can lead to high cardinality. Use
   them for dimensions that have a bounded set of values.

4. **Don't overuse histograms**: Histograms and summaries are expensive. Use
   them only when needed.

5. **Start early**: Initialize your metrics at startup, not when they're first
   used. This ensures they appear in your metrics endpoint even if they haven't
   been used yet.

6. **Use the same buckets for similar metrics**: This makes it easier to compare
   metrics.

7. **Make metrics optional**: Always check if metrics are enabled before
   performing expensive operations.

8. **Use middleware for HTTP metrics**: Let the middleware handle the common
   metrics for you.

## Troubleshooting

### Common Issues

#### No metrics showing up

- Ensure the provider is started with `provider.Start()`
- Check that `Enabled` is set to `true` in the config
- Verify that the metrics endpoint is accessible

#### High cardinality issues

- Reduce the number of tag values, especially for unbounded dimensions
- Consider using buckets for continuous values
- Use tag filtering at the provider level

#### Slow performance

- Reduce the number of high-cardinality metrics
- Optimize histogram bucket configuration
- Consider sampling for high-volume metrics

## Conclusion

The metrics module provides a flexible and powerful way to instrument your
applications. By following the guidelines in this documentation, you can
effectively monitor your application's performance and behavior in production.
