// file: pkg/organization/tenant/manager_test.go
// version: 1.1.0
// guid: 0c9b693c-edf2-444e-ba17-50a0bf2ea8dc

package tenant

import (
	"context"
	"testing"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	gproto "google.golang.org/protobuf/proto"
)

// TestManager_TenantLifecycle verifies basic tenant operations.
func TestManager_TenantLifecycle(t *testing.T) {
	// Setup
	m := NewManager()
	ctx := context.Background()
	tenant := (&orgpb.Tenant_builder{Id: gproto.String("t1"), Name: gproto.String("TenantOne")}).Build()

	// Exercise: Create
	if err := m.CreateTenant(ctx, tenant); err != nil {
		t.Fatalf("create tenant: %v", err)
	}

	// Verify: Get
	got, err := m.GetTenant(ctx, "t1")
	if err != nil {
		t.Fatalf("get tenant: %v", err)
	}
	if got.GetName() != "TenantOne" {
		t.Fatalf("expected name TenantOne, got %s", got.GetName())
	}

	// Exercise: Update
	updated := (&orgpb.Tenant_builder{Id: gproto.String("t1"), Name: gproto.String("TenantUno")}).Build()
	if err := m.UpdateTenant(ctx, updated); err != nil {
		t.Fatalf("update tenant: %v", err)
	}

	// Verify: List
	list, err := m.ListTenants(ctx)
	if err != nil {
		t.Fatalf("list tenants: %v", err)
	}
	if len(list) != 1 {
		t.Fatalf("expected 1 tenant, got %d", len(list))
	}

	// Exercise: Delete
	if err := m.DeleteTenant(ctx, "t1"); err != nil {
		t.Fatalf("delete tenant: %v", err)
	}

	// Verify: Get after delete
	if _, err := m.GetTenant(ctx, "t1"); err == nil {
		t.Fatalf("expected error for missing tenant")
	}
}
