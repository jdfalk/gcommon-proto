// file: test/integration/modules/auth_test.go
// version: 1.1.0
// guid: fb3dd924-8a0d-4172-9372-39d3ec95ebc7

package modules

import (
	"context"
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	authpb "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/providers"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestAuthModuleIntegration verifies authentication flows.
func TestAuthModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	provider := providers.NewLocalProvider([]byte("secret"), map[string]string{"alice": "password"}, map[string]string{"alice": "admin"})

	var token string
	t.Run("login user", func(t *testing.T) {
		resp, err := provider.Authenticate(context.Background(), &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "alice", Password: "password"}})
		if err != nil {
			t.Fatalf("authenticate failed: %v", err)
		}
		token = resp.GetAccessToken()
		if token == "" {
			t.Fatalf("expected token")
		}
	})

	t.Run("validate token", func(t *testing.T) {
		resp, err := provider.ValidateToken(context.Background(), &authpb.ValidateTokenRequest{AccessToken: token})
		if err != nil || !resp.GetValid() {
			t.Fatalf("validate failed: %v", err)
		}
	})

	t.Run("refresh token", func(t *testing.T) {
		authResp, _ := provider.Authenticate(context.Background(), &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "alice", Password: "password"}})
		resp, err := provider.RefreshToken(context.Background(), &authpb.RefreshTokenRequest{RefreshToken: authResp.GetRefreshToken()})
		if err != nil || resp.GetAccessToken() == "" {
			t.Fatalf("refresh failed: %v", err)
		}
	})

	t.Run("logout user", func(t *testing.T) {
		resp, err := provider.RevokeToken(context.Background(), &authpb.RevokeTokenRequest{TokenId: "1"})
		if err != nil || resp.GetTokenId() == "" {
			t.Fatalf("revoke failed: %v", err)
		}
	})
}
