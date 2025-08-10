// file: pkg/auth/middleware/validation.go
// version: 1.0.0
// guid: d2c3b4a5-e6f7-8091-a2b3-c4d5e6f7a8b9

package middleware

import (
	"errors"
	"net/http"
)

// ValidateRequest ensures required headers are present.
func ValidateRequest(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Header.Get("Authorization") == "" {
			http.Error(w, errors.New("missing authorization").Error(), http.StatusBadRequest)
			return
		}
		next.ServeHTTP(w, r)
	})
}
