// file: pkg/web/handlers/metrics.go
// version: 1.0.0
// guid: 1d7e4c63-bd2d-4bb1-9f65-6cba9b53ae7b

package handlers

import "net/http"

// MetricsHandler returns an HTTP handler that serves metrics data.
func MetricsHandler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("metrics not implemented"))
	})
}
