// file: pkg/organization/tenant/isolation_test.go
// version: 1.1.0
// guid: ce431a3e-e0db-45c9-b44b-efe5caad3b5b

package tenant

import (
	"context"
	"testing"
)

// TestIsolationManager_ConfigAndEnforce verifies configuration and enforcement logic.
func TestIsolationManager_ConfigAndEnforce(t *testing.T) {
	// Setup
	ctx := context.Background()
	m := NewIsolationManager()
	cfg := &IsolationConfig{AllowedDomains: []string{"example.com"}, RestrictedResources: []string{"r1"}}

	// Exercise
	if err := m.Configure(ctx, "t1", cfg); err != nil {
		t.Fatalf("configure: %v", err)
	}

	// Verify allowed access
	if err := m.Enforce(ctx, "t1", "example.com", "r2"); err != nil {
		t.Fatalf("enforce allowed: %v", err)
	}

	// Verify restricted resource
	if err := m.Enforce(ctx, "t1", "example.com", "r1"); err == nil {
		t.Fatalf("expected restriction")
	}

	// Verify domain denial
	if err := m.Enforce(ctx, "t1", "bad.com", "r2"); err == nil {
		t.Fatalf("expected domain denial")
	}
}

// TestIsolationManager_RecordUsage ensures usage is accumulated.
func TestIsolationManager_RecordUsage(t *testing.T) {
	ctx := context.Background()
	m := NewIsolationManager()
	_ = m.Configure(ctx, "t1", &IsolationConfig{})
	usage := &Usage{CpuSeconds: 10}
	if err := m.RecordUsage(ctx, "t1", usage); err != nil {
		t.Fatalf("record usage: %v", err)
	}
	got, err := m.Usage(ctx, "t1")
	if err != nil {
		t.Fatalf("usage: %v", err)
	}
	if got.CpuSeconds != 10 {
		t.Fatalf("expected cpu 10, got %d", got.CpuSeconds)
	}
}
