// file: pkg/plugins/sdk/testutil.go
// version: 1.0.0
// guid: e1a1af2d-92bb-4ea1-8f74-52f7593bd84b

package sdk

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/plugins"
)

// NewTestManager returns a manager suitable for unit tests.
func NewTestManager() *plugins.Manager {
	r := plugins.NewRegistry()
	bus := plugins.NewInMemoryBus()
	checker := plugins.DefaultChecker{}
	return plugins.NewManager(r, bus, checker)
}

// StartPlugin starts a plugin using the test manager.
func StartPlugin(ctx context.Context, m *plugins.Manager, p plugins.Plugin, md plugins.Metadata) error {
	policy := plugins.Policy{Permissions: md.Permissions}
	if err := m.Register(p, md, policy); err != nil {
		return err
	}
	return p.Start(ctx)
}
