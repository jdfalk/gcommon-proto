// file: pkg/auth/policies/rbac_test.go
// version: 1.0.0
// guid: 0e92f21c-c656-41a0-8d1e-b9a662580bf5

package policies

import (
	"context"
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

func TestRBACAuthorize(t *testing.T) {
	secret := []byte("secret")
	engine := NewRBACEngine(secret)
	engine.Grant("admin", "res", "read")
	token, err := tokens.Generate(secret, jwt.SigningMethodHS256, "alice", time.Minute, map[string]any{"role": "admin"})
	if err != nil {
		t.Fatalf("generate token: %v", err)
	}
	req := &proto.AuthorizeRequest{}
	req.SetToken(token)
	req.SetResource("res")
	req.SetAction("read")
	resp, err := engine.Authorize(context.Background(), req)
	if err != nil {
		t.Fatalf("authorize: %v", err)
	}
	if !resp.GetAuthorized() {
		t.Fatalf("expected authorized")
	}
	req.SetAction("write")
	resp, err = engine.Authorize(context.Background(), req)
	if err != nil {
		t.Fatalf("authorize: %v", err)
	}
	if resp.GetAuthorized() {
		t.Fatalf("expected unauthorized")
	}
}
