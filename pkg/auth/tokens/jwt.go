// file: pkg/auth/tokens/jwt.go
// version: 1.1.0
// guid: ec5594fc-9a0e-4308-9120-1249387a0fc2

// Package tokens provides JWT utilities for the auth module.
package tokens

import (
	"errors"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

// Generate creates a signed JWT token using the provided signing method and
// custom claims. The subject and expiration are always set; additional claims
// may be provided via the claims map.
func Generate(secret []byte, alg jwt.SigningMethod, subject string, ttl time.Duration, claims map[string]any) (string, error) {
	if claims == nil {
		claims = make(map[string]any)
	}
	claims["sub"] = subject
	claims["exp"] = time.Now().Add(ttl).Unix()
	claims["iat"] = time.Now().Unix()
	token := jwt.NewWithClaims(alg, jwt.MapClaims(claims))
	return token.SignedString(secret)
}

// Parse validates a token and returns its claims as a map.
func Parse(secret []byte, tokenStr string) (jwt.MapClaims, error) {
	token, err := jwt.Parse(tokenStr, func(t *jwt.Token) (interface{}, error) {
		return secret, nil
	})
	if err != nil {
		return nil, err
	}
	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok || !token.Valid {
		return nil, errors.New("invalid token")
	}
	return claims, nil
}
