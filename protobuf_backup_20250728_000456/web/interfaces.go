// file: pkg/web/interfaces.go

package web

import (
	"context"
	"net/http"
	"time"
)

// Server defines the interface for HTTP servers
type Server interface {
	// Start starts the server
	Start(ctx context.Context) error

	// Stop gracefully stops the server
	Stop(ctx context.Context) error

	// Address returns the server address
	Address() string

	// Handler returns the root handler
	Handler() http.Handler

	// AddMiddleware adds middleware to the server
	AddMiddleware(middleware ...Middleware)

	// AddRoute adds a route to the server
	AddRoute(method, path string, handler HandlerFunc)

	// AddStaticRoute adds a static file route
	AddStaticRoute(path, dir string)
}

// HandlerFunc defines a handler function
type HandlerFunc func(ctx *Context) error

// Context represents an HTTP request/response context
type Context interface {
	// Request returns the HTTP request
	Request() *http.Request

	// Response returns the HTTP response writer
	Response() http.ResponseWriter

	// Param returns a URL parameter by name
	Param(name string) string

	// Query returns a query parameter by name
	Query(name string) string

	// Header returns a request header by name
	Header(name string) string

	// SetHeader sets a response header
	SetHeader(name, value string)

	// JSON writes JSON response
	JSON(status int, data interface{}) error

	// String writes string response
	String(status int, data string) error

	// Bind binds request data to a struct
	Bind(v interface{}) error

	// Context returns the request context
	Context() context.Context

	// WithContext returns a new context with the given context
	WithContext(ctx context.Context) Context
}

// Middleware defines middleware interface
type Middleware interface {
	// Handle processes the request
	Handle(next HandlerFunc) HandlerFunc
}

// MiddlewareFunc is a function type that implements Middleware
type MiddlewareFunc func(next HandlerFunc) HandlerFunc

// Handle implements the Middleware interface
func (m MiddlewareFunc) Handle(next HandlerFunc) HandlerFunc {
	return m(next)
}

// Config represents server configuration
type Config struct {
	// Address to bind to
	Address string

	// Read timeout
	ReadTimeout time.Duration

	// Write timeout
	WriteTimeout time.Duration

	// Idle timeout
	IdleTimeout time.Duration

	// Max header bytes
	MaxHeaderBytes int

	// TLS configuration
	TLS *TLSConfig

	// CORS configuration
	CORS *CORSConfig
}

// TLSConfig represents TLS configuration
type TLSConfig struct {
	// Certificate file path
	CertFile string

	// Key file path
	KeyFile string

	// Auto TLS (Let's Encrypt)
	AutoTLS bool

	// Hosts for auto TLS
	Hosts []string
}

// CORSConfig represents CORS configuration
type CORSConfig struct {
	// Allowed origins
	AllowedOrigins []string

	// Allowed methods
	AllowedMethods []string

	// Allowed headers
	AllowedHeaders []string

	// Exposed headers
	ExposedHeaders []string

	// Allow credentials
	AllowCredentials bool

	// Max age
	MaxAge time.Duration
}
