// file: pkg/auth/providers/jwt_test.go
// version: 1.0.0
// guid: 8c7d6e5f-4a3b-2c1d-0e9f-8a7b6c5d4e3f

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

func TestJWTProviderValidate(t *testing.T) {
	secret := []byte("s")
	prov := NewJWTProvider(secret)
	tok, err := tokens.Generate(secret, jwt.SigningMethodHS256, "dave", time.Minute, nil)
	if err != nil {
		t.Fatalf("generate: %v", err)
	}
	req := &proto.ValidateTokenRequest{}
	req.SetAccessToken(tok)
	resp, err := prov.ValidateToken(context.Background(), req)
	if err != nil || !resp.GetValid() {
		t.Fatalf("validate failed")
	}
}
