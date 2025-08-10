// file: pkg/web/routing/matcher.go
// version: 1.0.0
// guid: 2a88f26d-3f1e-4c8e-91ef-8efba3b9c5cb

package routing

// Match reports whether the path matches the pattern.
func Match(pattern, path string) bool {
	return pattern == path
}
