// file: pkg/health/http_test.go
package health

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"net/http/httptest"
	"testing"
)

// TestHealthHandlerAll tests that the health handler correctly handles requests to the root endpoint.
func TestHealthHandlerAll(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}))

	// Create a handler
	handler := newHealthHandler(provider)

	// Create a test request
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	w := httptest.NewRecorder()

	// Call the handler
	handler.handleAll(w, req)

	// Check the response
	resp := w.Result()
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		t.Errorf("Expected status OK, got %v", resp.StatusCode)
	}

	// Parse the response body
	var result map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		t.Fatalf("Failed to decode response body: %v", err)
	}

	// Check the status
	status, ok := result["status"]
	if !ok {
		t.Fatalf("Response does not contain 'status' field")
	}
	if status != StatusUp.String() {
		t.Errorf("Expected status %q, got %q", StatusUp.String(), status)
	}
}

// TestHealthHandlerLiveness tests that the health handler correctly handles liveness requests.
func TestHealthHandlerLiveness(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	config.EnableLivenessEndpoint = true
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks with different types
	provider.Register("liveness-up", NewSimpleCheck("liveness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeLiveness))

	provider.Register("readiness-up", NewSimpleCheck("readiness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeReadiness))

	// Create a handler
	handler := newHealthHandler(provider)

	// Create a test request
	req := httptest.NewRequest(http.MethodGet, config.LivenessPath, nil)
	w := httptest.NewRecorder()

	// Call the handler
	handler.handleLiveness(w, req)

	// Check the response
	resp := w.Result()
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		t.Errorf("Expected status OK, got %v", resp.StatusCode)
	}

	// Parse the response body
	var result map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		t.Fatalf("Failed to decode response body: %v", err)
	}

	// Check the status
	status, ok := result["status"]
	if !ok {
		t.Fatalf("Response does not contain 'status' field")
	}
	if status != StatusUp.String() {
		t.Errorf("Expected status %q, got %q", StatusUp.String(), status)
	}
}

// TestHealthHandlerReadiness tests that the health handler correctly handles readiness requests.
func TestHealthHandlerReadiness(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	config.EnableReadinessEndpoint = true
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks with different types
	provider.Register("liveness-up", NewSimpleCheck("liveness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeLiveness))

	provider.Register("readiness-up", NewSimpleCheck("readiness-up", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}), WithType(TypeReadiness))

	// Create a handler
	handler := newHealthHandler(provider)

	// Create a test request
	req := httptest.NewRequest(http.MethodGet, config.ReadinessPath, nil)
	w := httptest.NewRecorder()

	// Call the handler
	handler.handleReadiness(w, req)

	// Check the response
	resp := w.Result()
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		t.Errorf("Expected status OK, got %v", resp.StatusCode)
	}

	// Parse the response body
	var result map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		t.Fatalf("Failed to decode response body: %v", err)
	}

	// Check the status
	status, ok := result["status"]
	if !ok {
		t.Fatalf("Response does not contain 'status' field")
	}
	if status != StatusUp.String() {
		t.Errorf("Expected status %q, got %q", StatusUp.String(), status)
	}
}

// TestHealthHandlerDetails tests that the health handler correctly handles detailed requests.
func TestHealthHandlerDetails(t *testing.T) {
	// Create a provider with default config
	config := DefaultConfig()
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register some checks with different types and statuses
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp).
			WithDetails(map[string]interface{}{
				"key": "value",
			}), nil
	}))

	provider.Register("down-check", NewSimpleCheck("down-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("test error")), nil
	}))

	// Create a handler
	handler := newHealthHandler(provider)

	// Create a test request
	req := httptest.NewRequest(http.MethodGet, "/details", nil)
	w := httptest.NewRecorder()

	// Call the handler
	handler.handleDetails(w, req)

	// Check the response
	resp := w.Result()
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusServiceUnavailable {
		t.Errorf("Expected status ServiceUnavailable (503), got %v", resp.StatusCode)
	}

	// Parse the response body
	var result map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		t.Fatalf("Failed to decode response body: %v", err)
	}

	// Check the status
	status, ok := result["status"]
	if !ok {
		t.Fatalf("Response does not contain 'status' field")
	}
	if status != StatusDown.String() {
		t.Errorf("Expected status %q, got %q", StatusDown.String(), status)
	}

	// Check for checks field
	checks, ok := result["checks"].(map[string]interface{})
	if !ok {
		t.Fatalf("Response does not contain 'checks' field or it's not a map")
	}

	// Check if both checks are present
	upCheck, ok := checks["up-check"]
	if !ok {
		t.Fatalf("Checks does not contain 'up-check'")
	}

	downCheck, ok := checks["down-check"]
	if !ok {
		t.Fatalf("Checks does not contain 'down-check'")
	}

	// Verify the details of the up check
	upCheckMap, ok := upCheck.(map[string]interface{})
	if !ok {
		t.Fatalf("up-check is not a map")
	}
	upCheckStatus, ok := upCheckMap["status"]
	if !ok || upCheckStatus != StatusUp.String() {
		t.Errorf("up-check status is %v, expected %s", upCheckStatus, StatusUp.String())
	}

	// Verify the details of the down check
	downCheckMap, ok := downCheck.(map[string]interface{})
	if !ok {
		t.Fatalf("down-check is not a map")
	}
	downCheckStatus, ok := downCheckMap["status"]
	if !ok || downCheckStatus != StatusDown.String() {
		t.Errorf("down-check status is %v, expected %s", downCheckStatus, StatusDown.String())
	}
}

