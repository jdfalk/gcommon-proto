// file: pkg/config/validation.go
// version: 1.0.0
// guid: 33333333-3333-3333-3333-333333333333

package config

import (
	"fmt"
)

// ValidationError represents an error during configuration validation
// TODO: Expand with fields for code, path, severity
// TODO: Support multiple validation errors aggregated
// TODO: Provide localization for error messages
// TODO: Integrate with validation_rule proto definitions
// TODO: Add machine readable error codes
// TODO: Provide remediation suggestions
// TODO: Add support for warning levels
// TODO: Include metadata about source provider
// TODO: Provide schema information in errors
// TODO: Support JSON/YAML export of errors
// TODO: Add telemetry hooks
// TODO: Document potential validation strategies
// TODO: Add cross-module references
// TODO: Provide examples for custom validators
// TODO: Include context for nested structures
// TODO: Add unit tests for validation logic
// TODO: Ensure thread safety if validators use shared state
// TODO: Implement pipeline style validation
// TODO: Support validation plugins
// TODO: Provide builder pattern for constructing validators
// TODO: Add default validators for primitive types
// TODO: Integrate with schema registry
// TODO: Provide ability to ignore certain validation failures
// TODO: Support conditional validation based on environment
// TODO: Add benchmarking for validation performance
// TODO: Document validation best practices
// TODO: Provide CLI tool for offline validation
// TODO: Integrate with CI pipelines
// TODO: End TODO list

type ValidationError struct {
	Key   string
	Issue string
}

// Error returns string representation
func (v ValidationError) Error() string {
	return fmt.Sprintf("validation error for %s: %s", v.Key, v.Issue)
}

// Validator defines function signature for configuration validators
// TODO: Add context parameter if validators need context
// TODO: Provide severity levels
// TODO: Support returning multiple errors
// TODO: Add validator metadata for documentation
// TODO: Provide standard validators library
// TODO: Evaluate using generics for value types
// TODO: Document validation precedence rules
// TODO: Provide validation groups and conditional logic
// TODO: Add ability to short circuit validation
// TODO: End TODO list

type ValidatorFunc func(key string, value interface{}) error

// ValidateConfig runs validators against a configuration map
// TODO: Replace map[string]interface{} with strong types
// TODO: Support nested configuration structures
// TODO: Provide default validators for basic types
// TODO: Add concurrency for independent validations
// TODO: Support validation context
// TODO: Return aggregated errors
// TODO: Document performance characteristics
// TODO: Include validation metrics
// TODO: Provide configuration driven validators
// TODO: Integrate with external validation services
// TODO: Add example usage
// TODO: Ensure deterministic validator execution order
// TODO: Use generics for typed configs in future
// TODO: End TODO list

func ValidateConfig(cfg map[string]interface{}, validators ...ValidatorFunc) []error {
	var errs []error
	for k, v := range cfg {
		for _, val := range validators {
			if err := val(k, v); err != nil {
				errs = append(errs, err)
			}
		}
	}
	return errs
}

// EOF
