// file: pkg/auth/providers/oauth2_test.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-abcd-ef0123456789

package providers

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"golang.org/x/oauth2"
)

func TestOAuth2Provider(t *testing.T) {
	tokenSrv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]any{
			"access_token":  "acc",
			"refresh_token": "ref",
			"token_type":    "bearer",
			"expires_in":    3600,
		})
	}))
	defer tokenSrv.Close()

	introspectSrv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		json.NewEncoder(w).Encode(map[string]any{"active": true, "sub": "user", "exp": time.Now().Add(time.Hour).Unix()})
	}))
	defer introspectSrv.Close()

	revokeCalled := false
	revokeSrv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		revokeCalled = true
	}))
	defer revokeSrv.Close()

	cfg := &oauth2.Config{ClientID: "id", ClientSecret: "secret", Endpoint: oauth2.Endpoint{TokenURL: tokenSrv.URL}}
	prov := NewOAuth2Provider(cfg, nil, introspectSrv.URL, revokeSrv.URL, nil)

	req := &proto.AuthenticateRequest{}
	creds := &proto.OAuth2Credentials{}
	creds.SetCode("abc")
	req.SetOauth2(creds)
	resp, err := prov.Authenticate(context.Background(), req)
	if err != nil || resp.GetAccessToken() == "" {
		t.Fatalf("authenticate failed: %v", err)
	}

	vreq := &proto.ValidateTokenRequest{}
	vreq.SetAccessToken(resp.GetAccessToken())
	vresp, err := prov.ValidateToken(context.Background(), vreq)
	if err != nil || !vresp.GetValid() {
		t.Fatalf("validate failed")
	}

	rreq := &proto.RefreshTokenRequest{}
	rreq.SetRefreshToken(resp.GetRefreshToken())
	if _, err := prov.RefreshToken(context.Background(), rreq); err != nil {
		t.Fatalf("refresh failed: %v", err)
	}

	revReq := &proto.RevokeTokenRequest{}
	revReq.SetToken(resp.GetAccessToken())
	if _, err := prov.RevokeToken(context.Background(), revReq); err != nil {
		t.Fatalf("revoke failed: %v", err)
	}
	if !revokeCalled {
		t.Fatalf("revoke endpoint not called")
	}
}
