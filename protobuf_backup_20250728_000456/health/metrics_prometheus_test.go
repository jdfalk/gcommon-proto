// file: pkg/health/metrics_prometheus_test.go
package health

import (
	"context"
	"testing"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/testutil"
)

// TestPrometheusMetricsListener tests the PrometheusMetricsListener implementation
func TestPrometheusMetricsListener(t *testing.T) {
	// Create a test registry to avoid conflicts with the global one
	registry := prometheus.NewRegistry()

	// Create the Prometheus metrics listener with the test registry
	listener := NewPrometheusMetricsListener(PrometheusMetricsConfig{
		Namespace: "test",
		Subsystem: "health",
		Registry:  registry,
	})

	// Test health status reporting
	t.Run("HealthStatus", func(t *testing.T) {
		// Report an UP status
		listener.OnHealthStatus("test-check", StatusUp)

		// Verify metric was recorded
		metricFamilies, err := registry.Gather()
		if err != nil {
			t.Fatalf("Failed to gather metrics: %v", err)
		}

		// Check if we have the status gauge
		found := false
		for _, mf := range metricFamilies {
			if *mf.Name == "test_health_check_status" {
				found = true

				// Check if the test-check with UP status (1.0) is present
				for _, m := range mf.Metric {
					for _, label := range m.Label {
						if *label.Name == "check" && *label.Value == "test-check" {
							if *m.Gauge.Value != 1.0 {
								t.Errorf("Expected status value 1.0 (UP), got %f", *m.Gauge.Value)
							}
							break
						}
					}
				}
				break
			}
		}

		if !found {
			t.Error("Health check status metric not found")
		}

		// Report a DOWN status
		listener.OnHealthStatus("test-check", StatusDown)

		// Check metric again
		counter, err := testutil.GetGaugeValue(
			registry,
			prometheus.GaugeVec{},
			map[string]string{"check": "test-check"},
		)
		if err != nil {
			t.Fatalf("Failed to get gauge value: %v", err)
		}

		// DOWN status should be represented as 0.0
		if counter != 0.0 {
			t.Errorf("Expected status value 0.0 (DOWN), got %f", counter)
		}
	})

	// Test health check duration reporting
	t.Run("HealthCheckDuration", func(t *testing.T) {
		// Report a duration
		testDuration := 123 * time.Millisecond
		listener.OnHealthCheckDuration("duration-check", testDuration)

		// Verify metric was recorded
		metricFamilies, err := registry.Gather()
		if err != nil {
			t.Fatalf("Failed to gather metrics: %v", err)
		}

		// Check if we have the duration histogram
		found := false
		for _, mf := range metricFamilies {
			if *mf.Name == "test_health_check_duration_seconds" {
				found = true
				break
			}
		}

		if !found {
			t.Error("Health check duration metric not found")
		}
	})

	// Test health check error reporting
	t.Run("HealthCheckError", func(t *testing.T) {
		// Initial state - error counter should be 0
		initialCount, err := testutil.GetCounterValue(
			registry,
			prometheus.CounterVec{},
			map[string]string{"check": "error-check"},
		)

		// Report an error
		testErr := context.DeadlineExceeded
		listener.OnHealthCheckError("error-check", testErr)

		// Check if counter increased
		newCount, err := testutil.GetCounterValue(
			registry,
			prometheus.CounterVec{},
			map[string]string{"check": "error-check"},
		)
		if err != nil {
			t.Fatalf("Failed to get counter value: %v", err)
		}

		// Counter should have increased by 1
		if newCount != initialCount+1 {
			t.Errorf("Expected error count to increase by 1, got %f -> %f", initialCount, newCount)
		}
	})

	// Test remediation attempt reporting
	t.Run("RemediationAttempt", func(t *testing.T) {
		// Report a remediation attempt
		listener.OnRemediationAttempt(RemediationDetails{
			CheckName:    "remediation-check",
			AttemptCount: 2,
			Success:      true,
			Duration:     50 * time.Millisecond,
		})

		// Verify metrics were recorded
		metricFamilies, err := registry.Gather()
		if err != nil {
			t.Fatalf("Failed to gather metrics: %v", err)
		}

		// Check if we have the remediation counter and duration metrics
		foundCounter := false
		foundDuration := false

		for _, mf := range metricFamilies {
			if *mf.Name == "test_health_remediation_attempts_total" {
				foundCounter = true
			}
			if *mf.Name == "test_health_remediation_duration_seconds" {
				foundDuration = true
			}
		}

		if !foundCounter {
			t.Error("Remediation attempts counter metric not found")
		}
		if !foundDuration {
			t.Error("Remediation duration metric not found")
		}
	})
}
