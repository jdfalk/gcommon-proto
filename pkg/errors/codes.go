// file: pkg/errors/codes.go
// version: 1.1.0
// guid: e8950930-ae06-40b9-b3f6-2a64a16af24a

package errors

// ErrorCode represents a standardized gcommon error code.
type ErrorCode int

const (
	// General errors
	ErrCodeUnknown ErrorCode = iota
	ErrCodeInternal
	ErrCodeInvalidInput
	ErrCodeNotFound
	ErrCodeAlreadyExists
	ErrCodeTimeout
	ErrCodeUnavailable

	// Config module errors
	ErrCodeConfigNotFound
	ErrCodeConfigInvalid
	ErrCodeConfigReadOnly

	// Queue module errors
	ErrCodeQueueNotFound
	ErrCodeQueueFull
	ErrCodeMessageTooLarge

	// Auth module errors
	ErrCodeUnauthorized
	ErrCodeForbidden
	ErrCodeTokenExpired
	ErrCodeTokenInvalid

	// Metrics module errors
	ErrCodeMetricNotFound
	ErrCodeMetricInvalid
	ErrCodeMetricCollectionFailed
	ErrCodeMetricExportFailed
	ErrCodeMetricProviderUnavailable

	// Health module errors
	ErrCodeHealthCheckFailed
	ErrCodeHealthServiceUnavailable
	ErrCodeHealthTimeout

	// Cache module errors
	ErrCodeCacheMiss
	ErrCodeCacheUnavailable
	ErrCodeCacheCorrupted
	ErrCodeCacheSerialization
	ErrCodeCacheDeserialization

	// Web module errors
	ErrCodeRouteNotFound
	ErrCodeRenderFailed
	ErrCodeSessionExpired
	ErrCodeBadGateway
	ErrCodeCSRFDetected

	// Database module errors
	ErrCodeDBConnection
	ErrCodeDBQuery
	ErrCodeDBTransaction
	ErrCodeDBMigration
	ErrCodeDBConstraint

	// Logging module errors
	ErrCodeLogWriteFailed
	ErrCodeLogConfiguration
	ErrCodeLogRotationFailed
	ErrCodeLogPermissionDenied
	ErrCodeLogUnknownFormat
)
