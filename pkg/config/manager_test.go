// file: pkg/config/manager_test.go
// version: 1.2.0
// guid: 3c3b2a1d-5e6f-7890-ab12-cdefcdefcdef

package config

import "testing"

// TestManagerSetAndGet verifies basic Set and Get operations.
func TestManagerSetAndGet(t *testing.T) {
	m := NewManager()
	if err := m.Set("key", "value"); err != nil {
		t.Fatalf("Set returned error: %v", err)
	}
	v, err := m.GetString("key")
	if err != nil {
		t.Fatalf("GetString returned error: %v", err)
	}
	if v != "value" {
		t.Fatalf("expected value, got %s", v)
	}
}

// TestManagerWatch verifies that callbacks are triggered on Set.
func TestManagerWatch(t *testing.T) {
	m := NewManager()
	ch := make(chan interface{}, 1)
	if err := m.Watch("alpha", func(v interface{}) { ch <- v }); err != nil {
		t.Fatalf("Watch returned error: %v", err)
	}
	if err := m.Set("alpha", 42); err != nil {
		t.Fatalf("Set returned error: %v", err)
	}
	if v := <-ch; v != 42 {
		t.Fatalf("expected 42, got %v", v)
	}
}

// TestManagerMerge verifies merging ConfigData into Manager storage.
func TestManagerMerge(t *testing.T) {
	m := NewManager()
	cfg := NewConfig(GlobalConfig{Logger: LogConfig{Level: "info"}}, ModuleConfigs{})
	if err := m.Merge(cfg); err != nil {
		t.Fatalf("Merge returned error: %v", err)
	}
	v, err := m.GetString("global.logger.level")
	if err != nil {
		t.Fatalf("GetString returned error: %v", err)
	}
	if v != "info" {
		t.Fatalf("expected info, got %s", v)
	}
}
