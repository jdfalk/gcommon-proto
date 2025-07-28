// file: pkg/health/grpc_test.go
package health

import (
	"context"
	"errors"
	"fmt"
	"net"
	"sync"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"

	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
)

const bufSize = 1024 * 1024

// setupGRPCServer creates a test gRPC server and client connection.
func setupGRPCServer(provider Provider) (*grpc.Server, *grpc.ClientConn, error) {
	// Create a buffer-based network connection
	lis := bufconn.Listen(bufSize)

	// Create a gRPC server
	server := grpc.NewServer()

	// Register health service
	healthServer := NewGRPCServer(provider)
	healthServer.Register(server)

	// Start server
	go func() {
		if err := server.Serve(lis); err != nil {
			panic(fmt.Sprintf("Failed to serve: %v", err))
		}
	}()

	// Create a custom dialer using the buffer connection
	bufDialer := func(context.Context, string) (net.Conn, error) {
		return lis.Dial()
	}

	// Create client connection
	ctx := context.Background()
	conn, err := grpc.DialContext(
		ctx,
		"bufnet",
		grpc.WithContextDialer(bufDialer),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)

	return server, conn, err
}

// TestGRPCServerCheck tests the Check RPC method.
func TestGRPCServerCheck(t *testing.T) {
	// Create a provider with some checks
	provider := NewProvider()

	// Register some checks
	upCheck := NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp).WithDetails(map[string]interface{}{
			"info": "everything is fine",
		}), nil
	})

	downCheck := NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).WithError(errors.New("service unavailable")), nil
	})

	degradedCheck := NewSimpleCheck("degraded-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDegraded).WithError(errors.New("service degraded")), nil
	})

	provider.Register(upCheck)
	provider.Register(downCheck)
	provider.Register(degradedCheck)

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthClient(conn)

	// Test cases
	testCases := []struct {
		name         string
		checkName    string
		expectStatus healthpb.StatusCode
		expectError  codes.Code
	}{
		{
			name:         "Up check",
			checkName:    "up-check",
			expectStatus: healthpb.StatusCode_STATUS_CODE_UP,
			expectError:  codes.OK,
		},
		{
			name:         "Down check",
			checkName:    "down-check",
			expectStatus: healthpb.StatusCode_STATUS_CODE_DOWN,
			expectError:  codes.OK,
		},
		{
			name:         "Degraded check",
			checkName:    "degraded-check",
			expectStatus: healthpb.StatusCode_STATUS_CODE_DEGRADED,
			expectError:  codes.OK,
		},
		{
			name:         "Non-existent check",
			checkName:    "non-existent",
			expectStatus: 0, // Doesn't matter
			expectError:  codes.NotFound,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Call Check RPC
			res, err := client.Check(context.Background(), &healthpb.CheckRequest{
				Name: tc.checkName,
			})

			// Verify error handling
			if tc.expectError != codes.OK {
				require.Error(t, err)
				st, ok := status.FromError(err)
				require.True(t, ok)
				assert.Equal(t, tc.expectError, st.Code())
				return
			}

			// Verify success case
			require.NoError(t, err)
			require.NotNil(t, res)
			assert.Equal(t, tc.expectStatus, res.Status)

			// If check is up, verify details
			if tc.checkName == "up-check" {
				require.NotNil(t, res.Details)
				info, ok := res.Details["info"]
				require.True(t, ok)
				assert.Equal(t, "everything is fine", info)
			}

			// If check is down, verify error
			if tc.checkName == "down-check" {
				require.NotNil(t, res.Error)
				assert.Equal(t, "service unavailable", res.Error)
			}
		})
	}

	// Test CheckAll RPC
	t.Run("CheckAll", func(t *testing.T) {
		res, err := client.CheckAll(context.Background(), &healthpb.CheckAllRequest{})
		require.NoError(t, err)
		require.NotNil(t, res)

		// Overall status should be DOWN because we have a down check
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DOWN, res.Status)

		// Should have 3 results
		require.Equal(t, 3, len(res.Results))

		// Get map of results by name
		resultMap := make(map[string]*healthpb.CheckResponse)
		for _, r := range res.Results {
			resultMap[r.Name] = r
		}

		// Verify individual results
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_UP, resultMap["up-check"].Status)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DOWN, resultMap["down-check"].Status)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DEGRADED, resultMap["degraded-check"].Status)
	})
}

