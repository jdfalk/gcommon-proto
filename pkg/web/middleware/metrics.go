// file: pkg/web/middleware/metrics.go
// version: 1.0.0
// guid: a0f7f4d1-2d72-4f16-9cde-9e6466d1ff01

package middleware

import (
	"log"
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/web"
)

// MetricsMiddleware logs request durations.
func MetricsMiddleware() web.Middleware {
	return web.MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			start := time.Now()
			next.ServeHTTP(w, r)
			log.Printf("%s %s took %v", r.Method, r.URL.Path, time.Since(start))
		})
	})
}