// TestHealthHandlerAuthentication tests that the health handler correctly handles authentication.
func TestHealthHandlerAuthentication(t *testing.T) {
	// Create a provider with authentication required
	config := DefaultConfig()
	config.RequireAuthentication = true
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create provider: %v", err)
	}

	// Register a check
	provider.Register("up-check", NewSimpleCheck("up-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	}))

	// Create a handler
	handler := newHealthHandler(provider)

	// Test cases
	testCases := []struct {
		name           string
		path           string
		withAuth       bool
		expectedStatus int
	}{
		{
			name:           "Details without auth",
			path:           "/details",
			withAuth:       false,
			expectedStatus: http.StatusUnauthorized,
		},
		{
			name:           "Details with auth",
			path:           "/details",
			withAuth:       true,
			expectedStatus: http.StatusOK,
		},
		{
			name:           "Basic health without auth",
			path:           "/",
			withAuth:       false,
			expectedStatus: http.StatusOK, // Basic health should not require auth
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a test request
			req := httptest.NewRequest(http.MethodGet, tc.path, nil)
			if tc.withAuth {
				req.Header.Set("Authorization", "Bearer test-token")
			}
			w := httptest.NewRecorder()

			// Call the handler directly based on path
			switch tc.path {
			case "/details":
				handler.handleDetails(w, req)
			case "/":
				handler.handleAll(w, req)
			default:
				handler.ServeHTTP(w, req)
			}

			// Check the response
			resp := w.Result()
			defer resp.Body.Close()

			if resp.StatusCode != tc.expectedStatus {
				t.Errorf("Expected status %d, got %d", tc.expectedStatus, resp.StatusCode)
			}
		})
	}
}

// TestHealthHandlerErrors tests that the health handler correctly handles errors.
func TestHealthHandlerErrors(t *testing.T) {
	// Create a mock provider that returns errors
	mockProvider := &mockProvider{
		checkAllErr: errors.New("check all error"),
	}

	// Create a handler
	handler := newHealthHandler(mockProvider)

	// Test cases
	testCases := []struct {
		name           string
		path           string
		expectedStatus int
	}{
		{
			name:           "Error on handleAll",
			path:           "/",
			expectedStatus: http.StatusInternalServerError,
		},
		{
			name:           "Error on handleLiveness",
			path:           "/live",
			expectedStatus: http.StatusInternalServerError,
		},
		{
			name:           "Error on handleReadiness",
			path:           "/ready",
			expectedStatus: http.StatusInternalServerError,
		},
		{
			name:           "Error on handleDetails",
			path:           "/details",
			expectedStatus: http.StatusInternalServerError,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a test request
			req := httptest.NewRequest(http.MethodGet, tc.path, nil)
			w := httptest.NewRecorder()

			// Call the handler
			handler.ServeHTTP(w, req)

			// Check the response
			resp := w.Result()
			defer resp.Body.Close()

			if resp.StatusCode != tc.expectedStatus {
				t.Errorf("Expected status %d, got %d", tc.expectedStatus, resp.StatusCode)
			}

			// Parse the response body
			var result map[string]interface{}
			if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
				t.Fatalf("Failed to decode response body: %v", err)
			}

			// Check that the error message is present
			errorMsg, ok := result["error"]
			if !ok {
				t.Fatalf("Response does not contain 'error' field")
			}
			if errorMsg == "" {
				t.Errorf("Expected non-empty error message")
			}
		})
	}
}

// mockProvider is a mock implementation of the Provider interface for testing.
type mockProvider struct {
	checks      map[string]Check
	checkAllErr error
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
	if p.checkAllErr != nil {
		return nil, p.checkAllErr
	}
	return NewResult(StatusUp), nil
}

func (p *mockProvider) CheckReadiness(ctx context.Context) (Result, error) {
	if p.checkAllErr != nil {
		return nil, p.checkAllErr
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
