// file: pkg/auth/tokens/refresh.go
// version: 1.0.0
// guid: 5b4e1f9a-7350-4c34-9f5e-0e1d2f3c4b5a

// Package tokens provides JWT utilities for the auth module.
package tokens

import (
	"time"

	"github.com/golang-jwt/jwt/v5"
)

// GenerateRefresh creates a signed refresh token with the given subject and TTL.
func GenerateRefresh(secret []byte, alg jwt.SigningMethod, subject string, ttlSeconds int64, claims map[string]any) (string, error) {
	if claims == nil {
		claims = make(map[string]any)
	}
	claims["type"] = "refresh"
	return Generate(secret, alg, subject, time.Duration(ttlSeconds)*time.Second, claims)
}

// RotateRefresh parses the existing refresh token and issues a new one.
func RotateRefresh(secret []byte, alg jwt.SigningMethod, refresh string, ttlSeconds int64) (string, error) {
	claims, err := Parse(secret, refresh)
	if err != nil {
		return "", err
	}
	sub, _ := claims["sub"].(string)
	role, _ := claims["role"].(string)
	return GenerateRefresh(secret, alg, sub, ttlSeconds, map[string]any{"role": role})
}
