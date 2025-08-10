// file: pkg/plugins/security.go
// version: 1.0.0
// guid: 04b518ba-5c55-43fe-9080-78e03d1ddcd4

package plugins

import (
	"errors"
	"fmt"
	"runtime"
	"time"
)

// Permission represents a security permission granted to a plugin.
type Permission string

const (
	// PermissionRead allows read-only operations.
	PermissionRead Permission = "read"
	// PermissionWrite allows write operations.
	PermissionWrite Permission = "write"
	// PermissionNetwork allows outbound network access.
	PermissionNetwork Permission = "network"
)

// Policy defines security constraints for a plugin.
type Policy struct {
	Permissions []Permission
	MaxCPU      int // percentage
	MaxMemory   int // megabytes
	Timeout     time.Duration
}

// Checker validates plugin security requirements.
type Checker interface {
	Validate(p Plugin, policy Policy) error
}

// DefaultChecker implements basic security checks.
type DefaultChecker struct{}

// Validate ensures the plugin meets the provided policy constraints.
func (DefaultChecker) Validate(p Plugin, policy Policy) error {
	md, ok := GetMetadata(p)
	if !ok {
		return errors.New("plugin metadata not found")
	}
	if err := validatePermissions(md.Permissions, policy.Permissions); err != nil {
		return fmt.Errorf("permissions: %w", err)
	}
	if policy.MaxMemory > 0 {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		used := int(m.Alloc / 1024 / 1024)
		if used > policy.MaxMemory {
			return fmt.Errorf("memory limit exceeded: %dMB > %dMB", used, policy.MaxMemory)
		}
	}
	return nil
}

func validatePermissions(required, allowed []Permission) error {
	allowedSet := make(map[Permission]struct{}, len(allowed))
	for _, perm := range allowed {
		allowedSet[perm] = struct{}{}
	}
	for _, need := range required {
		if _, ok := allowedSet[need]; !ok {
			return fmt.Errorf("permission %s not granted", need)
		}
	}
	return nil
}

// metadataKey provides access to plugin metadata when wrapped.
type metadataKey struct{}

// WithMetadata attaches metadata to a plugin instance.
func WithMetadata(p Plugin, md Metadata) Plugin {
	return &metadataWrapper{Plugin: p, metadata: md}
}

// metadataWrapper exposes metadata for security checks.
type metadataWrapper struct {
	Plugin
	metadata Metadata
}

// GetMetadata extracts plugin metadata if available.
func GetMetadata(p Plugin) (Metadata, bool) {
	if w, ok := p.(*metadataWrapper); ok {
		return w.metadata, true
	}
	return Metadata{}, false
}
