// file: pkg/web/handlers/admin.go
// version: 1.0.0
// guid: 5b7fb5a6-d776-4c77-a82a-1192ce140f64

package handlers

import "net/http"

// AdminHandler returns an HTTP handler for administrative endpoints.
func AdminHandler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("admin ok"))
	})
}
