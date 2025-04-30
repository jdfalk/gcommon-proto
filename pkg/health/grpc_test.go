// file: pkg/health/grpc_test.go
package health

import (
	"context"
	"errors"
	"net"
	"net/http"
	"testing"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/test/bufconn"

	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
)

const bufSize = 1024 * 1024

// setupGRPCServer creates a test gRPC server and client connection.
func setupGRPCServer(provider Provider) (*grpc.Server, *grpc.ClientConn, error) {
	lis := bufconn.Listen(bufSize)
	server := grpc.NewServer()

	// Register health service
	healthServer := NewGRPCServer(provider)
	healthServer.Register(server)

	// Start server
	go func() {
		if err := server.Serve(lis); err != nil {
			panic(err)
		}
	}()

	// Create client connection
	ctx := context.Background()
	dialer := func(context.Context, string) (net.Conn, error) {
		return lis.Dial()
	}

	conn, err := grpc.DialContext(ctx, "bufnet",
		grpc.WithContextDialer(dialer),
		grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		return nil, nil, err
	}

	return server, conn, nil
}

// TestGRPCServerCheck tests the Check RPC method.
func TestGRPCServerCheck(t *testing.T) {
	// Create a provider with some checks
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeLiveness))

	provider.Register("down-check", NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("test error")), nil
	}), WithType(TypeReadiness))

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	if err != nil {
		t.Fatalf("Failed to setup gRPC server: %v", err)
	}
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthServiceClient(conn)

	// Test cases
	testCases := []struct {
		name           string
		checkType      healthpb.CheckType
		expectedStatus healthpb.Status
	}{
		{
			name:           "All checks",
			checkType:      healthpb.CheckType_ALL,
			expectedStatus: healthpb.Status_DOWN, // DOWN is worst status among all checks
		},
		{
			name:           "Liveness check",
			checkType:      healthpb.CheckType_LIVENESS,
			expectedStatus: healthpb.Status_UP,
		},
		{
			name:           "Readiness check",
			checkType:      healthpb.CheckType_READINESS,
			expectedStatus: healthpb.Status_DOWN,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Make request
			req := &healthpb.CheckRequest{
				Type: tc.checkType,
			}

			resp, err := client.Check(context.Background(), req)
			if err != nil {
				t.Fatalf("Check RPC failed: %v", err)
			}

			// Verify response
			if resp.Status != tc.expectedStatus {
				t.Errorf("Expected status %v, got %v", tc.expectedStatus, resp.Status)
			}

			if resp.Timestamp == nil {
				t.Error("Expected timestamp to be set")
			}
		})
	}
}

// TestGRPCServerCheckDetailed tests the CheckDetailed RPC method.
func TestGRPCServerCheckDetailed(t *testing.T) {
	// Create a provider with some checks
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks with details
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp).
			WithDetails(map[string]interface{}{
				"version": "1.0.0",
				"count":   42,
			}), nil
	}), WithType(TypeLiveness))

	provider.Register("down-check", NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("test error")).
			WithDetails(map[string]interface{}{
				"errorCode": 500,
			}), nil
	}), WithType(TypeReadiness))

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	if err != nil {
		t.Fatalf("Failed to setup gRPC server: %v", err)
	}
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthServiceClient(conn)

	// Test CheckDetailed for all checks
	req := &healthpb.CheckDetailedRequest{
		Type: healthpb.CheckType_ALL,
	}

	resp, err := client.CheckDetailed(context.Background(), req)
	if err != nil {
		t.Fatalf("CheckDetailed RPC failed: %v", err)
	}

	// Verify response
	if resp.Status != healthpb.Status_DOWN {
		t.Errorf("Expected status DOWN, got %v", resp.Status)
	}

	if resp.StatusInfo == nil {
		t.Fatal("Expected StatusInfo to be set")
	}

	if resp.Checks == nil {
		t.Fatal("Expected Checks map to be set")
	}

	// Verify check details
	if len(resp.Checks) != 2 {
		t.Errorf("Expected 2 checks, got %d", len(resp.Checks))
	}

	// Verify up-check details
	upCheck, ok := resp.Checks["up-check"]
	if !ok {
		t.Fatal("up-check not found in response")
	}

	if upCheck.Status != healthpb.Status_UP {
		t.Errorf("Expected up-check status UP, got %v", upCheck.Status)
	}

	if upCheck.Error != "" {
		t.Errorf("Expected no error for up-check, got %q", upCheck.Error)
	}

	if upCheck.Details == nil {
		t.Fatal("Expected up-check details to be set")
	}

	if upCheck.Details["version"] != "1.0.0" {
		t.Errorf("Expected version 1.0.0, got %q", upCheck.Details["version"])
	}

	if upCheck.Details["count"] != "42" {
		t.Errorf("Expected count 42, got %q", upCheck.Details["count"])
	}

	// Verify down-check details
	downCheck, ok := resp.Checks["down-check"]
	if !ok {
		t.Fatal("down-check not found in response")
	}

	if downCheck.Status != healthpb.Status_DOWN {
		t.Errorf("Expected down-check status DOWN, got %v", downCheck.Status)
	}

	if downCheck.Error != "test error" {
		t.Errorf("Expected error 'test error', got %q", downCheck.Error)
	}

	if downCheck.Details == nil {
		t.Fatal("Expected down-check details to be set")
	}

	if downCheck.Details["errorCode"] != "500" {
		t.Errorf("Expected errorCode 500, got %q", downCheck.Details["errorCode"])
	}
}

