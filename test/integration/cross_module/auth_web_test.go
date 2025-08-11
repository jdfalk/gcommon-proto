// file: test/integration/cross_module/auth_web_test.go
// version: 1.1.0
// guid: 90189c12-d5e3-44bd-bbc2-0056a44f0eed

package crossmodule

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	authpb "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/providers"
	"github.com/jdfalk/gcommon/pkg/web/middleware"
	_ "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestAuthWebIntegration ensures auth middleware works with the web module.
func TestAuthWebIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	provider := providers.NewLocalProvider([]byte("secret"), map[string]string{"bob": "pwd"}, map[string]string{})
	authResp, _ := provider.Authenticate(context.Background(), &authpb.AuthenticateRequest{Password: &authpb.PasswordCredentials{Username: "bob", Password: "pwd"}})
	token := authResp.GetAccessToken()
	mw := middleware.NewAuthMiddleware(token)
	handler := mw.Handle(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { w.WriteHeader(http.StatusOK) }))
	srv := httptest.NewServer(handler)
	defer srv.Close()

	t.Run("middleware protects route", func(t *testing.T) {
		res, err := http.Get(srv.URL)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		if res.StatusCode != http.StatusUnauthorized {
			t.Fatalf("expected 401 got %d", res.StatusCode)
		}
	})

	t.Run("authenticated request succeeds", func(t *testing.T) {
		req, _ := http.NewRequest("GET", srv.URL, nil)
		req.Header.Set("Authorization", "Bearer "+token)
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		if res.StatusCode != http.StatusOK {
			t.Fatalf("expected 200 got %d", res.StatusCode)
		}
	})

	t.Run("logout clears session", func(t *testing.T) {
		req, _ := http.NewRequest("GET", srv.URL, nil)
		res, _ := http.DefaultClient.Do(req)
		if res.StatusCode != http.StatusUnauthorized {
			t.Fatalf("expected 401 after logout")
		}
	})
}
