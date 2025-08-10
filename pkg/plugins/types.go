// file: pkg/plugins/types.go
// version: 1.0.0
// guid: 0c0c287a-7807-4f23-8f35-46a1b465a64f

package plugins

import (
	"context"
	"fmt"
)

// Type identifies the category of a plugin.
type Type int

const (
	// Provider implements a concrete service provider.
	Provider Type = iota
	// Middleware processes requests or responses.
	Middleware
	// Extension adds extra functionality to the host application.
	Extension
	// Integration connects third-party services.
	Integration
)

// String returns the string representation of the plugin type.
func (t Type) String() string {
	switch t {
	case Provider:
		return "provider"
	case Middleware:
		return "middleware"
	case Extension:
		return "extension"
	case Integration:
		return "integration"
	default:
		return fmt.Sprintf("unknown(%d)", int(t))
	}
}

// Metadata describes a plugin's basic information and requirements.
type Metadata struct {
	Name        string
	Version     string
	Type        Type
	Description string
	Permissions []Permission
}

// Descriptor exposes metadata and a factory for plugin instances.
type Descriptor struct {
	Metadata Metadata
	New      func() Plugin
}

// MiddlewarePlugin defines middleware behavior for request/response processing.
type MiddlewarePlugin interface {
	Plugin
	Handle(ctx context.Context, msg interface{}) (interface{}, error)
}

// ExtensionPlugin defines extensions that modify the host system.
type ExtensionPlugin interface {
	Plugin
	Extend(m *Manager) error
}

// IntegrationPlugin defines plugins that integrate external systems.
type IntegrationPlugin interface {
	Plugin
	Connect(ctx context.Context) error
}
