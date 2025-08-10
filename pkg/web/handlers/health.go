// file: pkg/web/handlers/health.go
// version: 1.0.0
// guid: 5aa5bcf9-1f54-4d18-a9f0-154bddc65aca

package handlers

import "net/http"

// HealthHandler returns an HTTP handler that reports service health.
func HealthHandler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("ok"))
	})
}
