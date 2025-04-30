// file: examples/health/main.go
package main

import (
	"context"
	"database/sql"
	"flag"
	"log"
	"net"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/jdfalk/gcommon/pkg/health/checks"
)

var (
	httpAddr = flag.String("http", ":8080", "HTTP server address")
	grpcAddr = flag.String("grpc", ":9090", "gRPC server address")
)

func main() {
	flag.Parse()
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Create a health provider with default configuration
	config := health.DefaultConfig()
	config.LogStatusChanges = true
	config.MetricsEnabled = true
	config.EnableLivenessEndpoint = true
	config.EnableReadinessEndpoint = true

	provider, err := health.NewProvider(config)
	if err != nil {
		log.Fatalf("Failed to create health provider: %v", err)
	}

	// Create a Prometheus registry for metrics
	registry := prometheus.NewRegistry()

	// Create a Prometheus metrics provider
	metricsProvider := health.NewPrometheusMetricsProvider(registry, "myapp")

	// Enable metrics reporting
	if err := health.EnableMetricsReporting(provider, metricsProvider); err != nil {
		log.Fatalf("Failed to enable metrics reporting: %v", err)
	}

	// Register health checks

	// System check - monitors memory and GC
	systemCheck := checks.NewSystemCheck(
		checks.WithMemoryThreshold(90),
		checks.WithGCPauseThreshold(100*time.Millisecond),
	)
	provider.Register("system", systemCheck, health.WithType(health.TypeLiveness))

	// HTTP dependency check with automatic remediation
	httpCheck := checks.NewRemediableHTTPCheck("https://www.google.com",
		checks.WithTimeout(5*time.Second),
		checks.WithExpectedStatus(http.StatusOK),
		checks.WithAlternateURLs("https://www.cloudflare.com", "https://www.microsoft.com"),
		checks.WithMaxRetries(3),
		checks.WithRetryDelay(1*time.Second),
	)
	provider.Register("external-http", httpCheck, health.WithType(health.TypeReadiness))

	// TCP dependency check
	tcpCheck := checks.NewTCPCheck("www.google.com:443",
		checks.WithTCPTimeout(2*time.Second),
		checks.WithRetries(2, 500*time.Millisecond),
	)
	provider.Register("external-tcp", tcpCheck, health.WithType(health.TypeReadiness))

	// Redis check (using mock for example purposes)
	redisOpts := &redis.UniversalOptions{
		Addrs: []string{"localhost:6379"},
		DB:    0,
	}
	redisCheck := checks.NewRedisCheck(nil,
		checks.WithRedisOptions(redisOpts),
		checks.WithRedisTimeout(3*time.Second),
		checks.WithRedisKeyValidation("app:*", "session:*"),
		checks.WithRedisMaxMemoryUsage(80),
		checks.WithRedisCommand("dbsize", "DBSIZE"),
	)
	provider.Register("redis", redisCheck, health.WithType(health.TypeReadiness))

	// Simple function check
	provider.Register("custom", health.NewSimpleCheck("custom", func(ctx context.Context) (health.Result, error) {
		return health.NewResult(health.StatusUp).
			WithDetails(map[string]interface{}{
				"message": "Custom check is working!",
				"time":    time.Now().Format(time.RFC3339),
			}), nil
	}), health.WithType(health.TypeComponent))

	// Database check (using a mock DB for the example)
	// In a real app, you would use your actual DB connection
	mockDB, _ := sql.Open("mock", "mock://localhost:1234/testdb")
	dbCheck := checks.NewDBCheck(mockDB,
		checks.WithDBName("primary"),
		checks.WithQuery("SELECT 1"),
		checks.WithSlowThreshold(500*time.Millisecond),
	)
	provider.Register("database", dbCheck, health.WithType(health.TypeReadiness))

	// Set up remediation manager for automatic recovery
	remediationConfig := health.DefaultRemediationConfig()
	remediationConfig.Strategy = health.RemediationStrategyExponential
	remediationConfig.MaxAttempts = 5
	remediationConfig.InitialDelay = 1 * time.Second
	remediationConfig.MaxDelay = 30 * time.Second
	remediationConfig.BackoffFactor = 2.0

	// Add remediation logging
	remediationConfig.OnRemediationStart = func(name string, attempt int) {
		log.Printf("Starting remediation for %s (attempt %d)", name, attempt)
	}
	remediationConfig.OnRemediationSuccess = func(name string, attempt int) {
		log.Printf("Remediation successful for %s (attempt %d)", name, attempt)
	}
	remediationConfig.OnRemediationFailure = func(name string, attempt int, err error) {
		log.Printf("Remediation failed for %s (attempt %d): %v", name, attempt, err)
	}
	remediationConfig.OnRemediationExhausted = func(name string, attempts int) {
		log.Printf("Remediation exhausted for %s after %d attempts", name, attempts)
	}

	remediationMgr := health.NewRemediationManager(provider, remediationConfig)
	if err := remediationMgr.Start(ctx); err != nil {
		log.Fatalf("Failed to start remediation manager: %v", err)
	}

	// Start background health checking
	if err := provider.Start(ctx); err != nil {
		log.Fatalf("Failed to start health checker: %v", err)
	}

	// Add a health status change listener
	provider.AddListener(&statusChangeLogger{})

	// Start HTTP server
	httpServer := &http.Server{
		Addr:    *httpAddr,
		Handler: setupHTTPServer(provider, registry),
	}
	go func() {
		log.Printf("Starting HTTP server on %s", *httpAddr)
		if err := httpServer.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("HTTP server failed: %v", err)
		}
	}()

	// Start gRPC server
	grpcServer := grpc.NewServer()
	// Register health service
	healthServer := health.NewGRPCServer(provider)
	healthServer.Register(grpcServer)
	// Enable reflection for tools like grpcurl
	reflection.Register(grpcServer)

	lis, err := net.Listen("tcp", *grpcAddr)
	if err != nil {
		log.Fatalf("Failed to listen on %s: %v", *grpcAddr, err)
	}

	go func() {
		log.Printf("Starting gRPC server on %s", *grpcAddr)
		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalf("gRPC server failed: %v", err)
		}
	}()

	// Wait for interrupt signal
	sigCh := make(chan os.Signal, 1)
	signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)
	<-sigCh

	log.Println("Shutting down...")

	// Stop the health checker
	if err := provider.Stop(ctx); err != nil {
		log.Printf("Error stopping health checker: %v", err)
	}

	// Stop the remediation manager
	if err := remediationMgr.Stop(ctx); err != nil {
		log.Printf("Error stopping remediation manager: %v", err)
	}

	// Shutdown HTTP server
	shutdownCtx, shutdownCancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer shutdownCancel()

	if err := httpServer.Shutdown(shutdownCtx); err != nil {
		log.Printf("HTTP server shutdown error: %v", err)
	}

	// Stop gRPC server
	grpcServer.GracefulStop()
}

// setupHTTPServer configures the HTTP server with routes
func setupHTTPServer(provider health.Provider, registry *prometheus.Registry) http.Handler {
	mux := http.NewServeMux()

	// Mount the health handler at the root health endpoint
	mux.Handle("/health/", http.StripPrefix("/health", provider.Handler()))

	// Add Prometheus metrics endpoint
	mux.Handle("/metrics", promhttp.HandlerFor(registry, promhttp.HandlerOpts{}))

	// Add other routes
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Health Check Example Service\n"))
		w.Write([]byte("Visit /health for health status\n"))
		w.Write([]byte("Visit /metrics for Prometheus metrics\n"))
	})

	return mux
}

// statusChangeLogger implements the health.Listener interface for logging health status changes
type statusChangeLogger struct{}

// OnStatusChange is called when a health status changes
func (l *statusChangeLogger) OnStatusChange(name string, previous, current health.Result) {
	log.Printf("Health status changed for %s: %s -> %s",
		name, previous.Status().String(), current.Status().String())

	if err := current.Error(); err != nil {
		log.Printf("Health check error for %s: %v", name, err)
	}
}
