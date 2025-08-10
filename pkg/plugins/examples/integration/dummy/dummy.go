// file: pkg/plugins/examples/integration/dummy/dummy.go
// version: 1.0.0
// guid: 1be0aa65-41e6-4bc0-8a94-d541b6b0cb91

package dummy

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin integrates with a dummy third-party service.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a dummy integration plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "dummy",
		Version:     "0.1.0",
		Type:        plugins.Integration,
		Description: "connects to a dummy service",
		Permissions: []plugins.Permission{plugins.PermissionNetwork},
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Connect simulates contacting the third-party service.
func (p *Plugin) Connect(ctx context.Context) error {
	fmt.Println("connecting to dummy service")
	return nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
