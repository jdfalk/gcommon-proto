// file: security/tools/validation_test.go
// version: 1.0.0
// guid: 0f5a585c-3b17-4f1f-80c9-d2121480d673

package tools

import "testing"

func TestValidateFunctions(t *testing.T) {
	if !ValidateInput("abc123") {
		t.Fatalf("valid input rejected")
	}
	if ValidateInput("bad!") {
		t.Fatalf("invalid input accepted")
	}
	if !ValidateEmail("a@b.com") {
		t.Fatalf("email invalid")
	}
	if ValidateEmail("bad@@example") {
		t.Fatalf("bad email accepted")
	}
	if !ValidateURL("https://example.com") {
		t.Fatalf("url invalid")
	}
	if ValidateURL("://bad") {
		t.Fatalf("bad url accepted")
	}
	if !ValidatePassword("Aa1!aaaa") {
		t.Fatalf("password invalid")
	}
}
