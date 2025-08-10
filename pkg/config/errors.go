// file: pkg/config/errors.go
// version: 1.0.0
// guid: 44444444-5555-6666-7777-888888888888

package config

import "errors"

// Common configuration errors
var (
	// ErrProviderNotFound is returned when a requested provider is not found
	ErrProviderNotFound = errors.New("provider not found")

	// ErrProviderNotConfigured is returned when a provider is not properly configured
	ErrProviderNotConfigured = errors.New("provider not configured")

	// ErrKeyNotFound is returned when a configuration key is not found
	ErrKeyNotFound = errors.New("key not found")

	// ErrInvalidKey is returned when a configuration key is invalid
	ErrInvalidKey = errors.New("invalid key")

	// ErrInvalidValue is returned when a configuration value is invalid
	ErrInvalidValue = errors.New("invalid value")

	// ErrWatchFailed is returned when watching a key fails
	ErrWatchFailed = errors.New("watch failed")

	// ErrProviderClosed is returned when attempting to use a closed provider
	ErrProviderClosed = errors.New("provider closed")
)
