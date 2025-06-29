// file: examples/health/kubernetes_integration.go
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
	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/prometheus"
)

func main() {
	// Create a metrics provider
	metricsConfig := metrics.Config{
		Enabled:              true,
		Provider:             "prometheus",
		Namespace:            "example",
		Subsystem:            "health",
		EnableRuntimeMetrics: true,
		PrometheusConfig: &metrics.PrometheusConfig{
			EnableGoCollector:      true,
			EnableProcessCollector: true,
		},
	}

	metricsProvider, err := metrics.NewProvider(metricsConfig)
	if err != nil {
		log.Fatalf("Failed to create metrics provider: %v", err)
	}

	// Create a health provider
	healthConfig := health.Config{
		Enabled:                 true,
		CheckInterval:           10 * time.Second,
		DefaultTimeout:          1 * time.Second,
		EnableLivenessEndpoint:  true,
		EnableReadinessEndpoint: true,
		LivenessPath:            "/health/live",
		ReadinessPath:           "/health/ready",
		DetailsPath:             "/health/details",
		LogStatusChanges:        true,
		MetricsEnabled:          true,
	}

	healthProvider, err := health.NewProvider(healthConfig)
	if err != nil {
		log.Fatalf("Failed to create health provider: %v", err)
	}

	// Create a metrics collector for health checks
	metricsConfig := health.DefaultMetricsConfig()
	metricsCollector := health.NewMetricsCollector(healthProvider, metricsProvider, metricsConfig)

	// Create a Kubernetes probe handler
	probeConfig := health.DefaultKubernetesProbeConfig()
	kubeProbeHandler := health.NewKubernetesProbeHandler(healthProvider, probeConfig)

	// Register health checks

	// System checks
	healthProvider.Register("cpu", checks.NewCPUCheck(70.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	healthProvider.Register("memory", checks.NewMemoryCheck(80.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	healthProvider.Register("disk", checks.NewDiskCheck("/", 90.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(60*time.Second),
	)

	healthProvider.Register("goroutines", checks.NewGoroutinesCheck(1000),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	// Dependency checks
	healthProvider.Register("example-api", checks.NewHTTPCheck("https://example.com/health"),
		health.WithType(health.TypeReadiness),
		health.WithTimeout(2*time.Second),
		health.WithInterval(15*time.Second),
	)

	// Custom check with remediation
	healthProvider.Register("database-connection",
		checks.NewRemediableHTTPCheck(
			"http://localhost:8080/db/ping",
			func(ctx context.Context, result health.Result) error {
				log.Println("Attempting to reconnect to database...")
				// In a real implementation, this would reconnect to the database
				time.Sleep(100 * time.Millisecond)
				return nil
			},
		),
		health.WithType(health.TypeReadiness),
		health.WithTimeout(1*time.Second),
		health.WithInterval(15*time.Second),
	)

	// Create a remediation manager
	remediationConfig := health.DefaultRemediationConfig()
	remediationConfig.OnRemediationStart = func(name string, attempt int) {
		log.Printf("Starting remediation for %s (attempt %d)", name, attempt)
	}
	remediationConfig.OnRemediationSuccess = func(name string, attempt int) {
		log.Printf("Remediation successful for %s (attempt %d)", name, attempt)
	}
	remediationConfig.OnRemediationFailure = func(name string, attempt int, err error) {
		log.Printf("Remediation failed for %s (attempt %d): %v", name, attempt, err)
	}

	remediationManager := health.NewRemediationManager(healthProvider, remediationConfig)

	// Set up HTTP server
	mux := http.NewServeMux()

	// Register health check handler
	mux.Handle("/health/", healthProvider.Handler())

	// Register Kubernetes probe handlers
	kubeProbeHandler.RegisterWithMux(mux)

	// Register metrics handler
	mux.Handle("/metrics", metricsProvider.Handler())

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

	if err := metricsCollector.Start(ctx); err != nil {
		log.Fatalf("Failed to start metrics collector: %v", err)
	}

	if err := remediationManager.Start(ctx); err != nil {
		log.Fatalf("Failed to start remediation manager: %v", err)
	}

	if err := metricsProvider.Start(ctx); err != nil {
		log.Fatalf("Failed to start metrics provider: %v", err)
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

	// Stop background components
	cancel()

	if err := healthProvider.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop health provider: %v", err)
	}

	if err := metricsCollector.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop metrics collector: %v", err)
	}

	if err := remediationManager.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop remediation manager: %v", err)
	}

	if err := metricsProvider.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop metrics provider: %v", err)
	}

	log.Println("Server stopped")
}
