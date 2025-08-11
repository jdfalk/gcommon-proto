// file: examples/modules/auth/jwt-auth/main.go
// version: 1.0.0
// guid: 11da1a3e-252b-4391-82a1-6374bf55089e

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/jdfalk/gcommon/pkg/auth/tokens"
)

// setup returns a shared secret used for signing tokens.
func setup(ctx context.Context) ([]byte, error) {
	return []byte("secret"), nil
}

// run generates and validates a JWT using the provided secret.
func run(ctx context.Context, secret []byte) error {
	tok, err := tokens.Generate(secret, jwt.SigningMethodHS256, "demo-user", time.Minute, map[string]any{"role": "user"})
	if err != nil {
		return err
	}
	claims, err := tokens.Parse(secret, tok)
	if err != nil {
		return err
	}
	fmt.Println("token:", tok)
	fmt.Println("claims:", claims)
	return nil
}

func main() {
	ctx := context.Background()
	secret, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, secret); err != nil {
		panic(err)
	}
}
