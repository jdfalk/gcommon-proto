// file: pkg/web/security.go
// version: 1.0.0
// guid: 40572546-830f-4b0c-93f3-42abdae67f58

package web

import (
	"crypto/rand"
	"database/sql"
	"encoding/base64"
	"net/http"

	"github.com/jdfalk/gcommon/security/tools"
)

// GenerateCSRFToken creates a random token for CSRF protection.
func GenerateCSRFToken() (string, error) {
	b := make([]byte, 32)
	if _, err := rand.Read(b); err != nil {
		return "", err
	}
	return base64.StdEncoding.EncodeToString(b), nil
}

// ValidateCSRFToken compares session token with form token.
func ValidateCSRFToken(sessionToken, formToken string) bool {
	return sessionToken != "" && formToken != "" && sessionToken == formToken
}

// SanitizeInput sanitizes user provided data.
func SanitizeInput(s string) string {
	return tools.Sanitize(s)
}

// ValidateInput ensures input matches allowed pattern.
func ValidateInput(s string) bool {
	return tools.ValidateInput(s)
}

// PrepareQuery creates a prepared statement to avoid SQL injection.
func PrepareQuery(db *sql.DB, query string) (*sql.Stmt, error) {
	cleaned := tools.StripSQLComments(query)
	return db.Prepare(cleaned)
}

// CSRFMiddleware verifies CSRF token on state-changing requests.
func CSRFMiddleware(getToken func(*http.Request) string) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if r.Method == http.MethodPost || r.Method == http.MethodPut || r.Method == http.MethodDelete {
				token := r.FormValue("csrf_token")
				if !ValidateCSRFToken(getToken(r), token) {
					http.Error(w, "invalid CSRF token", http.StatusForbidden)
					return
				}
			}
			next.ServeHTTP(w, r)
		})
	}
}
