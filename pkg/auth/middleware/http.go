// file: pkg/auth/middleware/http.go
// version: 1.0.0
// guid: a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d

package middleware

import (
	"net/http"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

// HTTPMiddleware validates bearer tokens on incoming HTTP requests.
func HTTPMiddleware(p auth.AuthProvider, next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token := r.Header.Get("Authorization")
		if token != "" {
			req := &proto.ValidateTokenRequest{}
			req.SetAccessToken(token)
			if _, err := p.ValidateToken(r.Context(), req); err != nil {
				w.WriteHeader(http.StatusUnauthorized)
				return
			}
		}
		next.ServeHTTP(w, r)
	})
}
