// file: pkg/plugins/examples/extension/hello/hello.go
// version: 1.0.0
// guid: f3e0f4f7-7c45-4d6a-90ab-77bd8bfa9a8e

package hello

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin adds a hello extension.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a hello extension plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "hello",
		Version:     "0.1.0",
		Type:        plugins.Extension,
		Description: "adds hello world extension",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Extend outputs a hello message using the manager's bus.
func (p *Plugin) Extend(m *plugins.Manager) error {
	return m.Bus().Publish(plugins.Message{Topic: "hello", Data: "world"})
}

// Start prints a startup message.
func (p *Plugin) Start(ctx context.Context) error {
	fmt.Println("hello extension started")
	return nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
