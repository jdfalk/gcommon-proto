// file: pkg/auth/tokens/jwt_test.go
// version: 1.1.0
// guid: bdfdb20d-be1f-4e14-a78e-8ec360f985d1

package tokens

import (
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

func TestGenerateAndParse(t *testing.T) {
	secret := []byte("secret")
	token, err := Generate(secret, jwt.SigningMethodHS256, "alice", time.Minute, map[string]any{"role": "admin"})
	if err != nil {
		t.Fatalf("generate token: %v", err)
	}
	claims, err := Parse(secret, token)
	if err != nil {
		t.Fatalf("parse token: %v", err)
	}
	if claims["sub"] != "alice" {
		t.Errorf("subject = %v want alice", claims["sub"])
	}
	if claims["role"] != "admin" {
		t.Errorf("role = %v want admin", claims["role"])
	}
}