// TestGRPCServerWatch tests the Watch streaming RPC method.
func TestGRPCServerWatch(t *testing.T) {
	// Create a provider with a variable check
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Create a variable check that we can change
	variableStatus := StatusUp
	variableCheck := NewSimpleCheck("variable-check", func(ctx context.Context) (Result, error) {
		return NewResult(variableStatus), nil
	})

	provider.Register("variable-check", variableCheck, WithType(TypeLiveness))

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	if err != nil {
		t.Fatalf("Failed to setup gRPC server: %v", err)
	}
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthServiceClient(conn)

	// Start watching
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	req := &healthpb.WatchRequest{
		Type: healthpb.CheckType_ALL,
	}

	watchClient, err := client.Watch(ctx, req)
	if err != nil {
		t.Fatalf("Watch RPC failed: %v", err)
	}

	// Receive initial status
	resp, err := watchClient.Recv()
	if err != nil {
		t.Fatalf("Failed to receive initial status: %v", err)
	}

	// Verify initial status
	if resp.Status != healthpb.Status_UP {
		t.Errorf("Expected initial status UP, got %v", resp.Status)
	}

	// Change status and trigger an update
	variableStatus = StatusDown

	// Execute a check to broadcast the status change
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Give some time for the update to propagate
	time.Sleep(100 * time.Millisecond)

	// Force another check to ensure the status change is detected
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Wait for the update
	resp, err = watchClient.Recv()
	if err != nil {
		t.Fatalf("Failed to receive status update: %v", err)
	}

	// Verify updated status
	if resp.Status != healthpb.Status_DOWN {
		t.Errorf("Expected updated status DOWN, got %v", resp.Status)
	}
}

// TestGRPCServerErrorHandling tests error handling in the gRPC server.
func TestGRPCServerErrorHandling(t *testing.T) {
	// Create a mock provider that returns errors
	mockProvider := &mockProvider{
		checkAllErr:     errors.New("check all error"),
		checkLivenessErr: errors.New("check liveness error"),
		checkReadinessErr: errors.New("check readiness error"),
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockProvider)
	if err != nil {
		t.Fatalf("Failed to setup gRPC server: %v", err)
	}
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthServiceClient(conn)

	// Test error handling for Check
	_, err = client.Check(context.Background(), &healthpb.CheckRequest{
		Type: healthpb.CheckType_ALL,
	})
	if err == nil {
		t.Fatal("Expected Check to return an error")
	}

	// Test error handling for CheckDetailed
	_, err = client.CheckDetailed(context.Background(), &healthpb.CheckDetailedRequest{
		Type: healthpb.CheckType_LIVENESS,
	})
	if err == nil {
		t.Fatal("Expected CheckDetailed to return an error")
	}

	// Test error handling for Watch
	watchClient, err := client.Watch(context.Background(), &healthpb.WatchRequest{
		Type: healthpb.CheckType_READINESS,
	})
	if err != nil {
		t.Fatalf("Watch RPC failed: %v", err)
	}

	// We should get an error when receiving the first message
	_, err = watchClient.Recv()
	if err == nil {
		t.Fatal("Expected Watch to return an error")
	}
}

// mockProvider extends mockProvider from http_test.go with additional error fields.
type mockProvider struct {
	checks            map[string]Check
	checkAllErr       error
	checkLivenessErr  error
	checkReadinessErr error
}

func (p *mockProvider) Register(name string, check Check, options ...CheckOption) error {
	return nil
}

func (p *mockProvider) Unregister(name string) error {
	return nil
}

func (p *mockProvider) Get(name string) (Check, bool) {
	check, ok := p.checks[name]
	return check, ok
}

func (p *mockProvider) CheckAll(ctx context.Context) (Result, error) {
	if p.checkAllErr != nil {
		return nil, p.checkAllErr
	}
	return NewResult(StatusUp), nil
}

func (p *mockProvider) CheckLiveness(ctx context.Context) (Result, error) {
	if p.checkLivenessErr != nil {
		return nil, p.checkLivenessErr
	}
	return NewResult(StatusUp), nil
}

func (p *mockProvider) CheckReadiness(ctx context.Context) (Result, error) {
	if p.checkReadinessErr != nil {
		return nil, p.checkReadinessErr
	}
	return NewResult(StatusUp), nil
}

func (p *mockProvider) Handler() http.Handler {
	return nil
}

func (p *mockProvider) Start(ctx context.Context) error {
	return nil
}

func (p *mockProvider) Stop(ctx context.Context) error {
	return nil
}

func (p *mockProvider) AddListener(listener Listener) error {
	return nil
}

func (p *mockProvider) RemoveListener(listener Listener) error {
	return nil
}
