// file: pkg/auth/examples/rbac_demo.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-1a2b-3c4d5e6f7a8b

package examples

import (
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/jdfalk/gcommon/pkg/auth/policies"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

// RunRBACDemo demonstrates RBAC authorization.
func RunRBACDemo() error {
	secret := []byte("s")
	eng := policies.NewRBACEngine(secret)
	eng.Grant("admin", "res", "read")
	tok, _ := tokens.Generate(secret, jwt.SigningMethodHS256, "alice", time.Minute, map[string]any{"role": "admin"})
	req := &proto.AuthorizeRequest{}
	req.SetToken(tok)
	req.SetResource("res")
	req.SetAction("read")
	resp, err := eng.Authorize(nil, req)
	if err != nil {
		return err
	}
	fmt.Println("authorized:", resp.GetAuthorized())
	return nil
}
