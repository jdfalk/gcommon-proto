// file: pkg/config/validator_test.go
// version: 1.0.0
// guid: 66666666-7777-8888-9999-cccccccccccc

package config

import "testing"

// TestValidatorRequiredRule ensures missing keys produce errors.
func TestValidatorRequiredRule(t *testing.T) {
	v := NewValidator()
	v.AddRule(RequiredRule{Keys: []string{"alpha"}})
	if err := v.Validate(map[string]interface{}{}); err == nil {
		t.Fatalf("expected error for missing key")
	}
}

// TODO:
//  - Add tests for multiple rules executing together
//  - Verify error aggregation behaviour
//  - Test validation with nested maps
//  - Include benchmarks for rule execution
//  - Mock custom validation rules
//  - Validate correct messages are returned
//  - Add tests for successful validation paths
//  - Cover edge cases like nil configuration maps
//  - Ensure thread safety when validator used concurrently
//  - Provide integration tests with ConfigManager
