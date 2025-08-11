// file: test/integration/modules/organization_test.go
// version: 1.1.0
// guid: 0780daff-c233-464f-aff0-99828621a915

package modules

import (
	"context"
	"testing"

	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"github.com/jdfalk/gcommon/pkg/organization/tenant"
	"github.com/jdfalk/gcommon/test/integration/framework"
	gproto "google.golang.org/protobuf/proto"
)

// TestOrganizationModuleIntegration covers multi-tenant features.
func TestOrganizationModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	mgr := tenant.NewManager()
	ctx := context.Background()

	t.Run("create organization", func(t *testing.T) {
		err := mgr.CreateTenant(ctx, &orgpb.Tenant{Id: gproto.String("t1")})
		if err != nil {
			t.Fatalf("create tenant failed: %v", err)
		}
	})

	t.Run("add member", func(t *testing.T) {
		t1, _ := mgr.GetTenant(ctx, "t1")
		t1.Users = append(t1.Users, &orgpb.User{Id: gproto.String("u1")})
		if err := mgr.UpdateTenant(ctx, t1); err != nil {
			t.Fatalf("update tenant: %v", err)
		}
	})

	t.Run("list members", func(t *testing.T) {
		t1, _ := mgr.GetTenant(ctx, "t1")
		if len(t1.Users) != 1 {
			t.Fatalf("expected 1 user got %d", len(t1.Users))
		}
	})

	t.Run("remove member", func(t *testing.T) {
		t1, _ := mgr.GetTenant(ctx, "t1")
		t1.Users = nil
		_ = mgr.UpdateTenant(ctx, t1)
		t1, _ = mgr.GetTenant(ctx, "t1")
		if len(t1.Users) != 0 {
			t.Fatalf("expected 0 users got %d", len(t1.Users))
		}
	})

	t.Run("delete organization", func(t *testing.T) {
		if err := mgr.DeleteTenant(ctx, "t1"); err != nil {
			t.Fatalf("delete tenant failed: %v", err)
		}
		if _, err := mgr.GetTenant(ctx, "t1"); err == nil {
			t.Fatalf("expected not found")
		}
	})
}
