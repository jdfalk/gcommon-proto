// file: pkg/plugins/registry_test.go
// version: 1.0.0
// guid: f3354f27-f606-45a2-8867-ac15ea4cd076

package plugins

import (
	"context"
	"testing"
)

type testPlugin struct{ name string }

func (t *testPlugin) Name() string                                   { return t.name }
func (t *testPlugin) Version() string                                { return "v1" }
func (t *testPlugin) Initialize(config map[string]interface{}) error { return nil }
func (t *testPlugin) Start(ctx context.Context) error                { return nil }
func (t *testPlugin) Stop(ctx context.Context) error                 { return nil }
func (t *testPlugin) Health() HealthStatus                           { return HealthStatus{OK: true} }

func TestRegistryRegisterGet(t *testing.T) {
	r := NewRegistry()
	p := &testPlugin{name: "test"}
	md := Metadata{Name: "test", Version: "v1", Type: Provider}
	if err := r.Register(p, md); err != nil {
		t.Fatalf("register: %v", err)
	}

	got, gmd, ok := r.Get("test")
	if !ok {
		t.Fatalf("plugin not found")
	}
	if got != p || gmd.Name != md.Name {
		t.Fatalf("got %v %v, want %v %v", got, gmd, p, md)
	}
}

func TestRegistryListByType(t *testing.T) {
	r := NewRegistry()
	p1 := &testPlugin{name: "p1"}
	r.Register(p1, Metadata{Name: "p1", Version: "v1", Type: Provider})
	p2 := &testPlugin{name: "p2"}
	r.Register(p2, Metadata{Name: "p2", Version: "v1", Type: Middleware})

	providers := r.ListByType(Provider)
	if len(providers) != 1 || providers[0].Name() != "p1" {
		t.Fatalf("unexpected providers %v", providers)
	}
}
