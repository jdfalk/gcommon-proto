// file: security/tools/sanitization.go
// version: 1.1.0
// guid: 41c45b9a-c489-4e69-b843-0caf3546a4e8

package tools

import (
	"html"
	"path/filepath"
	"strings"
)

// Sanitize removes potentially dangerous characters from input.
func Sanitize(input string) string {
	replacer := strings.NewReplacer("\n", " ", "\r", " ", "\t", " ")
	cleaned := replacer.Replace(input)
	return html.EscapeString(cleaned)
}

// SanitizePath cleans a file path and prevents directory traversal.
func SanitizePath(p string) string {
	cleaned := filepath.Clean(p)
	cleaned = strings.ReplaceAll(cleaned, "..", "")
	return cleaned
}

// StripSQLComments removes SQL comments to reduce injection risk.
func StripSQLComments(query string) string {
	for {
		if idx := strings.Index(query, "--"); idx >= 0 {
			if nl := strings.Index(query[idx:], "\n"); nl >= 0 {
				query = query[:idx] + query[idx+nl:]
			} else {
				query = query[:idx]
			}
			continue
		}
		break
	}
	return query
}
