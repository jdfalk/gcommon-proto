// file: pkg/plugins/examples/provider/reverse/reverse.go
// version: 1.0.0
// guid: d295eddd-6e5b-4475-8c55-76fac1a5f477

package reverse

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/plugins"
	sdk "github.com/jdfalk/gcommon/pkg/plugins/sdk"
)

// Plugin provides a string reversal provider.
type Plugin struct {
	sdk.BasePlugin
}

// New creates a new reverse plugin.
func New() *Plugin {
	md := plugins.Metadata{
		Name:        "reverse",
		Version:     "0.1.0",
		Type:        plugins.Provider,
		Description: "reverses strings",
	}
	return &Plugin{BasePlugin: sdk.BasePlugin{Metadata: md}}
}

// GetProvider returns the reverse provider implementation.
func (p *Plugin) GetProvider() interface{} {
	return func(s string) string { return reverseString(s) }
}

func reverseString(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func (p *Plugin) Start(ctx context.Context) error { return nil }

var Descriptor = plugins.Descriptor{
	Metadata: New().Metadata,
	New:      func() plugins.Plugin { return New() },
}
