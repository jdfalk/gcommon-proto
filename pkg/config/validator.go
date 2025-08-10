// file: pkg/config/validator.go
// version: 1.0.0
// guid: 22222222-3333-4444-5555-666666666666

package config

import "fmt"

// ValidationRule defines a single configuration validation rule.
type ValidationRule interface {
	Validate(cfg map[string]interface{}) error
}

// Validator runs a set of validation rules against configuration data.
type Validator struct {
	rules []ValidationRule
}

// NewValidator creates an empty validator.
func NewValidator() *Validator { return &Validator{} }

// AddRule appends a new rule to the validator.
func (v *Validator) AddRule(r ValidationRule) { v.rules = append(v.rules, r) }

// Validate executes all validation rules.
func (v *Validator) Validate(cfg map[string]interface{}) error {
	for _, r := range v.rules {
		if err := r.Validate(cfg); err != nil {
			return err
		}
	}
	return nil
}

// RequiredRule ensures specified keys are present.
type RequiredRule struct {
	Keys []string
}

// Validate checks required keys.
func (r RequiredRule) Validate(cfg map[string]interface{}) error {
	for _, k := range r.Keys {
		if _, ok := cfg[k]; !ok {
			return fmt.Errorf("missing required key %s", k)
		}
	}
	return nil
}

// ValidateMap provides a convenience wrapper for basic validation.
func ValidateMap(cfg map[string]interface{}) error {
	v := NewValidator()
	// TODO: add schema and dependency rules
	return v.Validate(cfg)
}

// TODO:
//  - Implement JSON schema validation for structured configs
//  - Validate cross-field dependencies such as port ranges
//  - Provide environment specific validation profiles
//  - Allow custom user-defined validation callbacks
//  - Integrate with logging to report validation errors
//  - Accumulate multiple errors before returning
//  - Support default value injection for missing keys
//  - Expose metrics for validation latency and failures
//  - Add context-aware cancellation for long validations
//  - Consider caching validation results for identical inputs
//  - Provide CLI tool for offline validation of configuration files
//  - Write extensive unit tests for edge cases
//  - Document validation rule writing guidelines
//  - Support localization for error messages
//  - Add linting-style warnings in addition to errors
//  - Evaluate performance of rule execution
//  - Enable rule grouping and conditional execution
//  - Allow referencing values from multiple modules
//  - Validate dynamic updates before applying them
//  - Research integration with policy engines like OPA
