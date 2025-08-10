// file: pkg/plugins/examples/middleware/uppercase/uppercase.go
// version: 1.0.0
// guid: 60fc3b21-9436-45b2-b396-975c3b72d8fa

package uppercase

import (
	"context"
	"fmt"
	"strings"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin converts messages to uppercase as middleware.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a new uppercase middleware plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "uppercase",
		Version:     "0.1.0",
		Type:        plugins.Middleware,
		Description: "converts messages to uppercase",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Handle converts the message to uppercase.
func (p *Plugin) Handle(ctx context.Context, msg interface{}) (interface{}, error) {
	if s, ok := msg.(string); ok {
		u := strings.ToUpper(s)
		fmt.Printf("uppercase middleware: %s -> %s\n", s, u)
		return u, nil
	}
	return msg, nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
