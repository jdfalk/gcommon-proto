// file: pkg/plugins/examples/provider/echo/echo.go
// version: 1.0.0
// guid: 0ae6fa8f-760e-4f0c-80ba-623a5a89f721

package echo

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin provides an echo provider.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a new Plugin instance.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "echo",
		Version:     "0.1.0",
		Type:        plugins.Provider,
		Description: "echo provider returns input as output",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// GetProvider returns the echo provider implementation.
func (p *Plugin) GetProvider() interface{} {
	return func(s string) string { return s }
}

// Start announces plugin start via bus.
func (p *Plugin) Start(ctx context.Context) error { return nil }

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
