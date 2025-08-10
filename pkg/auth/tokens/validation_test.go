// file: pkg/auth/tokens/validation_test.go
// version: 1.0.0
// guid: a14c7f23-7a21-4e6c-bd3a-0bfa0b8574a9

package tokens

import (
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

func TestValidate(t *testing.T) {
	secret := []byte("secret")
	token, err := Generate(secret, jwt.SigningMethodHS256, "bob", time.Minute, nil)
	if err != nil {
		t.Fatalf("generate: %v", err)
	}
	if _, err := Validate(token, secret); err != nil {
		t.Fatalf("validate: %v", err)
	}
}
