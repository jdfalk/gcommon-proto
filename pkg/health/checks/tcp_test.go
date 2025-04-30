// file: pkg/health/checks/tcp_test.go
package checks

import (
	"context"
	"net"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// startTestServer starts a TCP server on a random port for testing.
// It returns the address of the server and a function to stop the server.
func startTestServer(t *testing.T) (string, func()) {
	// Start a TCP listener on a random port
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatalf("Failed to start test TCP server: %v", err)
	}

	// Accept connections in a goroutine
	done := make(chan struct{})
	go func() {
		defer close(done)
		for {
			conn, err := listener.Accept()
			if err != nil {
				// Listener closed
				return
			}
			// Close connection immediately after accepting
			conn.Close()
		}
	}()

	// Return the server address and a function to stop the server
	return listener.Addr().String(), func() {
		listener.Close()
		<-done // Wait for the goroutine to exit
	}
}

// TestTCPCheckSuccess tests that the TCP check correctly handles successful connections.
func TestTCPCheckSuccess(t *testing.T) {
	// Start a test TCP server
	address, stopServer := startTestServer(t)
	defer stopServer()

	// Create a TCP check targeting our test server
	check := NewTCPCheck("test-tcp", address, 1*time.Second)

	// Execute the check
	ctx := context.Background()
	result, err := check.Execute(ctx)

	// Validate results
	if err != nil {
		t.Errorf("TCP check execution failed: %v", err)
	}

	if result.Status() != health.StatusUp {
		t.Errorf("Expected status UP, got %v", result.Status())
	}

	// Check details
	details := result.Details()
	if details == nil {
		t.Fatal("Expected details to be set")
	}

	// Validate that the connection time is recorded
	if _, ok := details["connectionTime"]; !ok {
		t.Error("Expected connectionTime in details")
	}

	if address, ok := details["address"]; !ok || address != check.Address() {
		t.Errorf("Expected address %q in details, got %v", check.Address(), address)
	}
}

// TestTCPCheckFailure tests that the TCP check correctly handles connection failures.
func TestTCPCheckFailure(t *testing.T) {
	// Use a non-routable IP address to ensure failure
	address := "10.255.255.255:12345"

	// Create a TCP check with a short timeout
	check := NewTCPCheck("test-tcp-fail", address, 100*time.Millisecond)

	// Execute the check
	ctx := context.Background()
	result, err := check.Execute(ctx)

	// There should be no execution error
	if err != nil {
		t.Errorf("TCP check execution returned error: %v", err)
	}

	// The status should be DOWN due to connection failure
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status DOWN, got %v", result.Status())
	}

	// There should be an error in the result
	if result.Error() == nil {
		t.Error("Expected error in result, got nil")
	}

	// Check details
	details := result.Details()
	if details == nil {
		t.Fatal("Expected details to be set")
	}

	if address, ok := details["address"]; !ok || address != check.Address() {
		t.Errorf("Expected address %q in details, got %v", check.Address(), address)
	}
}

// TestTCPCheckTimeout tests that the TCP check correctly handles timeouts.
func TestTCPCheckTimeout(t *testing.T) {
	// Use a non-routable IP address that will cause a timeout
	address := "10.255.255.255:12345"

	// Create a TCP check with a very short timeout
	check := NewTCPCheck("test-tcp-timeout", address, 1*time.Millisecond)

	// Execute the check
	ctx := context.Background()
	result, err := check.Execute(ctx)

	// There should be no execution error
	if err != nil {
		t.Errorf("TCP check execution returned error: %v", err)
	}

	// The status should be DOWN due to timeout
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status DOWN, got %v", result.Status())
	}

	// There should be an error in the result
	if result.Error() == nil {
		t.Error("Expected error in result, got nil")
	}

	// Check for timeout error
	errStr := result.Error().Error()
	if errStr == "" {
		t.Error("Expected non-empty error string")
	}
}

// TestTCPCheckContextCancellation tests that the TCP check respects context cancellation.
func TestTCPCheckContextCancellation(t *testing.T) {
	// Use a non-routable IP address that would normally timeout
	address := "10.255.255.255:12345"

	// Create a TCP check with a long timeout
	check := NewTCPCheck("test-tcp-cancel", address, 10*time.Second)

	// Create a context and cancel it immediately
	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	// Execute the check with the cancelled context
	result, err := check.Execute(ctx)

	// There should be no execution error, just a result with DOWN status
	if err != nil {
		t.Errorf("TCP check execution returned error: %v", err)
	}

	// The status should be DOWN due to cancellation
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status DOWN, got %v", result.Status())
	}

	// There should be an error in the result indicating context cancellation
	if result.Error() == nil || result.Error().Error() != "context canceled" {
		t.Errorf("Expected 'context canceled' error, got %v", result.Error())
	}
}

// TestTCPCheckConfig tests the configuration options of the TCP check.
func TestTCPCheckConfig(t *testing.T) {
	address := "example.com:80"
	timeout := 5 * time.Second
	interval := 30 * time.Second
	checkType := health.TypeDependency

	// Create a TCP check with custom configuration
	check := NewTCPCheck("test-tcp-config", address, timeout,
		WithInterval(interval),
		WithType(checkType),
		WithEnabled(false),
	)

	// Verify configuration
	if check.Name() != "test-tcp-config" {
		t.Errorf("Expected name 'test-tcp-config', got %q", check.Name())
	}

	if check.Address() != address {
		t.Errorf("Expected address %q, got %q", address, check.Address())
	}

	if check.Timeout() != timeout {
		t.Errorf("Expected timeout %v, got %v", timeout, check.Timeout())
	}

	if check.Interval() != interval {
		t.Errorf("Expected interval %v, got %v", interval, check.Interval())
	}

	if check.Type() != checkType {
		t.Errorf("Expected type %v, got %v", checkType, check.Type())
	}

	if check.Enabled() {
		t.Error("Expected check to be disabled")
	}

	// Enable the check and verify
	check.SetEnabled(true)
	if !check.Enabled() {
		t.Error("Expected check to be enabled after SetEnabled(true)")
	}
}
