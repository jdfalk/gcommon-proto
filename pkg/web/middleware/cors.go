// file: pkg/web/middleware/cors.go
// version: 1.0.0
// guid: 59da3c2d-2ea8-4a10-bb47-bb9f0e2c2ea2

package middleware

import (
	"net/http"

	"github.com/jdfalk/gcommon/pkg/web"
)

// CORSMiddleware adds basic CORS headers to responses.
func CORSMiddleware() web.Middleware {
	return web.MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			w.Header().Set("Access-Control-Allow-Origin", "*")
			w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
			if r.Method == http.MethodOptions {
				w.WriteHeader(http.StatusNoContent)
				return
			}
			next.ServeHTTP(w, r)
		})
	})
}
