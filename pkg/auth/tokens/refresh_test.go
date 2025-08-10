// file: pkg/auth/tokens/refresh_test.go
// version: 1.1.0
// guid: 873f3a48-9cd5-4de0-9b6e-9e6a679a5b9f

package tokens

import (
	"testing"

	"github.com/golang-jwt/jwt/v5"
)

func TestGenerateRefresh(t *testing.T) {
	secret := []byte("s")
	tok, err := GenerateRefresh(secret, jwt.SigningMethodHS256, "carol", 60, nil)
	if err != nil {
		t.Fatalf("generate refresh: %v", err)
	}
	if tok == "" {
		t.Fatalf("expected token")
	}
	if _, err := RotateRefresh(secret, jwt.SigningMethodHS256, tok, 60); err != nil {
		t.Fatalf("rotate refresh: %v", err)
	}
}
