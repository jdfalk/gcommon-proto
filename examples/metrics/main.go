// Package main provides an example usage of the metrics module.
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	_ "github.com/jdfalk/gcommon/pkg/metrics/prometheus" // Import for side-effects
)

func main() {
	// Create a metrics provider
	config := metrics.Config{
		Provider:             "prometheus",
		Enabled:              true,
		Namespace:            "example",
		Subsystem:            "app",
		EnableRuntimeMetrics: true,
		Endpoint:             "/metrics",
		Tags: []metrics.Tag{
			{Key: "service", Value: "metrics-example"},
			{Key: "version", Value: "1.0.0"},
		},
		PrometheusConfig: &metrics.PrometheusConfig{
			Path:                   "/metrics",
			EnableGoCollector:      true,
			EnableProcessCollector: true,
		},
	}

	provider, err := metrics.NewProvider(config)
	if err != nil {
		log.Fatalf("Failed to create metrics provider: %v", err)
	}

	// Start the provider
	if err := provider.Start(context.Background()); err != nil {
		log.Fatalf("Failed to start metrics provider: %v", err)
	}
	defer provider.Stop(context.Background())

	// Create metrics
	requestCounter := provider.Counter("requests_total",
		metrics.WithDescription("Total number of requests"),
		metrics.WithTags(metrics.Tag{Key: "handler", Value: "main"}),
	)

	errorCounter := provider.Counter("errors_total",
		metrics.WithDescription("Total number of errors"),
	)

	activeConnections := provider.Gauge("active_connections",
		metrics.WithDescription("Number of active connections"),
	)

	requestDuration := provider.Histogram("request_duration_seconds",
		metrics.WithDescription("Request duration in seconds"),
		metrics.WithBuckets([]float64{0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5}),
	)

	responseSize := provider.Summary("response_size_bytes",
		metrics.WithDescription("Response size in bytes"),
	)

	requestTimer := provider.Timer("request_processing_seconds",
		metrics.WithDescription("Time to process request"),
	)

	// Create HTTP handlers to demonstrate metrics usage
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Start timer using stopwatch pattern
		stopwatch := requestTimer.NewStopwatch()
		defer stopwatch.Stop()

		// Increment request counter
		requestCounter.WithTags(
			metrics.Tag{Key: "method", Value: r.Method},
			metrics.Tag{Key: "path", Value: "/"},
		).Inc()

		// Update active connections gauge
		activeConnections.Inc()
		defer activeConnections.Dec()

		// Simulate work
		start := time.Now()
		time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
		duration := time.Since(start)

		// Record request duration
		requestDuration.WithTags(
			metrics.Tag{Key: "method", Value: r.Method},
		).Observe(duration.Seconds())

		// Simulate response size
		size := rand.Intn(1000) + 100
		responseSize.Observe(float64(size))

		// Randomly generate errors
		if rand.Intn(10) == 0 {
			errorCounter.WithTags(
				metrics.Tag{Key: "method", Value: r.Method},
				metrics.Tag{Key: "code", Value: "500"},
			).Inc()
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}

		// Respond with success
		fmt.Fprintf(w, "Hello World! Took %v to process.\n", duration)
	})

	// Expose the metrics endpoint
	http.Handle("/metrics", provider.Handler())

	// Start the HTTP server
	log.Println("Starting server on :8080")
	log.Println("Visit http://localhost:8080/ to generate metrics")
	log.Println("Visit http://localhost:8080/metrics to view metrics")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("HTTP server error: %v", err)
	}
}
