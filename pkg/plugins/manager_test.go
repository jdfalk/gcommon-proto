// file: pkg/plugins/manager_test.go
// version: 1.0.0
// guid: e7324c9a-331b-4a50-98c8-afb61896c5a5

package plugins

import (
	"context"
	"testing"
)

type simplePlugin struct{ started bool }

func (s *simplePlugin) Name() string                            { return "simple" }
func (s *simplePlugin) Version() string                         { return "v1" }
func (s *simplePlugin) Initialize(map[string]interface{}) error { return nil }
func (s *simplePlugin) Start(ctx context.Context) error         { s.started = true; return nil }
func (s *simplePlugin) Stop(ctx context.Context) error          { s.started = false; return nil }
func (s *simplePlugin) Health() HealthStatus                    { return HealthStatus{OK: true} }

func TestManagerStartStop(t *testing.T) {
	r := NewRegistry()
	m := NewManager(r, nil, nil)
	p := &simplePlugin{}
	md := Metadata{Name: "simple", Type: Provider}
	if err := m.Register(p, md, Policy{}); err != nil {
		t.Fatalf("register: %v", err)
	}
	if err := m.StartAll(context.Background()); err != nil {
		t.Fatalf("start: %v", err)
	}
	if !p.started {
		t.Fatalf("plugin not started")
	}
	if err := m.StopAll(context.Background()); err != nil {
		t.Fatalf("stop: %v", err)
	}
	if p.started {
		t.Fatalf("plugin not stopped")
	}
}
