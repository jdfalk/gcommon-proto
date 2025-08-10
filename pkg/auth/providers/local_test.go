// file: pkg/auth/providers/local_test.go
// version: 1.0.0
// guid: c435feb8-73af-440f-b59a-bf6a77501547

package providers

import (
	"context"
	"testing"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

func TestLocalProvider(t *testing.T) {
	users := map[string]string{"alice": "password"}
	roles := map[string]string{"alice": "admin"}
	p := NewLocalProvider([]byte("secret"), users, roles)
	req := &proto.AuthenticateRequest{}
	creds := &proto.PasswordCredentials{}
	creds.SetUsername("alice")
	creds.SetPassword("password")
	req.SetPassword(creds)
	resp, err := p.Authenticate(context.Background(), req)
	if err != nil {
		t.Fatalf("authenticate: %v", err)
	}
	if resp.GetAccessToken() == "" || resp.GetRefreshToken() == "" {
		t.Fatalf("expected tokens")
	}
	vreq := &proto.ValidateTokenRequest{}
	vreq.SetAccessToken(resp.GetAccessToken())
	vresp, err := p.ValidateToken(context.Background(), vreq)
	if err != nil || !vresp.GetValid() {
		t.Fatalf("validate token failed")
	}
	rreq := &proto.RefreshTokenRequest{}
	rreq.SetRefreshToken(resp.GetRefreshToken())
	if _, err := p.RefreshToken(context.Background(), rreq); err != nil {
		t.Fatalf("refresh token: %v", err)
	}
	creds.SetPassword("bad")
	req.SetPassword(creds)
	if _, err := p.Authenticate(context.Background(), req); err == nil {
		t.Fatalf("expected error for bad password")
	}
}
