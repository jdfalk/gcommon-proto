// file: pkg/health/provider_test.go
package health

import (
	"context"
	"errors"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"testing"
	"time"
)

// TestProviderRegisterUnregister verifies that checks can be registered and unregistered correctly.
func TestProviderRegisterUnregister(t *testing.T) {
	// Create a provider with default config
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Create a test check
	checkName := "test-check"
	check := NewSimpleCheck(checkName, func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	})

	// Register the check
	err = provider.Register(checkName, check)
	if err != nil {
		t.Fatalf("Failed to register check: %v", err)
	}

	// Verify the check was registered
	registeredCheck, exists := provider.Get(checkName)
	if !exists {
		t.Fatal("Expected check to be registered, but it wasn't found")
	}
	if registeredCheck != check {
		t.Fatalf("Expected registered check to be the same as original, got %v", registeredCheck)
	}

	// Try to register with the same name again, should fail
	err = provider.Register(checkName, check)
	if err == nil {
		t.Fatal("Expected error when registering duplicate check name")
	}

	// Unregister the check
	err = provider.Unregister(checkName)
	if err != nil {
		t.Fatalf("Failed to unregister check: %v", err)
	}

	// Verify the check was unregistered
	_, exists = provider.Get(checkName)
	if exists {
		t.Fatal("Expected check to be unregistered, but it was found")
	}

	// Try to unregister again, should fail
	err = provider.Unregister(checkName)
	if err == nil {
		t.Fatal("Expected error when unregistering non-existent check")
	}
}

// TestProviderCheckAll verifies that CheckAll correctly executes all registered checks.
func TestProviderCheckAll(t *testing.T) {
	// Create a provider with default config
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register checks with different statuses
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}))

	provider.Register("down-check", NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("intentional failure")), nil
	}))

	provider.Register("degraded-check", NewSimpleCheck("degraded-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDegraded).
			WithError(errors.New("partially degraded")), nil
	}))

	// Execute all checks
	result, err := provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Verify the result
	if result.Status() != StatusDown {
		t.Errorf("Expected status Down, got %v", result.Status())
	}

	// Verify child results
	children := result.Children()
	if len(children) != 3 {
		t.Fatalf("Expected 3 child results, got %d", len(children))
	}

	// Verify details
	details := result.Details()
	if details["total"] != 3 {
		t.Errorf("Expected total=3, got %v", details["total"])
	}
	if details["up"] != 1 {
		t.Errorf("Expected up=1, got %v", details["up"])
	}
	if details["down"] != 1 {
		t.Errorf("Expected down=1, got %v", details["down"])
	}
	if details["degraded"] != 1 {
		t.Errorf("Expected degraded=1, got %v", details["degraded"])
	}
}

