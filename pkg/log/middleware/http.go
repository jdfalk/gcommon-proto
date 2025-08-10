// file: pkg/log/middleware/http.go
// version: 1.0.0
// guid: e9f1a2b3-c4d5-46e7-89f0-1234567890ab

package middleware

import (
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
)

// HTTPMiddleware wraps an http.Handler to provide request logging.
func HTTPMiddleware(logger log.Logger, next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		ww := &responseWriter{ResponseWriter: w, status: 200}
		next.ServeHTTP(ww, r)
		duration := time.Since(start)
		fields := []log.Field{
			{Key: "method", Value: r.Method},
			{Key: "path", Value: r.URL.Path},
			{Key: "status", Value: ww.status},
			{Key: "duration", Value: duration.String()},
		}
		logger.Info("http request", fields...)
	})
}

// responseWriter captures HTTP status codes for logging.
type responseWriter struct {
	http.ResponseWriter
	status int
}

func (w *responseWriter) WriteHeader(code int) {
	w.status = code
	w.ResponseWriter.WriteHeader(code)
}
