// file: pkg/errors/codes_test.go
// version: 1.0.0
// guid: b1c2d3e4-1516-4f12-f345-1234567890cd

package errors

import "testing"

// TestErrorCodeUniqueness ensures error codes are unique.
func TestErrorCodeUniqueness(t *testing.T) {
	seen := map[ErrorCode]bool{}
	codes := []ErrorCode{
		ErrCodeUnknown, ErrCodeInternal, ErrCodeInvalidInput, ErrCodeNotFound,
		ErrCodeAlreadyExists, ErrCodeTimeout, ErrCodeUnavailable,
		ErrCodeConfigNotFound, ErrCodeConfigInvalid, ErrCodeConfigReadOnly,
		ErrCodeQueueNotFound, ErrCodeQueueFull, ErrCodeMessageTooLarge,
		ErrCodeUnauthorized, ErrCodeForbidden, ErrCodeTokenExpired, ErrCodeTokenInvalid,
		ErrCodeMetricNotFound, ErrCodeMetricInvalid, ErrCodeMetricCollectionFailed,
		ErrCodeMetricExportFailed, ErrCodeMetricProviderUnavailable,
		ErrCodeHealthCheckFailed, ErrCodeHealthServiceUnavailable, ErrCodeHealthTimeout,
		ErrCodeCacheMiss, ErrCodeCacheUnavailable, ErrCodeCacheCorrupted,
		ErrCodeCacheSerialization, ErrCodeCacheDeserialization,
		ErrCodeRouteNotFound, ErrCodeRenderFailed, ErrCodeSessionExpired,
		ErrCodeBadGateway, ErrCodeCSRFDetected,
		ErrCodeDBConnection, ErrCodeDBQuery, ErrCodeDBTransaction,
		ErrCodeDBMigration, ErrCodeDBConstraint,
		ErrCodeLogWriteFailed, ErrCodeLogConfiguration, ErrCodeLogRotationFailed,
		ErrCodeLogPermissionDenied, ErrCodeLogUnknownFormat,
	}
	for _, c := range codes {
		if seen[c] {
			t.Fatalf("duplicate code: %v", c)
		}
		seen[c] = true
	}
}
