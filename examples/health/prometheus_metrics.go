// file: examples/health/prometheus_metrics.go
package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/jdfalk/gcommon/pkg/health/checks"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Example demonstrating the health module with Prometheus metrics integration
func main() {
	// Create a Prometheus registry
	registry := prometheus.NewRegistry()

	// Create a health provider
	healthConfig := health.Config{
		Enabled:                true,
		CheckInterval:          10 * time.Second,
		DefaultTimeout:         1 * time.Second,
		EnableLivenessEndpoint: true,
		EnableReadinessEndpoint: true,
		LivenessPath:          "/health/live",
		ReadinessPath:         "/health/ready",
		DetailsPath:           "/health/details",
		LogStatusChanges:      true,
		MetricsEnabled:        true,
	}

	healthProvider, err := health.NewProvider(healthConfig)
	if err != nil {
		log.Fatalf("Failed to create health provider: %v", err)
	}

	// Create a Prometheus metrics provider for health checks
	metricsProvider := health.NewPrometheusMetricsProvider(registry, "app_health")

	// Register health metrics listener
	err = health.EnableMetricsReporting(healthProvider, metricsProvider)
	if err != nil {
		log.Fatalf("Failed to enable metrics reporting: %v", err)
	}

	// Register system health checks
	healthProvider.Register("cpu", checks.NewCPUCheck(70.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	healthProvider.Register("memory", checks.NewMemoryCheck(80.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	// Register a custom health check
	healthProvider.Register("example-check", health.CheckFunc(func(ctx context.Context) (health.Result, error) {
		// Simulate random health status
		time.Sleep(50 * time.Millisecond) // Simulate work

		// Return success status
		return health.NewResult(health.StatusUp).
			WithDetails(map[string]interface{}{
				"checked_at": time.Now().Format(time.RFC3339),
				"stat1": 123,
				"stat2": 456,
			}), nil
	}),
		health.WithType(health.TypeReadiness),
		health.WithInterval(15*time.Second),
	)

	// Create a Kubernetes probe handler
	probeConfig := health.DefaultKubernetesProbeConfig()
	kubeProbeHandler := health.NewKubernetesProbeHandler(healthProvider, probeConfig)

	// Set up HTTP server
	mux := http.NewServeMux()

	// Register health check handler
	mux.Handle("/health/", healthProvider.Handler())

	// Register Kubernetes probe handlers
	kubeProbeHandler.RegisterWithMux(mux)

	// Register Prometheus metrics handler
	mux.Handle("/metrics", promhttp.HandlerFor(registry, promhttp.HandlerOpts{}))

	// Start the HTTP server
	server := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	// Start background components
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := healthProvider.Start(ctx); err != nil {
		log.Fatalf("Failed to start health provider: %v", err)
	}

	// Start the server
	go func() {
		log.Printf("Starting server on :8080")
		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("Failed to start server: %v", err)
		}
	}()

	// Handle graceful shutdown
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)

	// Wait for shutdown signal
	<-stop
	log.Println("Shutting down...")

	// Create a deadline for graceful shutdown
	shutdownCtx, shutdownCancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer shutdownCancel()

	// Shut down the HTTP server
	if err := server.Shutdown(shutdownCtx); err != nil {
		log.Fatalf("Server shutdown failed: %v", err)
	}

	// Stop health provider
	if err := healthProvider.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop health provider: %v", err)
	}

	log.Println("Server stopped")
}
