// file: security/policies/data.go
// version: 1.1.0
// guid: 616965da-91fe-4263-83da-407a00d0a8f0

package policies

import "time"

// Classification defines sensitivity levels for data.
type Classification string

// Supported classification levels.
const (
	ClassificationPublic   Classification = "PUBLIC"
	ClassificationInternal Classification = "INTERNAL"
	ClassificationSecret   Classification = "SECRET"
)

// DataPolicy defines data protection requirements.
type DataPolicy struct {
	Classification Classification
	RetentionDays  int
	Encrypted      bool
}

// RetentionExpired returns true if the data age exceeds retention policy.
func (p DataPolicy) RetentionExpired(createdAt time.Time) bool {
	if p.RetentionDays <= 0 {
		return false
	}
	return time.Since(createdAt) > time.Duration(p.RetentionDays)*24*time.Hour
}

// Validate checks whether access is permitted given classification and encryption status.
func (p DataPolicy) Validate(encrypted bool) bool {
	if p.Classification == ClassificationSecret && !encrypted {
		return false
	}
	if p.Classification == ClassificationInternal && !encrypted {
		return false
	}
	return true
}