// TestGRPCServerCheckDetailed tests the CheckDetailed RPC method.
func TestGRPCServerCheckDetailed(t *testing.T) {
	// Create a provider with some checks
	provider := NewProvider()

	// Register some checks with details
	upCheck := NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp).WithDetails(map[string]interface{}{
			"version": "1.2.3",
			"uptime":  "24h",
			"metrics": map[string]interface{}{
				"requests": 1000,
				"errors":   10,
			},
		}), nil
	})

	downCheck := NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("service unavailable")).
			WithDetails(map[string]interface{}{
				"lastSuccess": "2023-04-29T12:00:00Z",
				"attempts":    5,
			}), nil
	})

	provider.Register(upCheck)
	provider.Register(downCheck)

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthClient(conn)

	// Test CheckDetailed for all checks
	t.Run("CheckAllDetailed", func(t *testing.T) {
		res, err := client.CheckAllDetailed(context.Background(), &healthpb.CheckAllDetailedRequest{})
		require.NoError(t, err)
		require.NotNil(t, res)

		// Verify response
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DOWN, res.Status)
		require.Equal(t, 2, len(res.Results))

		// Get results by name
		var upResult, downResult *healthpb.CheckDetailedResponse
		for _, r := range res.Results {
			if r.Name == "up-check" {
				upResult = r
			} else if r.Name == "down-check" {
				downResult = r
			}
		}

		// Verify check details
		require.NotNil(t, upResult)
		require.NotNil(t, downResult)

		// Verify up-check details
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_UP, upResult.Status)
		assert.Empty(t, upResult.Error)
		require.NotNil(t, upResult.Details)
		assert.Equal(t, "1.2.3", upResult.Details["version"])
		assert.Equal(t, "24h", upResult.Details["uptime"])

		metrics, ok := upResult.Details["metrics"].(map[string]interface{})
		require.True(t, ok)
		assert.Equal(t, float64(1000), metrics["requests"])
		assert.Equal(t, float64(10), metrics["errors"])

		// Verify down-check details
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DOWN, downResult.Status)
		assert.Equal(t, "service unavailable", downResult.Error)
		require.NotNil(t, downResult.Details)
		assert.Equal(t, "2023-04-29T12:00:00Z", downResult.Details["lastSuccess"])
		assert.Equal(t, float64(5), downResult.Details["attempts"])
	})

	// Test individual check detailed
	t.Run("CheckDetailed", func(t *testing.T) {
		res, err := client.CheckDetailed(context.Background(), &healthpb.CheckDetailedRequest{
			Name: "up-check",
		})
		require.NoError(t, err)
		require.NotNil(t, res)

		assert.Equal(t, "up-check", res.Name)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_UP, res.Status)
		assert.Empty(t, res.Error)
		require.NotNil(t, res.Details)
		assert.Equal(t, "1.2.3", res.Details["version"])
	})

	// Test non-existent check
	t.Run("CheckDetailed_NotFound", func(t *testing.T) {
		_, err := client.CheckDetailed(context.Background(), &healthpb.CheckDetailedRequest{
			Name: "non-existent",
		})
		require.Error(t, err)
		st, ok := status.FromError(err)
		require.True(t, ok)
		assert.Equal(t, codes.NotFound, st.Code())
	})
}

// TestGRPCServerWatch tests the Watch streaming RPC method.
func TestGRPCServerWatch(t *testing.T) {
	// Create a provider
	provider := NewProvider()

	// Register a dynamic check that we'll change during the test
	var checkStatus = StatusUp
	var checkMutex = &sync.Mutex{}

	dynamicCheck := NewSimpleCheck("dynamic-check", func(ctx context.Context) (Result, error) {
		checkMutex.Lock()
		defer checkMutex.Unlock()
		return NewResult(checkStatus), nil
	})

	provider.Register(dynamicCheck)

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(provider)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthClient(conn)

	// Start watching the health status
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	watchClient, err := client.Watch(ctx, &healthpb.WatchRequest{
		Name: "dynamic-check",
	})
	require.NoError(t, err)

	// Create a channel to receive watch events
	eventCh := make(chan *healthpb.WatchResponse)
	errorCh := make(chan error)

	// Start a goroutine to receive events
	go func() {
		for {
			event, err := watchClient.Recv()
			if err != nil {
				errorCh <- err
				return
			}
			eventCh <- event
		}
	}()

	// Initial status should be UP
	select {
	case event := <-eventCh:
		assert.Equal(t, "dynamic-check", event.Name)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_UP, event.Status)
	case err := <-errorCh:
		t.Fatalf("Error receiving watch event: %v", err)
	case <-time.After(2 * time.Second):
		t.Fatal("Timeout waiting for initial watch event")
	}

	// Change status to DOWN
	checkMutex.Lock()
	checkStatus = StatusDown
	checkMutex.Unlock()

	// Trigger check execution to publish status change
	_, err = provider.Check(ctx, "dynamic-check")
	require.NoError(t, err)

	// Should receive DOWN status update
	select {
	case event := <-eventCh:
		assert.Equal(t, "dynamic-check", event.Name)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DOWN, event.Status)
	case err := <-errorCh:
		t.Fatalf("Error receiving watch event: %v", err)
	case <-time.After(2 * time.Second):
		t.Fatal("Timeout waiting for status change event")
	}

	// Change status to DEGRADED
	checkMutex.Lock()
	checkStatus = StatusDegraded
	checkMutex.Unlock()

	// Trigger check execution to publish status change
	_, err = provider.Check(ctx, "dynamic-check")
	require.NoError(t, err)

	// Should receive DEGRADED status update
	select {
	case event := <-eventCh:
		assert.Equal(t, "dynamic-check", event.Name)
		assert.Equal(t, healthpb.StatusCode_STATUS_CODE_DEGRADED, event.Status)
	case err := <-errorCh:
		t.Fatalf("Error receiving watch event: %v", err)
	case <-time.After(2 * time.Second):
		t.Fatal("Timeout waiting for status change event")
	}
}

