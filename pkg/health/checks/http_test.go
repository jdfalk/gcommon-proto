// file: pkg/health/checks/http_test.go
package checks

import (
	"context"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// TestHTTPCheckSuccess tests that the HTTP check correctly handles successful responses.
func TestHTTPCheckSuccess(t *testing.T) {
	// Create a test server that returns a 200 OK
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method
		if r.Method != http.MethodGet {
			t.Errorf("Expected method %s, got %s", http.MethodGet, r.Method)
		}

		// Verify custom headers if set
		if r.Header.Get("User-Agent") != "health-check" {
			t.Errorf("Expected User-Agent %q, got %q", "health-check", r.Header.Get("User-Agent"))
		}

		// Return a successful response
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(`{"status":"ok"}`))
	}))
	defer server.Close()

	// Create an HTTP check with options
	check := NewHTTPCheck(server.URL,
		WithMethod(http.MethodGet),
		WithTimeout(1*time.Second),
		WithExpectedStatus(http.StatusOK),
		WithHeader("User-Agent", "health-check"),
	)

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusUp {
		t.Errorf("Expected status %v, got %v", health.StatusUp, result.Status())
	}

	// Verify the details
	details := result.Details()
	if details["url"] != server.URL {
		t.Errorf("Expected url %q, got %q", server.URL, details["url"])
	}
	if details["method"] != http.MethodGet {
		t.Errorf("Expected method %q, got %q", http.MethodGet, details["method"])
	}
	if details["statusCode"] != http.StatusOK {
		t.Errorf("Expected statusCode %d, got %v", http.StatusOK, details["statusCode"])
	}
}

// TestHTTPCheckFailedStatus tests that the HTTP check correctly handles unexpected status codes.
func TestHTTPCheckFailedStatus(t *testing.T) {
	// Create a test server that returns a 500 error
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte(`{"error":"internal server error"}`))
	}))
	defer server.Close()

	// Create an HTTP check expecting a 200 OK
	check := NewHTTPCheck(server.URL,
		WithExpectedStatus(http.StatusOK),
	)

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status %v, got %v", health.StatusDown, result.Status())
	}

	// Verify the error
	if result.Error() == nil {
		t.Fatal("Expected error, but got nil")
	}

	// Verify the details
	details := result.Details()
	if details["statusCode"] != http.StatusInternalServerError {
		t.Errorf("Expected statusCode %d, got %v", http.StatusInternalServerError, details["statusCode"])
	}
	if details["expectedStatusCode"] != http.StatusOK {
		t.Errorf("Expected expectedStatusCode %d, got %v", http.StatusOK, details["expectedStatusCode"])
	}
}

// TestHTTPCheckTimeout tests that the HTTP check correctly handles timeouts.
func TestHTTPCheckTimeout(t *testing.T) {
	// Create a test server that simulates a timeout by sleeping
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Sleep longer than the check timeout
		time.Sleep(500 * time.Millisecond)
		w.WriteHeader(http.StatusOK)
	}))
	defer server.Close()

	// Create an HTTP check with a short timeout
	check := NewHTTPCheck(server.URL,
		WithTimeout(100*time.Millisecond),
	)

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status %v, got %v", health.StatusDown, result.Status())
	}

	// Verify the error
	if result.Error() == nil {
		t.Fatal("Expected error, but got nil")
	}

	// The error should contain "timeout" or "deadline exceeded"
	errorMsg := result.Error().Error()
	if !contains(errorMsg, "timeout", "deadline") {
		t.Errorf("Expected error to contain 'timeout' or 'deadline', got: %s", errorMsg)
	}
}

// TestHTTPCheckConnectionRefused tests that the HTTP check correctly handles connection failures.
func TestHTTPCheckConnectionRefused(t *testing.T) {
	// Use an invalid URL that should refuse connections
	check := NewHTTPCheck("http://localhost:12345")

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status %v, got %v", health.StatusDown, result.Status())
	}

	// Verify the error
	if result.Error() == nil {
		t.Fatal("Expected error, but got nil")
	}

	// Error details should be present
	details := result.Details()
	if details["error"] == nil {
		t.Error("Expected error details to be present")
	}
}

// TestHTTPCheckCustomValidator tests that the HTTP check correctly uses custom validator functions.
func TestHTTPCheckCustomValidator(t *testing.T) {
	// Create a test server that returns a JSON response
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(`{"status":"healthy","version":"1.2.3"}`))
	}))
	defer server.Close()

	// Create a custom validator that checks for specific JSON fields
	customValidator := func(resp *http.Response, body []byte) error {
		if resp.Header.Get("Content-Type") != "application/json" {
			return health.NewError("expected Content-Type: application/json")
		}

		// Check if the body contains the expected string
		if !contains(string(body), "healthy", "version") {
			return health.NewError("response body missing expected content")
		}

		return nil
	}

	// Create an HTTP check with the custom validator
	check := NewHTTPCheck(server.URL,
		WithValidator(customValidator),
	)

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusUp {
		t.Errorf("Expected status %v, got %v", health.StatusUp, result.Status())
	}

	// Now test with a validator that will fail
	failingValidator := func(resp *http.Response, body []byte) error {
		return health.NewError("intentional validator failure")
	}

	// Update the check with the failing validator
	check = NewHTTPCheck(server.URL,
		WithValidator(failingValidator),
	)

	// Execute the check again
	result, err = check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusDown {
		t.Errorf("Expected status %v, got %v", health.StatusDown, result.Status())
	}

	// Verify the error
	if result.Error() == nil {
		t.Fatal("Expected error, but got nil")
	}

	// Check the error message
	errorMsg := result.Error().Error()
	if errorMsg != "validation failed: intentional validator failure" {
		t.Errorf("Expected specific error message, got: %s", errorMsg)
	}
}

// TestHTTPCheckDisabled tests that a disabled HTTP check returns the expected result.
func TestHTTPCheckDisabled(t *testing.T) {
	check := NewHTTPCheck("http://example.com")
	check.SetEnabled(false)

	// Execute the check
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Fatalf("Unexpected error: %v", err)
	}

	// Verify the result
	if result.Status() != health.StatusUnknown {
		t.Errorf("Expected status %v, got %v", health.StatusUnknown, result.Status())
	}

	// Verify the error
	if result.Error() == nil {
		t.Fatal("Expected error, but got nil")
	}

	// Check the error message
	errorMsg := result.Error().Error()
	if errorMsg != "check disabled" {
		t.Errorf("Expected error 'check disabled', got: %s", errorMsg)
	}
}

// contains checks if the string s contains any of the substrings.
func contains(s string, substrings ...string) bool {
	for _, substr := range substrings {
		if containsInsensitive(s, substr) {
			return true
		}
	}
	return false
}

// containsInsensitive checks if the string s contains the substring, case-insensitive.
func containsInsensitive(s, substr string) bool {
	s, substr = strings.ToLower(s), strings.ToLower(substr)
	return strings.Contains(s, substr)
}
