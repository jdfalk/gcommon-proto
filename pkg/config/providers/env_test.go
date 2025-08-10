// file: pkg/config/providers/env_test.go
// version: 1.0.1
// guid: 74e45086-560a-41ab-8605-cacc54926261

package providers

import (
	"os"
	"testing"
)

func TestEnvProvider_GetSet(t *testing.T) {
	t.Parallel()
	pIface, err := NewEnvProvider("TEST_")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	p := pIface
	if err := p.Set("KEY", "VALUE"); err != nil {
		t.Fatalf("set error: %v", err)
	}
	val, err := p.Get("KEY")
	if err != nil {
		t.Fatalf("get error: %v", err)
	}
	if val != "VALUE" {
		t.Fatalf("expected VALUE, got %v", val)
	}
	os.Unsetenv("TEST_KEY")
}

// TestEnvProvider basic get/set with additional edge cases
func TestEnvProviderEdgeCases(t *testing.T) {
	p, err := NewEnvProvider("TEST_")
	if err != nil {
		t.Fatalf("error: %v", err)
	}
	defer p.Close()
	if err := p.Set("KEY", "VALUE"); err != nil {
		t.Fatalf("set error: %v", err)
	}
	v, err := p.Get("KEY")
	if err != nil || v.(string) != "VALUE" {
		t.Fatalf("unexpected get: %v %v", v, err)
	}
}

// TODO: Add watch tests
// TODO: Add edge case tests for missing keys
// TODO: Clean up env vars after tests

// Ensure environment variable cleared after tests
func TestMain(m *testing.M) {
	code := m.Run()
	os.Unsetenv("TEST_KEY")
	os.Exit(code)
}