// TestGRPCServerErrorHandling tests error handling in the gRPC server.
func TestGRPCServerErrorHandling(t *testing.T) {
	// Create mock provider that returns errors
	mockProv := &mockProvider{
		checkError:    errors.New("check execution failed"),
		checkAllError: errors.New("check all execution failed"),
	}

	// Setup gRPC server and client
	server, conn, err := setupGRPCServer(mockProv)
	require.NoError(t, err)
	defer server.Stop()
	defer conn.Close()

	// Create client
	client := healthpb.NewHealthClient(conn)

	// Test Check error handling
	t.Run("Check_Error", func(t *testing.T) {
		_, err := client.Check(context.Background(), &healthpb.CheckRequest{
			Name: "error-check",
		})
		require.Error(t, err)
		st, ok := status.FromError(err)
		require.True(t, ok)
		assert.Equal(t, codes.Internal, st.Code())
		assert.Contains(t, st.Message(), "check execution failed")
	})

	// Test CheckAll error handling
	t.Run("CheckAll_Error", func(t *testing.T) {
		_, err := client.CheckAll(context.Background(), &healthpb.CheckAllRequest{})
		require.Error(t, err)
		st, ok := status.FromError(err)
		require.True(t, ok)
		assert.Equal(t, codes.Internal, st.Code())
		assert.Contains(t, st.Message(), "check all execution failed")
	})

	// Test CheckDetailed error handling
	t.Run("CheckDetailed_Error", func(t *testing.T) {
		_, err := client.CheckDetailed(context.Background(), &healthpb.CheckDetailedRequest{
			Name: "error-check",
		})
		require.Error(t, err)
		st, ok := status.FromError(err)
		require.True(t, ok)
		assert.Equal(t, codes.Internal, st.Code())
		assert.Contains(t, st.Message(), "check execution failed")
	})

	// Test CheckAllDetailed error handling
	t.Run("CheckAllDetailed_Error", func(t *testing.T) {
		_, err := client.CheckAllDetailed(context.Background(), &healthpb.CheckAllDetailedRequest{})
		require.Error(t, err)
		st, ok := status.FromError(err)
		require.True(t, ok)
		assert.Equal(t, codes.Internal, st.Code())
		assert.Contains(t, st.Message(), "check all execution failed")
	})
}

// mockProvider extends mockProvider with additional error fields.
type mockProvider struct {
	checks        map[string]Result
	checkError    error
	checkAllError error
}

func (m *mockProvider) Register(check Check) {
	// Not implemented
}

func (m *mockProvider) Check(ctx context.Context, name string) (Result, error) {
	if m.checkError != nil {
		return nil, m.checkError
	}
	return nil, fmt.Errorf("check not found: %s", name)
}

func (m *mockProvider) CheckAll(ctx context.Context) (Result, error) {
	if m.checkAllError != nil {
		return nil, m.checkAllError
	}
	return NewResult(StatusDown), nil
}

func (m *mockProvider) Get(name string) (Check, bool) {
	return nil, false
}

func (m *mockProvider) List() []Check {
	return nil
}

func (m *mockProvider) CheckAsync(name string, callback ResultCallback) {
	// Not implemented
}

func (m *mockProvider) CheckAllAsync(callback ResultCallback) {
	// Not implemented
}

func (m *mockProvider) RunChecks(ctx context.Context) {
	// Not implemented
}

func (m *mockProvider) AddListener(listener Listener) {
	// Not implemented
}

func (m *mockProvider) RemoveListener(listener Listener) {
	// Not implemented
}
