// file: pkg/web/middleware/auth.go
// version: 1.0.0
// guid: 87b40fd0-ef1f-4d8d-b645-13dfb68c5fa0

package middleware

import (
	"net/http"

	"github.com/jdfalk/gcommon/pkg/web"
)

// AuthMiddleware validates bearer tokens in the Authorization header.
type AuthMiddleware struct {
	token string
}

// NewAuthMiddleware creates an AuthMiddleware.
func NewAuthMiddleware(token string) *AuthMiddleware {
	return &AuthMiddleware{token: token}
}

// Handle checks the Authorization header and validates the token.
func (a *AuthMiddleware) Handle(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		auth := r.Header.Get("Authorization")
		if auth != "Bearer "+a.token {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}
		next.ServeHTTP(w, r)
	})
}

var _ web.Middleware = (*AuthMiddleware)(nil)
