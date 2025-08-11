// file: pkg/web/middleware/compression.go
// version: 1.0.0
// guid: c1d2e3f4-a5b6-789c-d0e1-f234567890ab

package middleware

import (
	"compress/gzip"
	"net/http"
	"strings"

	"github.com/jdfalk/gcommon/pkg/web"
)

type gzipResponseWriter struct {
	http.ResponseWriter
	writer *gzip.Writer
}

func (g *gzipResponseWriter) Write(b []byte) (int, error) {
	return g.writer.Write(b)
}

func (g *gzipResponseWriter) Close() error {
	return g.writer.Close()
}

// Compression returns middleware that gzips responses when supported by client.
func Compression(level int) web.Middleware {
	return web.MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if !strings.Contains(r.Header.Get("Accept-Encoding"), "gzip") {
				next.ServeHTTP(w, r)
				return
			}
			gz, err := gzip.NewWriterLevel(w, level)
			if err != nil {
				http.Error(w, "compression error", http.StatusInternalServerError)
				return
			}
			w.Header().Set("Content-Encoding", "gzip")
			gzw := &gzipResponseWriter{ResponseWriter: w, writer: gz}
			defer gzw.Close()
			next.ServeHTTP(gzw, r)
		})
	})
}
