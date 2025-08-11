// file: test/integration/cross_module/organization_auth_test.go
// version: 1.1.0
// guid: 7becba6b-a484-4276-a38c-b88f4476b1cb

package crossmodule

import (
	"context"
	"testing"

	authpb "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/providers"
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"github.com/jdfalk/gcommon/pkg/organization/tenant"
	"github.com/jdfalk/gcommon/test/integration/framework"
	gproto "google.golang.org/protobuf/proto"
)

// TestOrganizationAuthIntegration verifies multi-tenant authentication.
func TestOrganizationAuthIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	mgr := tenant.NewManager()
	ctx := context.Background()
	_ = mgr.CreateTenant(ctx, &orgpb.Tenant{Id: gproto.String("t1")})
	_ = mgr.CreateTenant(ctx, &orgpb.Tenant{Id: gproto.String("t2")})
	provider := providers.NewLocalProvider([]byte("secret"), map[string]string{"a": "p", "b": "p"}, map[string]string{"a": "t1", "b": "t2"})

	t.Run("tenant isolation", func(t *testing.T) {
		resp, _ := provider.Authenticate(ctx, &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "a", Password: "p"}})
		if resp.GetAccessToken() == "" {
			t.Fatalf("no token")
		}
	})

	t.Run("cross-tenant access denied", func(t *testing.T) {
		if err := mgr.DeleteTenant(ctx, "t2"); err != nil {
			t.Fatalf("delete tenant failed: %v", err)
		}
		if _, err := mgr.GetTenant(ctx, "t2"); err == nil {
			t.Fatalf("tenant still exists")
		}
	})

	t.Run("tenant admin", func(t *testing.T) {
		resp, _ := provider.Authenticate(ctx, &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "a", Password: "p"}})
		if resp.GetAccessToken() == "" {
			t.Fatalf("tenant admin auth failed")
		}
	})

	t.Run("global admin", func(t *testing.T) {
		provider := providers.NewLocalProvider([]byte("secret"), map[string]string{"admin": "p"}, map[string]string{"admin": "*"})
		resp, _ := provider.Authenticate(ctx, &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "admin", Password: "p"}})
		if resp.GetAccessToken() == "" {
			t.Fatalf("global admin auth failed")
		}
	})
}
