// file: pkg/auth/policies/policy_engine_test.go
// version: 1.0.0
// guid: 746a9d4e-65fb-4c5e-99af-c7e3c051c9e2

package policies

import (
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

func TestPolicyEngine(t *testing.T) {
	rbac := NewRBACEngine([]byte("s"))
	rbac.Grant("admin", "res", "read")
	eng := NewPolicyEngine(rbac, nil)
	// create token for admin role
	tok, _ := tokens.Generate([]byte("s"), jwt.SigningMethodHS256, "alice", time.Minute, map[string]any{"role": "admin"})
	req := &proto.AuthorizeRequest{}
	req.SetToken(tok)
	req.SetResource("res")
	req.SetAction("read")
	resp, err := eng.Authorize(nil, req)
	if err != nil {
		t.Fatalf("authorize: %v", err)
	}
	if !resp.GetAuthorized() {
		t.Fatalf("expected authorized")
	}
}
