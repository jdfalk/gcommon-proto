// file: pkg/plugins/sdk/base.go
// version: 1.0.0
// guid: 5bb1cce2-b9fa-4e75-8a38-2a1a2e4f5952

package sdk

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
)

// BasePlugin provides default implementations for common plugin behavior.
type BasePlugin struct {
	Metadata plugins.Metadata
}

// Name returns the plugin name.
func (b *BasePlugin) Name() string { return b.Metadata.Name }

// Version returns the plugin version.
func (b *BasePlugin) Version() string { return b.Metadata.Version }

// Initialize sets up plugin configuration. Override for custom behavior.
func (b *BasePlugin) Initialize(config map[string]interface{}) error { return nil }

// Start activates the plugin. Override for custom behavior.
func (b *BasePlugin) Start(ctx context.Context) error { return nil }

// Stop deactivates the plugin. Override for custom behavior.
func (b *BasePlugin) Stop(ctx context.Context) error { return nil }

// Health reports plugin health. Override for custom behavior.
func (b *BasePlugin) Health() plugins.HealthStatus {
	return plugins.HealthStatus{OK: true, Info: "healthy"}
}

// GenerateDocumentation creates a simple documentation string for a plugin.
func GenerateDocumentation(md plugins.Metadata) string {
	perms := "none"
	if len(md.Permissions) > 0 {
		perms = fmt.Sprint(md.Permissions)
	}
	return fmt.Sprintf("%s (v%s) - %s\nPermissions: %s\n", md.Name, md.Version, md.Description, perms)
}

// ProviderTemplate returns a Go code template for a provider plugin.
func ProviderTemplate(name string) string {
	return fmt.Sprintf(`package %s

import (
        "context"

        "github.com/jdfalk/gcommon/pkg/plugins"
        sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// %s implements a simple provider plugin.
type %s struct {
        sdk.BasePlugin
}

// New creates a new %s.
func New() *%s {
        md := plugins.Metadata{
                Name:        "%s",
                Version:     "0.1.0",
                Type:        plugins.Provider,
                Description: "%s provider",
        }
        return &%s{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// GetProvider returns the provider implementation.
func (p *%s) GetProvider() interface{} {
        return func() string { return "%s" }
}

var Descriptor = plugins.Descriptor{
        Metadata: New().Metadata,
        New: func() plugins.Plugin { return New() },
}
`, name, name, name, name, name, name, name, name, name, name)
}
