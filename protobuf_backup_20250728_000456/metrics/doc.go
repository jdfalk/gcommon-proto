// Package metrics provides a unified interface for metrics collection across different backends.
//
// This package abstracts away the specifics of various metrics backends (like Prometheus
// and OpenTelemetry) and provides a consistent API for creating and using metrics.
//
// # Basic Usage
//
// To use this package, first create a metrics provider with a configuration:
//
//	config := metrics.Config{
//	    Enabled:   true,
//	    Provider:  "prometheus",
//	    Namespace: "myapp",
//	    Tags: []metrics.Tag{
//	        {Key: "environment", Value: "production"},
//	    },
//	}
//
//	provider, err := metrics.NewProvider(config)
//	if err != nil {
//	    log.Fatalf("Failed to create metrics provider: %v", err)
//	}
//
//	ctx := context.Background()
//	provider.Start(ctx)
//	defer provider.Stop(ctx)
//
// Then create and use metrics:
//
//	// Create a counter
//	counter := provider.Counter("requests_total",
//	    metrics.WithDescription("Total number of requests"),
//	    metrics.WithTags(metrics.Tag{Key: "service", Value: "api"}),
//	)
//
//	// Increment the counter
//	counter.Inc()
//
//	// Create a gauge
//	gauge := provider.Gauge("active_connections",
//	    metrics.WithDescription("Number of active connections"),
//	)
//
//	// Set the gauge
//	gauge.Set(42)
//
//	// Create a histogram
//	histogram := provider.Histogram("request_duration_seconds",
//	    metrics.WithDescription("Request duration in seconds"),
//	    metrics.WithBuckets([]float64{0.01, 0.1, 0.5, 1, 5}),
//	)
//
//	// Observe a value
//	histogram.Observe(0.42)
//
//	// Create a timer
//	timer := provider.Timer("request_time_seconds",
//	    metrics.WithDescription("Request time in seconds"),
//	)
//
//	// Record a duration
//	timer.Record(time.Second * 2)
//
//	// Or time a function
//	timer.Time(func() {
//	    // Do something
//	})
//
// # HTTP Middleware
//
// The package also provides HTTP middleware for collecting request metrics:
//
//	mux := http.NewServeMux()
//	mux.Handle("/", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
//	    w.Write([]byte("Hello, world!"))
//	})))
//
// # Metric Exposition
//
// To expose metrics for scraping:
//
//	http.Handle("/metrics", provider.Handler())
//	http.ListenAndServe(":8080", nil)
//
// # Supported Providers
//
// The following providers are supported:
//
//   - Prometheus ("prometheus")
//   - OpenTelemetry ("opentelemetry" or "otel")
//
// # Dimensional Metrics with Tags
//
// All metrics support tags (labels) for dimensional metrics:
//
//	counter := provider.Counter("requests_total")
//
//	// Add dimensions
//	counter.WithTags(
//	    metrics.Tag{Key: "method", Value: "GET"},
//	    metrics.Tag{Key: "status", Value: "200"},
//	).Inc()
package metrics
