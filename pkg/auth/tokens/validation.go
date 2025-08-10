// file: pkg/auth/tokens/validation.go
// version: 1.0.0
// guid: a290df12-6c3e-4f6c-9bc6-4c55a9f1e1d0

// Package tokens provides JWT utilities for the auth module.
package tokens

import (
	"errors"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

// Validate parses the token string and ensures it has not expired.
func Validate(tokenStr string, secret []byte) (jwt.MapClaims, error) {
	token, err := jwt.Parse(tokenStr, func(t *jwt.Token) (interface{}, error) { return secret, nil })
	if err != nil {
		return nil, err
	}
	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok || !token.Valid {
		return nil, errors.New("invalid token")
	}
	exp, err := claims.GetExpirationTime()
	if err != nil {
		return nil, err
	}
	if !exp.After(time.Now()) {
		return nil, errors.New("token expired")
	}
	return claims, nil
}
