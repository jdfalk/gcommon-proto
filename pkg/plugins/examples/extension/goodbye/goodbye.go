// file: pkg/plugins/examples/extension/goodbye/goodbye.go
// version: 1.0.0
// guid: 2d80bb91-d5b0-476e-9bb4-c7fefb5ea182

package goodbye

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin publishes a goodbye message.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a goodbye extension plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "goodbye",
		Version:     "0.1.0",
		Type:        plugins.Extension,
		Description: "publishes goodbye messages",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Extend publishes a goodbye message via manager bus.
func (p *Plugin) Extend(m *plugins.Manager) error {
	return m.Bus().Publish(plugins.Message{Topic: "goodbye", Data: "farewell"})
}

// Start announces start.
func (p *Plugin) Start(ctx context.Context) error {
	fmt.Println("goodbye extension started")
	return nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
