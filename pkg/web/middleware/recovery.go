// file: pkg/web/middleware/recovery.go
// version: 1.0.0
// guid: 0f5d0e3a-3cfe-4a27-9ce9-293e2d498dc9

package middleware

import (
	"log"
	"net/http"

	"github.com/jdfalk/gcommon/pkg/web"
)

// RecoveryMiddleware recovers from panics in handlers.
func RecoveryMiddleware() web.Middleware {
	return web.MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			defer func() {
				if rec := recover(); rec != nil {
					log.Printf("panic: %v", rec)
					http.Error(w, "internal server error", http.StatusInternalServerError)
				}
			}()
			next.ServeHTTP(w, r)
		})
	})
}
