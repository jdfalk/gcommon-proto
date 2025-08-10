// file: pkg/web/routing/router.go
// version: 1.0.0
// guid: 65c16a06-6734-4b37-8fdd-88aa3ad04e02

package routing

import "net/http"

// Router provides simple pattern-based routing.
type Router struct {
	routes map[string]http.Handler
}

// NewRouter creates an empty Router.
func NewRouter() *Router {
	return &Router{routes: make(map[string]http.Handler)}
}

// Register registers a handler for a pattern.
func (r *Router) Register(pattern string, h http.Handler) {
	r.routes[pattern] = h
}

// Handler returns the handler for the given path or nil.
func (r *Router) Handler(path string) http.Handler {
	return r.routes[path]
}
