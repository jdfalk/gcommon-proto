// file: pkg/health/remediation_test.go
package health

import (
	"context"
	"errors"
	"sync/atomic"
	"testing"
	"time"
)

// MockRemediableCheck implements both Check and RemediableCheck interfaces for testing
type MockRemediableCheck struct {
	name                   string
	checkType              CheckType
	timeout                time.Duration
	interval               time.Duration
	enabled                bool
	status                 Status
	remediationCalled      int32
	remediationFunc        func(ctx context.Context) error
	maxAttempts            int
	failuresUntilRemediate int
}

func NewMockRemediableCheck(name string, status Status, maxAttempts int, failuresUntilRemediate int) *MockRemediableCheck {
	return &MockRemediableCheck{
		name:                   name,
		checkType:              TypeLiveness,
		timeout:                time.Second,
		interval:               time.Second * 5,
		enabled:                true,
		status:                 status,
		maxAttempts:            maxAttempts,
		failuresUntilRemediate: failuresUntilRemediate,
	}
}

// Execute implements the Check interface
func (m *MockRemediableCheck) Execute(ctx context.Context) (Result, error) {
	return NewResult(m.status).WithDetails(map[string]interface{}{
		"remediationCalled": atomic.LoadInt32(&m.remediationCalled),
	}), nil
}

// Name implements the Check interface
func (m *MockRemediableCheck) Name() string {
	return m.name
}

// Type implements the Check interface
func (m *MockRemediableCheck) Type() CheckType {
	return m.checkType
}

// Timeout implements the Check interface
func (m *MockRemediableCheck) Timeout() time.Duration {
	return m.timeout
}

// Interval implements the Check interface
func (m *MockRemediableCheck) Interval() time.Duration {
	return m.interval
}

// Enabled implements the Check interface
func (m *MockRemediableCheck) Enabled() bool {
	return m.enabled
}

// SetEnabled implements the Check interface
func (m *MockRemediableCheck) SetEnabled(enabled bool) {
	m.enabled = enabled
}

// Remediate implements the RemediableCheck interface
func (m *MockRemediableCheck) Remediate(ctx context.Context) error {
	atomic.AddInt32(&m.remediationCalled, 1)
	if m.remediationFunc != nil {
		return m.remediationFunc(ctx)
	}
	// Default: remediation sets status to UP
	m.status = StatusUp
	return nil
}

// MaxRemediationAttempts implements the RemediableCheck interface
func (m *MockRemediableCheck) MaxRemediationAttempts() int {
	return m.maxAttempts
}

// FailuresUntilRemediate implements the RemediableCheck interface
func (m *MockRemediableCheck) FailuresUntilRemediate() int {
	return m.failuresUntilRemediate
}

