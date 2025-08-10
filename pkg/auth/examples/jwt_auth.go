// file: pkg/auth/examples/jwt_auth.go
// version: 1.0.0
// guid: e9f0a1b2-c3d4-5e6f-7081-92a3b4c5d6e7

package examples

import (
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

// RunJWTAuth demonstrates generating and validating a JWT.
func RunJWTAuth() error {
	secret := []byte("secret")
	token, err := tokens.Generate(secret, jwt.SigningMethodHS256, "demo", time.Minute, nil)
	if err != nil {
		return err
	}
	claims, err := tokens.Parse(secret, token)
	if err != nil {
		return err
	}
	fmt.Println("claims:", claims)
	return nil
}
