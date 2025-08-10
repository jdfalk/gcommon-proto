// file: pkg/web/middleware/logging.go
// version: 1.0.0
// guid: 25c3bbb7-b0b7-4fec-a7f3-8ae731807a2a

package middleware

import (
	"log"
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/web"
)

// Logging returns middleware that logs requests.
func Logging() web.Middleware {
	return web.MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			start := time.Now()
			next.ServeHTTP(w, r)
			log.Printf("%s %s %s", r.Method, r.URL.Path, time.Since(start))
		})
	})
}
