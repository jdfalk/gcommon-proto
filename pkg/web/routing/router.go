// file: pkg/web/routing/router.go
// version: 1.1.0
// guid: 65c16a06-6734-4b37-8fdd-88aa3ad04e02

package routing

import (
	"context"
	"net/http"
)

type route struct {
	method  string
	pattern string
	handler http.Handler
}

// Router dispatches requests based on method and pattern.
type Router struct {
	routes []route
}

// NewRouter creates an empty Router.
func NewRouter() *Router {
	return &Router{}
}

// Register adds a route for the given method and pattern.
// If method is empty, the route matches any method.
func (r *Router) Register(method, pattern string, h http.Handler) {
	r.routes = append(r.routes, route{method: method, pattern: pattern, handler: h})
}

// ServeHTTP implements http.Handler and dispatches requests to matching routes.
func (r *Router) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	for _, rt := range r.routes {
		if rt.method != "" && rt.method != req.Method {
			continue
		}
		if ok, params := Match(rt.pattern, req.URL.Path); ok {
			ctx := context.WithValue(req.Context(), paramsKey{}, params)
			rt.handler.ServeHTTP(w, req.WithContext(ctx))
			return
		}
	}
	http.NotFound(w, req)
}

type paramsKey struct{}

// Params returns URL parameters for the request.
func Params(r *http.Request) map[string]string {
	if v, ok := r.Context().Value(paramsKey{}).(map[string]string); ok {
		return v
	}
	return map[string]string{}
}
