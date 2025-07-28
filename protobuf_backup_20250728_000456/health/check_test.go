// file: pkg/health/check_test.go
package health

import (
	"context"
	"errors"
	"testing"
	"time"
)

// TestBaseCheck verifies that BaseCheck correctly implements the Check interface.
func TestBaseCheck(t *testing.T) {
	// Test parameters
	testName := "test-check"
	testType := TypeLiveness
	testTimeout := 5 * time.Second
	testInterval := 30 * time.Second

	// Create a new base check
	baseCheck := NewBaseCheck(testName, testType, testTimeout, testInterval)

	// Verify the check properties
	if baseCheck.Name() != testName {
		t.Errorf("Expected name %q, got %q", testName, baseCheck.Name())
	}

	if baseCheck.Type() != testType {
		t.Errorf("Expected type %v, got %v", testType, baseCheck.Type())
	}

	if baseCheck.Timeout() != testTimeout {
		t.Errorf("Expected timeout %v, got %v", testTimeout, baseCheck.Timeout())
	}

	if baseCheck.Interval() != testInterval {
		t.Errorf("Expected interval %v, got %v", testInterval, baseCheck.Interval())
	}

	// Check default enabled state
	if !baseCheck.Enabled() {
		t.Error("Expected check to be enabled by default")
	}

	// Test disabling the check
	baseCheck.SetEnabled(false)
	if baseCheck.Enabled() {
		t.Error("Expected check to be disabled after SetEnabled(false)")
	}

	// Test re-enabling the check
	baseCheck.SetEnabled(true)
	if !baseCheck.Enabled() {
		t.Error("Expected check to be enabled after SetEnabled(true)")
	}

	// Execute should return a "not implemented" error
	_, err := baseCheck.Execute(context.Background())
	if err == nil {
		t.Error("Expected Execute() to return an error")
	}
}

// TestCheckOptions verifies that check options correctly modify a check's properties.
func TestCheckOptions(t *testing.T) {
	// Test parameters
	testName := "test-check"
	initialType := TypeComponent
	initialTimeout := 5 * time.Second
	initialInterval := 30 * time.Second

	// New types and values to set
	newType := TypeLiveness
	newTimeout := 10 * time.Second
	newInterval := 60 * time.Second

	// Create a new base check
	baseCheck := NewBaseCheck(testName, initialType, initialTimeout, initialInterval)

	// Apply options
	options := []CheckOption{
		WithType(newType),
		WithTimeout(newTimeout),
		WithInterval(newInterval),
		WithEnabled(false),
	}

	for _, opt := range options {
		err := opt(baseCheck)
		if err != nil {
			t.Errorf("Expected option to apply without error, got %v", err)
		}
	}

	// Verify the changes
	if baseCheck.Type() != newType {
		t.Errorf("Expected type %v after WithType, got %v", newType, baseCheck.Type())
	}

	if baseCheck.Timeout() != newTimeout {
		t.Errorf("Expected timeout %v after WithTimeout, got %v", newTimeout, baseCheck.Timeout())
	}

	if baseCheck.Interval() != newInterval {
		t.Errorf("Expected interval %v after WithInterval, got %v", newInterval, baseCheck.Interval())
	}

	if baseCheck.Enabled() {
		t.Error("Expected check to be disabled after WithEnabled(false)")
	}
}

// TestSimpleCheck verifies that SimpleCheck correctly executes a check function.
func TestSimpleCheck(t *testing.T) {
	// Test parameters
	testName := "test-simple-check"
	testError := errors.New("test error")

	testCases := []struct {
		name           string
		checkFn        CheckFunc
		enabled        bool
		expectedStatus Status
		expectedError  error
	}{
		{
			name: "Successful check",
			checkFn: func(ctx context.Context) (Result, error) {
				return NewResult(StatusUp).
					WithDetails(map[string]interface{}{"key": "value"}), nil
			},
			enabled:        true,
			expectedStatus: StatusUp,
			expectedError:  nil,
		},
		{
			name: "Failed check",
			checkFn: func(ctx context.Context) (Result, error) {
				return NewResult(StatusDown).WithError(testError), nil
			},
			enabled:        true,
			expectedStatus: StatusDown,
			expectedError:  testError,
		},
		{
			name: "Check with error",
			checkFn: func(ctx context.Context) (Result, error) {
				return nil, testError
			},
			enabled:        true,
			expectedStatus: StatusDown,
			expectedError:  testError,
		},
		{
			name: "Disabled check",
			checkFn: func(ctx context.Context) (Result, error) {
				return NewResult(StatusUp), nil
			},
			enabled:        false,
			expectedStatus: StatusUnknown,
			expectedError:  errors.New("check disabled"),
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a simple check with the test function
			check := NewSimpleCheck(testName, tc.checkFn)
			check.SetEnabled(tc.enabled)

			// Execute the check
			result, err := check.Execute(context.Background())

			// Verify the result
			if result.Status() != tc.expectedStatus {
				t.Errorf("Expected status %v, got %v", tc.expectedStatus, result.Status())
			}

			// Check error conditions
			if tc.expectedError != nil {
				if result.Error() == nil {
					t.Errorf("Expected error %v, got nil", tc.expectedError)
				} else if result.Error().Error() != tc.expectedError.Error() {
					t.Errorf("Expected error %v, got %v", tc.expectedError, result.Error())
				}
			} else if result.Error() != nil {
				t.Errorf("Expected no error, got %v", result.Error())
			}

			// For successful execution, verify check and duration are set
			if tc.enabled && tc.expectedError == nil {
				if result.Check() == nil {
					t.Error("Expected check reference to be set in result")
				}
				if result.Duration() == 0 {
					t.Error("Expected non-zero duration in result")
				}
			}
		})
	}
}

