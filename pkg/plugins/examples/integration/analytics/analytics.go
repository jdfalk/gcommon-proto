// file: pkg/plugins/examples/integration/analytics/analytics.go
// version: 1.0.0
// guid: c0d9e7e6-e51d-4dec-8a59-98992bcc12c7

package analytics

import (
	"context"
	"fmt"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin integrates with a dummy analytics service.
type Plugin struct {
	sdk.BasePlugin
}

// New creates an analytics integration plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "analytics",
		Version:     "0.1.0",
		Type:        plugins.Integration,
		Description: "sends events to a dummy analytics service",
		Permissions: []plugins.Permission{plugins.PermissionNetwork},
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// Connect simulates event reporting.
func (p *Plugin) Connect(ctx context.Context) error {
	fmt.Println("sending event to analytics service")
	return nil
}

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
