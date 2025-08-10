// file: pkg/web/security_test.go
// version: 1.0.0
// guid: 01d1d82a-063a-4d70-9fe6-201cb932d1d7

package web

import "testing"

func TestCSRFToken(t *testing.T) {
	tok, err := GenerateCSRFToken()
	if err != nil {
		t.Fatalf("generate: %v", err)
	}
	if !ValidateCSRFToken(tok, tok) {
		t.Fatalf("token should validate")
	}
}
