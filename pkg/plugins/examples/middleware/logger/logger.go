// file: pkg/plugins/examples/middleware/logger/logger.go
// version: 1.0.0
// guid: 452445b8-2d87-4f39-8fbe-eb6e56b51b96

package logger

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin logs messages as middleware.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a logger middleware plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "logger",
		Version:     "0.1.0",
		Type:        plugins.Middleware,
		Description: "logs messages passing through",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Handle logs the message and returns it unchanged.
func (p *Plugin) Handle(ctx context.Context, msg interface{}) (interface{}, error) {
	fmt.Printf("logger middleware: %v\n", msg)
	return msg, nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
