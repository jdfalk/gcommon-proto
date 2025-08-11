// file: pkg/web/routing/matcher.go
// version: 1.1.0
// guid: 2a88f26d-3f1e-4c8e-91ef-8efba3b9c5cb

package routing

import "strings"

// Match reports whether the path matches the pattern and returns extracted parameters.
// Patterns may include segments prefixed with ':' to capture values.
// For example, pattern "/users/:id" matches path "/users/42" and returns map{"id": "42"}.
func Match(pattern, path string) (bool, map[string]string) {
	p := strings.Split(strings.Trim(pattern, "/"), "/")
	s := strings.Split(strings.Trim(path, "/"), "/")
	if len(p) != len(s) {
		return false, nil
	}
	params := make(map[string]string)
	for i := range p {
		if strings.HasPrefix(p[i], ":") {
			params[p[i][1:]] = s[i]
			continue
		}
		if p[i] != s[i] {
			return false, nil
		}
	}
	return true, params
}
