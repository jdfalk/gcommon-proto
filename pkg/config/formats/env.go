// file: pkg/config/formats/env.go
// version: 1.0.0
// guid: 22222222-3333-4444-5555-bbbbbbbbbbbb

package formats

import "strings"

// EnvDecoder parses .env style key-value pairs.
type EnvDecoder struct{}

// Decode converts ENV bytes into a map.
func (EnvDecoder) Decode(b []byte) (map[string]interface{}, error) {
	result := make(map[string]interface{})
	lines := strings.Split(string(b), "\n")
	for _, line := range lines {
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		parts := strings.SplitN(line, "=", 2)
		if len(parts) != 2 {
			continue
		}
		result[strings.TrimSpace(parts[0])] = strings.TrimSpace(parts[1])
	}
	return result, nil
}

// TODO:
//  - Support quoted values with escape sequences
//  - Handle multiline values using continuation characters
//  - Validate variable names against allowed patterns
//  - Provide option to ignore duplicate keys
//  - Add examples for parsing dotenv files
//  - Implement variable expansion referencing other keys
//  - Support comments at end of lines
//  - Expose metrics for parsing performance
//  - Offer streaming parser for very large env files
//  - Document portability across different shells
