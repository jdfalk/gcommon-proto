// file: security/tools/validation.go
// version: 1.1.0
// guid: 1d56886b-8db1-42cc-8df3-bb31773e59ca

package tools

import (
	"net/url"
	"regexp"
	"unicode"
)

var inputPattern = regexp.MustCompile(`^[a-zA-Z0-9_]+$`)
var emailPattern = regexp.MustCompile(`^[^@\s]+@[^@\s]+\.[^@\s]+$`)

// ValidateInput checks if input matches the allowed pattern.
func ValidateInput(input string) bool {
	return inputPattern.MatchString(input)
}

// ValidateEmail checks if the value is a valid email address.
func ValidateEmail(email string) bool {
	return emailPattern.MatchString(email)
}

// ValidateURL ensures the string is a valid absolute URL.
func ValidateURL(raw string) bool {
	u, err := url.Parse(raw)
	return err == nil && u.Scheme != "" && u.Host != ""
}

// ValidatePassword ensures password meets complexity requirements.
func ValidatePassword(pw string) bool {
	var hasUpper, hasLower, hasNumber, hasSpecial bool
	for _, c := range pw {
		switch {
		case unicode.IsUpper(c):
			hasUpper = true
		case unicode.IsLower(c):
			hasLower = true
		case unicode.IsNumber(c):
			hasNumber = true
		case unicode.IsPunct(c) || unicode.IsSymbol(c):
			hasSpecial = true
		}
	}
	return len(pw) >= 8 && hasUpper && hasLower && hasNumber && hasSpecial
}
