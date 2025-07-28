// file: pkg/health/kubernetes_test.go
package health

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

// TestKubernetesProbeHandler tests the Kubernetes probe handler implementation
func TestKubernetesProbeHandler(t *testing.T) {
	// Create a test health provider
	config := Config{
		Enabled:        true,
		DefaultTimeout: 100 * time.Millisecond,
	}
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create health provider: %v", err)
	}

	// Register a simple mock health check that always returns UP
	provider.Register("test-liveness", CheckFunc(func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp).WithDetails(map[string]interface{}{
			"time": time.Now().Format(time.RFC3339),
		}), nil
	}), WithType(TypeLiveness))

	// Register a simple mock health check that always returns DOWN for readiness
	provider.Register("test-readiness", CheckFunc(func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).WithDetails(map[string]interface{}{
			"time": time.Now().Format(time.RFC3339),
		}), nil
	}), WithType(TypeReadiness))

	// Create Kubernetes probe config with default settings
	probeConfig := DefaultKubernetesProbeConfig()

	// Create a Kubernetes probe handler
	kubeHandler := NewKubernetesProbeHandler(provider, probeConfig)

	// Test liveness probe endpoint
	t.Run("LivenessProbe", func(t *testing.T) {
		req := httptest.NewRequest("GET", "/healthz", nil)
		res := httptest.NewRecorder()

		kubeHandler.LivenessHandler(res, req)

		if res.Code != http.StatusOK {
			t.Errorf("Expected status code %d, got %d", http.StatusOK, res.Code)
		}
	})

	// Test readiness probe endpoint - should fail since our mock returns DOWN
	t.Run("ReadinessProbe", func(t *testing.T) {
		req := httptest.NewRequest("GET", "/readyz", nil)
		res := httptest.NewRecorder()

		kubeHandler.ReadinessHandler(res, req)

		if res.Code != http.StatusServiceUnavailable {
			t.Errorf("Expected status code %d, got %d", http.StatusServiceUnavailable, res.Code)
		}
	})

	// Test startup probe endpoint (inherits from liveness by default)
	t.Run("StartupProbe", func(t *testing.T) {
		req := httptest.NewRequest("GET", "/startupz", nil)
		res := httptest.NewRecorder()

		kubeHandler.StartupHandler(res, req)

		if res.Code != http.StatusOK {
			t.Errorf("Expected status code %d, got %d", http.StatusOK, res.Code)
		}
	})

	// Test RegisterWithMux method
	t.Run("RegisterWithMux", func(t *testing.T) {
		mux := http.NewServeMux()
		kubeHandler.RegisterWithMux(mux)

		// Test the liveness endpoint
		req := httptest.NewRequest("GET", "/healthz", nil)
		res := httptest.NewRecorder()

		mux.ServeHTTP(res, req)

		if res.Code != http.StatusOK {
			t.Errorf("Expected status code %d, got %d", http.StatusOK, res.Code)
		}

		// Test the readiness endpoint
		req = httptest.NewRequest("GET", "/readyz", nil)
		res = httptest.NewRecorder()

		mux.ServeHTTP(res, req)

		if res.Code != http.StatusServiceUnavailable {
			t.Errorf("Expected status code %d, got %d", http.StatusServiceUnavailable, res.Code)
		}
	})

	// Test custom probe paths
	t.Run("CustomProbePaths", func(t *testing.T) {
		customConfig := DefaultKubernetesProbeConfig()
		customConfig.LivenessPath = "/custom-liveness"
		customConfig.ReadinessPath = "/custom-readiness"
		customConfig.StartupPath = "/custom-startup"

		customHandler := NewKubernetesProbeHandler(provider, customConfig)

		mux := http.NewServeMux()
		customHandler.RegisterWithMux(mux)

		// Test the custom liveness path
		req := httptest.NewRequest("GET", "/custom-liveness", nil)
		res := httptest.NewRecorder()

		mux.ServeHTTP(res, req)

		if res.Code != http.StatusOK {
			t.Errorf("Expected status code %d, got %d", http.StatusOK, res.Code)
		}
	})
}
