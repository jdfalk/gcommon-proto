// file: pkg/health/metrics_test.go
package health

import (
	"context"
	"testing"
	"time"
)

// MockMetricsListener implements the MetricsListener interface for testing
type MockMetricsListener struct {
	statusCalled       bool
	statusCheckName    string
	statusValue        Status
	durationCalled     bool
	durationCheckName  string
	durationValue      time.Duration
	errorCalled        bool
	errorCheckName     string
	remediationCalled  bool
	remediationDetails RemediationDetails
}

// OnHealthStatus records a health status metrics call
func (m *MockMetricsListener) OnHealthStatus(checkName string, status Status) {
	m.statusCalled = true
	m.statusCheckName = checkName
	m.statusValue = status
}

// OnHealthCheckDuration records a health check duration metrics call
func (m *MockMetricsListener) OnHealthCheckDuration(checkName string, duration time.Duration) {
	m.durationCalled = true
	m.durationCheckName = checkName
	m.durationValue = duration
}

// OnHealthCheckError records a health check error metrics call
func (m *MockMetricsListener) OnHealthCheckError(checkName string, err error) {
	m.errorCalled = true
	m.errorCheckName = checkName
}

// OnRemediationAttempt records a remediation attempt metrics call
func (m *MockMetricsListener) OnRemediationAttempt(details RemediationDetails) {
	m.remediationCalled = true
	m.remediationDetails = details
}

// TestEnableMetricsReporting tests the EnableMetricsReporting function
func TestEnableMetricsReporting(t *testing.T) {
	// Create a test health provider
	config := Config{
		Enabled:        true,
		DefaultTimeout: 100 * time.Millisecond,
		MetricsEnabled: true,
	}
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create health provider: %v", err)
	}

	// Create a mock metrics listener
	mockListener := &MockMetricsListener{}

	// Enable metrics reporting
	err = EnableMetricsReporting(provider, mockListener)
	if err != nil {
		t.Fatalf("Failed to enable metrics reporting: %v", err)
	}

	// Register a simple health check that returns UP after a small delay
	provider.Register("test-check", CheckFunc(func(ctx context.Context) (Result, error) {
		time.Sleep(10 * time.Millisecond) // Small delay to ensure duration is measurable
		return NewResult(StatusUp).WithDetails(map[string]interface{}{
			"time": time.Now().Format(time.RFC3339),
		}), nil
	}))

	// Start the health provider
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	err = provider.Start(ctx)
	if err != nil {
		t.Fatalf("Failed to start health provider: %v", err)
	}

	// Run the health check
	result, err := provider.CheckAll(ctx)
	if err != nil {
		t.Fatalf("Failed to run health check: %v", err)
	}

	// Verify the check succeeded
	if result.Status() != StatusUp {
		t.Errorf("Expected status %v, got %v", StatusUp, result.Status())
	}

	// Wait for metrics to be recorded (may take a moment due to async nature)
	time.Sleep(50 * time.Millisecond)

	// Verify metrics were recorded
	if !mockListener.statusCalled {
		t.Error("OnHealthStatus was not called")
	}
	if mockListener.statusCheckName != "test-check" {
		t.Errorf("Expected check name %s, got %s", "test-check", mockListener.statusCheckName)
	}
	if mockListener.statusValue != StatusUp {
		t.Errorf("Expected status %v, got %v", StatusUp, mockListener.statusValue)
	}

	if !mockListener.durationCalled {
		t.Error("OnHealthCheckDuration was not called")
	}
	if mockListener.durationCheckName != "test-check" {
		t.Errorf("Expected check name %s, got %s", "test-check", mockListener.durationCheckName)
	}
	if mockListener.durationValue < 10*time.Millisecond {
		t.Errorf("Expected duration >= %v, got %v", 10*time.Millisecond, mockListener.durationValue)
	}

	// Ensure error reporting works too by registering a check that fails
	provider.Register("error-check", CheckFunc(func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).WithError(context.DeadlineExceeded), nil
	}))

	// Run the health check for the error case
	result, err = provider.Get("error-check").Execute(ctx)
	if err != nil {
		t.Fatalf("Failed to run health check: %v", err)
	}

	// Verify the check failed as expected
	if result.Status() != StatusDown {
		t.Errorf("Expected status %v, got %v", StatusDown, result.Status())
	}
	if result.Error() != context.DeadlineExceeded {
		t.Errorf("Expected error %v, got %v", context.DeadlineExceeded, result.Error())
	}

	// Wait for metrics to be recorded
	time.Sleep(50 * time.Millisecond)

	// Verify error metrics were recorded
	if !mockListener.errorCalled {
		t.Error("OnHealthCheckError was not called")
	}
	if mockListener.errorCheckName != "error-check" {
		t.Errorf("Expected check name %s, got %s", "error-check", mockListener.errorCheckName)
	}

	// Stop the health provider
	if err := provider.Stop(ctx); err != nil {
		t.Fatalf("Failed to stop health provider: %v", err)
	}
}
