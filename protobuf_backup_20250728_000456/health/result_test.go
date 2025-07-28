// file: pkg/health/result_test.go
package health

import (
	"errors"
	"testing"
	"time"
)

// TestNewResult verifies that NewResult correctly initializes a Result with the given status.
func TestNewResult(t *testing.T) {
	// Test cases with different health statuses
	testCases := []struct {
		name           string
		status         Status
		expectedStatus Status
	}{
		{
			name:           "StatusUp",
			status:         StatusUp,
			expectedStatus: StatusUp,
		},
		{
			name:           "StatusDown",
			status:         StatusDown,
			expectedStatus: StatusDown,
		},
		{
			name:           "StatusDegraded",
			status:         StatusDegraded,
			expectedStatus: StatusDegraded,
		},
		{
			name:           "StatusUnknown",
			status:         StatusUnknown,
			expectedStatus: StatusUnknown,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := NewResult(tc.status)

			// Verify the result has the correct status
			if result.Status() != tc.expectedStatus {
				t.Errorf("Expected status %v, got %v", tc.expectedStatus, result.Status())
			}

			// Verify details map is initialized but empty
			if result.Details() == nil {
				t.Error("Expected non-nil details map")
			}
			if len(result.Details()) != 0 {
				t.Errorf("Expected empty details map, got %v", result.Details())
			}

			// Verify timestamp is set
			if result.Timestamp().IsZero() {
				t.Error("Expected non-zero timestamp")
			}
		})
	}
}

// TestResultWithError verifies that WithError correctly sets the error on the Result.
func TestResultWithError(t *testing.T) {
	// Create a test error
	testError := errors.New("test error")

	// Create a result and set the error
	result := NewResult(StatusDown).WithError(testError)

	// Verify the error was set correctly
	if result.Error() != testError {
		t.Errorf("Expected error %v, got %v", testError, result.Error())
	}
}

// TestResultWithDetails verifies that WithDetails correctly adds details to the Result.
func TestResultWithDetails(t *testing.T) {
	// Create details for testing
	details := map[string]interface{}{
		"key1": "value1",
		"key2": 42,
		"key3": true,
	}

	// Create a result and add details
	result := NewResult(StatusUp).WithDetails(details)

	// Verify the details were added correctly
	resultDetails := result.Details()
	for k, v := range details {
		if resultDetails[k] != v {
			t.Errorf("Expected details[%s] = %v, got %v", k, v, resultDetails[k])
		}
	}

	// Test adding additional details
	additionalDetails := map[string]interface{}{
		"key4": "value4",
		"key2": "updated", // This should override the previous value
	}

	// Add the additional details
	result = result.WithDetails(additionalDetails)

	// Verify the updated details
	resultDetails = result.Details()
	expectedDetails := map[string]interface{}{
		"key1": "value1",
		"key2": "updated", // Updated value
		"key3": true,
		"key4": "value4", // New key
	}

	for k, v := range expectedDetails {
		if resultDetails[k] != v {
			t.Errorf("Expected details[%s] = %v, got %v", k, v, resultDetails[k])
		}
	}
}

// TestResultWithCheck verifies that WithCheck correctly sets the check on the Result.
func TestResultWithCheck(t *testing.T) {
	// Create a mock check
	mockCheck := &mockCheck{name: "test-check"}

	// Create a result and set the check
	result := NewResult(StatusUp)
	if hr, ok := result.(*healthResult); ok {
		hr.WithCheck(mockCheck)

		// Verify the check was set correctly
		if hr.Check() != mockCheck {
			t.Errorf("Expected check %v, got %v", mockCheck, hr.Check())
		}
	} else {
		t.Errorf("Expected *healthResult, got %T", result)
	}
}

// TestResultWithDuration verifies that WithDuration correctly sets the duration on the Result.
func TestResultWithDuration(t *testing.T) {
	// Create a test duration
	testDuration := 500 * time.Millisecond

	// Create a result and set the duration
	result := NewResult(StatusUp)
	if hr, ok := result.(*healthResult); ok {
		hr.WithDuration(testDuration)

		// Verify the duration was set correctly
		if hr.Duration() != testDuration {
			t.Errorf("Expected duration %v, got %v", testDuration, hr.Duration())
		}
	} else {
		t.Errorf("Expected *healthResult, got %T", result)
	}
}

