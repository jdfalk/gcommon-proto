// Package main provides an example of using the metrics module.
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/middleware"
)

func main() {
	// Create a metrics configuration
	config := metrics.Config{
		Enabled:          true,
		Provider:         "prometheus", // Could also be "opentelemetry" or "otel"
		Namespace:        "example",
		Subsystem:        "app",
		EnableRuntimeMetrics: true,
		Tags: []metrics.Tag{
			{Key: "environment", Value: "development"},
			{Key: "service", Value: "example-service"},
		},
		PrometheusConfig: &metrics.PrometheusConfig{
			// Optionally configure Prometheus-specific settings
			EnableGoCollector:      true,
			EnableProcessCollector: true,
		},
	}

	// Create a metrics provider
	provider, err := metrics.NewProvider(config)
	if err != nil {
		log.Fatalf("Failed to create metrics provider: %v", err)
	}

	// Start the provider
	ctx := context.Background()
	if err := provider.Start(ctx); err != nil {
		log.Fatalf("Failed to start metrics provider: %v", err)
	}
	defer provider.Stop(ctx)

	// Create some example metrics
	counter := provider.Counter(
		"example_counter",
		metrics.WithDescription("Example counter metric"),
		metrics.WithTags(metrics.Tag{Key: "type", Value: "example"}),
	)

	gauge := provider.Gauge(
		"example_gauge",
		metrics.WithDescription("Example gauge metric"),
		metrics.WithTags(metrics.Tag{Key: "type", Value: "example"}),
	)

	histogram := provider.Histogram(
		"example_histogram",
		metrics.WithDescription("Example histogram metric"),
		metrics.WithBuckets([]float64{0.1, 0.5, 1, 5, 10}),
		metrics.WithTags(metrics.Tag{Key: "type", Value: "example"}),
	)

	timer := provider.Timer(
		"example_timer",
		metrics.WithDescription("Example timer metric"),
		metrics.WithTags(metrics.Tag{Key: "type", Value: "example"}),
	)

	// Create a context that cancels on SIGINT or SIGTERM
	signalCtx, cancel := signal.NotifyContext(ctx, syscall.SIGINT, syscall.SIGTERM)
	defer cancel()

	// Create an HTTP server for metrics and example endpoints
	mux := http.NewServeMux()

	// Add metrics endpoint
	mux.Handle("/metrics", provider.Handler())

	// Add some example endpoints with metrics middleware
	mux.Handle("/", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, world!\n"))
	})))

	mux.Handle("/counter", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		counter.Inc()
		w.Write([]byte(fmt.Sprintf("Counter value: %v\n", counter.Value())))
	})))

	mux.Handle("/gauge", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		value := rand.Float64() * 100
		gauge.Set(value)
		w.Write([]byte(fmt.Sprintf("Gauge value: %v\n", value)))
	})))

	mux.Handle("/histogram", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		value := rand.Float64() * 10
		histogram.Observe(value)
		w.Write([]byte(fmt.Sprintf("Observed value: %v\n", value)))
	})))

	mux.Handle("/timer", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Create a stopwatch
		stopwatch := timer.NewStopwatch()
		defer stopwatch.Stop()

		// Simulate some work
		time.Sleep(time.Duration(rand.Intn(500)) * time.Millisecond)
		w.Write([]byte("Timer recorded\n"))
	})))

	mux.Handle("/error", middleware.StandardMetrics(provider)(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Simulate an error response
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("Internal Server Error\n"))
	})))

	// Start a background task that updates metrics
	go func() {
		ticker := time.NewTicker(1 * time.Second)
		defer ticker.Stop()

		counterWithLabel := counter.WithTags(metrics.Tag{Key: "background", Value: "true"})
		gaugeWithLabel := gauge.WithTags(metrics.Tag{Key: "background", Value: "true"})

		i := 0
		for {
			select {
			case <-ticker.C:
				i++
				counterWithLabel.Inc()
				gaugeWithLabel.Set(float64(i % 10))

				// Also use the timer to measure a function's execution time
				timer.WithTags(metrics.Tag{Key: "background", Value: "true"}).Time(func() {
					// Simulate some work
					time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
				})
			case <-signalCtx.Done():
				return
			}
		}
	}()

	// Start the HTTP server
	server := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	// Start server in a goroutine
	go func() {
		log.Printf("Starting server on :8080")
		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("Failed to start server: %v", err)
		}
	}()

	// Wait for signal to shut down
	<-signalCtx.Done()
	log.Println("Shutting down...")

	// Create a context with timeout for shutdown
	shutdownCtx, shutdownCancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer shutdownCancel()

	// Shutdown the server
	if err := server.Shutdown(shutdownCtx); err != nil {
		log.Fatalf("Server shutdown failed: %v", err)
	}

	log.Println("Server stopped")
}