// TestSimpleCheckRemediation verifies that SimpleCheck correctly handles remediation.
func TestSimpleCheckRemediation(t *testing.T) {
	// Test parameters
	testName := "test-remediation-check"
	remediationCalled := false

	// Create a check that will fail
	check := NewSimpleCheck(testName, func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("intentional failure")), nil
	})

	// Add remediation function
	remediationFn := func(ctx context.Context, result Result) error {
		remediationCalled = true
		return nil
	}

	err := WithRemediation(remediationFn)(check)
	if err != nil {
		t.Errorf("Expected WithRemediation to succeed, got error %v", err)
	}

	// Execute the check to get a failed result
	result, err := check.Execute(context.Background())
	if err != nil {
		t.Errorf("Expected no error from Execute, got %v", err)
	}
	if result.Status() != StatusDown {
		t.Errorf("Expected status Down, got %v", result.Status())
	}

	// Attempt remediation
	err = check.Remediate(context.Background(), result)
	if err != nil {
		t.Errorf("Expected remediation to succeed, got %v", err)
	}
	if !remediationCalled {
		t.Error("Expected remediation function to be called")
	}

	// Try remediation on a check without remediation function
	checkNoRemediation := NewSimpleCheck("no-remediation", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	})

	err = checkNoRemediation.Remediate(context.Background(), result)
	if err == nil {
		t.Error("Expected error for remediation without remediation function")
	}
}

// TestCompositeCheck verifies that CompositeCheck correctly executes multiple checks.
func TestCompositeCheck(t *testing.T) {
	// Create test child checks
	successCheck := NewSimpleCheck("success-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	})

	failureCheck := NewSimpleCheck("failure-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDown).
			WithError(errors.New("intentional failure")), nil
	})

	degradedCheck := NewSimpleCheck("degraded-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusDegraded).
			WithError(errors.New("partially degraded")), nil
	})

	disabledCheck := NewSimpleCheck("disabled-check", func(ctx context.Context) (Result, error) {
		return NewResult(StatusUp), nil
	})
	disabledCheck.SetEnabled(false)

	testCases := []struct {
		name           string
		checks         []Check
		enabled        bool
		expectedStatus Status
		expectedCount  int // Expected number of results
	}{
		{
			name:           "All successful",
			checks:         []Check{successCheck, successCheck},
			enabled:        true,
			expectedStatus: StatusUp,
			expectedCount:  2,
		},
		{
			name:           "One failure",
			checks:         []Check{successCheck, failureCheck, successCheck},
			enabled:        true,
			expectedStatus: StatusDown,
			expectedCount:  3,
		},
		{
			name:           "One degraded",
			checks:         []Check{successCheck, degradedCheck, successCheck},
			enabled:        true,
			expectedStatus: StatusDegraded,
			expectedCount:  3,
		},
		{
			name:           "Mixed with disabled",
			checks:         []Check{successCheck, disabledCheck, successCheck},
			enabled:        true,
			expectedStatus: StatusUp,
			expectedCount:  2, // Disabled check should be skipped
		},
		{
			name:           "Composite disabled",
			checks:         []Check{successCheck, successCheck},
			enabled:        false,
			expectedStatus: StatusUnknown,
			expectedCount:  0,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create composite check
			composite := NewCompositeCheck("composite")
			composite.SetEnabled(tc.enabled)
			composite.AddChecks(tc.checks...)

			// Execute the composite check
			result, err := composite.Execute(context.Background())
			if err != nil {
				t.Errorf("Expected no error, got %v", err)
			}

			// Check the status
			if result.Status() != tc.expectedStatus {
				t.Errorf("Expected status %v, got %v", tc.expectedStatus, result.Status())
			}

			// Check child results
			children := result.Children()
			if tc.enabled && len(children) != tc.expectedCount {
				t.Errorf("Expected %d child results, got %d", tc.expectedCount, len(children))
			}

			// Verify the check reference in the result
			if result.Check() != composite {
				t.Error("Expected result.Check() to reference the composite check")
			}

			// Test removing a check
			if len(tc.checks) > 0 {
				checkToRemove := tc.checks[0]
				removed := composite.RemoveCheck(checkToRemove.Name())
				if !removed {
					t.Errorf("Expected RemoveCheck(%q) to return true", checkToRemove.Name())
				}

				// Verify the check was removed
				remainingChecks := composite.Checks()
				if len(remainingChecks) != len(tc.checks)-1 {
					t.Errorf("Expected %d remaining checks, got %d", len(tc.checks)-1, len(remainingChecks))
				}

				// Try removing a non-existent check
				removed = composite.RemoveCheck("non-existent-check")
				if removed {
					t.Error("Expected RemoveCheck for non-existent check to return false")
				}
			}
		})
	}
}