// TestProviderCheckLivenessReadiness verifies that CheckLiveness and CheckReadiness correctly filter checks by type.
func TestProviderCheckLivenessReadiness(t *testing.T) {
	// Create a provider with default config
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register checks with different types
	provider.Register("liveness-up", NewSimpleCheck("liveness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeLiveness))

	provider.Register("liveness-down", NewSimpleCheck("liveness-down", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("intentional failure")), nil
	}), WithType(TypeLiveness))

	provider.Register("readiness-up", NewSimpleCheck("readiness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeReadiness))

	provider.Register("component-up", NewSimpleCheck("component-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeComponent))

	// Test CheckLiveness
	livenessResult, err := provider.CheckLiveness(context.Background())
	if err != nil {
		t.Fatalf("CheckLiveness failed: %v", err)
	}

	// Verify liveness result
	if livenessResult.Status() != StatusDown {
		t.Errorf("Expected liveness status Down, got %v", livenessResult.Status())
	}

	livenessChildren := livenessResult.Children()
	if len(livenessChildren) != 2 {
		t.Fatalf("Expected 2 liveness checks, got %d", len(livenessChildren))
	}

	// Test CheckReadiness
	readinessResult, err := provider.CheckReadiness(context.Background())
	if err != nil {
		t.Fatalf("CheckReadiness failed: %v", err)
	}

	// Verify readiness result
	if readinessResult.Status() != StatusUp {
		t.Errorf("Expected readiness status Up, got %v", readinessResult.Status())
	}

	readinessChildren := readinessResult.Children()
	if len(readinessChildren) != 1 {
		t.Fatalf("Expected 1 readiness check, got %d", len(readinessChildren))
	}

	// Verify check type in details
	if readinessResult.Details()["type"] != TypeReadiness.String() {
		t.Errorf("Expected type=%s, got %v", TypeReadiness.String(), readinessResult.Details()["type"])
	}
}

// TestProviderHandler verifies that the HTTP handler correctly responds to health check requests.
func TestProviderHandler(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	config.Endpoint = "/health"
	config.LivenessPath = "/live"
	config.ReadinessPath = "/ready"
	config.EnableLivenessEndpoint = true
	config.EnableReadinessEndpoint = true

	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register checks with different types
	provider.Register("liveness-up", NewSimpleCheck("liveness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeLiveness))

	provider.Register("readiness-up", NewSimpleCheck("readiness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeReadiness))

	// Get the HTTP handler
	handler := provider.Handler()

	// Test cases for different endpoints
	testCases := []struct {
		name           string
		path           string
		expectedStatus int
		expectedBody   string
	}{
		{
			name:           "Root health endpoint",
			path:           "/health",
			expectedStatus: http.StatusOK,
			expectedBody:   `"status":"UP"`,
		},
		{
			name:           "Liveness endpoint",
			path:           "/health/live",
			expectedStatus: http.StatusOK,
			expectedBody:   `"status":"UP"`,
		},
		{
			name:           "Readiness endpoint",
			path:           "/health/ready",
			expectedStatus: http.StatusOK,
			expectedBody:   `"status":"UP"`,
		},
		{
			name:           "Details endpoint",
			path:           "/health/details",
			expectedStatus: http.StatusOK,
			expectedBody:   `"checks"`,
		},
		{
			name:           "Non-existent endpoint",
			path:           "/health/invalid",
			expectedStatus: http.StatusNotFound,
			expectedBody:   ``,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			req, err := http.NewRequest("GET", tc.path, nil)
			if err != nil {
				t.Fatalf("Failed to create request: %v", err)
			}

			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)

			// Check status code
			if rr.Code != tc.expectedStatus {
				t.Errorf("Expected status %d, got %d", tc.expectedStatus, rr.Code)
			}

			// For success cases, check response body
			if tc.expectedStatus == http.StatusOK && tc.expectedBody != "" {
				if !strings.Contains(rr.Body.String(), tc.expectedBody) {
					t.Errorf("Expected body to contain %q, got %q", tc.expectedBody, rr.Body.String())
				}
			}
		})
	}
}

// TestProviderStartStop verifies that the provider correctly starts and stops background health checking.
func TestProviderStartStop(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	config.CheckInterval = 100 * time.Millisecond // Short interval for testing
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Create a check with a counter to track executions
	var counter int
	var counterMu sync.Mutex

	provider.Register("counter-check", NewSimpleCheck("counter-check", func(ctx context.Context) (Result, error) {
		counterMu.Lock()
		defer counterMu.Unlock()
		counter++
		return NewResult(StatusUp), nil
	}))

	// Start the provider
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	err = provider.Start(ctx)
	if err != nil {
		t.Fatalf("Failed to start provider: %v", err)
	}

	// Wait for multiple executions
	time.Sleep(350 * time.Millisecond)

	// Stop the provider
	err = provider.Stop(ctx)
	if err != nil {
		t.Fatalf("Failed to stop provider: %v", err)
	}

	// Check that the counter was incremented
	counterMu.Lock()
	initialCount := counter
	counterMu.Unlock()

	if initialCount < 2 {
		t.Errorf("Expected at least 2 check executions, got %d", initialCount)
	}

	// Wait to verify no more executions
	time.Sleep(200 * time.Millisecond)

	// Check counter again
	counterMu.Lock()
	finalCount := counter
	counterMu.Unlock()

	if finalCount != initialCount {
		t.Errorf("Expected counter to stay at %d after stop, got %d", initialCount, finalCount)
	}

	// Try to start again, should succeed
	err = provider.Start(ctx)
	if err != nil {
		t.Fatalf("Failed to restart provider: %v", err)
	}

	// Stop again
	err = provider.Stop(ctx)
	if err != nil {
		t.Fatalf("Failed to stop provider: %v", err)
	}
}

// TestProviderListeners verifies that listeners are correctly notified of health status changes.
func TestProviderListeners(t *testing.T) {
	// Create a provider with default config
	provider, err := NewProvider(DefaultConfig())
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Create a variable check that we can change the status of
	checkName := "variable-check"
	variableStatus := StatusUp
	variableCheck := NewSimpleCheck(checkName, func(ctx context.Context) (Result, error) {
		return NewResult(variableStatus), nil
	})

	err = provider.Register(checkName, variableCheck)
	if err != nil {
		t.Fatalf("Failed to register check: %v", err)
	}

	// Create a listener to track status changes
	statusChanges := make([]Status, 0)
	statusMu := sync.Mutex{}

	listener := &testListener{
		onStatusChange: func(name string, previous, current Result) {
			if name == checkName {
				statusMu.Lock()
				defer statusMu.Unlock()
				statusChanges = append(statusChanges, current.Status())
			}
		},
	}

	// Add the listener
	err = provider.AddListener(listener)
	if err != nil {
		t.Fatalf("Failed to add listener: %v", err)
	}

	// Run an initial check to establish the baseline
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Change the status and run again
	variableStatus = StatusDegraded
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Change the status again and run again
	variableStatus = StatusDown
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Verify status changes were tracked
	statusMu.Lock()
	changesCount := len(statusChanges)
	statusMu.Unlock()

	if changesCount != 2 { // Two status changes
		t.Errorf("Expected 2 status changes, got %d", changesCount)
	}

	// Verify the status changes were correct
	if len(statusChanges) >= 2 {
		if statusChanges[0] != StatusDegraded {
			t.Errorf("Expected first status change to be Degraded, got %v", statusChanges[0])
		}
		if statusChanges[1] != StatusDown {
			t.Errorf("Expected second status change to be Down, got %v", statusChanges[1])
		}
	}

	// Remove the listener
	err = provider.RemoveListener(listener)
	if err != nil {
		t.Fatalf("Failed to remove listener: %v", err)
	}

	// Change the status again, should not be tracked
	statusMu.Lock()
	previousChanges := len(statusChanges)
	statusMu.Unlock()

	variableStatus = StatusUp
	_, err = provider.CheckAll(context.Background())
	if err != nil {
		t.Fatalf("CheckAll failed: %v", err)
	}

	// Verify no new status changes were tracked
	statusMu.Lock()
	newChanges := len(statusChanges)
	statusMu.Unlock()

	if newChanges != previousChanges {
		t.Errorf("Expected no new status changes after removing listener, got %d (before: %d)", newChanges, previousChanges)
	}
}

// testListener is a test implementation of the Listener interface.
type testListener struct {
	onStatusChange func(name string, previous, current Result)
}

func (l *testListener) OnStatusChange(name string, previous, current Result) {
	if l.onStatusChange != nil {
		l.onStatusChange(name, previous, current)
	}
}