// TestRemediationManager tests the remediation system
func TestRemediationManager(t *testing.T) {
	// Create a test health provider
	config := Config{
		Enabled:            true,
		DefaultTimeout:     100 * time.Millisecond,
		RemediationEnabled: true,
	}
	provider, err := NewProvider(config)
	if err != nil {
		t.Fatalf("Failed to create health provider: %v", err)
	}

	// Create a mock metrics listener to track remediation events
	mockListener := &MockMetricsListener{}
	err = EnableMetricsReporting(provider, mockListener)
	if err != nil {
		t.Fatalf("Failed to enable metrics reporting: %v", err)
	}

	// Test basic remediation
	t.Run("BasicRemediation", func(t *testing.T) {
		// Create a check that's initially DOWN but can be remediated
		check := NewMockRemediableCheck("basic-check", StatusDown, 3, 1)

		// Register the check
		provider.Register(check.Name(), check)

		// Start the health provider
		ctx, cancel := context.WithCancel(context.Background())
		defer cancel()

		err = provider.Start(ctx)
		if err != nil {
			t.Fatalf("Failed to start health provider: %v", err)
		}

		// Execute the check to trigger remediation
		result, err := provider.Get(check.Name()).Execute(ctx)
		if err != nil {
			t.Fatalf("Failed to execute check: %v", err)
		}

		if result.Status() != StatusDown {
			t.Errorf("Expected initial status DOWN, got %v", result.Status())
		}

		// Let the remediation system work
		time.Sleep(300 * time.Millisecond)

		// Check should have been remediated
		result, err = provider.Get(check.Name()).Execute(ctx)
		if err != nil {
			t.Fatalf("Failed to execute check after remediation: %v", err)
		}

		// Check should now be UP after remediation
		if result.Status() != StatusUp {
			t.Errorf("Expected status UP after remediation, got %v", result.Status())
		}

		// Verify remediation was called
		if atomic.LoadInt32(&check.remediationCalled) != 1 {
			t.Errorf("Expected remediation to be called once, got %d", atomic.LoadInt32(&check.remediationCalled))
		}

		// Verify metrics were collected
		if !mockListener.remediationCalled {
			t.Error("Remediation metrics were not collected")
		}
		if mockListener.remediationDetails.CheckName != check.Name() {
			t.Errorf("Expected check name %s in metrics, got %s", check.Name(), mockListener.remediationDetails.CheckName)
		}
		if !mockListener.remediationDetails.Success {
			t.Error("Expected successful remediation in metrics")
		}
	})

	// Test failed remediation
	t.Run("FailedRemediation", func(t *testing.T) {
		// Create a check with failing remediation
		check := NewMockRemediableCheck("failing-check", StatusDown, 2, 1)
		remediationErr := errors.New("remediation failed")
		check.remediationFunc = func(ctx context.Context) error {
			return remediationErr
		}

		// Register the check
		provider.Register(check.Name(), check)

		// Create a new context for this test
		ctx, cancel := context.WithCancel(context.Background())
		defer cancel()

		// Execute the check to trigger remediation
		result, err := provider.Get(check.Name()).Execute(ctx)
		if err != nil {
			t.Fatalf("Failed to execute check: %v", err)
		}

		// Let the remediation system work
		time.Sleep(300 * time.Millisecond)

		// Check should still be DOWN after failed remediation
		result, err = provider.Get(check.Name()).Execute(ctx)
		if err != nil {
			t.Fatalf("Failed to execute check after remediation: %v", err)
		}

		if result.Status() != StatusDown {
			t.Errorf("Expected status to remain DOWN after failed remediation, got %v", result.Status())
		}
	})

	// Test multiple remediation attempts
	t.Run("MultipleRemediationAttempts", func(t *testing.T) {
		// Create a check that stays DOWN after remediation
		check := NewMockRemediableCheck("persistent-check", StatusDown, 3, 1)
		check.remediationFunc = func(ctx context.Context) error {
			// Successful remediation but status doesn't change
			return nil
		}

		// Register the check
		provider.Register(check.Name(), check)

		// Create a new context for this test
		ctx, cancel := context.WithCancel(context.Background())
		defer cancel()

		// Execute the check multiple times to trigger multiple remediation attempts
		for i := 0; i < 4; i++ {
			_, err := provider.Get(check.Name()).Execute(ctx)
			if err != nil {
				t.Fatalf("Failed to execute check: %v", err)
			}

			// Let the remediation system work
			time.Sleep(100 * time.Millisecond)
		}

		// Verify remediation was called up to maxAttempts times
		called := atomic.LoadInt32(&check.remediationCalled)
		if called > int32(check.MaxRemediationAttempts()) {
			t.Errorf("Expected remediation to be called at most %d times, got %d",
				check.MaxRemediationAttempts(), called)
		}
	})

	// Test the failures counter threshold
	t.Run("FailuresThreshold", func(t *testing.T) {
		// Create a check that requires multiple failures before remediation
		check := NewMockRemediableCheck("threshold-check", StatusDown, 1, 3)

		// Register the check
		provider.Register(check.Name(), check)

		// Create a new context for this test
		ctx, cancel := context.WithCancel(context.Background())
		defer cancel()

		// Execute the check, this is failure #1
		_, err := provider.Get(check.Name()).Execute(ctx)
		if err != nil {
			t.Fatalf("Failed to execute check: %v", err)
		}

		// Let the remediation system work
		time.Sleep(100 * time.Millisecond)

		// Remediation should not have been called yet (only 1 failure)
		if atomic.LoadInt32(&check.remediationCalled) != 0 {
			t.Error("Remediation was called before threshold was reached")
		}

		// Trigger more failures to reach threshold
		for i := 0; i < 2; i++ {
			_, err := provider.Get(check.Name()).Execute(ctx)
			if err != nil {
				t.Fatalf("Failed to execute check: %v", err)
			}
			time.Sleep(100 * time.Millisecond)
		}

		// Let the remediation system work
		time.Sleep(100 * time.Millisecond)

		// Now remediation should have been called
		if atomic.LoadInt32(&check.remediationCalled) == 0 {
			t.Error("Remediation was not called after threshold was reached")
		}
	})
}