// TestResultWithChildren verifies that WithChildren correctly sets child results on the Result.
func TestResultWithChildren(t *testing.T) {
	// Create test child results
	child1 := NewResult(StatusUp)
	child2 := NewResult(StatusDown)
	children := []Result{child1, child2}

	// Create a result and set the children
	result := NewResult(StatusUp)
	if hr, ok := result.(*healthResult); ok {
		hr.WithChildren(children)

		// Verify the children were set correctly
		resultChildren := hr.Children()
		if len(resultChildren) != len(children) {
			t.Errorf("Expected %d children, got %d", len(children), len(resultChildren))
		}

		for i, child := range children {
			if resultChildren[i] != child {
				t.Errorf("Expected child[%d] = %v, got %v", i, child, resultChildren[i])
			}
		}

		// Test adding a single child
		child3 := NewResult(StatusDegraded)
		hr.AddChild(child3)

		// Verify the new child was added correctly
		resultChildren = hr.Children()
		if len(resultChildren) != len(children)+1 {
			t.Errorf("Expected %d children, got %d", len(children)+1, len(resultChildren))
		}

		if resultChildren[len(resultChildren)-1] != child3 {
			t.Errorf("Expected last child = %v, got %v", child3, resultChildren[len(resultChildren)-1])
		}
	} else {
		t.Errorf("Expected *healthResult, got %T", result)
	}
}

// TestComputeAggregateStatus verifies that ComputeAggregateStatus correctly aggregates multiple Result statuses.
func TestComputeAggregateStatus(t *testing.T) {
	// Test cases for different combinations of statuses
	testCases := []struct {
		name           string
		results        []Result
		expectedStatus Status
	}{
		{
			name:           "Empty results",
			results:        []Result{},
			expectedStatus: StatusUnknown,
		},
		{
			name:           "All UP",
			results:        []Result{NewResult(StatusUp), NewResult(StatusUp), NewResult(StatusUp)},
			expectedStatus: StatusUp,
		},
		{
			name:           "One DOWN",
			results:        []Result{NewResult(StatusUp), NewResult(StatusDown), NewResult(StatusUp)},
			expectedStatus: StatusDown,
		},
		{
			name:           "One DEGRADED",
			results:        []Result{NewResult(StatusUp), NewResult(StatusDegraded), NewResult(StatusUp)},
			expectedStatus: StatusDegraded,
		},
		{
			name:           "One UNKNOWN",
			results:        []Result{NewResult(StatusUp), NewResult(StatusUnknown), NewResult(StatusUp)},
			expectedStatus: StatusUnknown,
		},
		{
			name:           "DOWN takes precedence over DEGRADED",
			results:        []Result{NewResult(StatusUp), NewResult(StatusDegraded), NewResult(StatusDown)},
			expectedStatus: StatusDown,
		},
		{
			name:           "DEGRADED takes precedence over UNKNOWN",
			results:        []Result{NewResult(StatusUp), NewResult(StatusDegraded), NewResult(StatusUnknown)},
			expectedStatus: StatusDegraded,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			status := ComputeAggregateStatus(tc.results)
			if status != tc.expectedStatus {
				t.Errorf("Expected status %v, got %v", tc.expectedStatus, status)
			}
		})
	}
}

// mockCheck is a minimal implementation of the Check interface for testing.
type mockCheck struct {
	name      string
	checkType CheckType
	timeout   time.Duration
	interval  time.Duration
	enabled   bool
}

func (c *mockCheck) Name() string {
	return c.name
}

func (c *mockCheck) Type() CheckType {
	return c.checkType
}

func (c *mockCheck) Timeout() time.Duration {
	return c.timeout
}

func (c *mockCheck) Interval() time.Duration {
	return c.interval
}

func (c *mockCheck) Enabled() bool {
	return c.enabled
}

func (c *mockCheck) SetEnabled(enabled bool) {
	c.enabled = enabled
}

func (c *mockCheck) Execute(ctx context.Context) (Result, error) {
	return NewResult(StatusUp), nil
}
