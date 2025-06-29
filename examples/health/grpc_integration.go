// file: examples/health/grpc_integration.go
package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/jdfalk/gcommon/pkg/health/checks"
	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/protobuf/encoding/protojson"
)

// Example demonstrating the health module with gRPC integration
func main() {
	// Determine whether to run as server or client based on command-line argument
	if len(os.Args) > 1 && os.Args[1] == "client" {
		runClient()
		return
	}

	runServer()
}

// runServer runs a gRPC server with health checks
func runServer() {
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
	}

	healthProvider, err := health.NewProvider(healthConfig)
	if err != nil {
		log.Fatalf("Failed to create health provider: %v", err)
	}

	// Register health checks
	healthProvider.Register("cpu", checks.NewCPUCheck(70.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	healthProvider.Register("memory", checks.NewMemoryCheck(80.0),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	healthProvider.Register("goroutines", checks.NewGoroutinesCheck(1000),
		health.WithType(health.TypeLiveness),
		health.WithInterval(30*time.Second),
	)

	// Register a flaky health check that alternates between UP and DOWN
	// This demonstrates the watch functionality
	healthProvider.Register("flaky", health.CheckFunc(func(ctx context.Context) (health.Result, error) {
		// Alternate between UP and DOWN based on current second (even/odd)
		if time.Now().Second()%2 == 0 {
			return health.NewResult(health.StatusUp).WithDetails(map[string]interface{}{
				"reason": "Even second",
				"time":   time.Now().Format(time.RFC3339),
			}), nil
		}

		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("failing on odd second")).
			WithDetails(map[string]interface{}{
				"reason": "Odd second",
				"time":   time.Now().Format(time.RFC3339),
			}), nil
	}),
		health.WithType(health.TypeReadiness),
		health.WithInterval(1*time.Second),
	)

	// Register a remediable health check that can recover itself
	healthProvider.Register("remediable", checks.NewRemediableCheck(
		"remediable-check",
		func(ctx context.Context) (health.Result, error) {
			// Fail randomly with 10% probability
			if time.Now().UnixNano()%10 == 0 {
				return health.NewResult(health.StatusDown).
					WithError(fmt.Errorf("random failure")).
					WithDetails(map[string]interface{}{
						"time": time.Now().Format(time.RFC3339),
					}), nil
			}

			return health.NewResult(health.StatusUp).WithDetails(map[string]interface{}{
				"time": time.Now().Format(time.RFC3339),
			}), nil
		},
		func(ctx context.Context, result health.Result) error {
			// Remediation logic - in a real scenario this might restart a connection
			log.Printf("Remediating failure: %v", result.Error())
			// Simulate remediation work
			time.Sleep(100 * time.Millisecond)
			return nil
		},
	),
		health.WithType(health.TypeComponent),
		health.WithInterval(5*time.Second),
	)

	// Create a remediation manager
	remediationConfig := health.DefaultRemediationConfig()
	remediationConfig.Strategy = health.RemediationStrategyExponential
	remediationConfig.MaxAttempts = 3
	remediationConfig.OnRemediationStart = func(name string, attempt int) {
		log.Printf("Starting remediation for %s (attempt %d)", name, attempt)
	}
	remediationConfig.OnRemediationSuccess = func(name string, attempt int) {
		log.Printf("Remediation successful for %s (attempt %d)", name, attempt)
	}

	remediationManager := health.NewRemediationManager(healthProvider, remediationConfig)

	// Create a gRPC server
	grpcServer := grpc.NewServer()

	// Create and register the health gRPC service
	healthGRPC := health.NewGRPCServer(healthProvider)
	healthGRPC.Register(grpcServer)

	// Start health provider and remediation manager
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := healthProvider.Start(ctx); err != nil {
		log.Fatalf("Failed to start health provider: %v", err)
	}

	if err := remediationManager.Start(ctx); err != nil {
		log.Fatalf("Failed to start remediation manager: %v", err)
	}

	// Set up HTTP server for standard health checks
	httpServer := &http.Server{
		Addr:    ":8080",
		Handler: healthProvider.Handler(),
	}

	// Start the HTTP server
	go func() {
		log.Printf("Starting HTTP server on :8080")
		if err := httpServer.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("Failed to start HTTP server: %v", err)
		}
	}()

	// Start the gRPC server
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	go func() {
		log.Printf("Starting gRPC server on :50051")
		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalf("Failed to serve: %v", err)
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

	// Gracefully stop all components
	grpcServer.GracefulStop()

	if err := httpServer.Shutdown(shutdownCtx); err != nil {
		log.Printf("HTTP server shutdown failed: %v", err)
	}

	if err := healthProvider.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop health provider: %v", err)
	}

	if err := remediationManager.Stop(shutdownCtx); err != nil {
		log.Printf("Failed to stop remediation manager: %v", err)
	}

	log.Println("Server stopped")
}

// runClient runs a gRPC client to check server health
func runClient() {
	// Set up connection to the gRPC server
	conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("Failed to connect: %v", err)
	}
	defer conn.Close()

	// Create health client
	client := healthpb.NewHealthServiceClient(conn)

	// Perform a simple health check
	log.Println("Performing simple health check...")
	resp, err := client.Check(context.Background(), &healthpb.CheckRequest{
		Type: healthpb.CheckType_ALL,
	})
	if err != nil {
		log.Fatalf("Check failed: %v", err)
	}

	log.Printf("Health status: %s", resp.Status)

	// Perform a detailed health check
	log.Println("\nPerforming detailed health check...")
	detailedResp, err := client.CheckDetailed(context.Background(), &healthpb.CheckDetailedRequest{
		Type: healthpb.CheckType_ALL,
	})
	if err != nil {
		log.Fatalf("Detailed check failed: %v", err)
	}

	// Convert to JSON for prettier output
	marshaler := protojson.MarshalOptions{
		Indent:    "  ",
		Multiline: true,
	}
	jsonBytes, err := marshaler.Marshal(detailedResp)
	if err != nil {
		log.Fatalf("Failed to marshal response: %v", err)
	}
	log.Printf("Detailed health status:\n%s", string(jsonBytes))

	// Watch health changes
	log.Println("\nWatching health status changes for 20 seconds...")
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()

	stream, err := client.Watch(ctx, &healthpb.WatchRequest{
		Type: healthpb.CheckType_ALL,
	})
	if err != nil {
		log.Fatalf("Watch failed: %v", err)
	}

	for {
		watchResp, err := stream.Recv()
		if err != nil {
			log.Printf("Watch ended: %v", err)
			break
		}

		log.Printf("Health status changed: %s at %s",
			watchResp.Status,
			watchResp.Timestamp.AsTime().Format(time.RFC3339))
	}
}
