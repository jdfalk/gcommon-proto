# Web Server Module Technical Design

## Overview

The web server module provides a unified interface for building HTTP services
with support for middleware, routing, template rendering, and static file
serving. This design document outlines the architecture, interfaces, and
implementation details for the web server module.

## Goals

- Provide a consistent API for HTTP server development
- Support middleware chains for request processing
- Enable flexible routing with path parameters
- Support template rendering with Go templates
- Provide static file serving capabilities
- Integrate with metrics and logging modules
- Support graceful shutdown
- Enable websocket connections
- Handle CORS and common security headers
- Support both REST and GraphQL APIs
- Allow for API versioning

## Architecture

### Core Components

```text
              +-----------------+
              |     Server      |
              +--------+--------+
                       |
    +------------------+-------------------+
    |                  |                   |
+---+----+      +------+------+      +-----+-----+
| Router |      | Middleware  |      | Handlers  |
+--------+      +-------------+      +-----------+
    |                  |                   |
    |                  |                   |
+---+----+      +------+------+      +-----+-----+
| Routes |      | Templates   |      |  Static   |
+--------+      +-------------+      +-----------+
```

### Component Design

#### Server Interface

The core of the module is the `Server` interface, which defines the common
operations for HTTP server management.

#### Router Interface

The Router interface provides routing functionality with support for different
HTTP methods and path parameters.

#### Middleware Interface

The middleware chain processes requests and responses, supporting both standard
Go HTTP handlers and custom middleware.

#### Handler Interface

Handlers process individual HTTP requests and generate responses.

## Interface Design

### Server

```go
// Server represents a web server.
type Server interface {
    // Start starts the server.
    Start(ctx context.Context) error

    // Stop stops the server.
    Stop(ctx context.Context) error

    // Router returns the router.
    Router() Router

    // Use adds middleware to the server.
    Use(middleware ...Middleware)

    // ListenAddr returns the address the server is listening on.
    ListenAddr() string

    // WithTLS configures the server to use TLS.
    WithTLS(certFile, keyFile string) Server

    // WithLogger sets the logger for the server.
    WithLogger(logger log.Logger) Server

    // WithMetrics sets the metrics provider for the server.
    WithMetrics(metrics metrics.Provider) Server
}
```

### Router

```go
// Router represents a router.
type Router interface {
    // GET registers a handler for GET requests.
    GET(path string, handler HandlerFunc)

    // POST registers a handler for POST requests.
    POST(path string, handler HandlerFunc)

    // PUT registers a handler for PUT requests.
    PUT(path string, handler HandlerFunc)

    // DELETE registers a handler for DELETE requests.
    DELETE(path string, handler HandlerFunc)

    // PATCH registers a handler for PATCH requests.
    PATCH(path string, handler HandlerFunc)

    // HEAD registers a handler for HEAD requests.
    HEAD(path string, handler HandlerFunc)

    // OPTIONS registers a handler for OPTIONS requests.
    OPTIONS(path string, handler HandlerFunc)

    // Group creates a new router group.
    Group(prefix string) Router

    // Use adds middleware to the router.
    Use(middleware ...Middleware)

    // Static serves static files.
    Static(path, dir string)

    // StaticFS serves static files from an embedded filesystem.
    StaticFS(path string, fs fs.FS)

    // Template renders a template.
    Template(path string, template string, data interface{})

    // Handler returns an http.Handler.
    Handler() http.Handler
}
```

### Context

```go
// Context represents the context of an HTTP request.
type Context interface {
    // Request returns the HTTP request.
    Request() *http.Request

    // Response returns the HTTP response writer.
    Response() http.ResponseWriter

    // Context returns the request context.
    Context() context.Context

    // WithContext sets the request context.
    WithContext(ctx context.Context) Context

    // Param returns the value of the URL parameter.
    Param(name string) string

    // Query returns the value of the URL query parameter.
    Query(name string) string

    // Form returns the value of the form parameter.
    Form(name string) string

    // JSON binds the request body to the given value as JSON.
    JSON(v interface{}) error

    // XML binds the request body to the given value as XML.
    XML(v interface{}) error

    // FormValue binds form values to the given struct.
    FormValue(v interface{}) error

    // Render renders a template with the given data.
    Render(name string, data interface{}) error

    // JSON sends a JSON response.
    JSON(code int, v interface{}) error

    // XML sends an XML response.
    XML(code int, v interface{}) error

    // Text sends a text response.
    Text(code int, format string, v ...interface{}) error

    // HTML sends an HTML response.
    HTML(code int, html string) error

    // File sends a file response.
    File(filepath string) error

    // Redirect sends a redirect response.
    Redirect(code int, url string) error

    // NoContent sends a no-content response.
    NoContent() error

    // Error sends an error response.
    Error(err error) error

    // Logger returns the logger.
    Logger() log.Logger

    // SetLogger sets the logger.
    SetLogger(logger log.Logger) Context

    // Metrics returns the metrics provider.
    Metrics() metrics.Provider

    // SetMetrics sets the metrics provider.
    SetMetrics(metrics metrics.Provider) Context
}
```

### HandlerFunc

```go
// HandlerFunc is the function that handles HTTP requests.
type HandlerFunc func(ctx Context) error
```

### Middleware

```go
// Middleware is a function that wraps a handler.
type Middleware func(HandlerFunc) HandlerFunc
```

## Configuration

### Config Structure

```go
// Config represents the server configuration.
type Config struct {
    // Addr is the address to listen on.
    Addr string

    // ReadTimeout is the maximum duration for reading the entire request.
    ReadTimeout time.Duration

    // WriteTimeout is the maximum duration before timing out writes of the response.
    WriteTimeout time.Duration

    // IdleTimeout is the maximum amount of time to wait for the next request.
    IdleTimeout time.Duration

    // ShutdownTimeout is the maximum duration to wait for the server to shutdown.
    ShutdownTimeout time.Duration

    // TLSCertFile is the path to the TLS certificate file.
    TLSCertFile string

    // TLSKeyFile is the path to the TLS key file.
    TLSKeyFile string

    // EnableTLS indicates whether TLS should be enabled.
    EnableTLS bool

    // EnableHTTP2 indicates whether HTTP/2 should be enabled.
    EnableHTTP2 bool

    // EnableH2C indicates whether H2C (HTTP/2 over TCP) should be enabled.
    EnableH2C bool

    // EnableCompression indicates whether compression should be enabled.
    EnableCompression bool

    // MaxHeaderBytes controls the maximum number of bytes the server will read parsing the request header.
    MaxHeaderBytes int

    // TemplateDir is the directory containing templates.
    TemplateDir string

    // StaticDir is the directory containing static files.
    StaticDir string

    // StaticPrefix is the URL prefix for static files.
    StaticPrefix string

    // TemplateExt is the extension for template files.
    TemplateExt string

    // TemplateFuncMap is the function map for templates.
    TemplateFuncMap template.FuncMap
}
```

## Implementation Details

### Standard HTTP Implementation

The standard HTTP implementation uses the `net/http` package for server
functionality, providing a lightweight server solution.

### Template Rendering

The template rendering component uses the `html/template` package to render
templates with proper HTML escaping.

### Static File Serving

Static file serving uses the `http.FileServer` functionality with caching and
compression middleware.

### Middleware Implementations

#### Common Middleware

- **Logger**: Logs request/response information
- **Recovery**: Recovers from panics
- **CORS**: Handles Cross-Origin Resource Sharing
- **Compression**: Compresses responses with gzip/deflate
- **Cache**: Controls caching with appropriate headers
- **Timeout**: Enforces request timeouts
- **RateLimit**: Limits request rates by various criteria
- **JWT**: Handles JWT authentication
- **CSRF**: Protects against CSRF attacks

#### Integration Middleware

- **Metrics**: Collects metrics about requests
- **Tracing**: Adds distributed tracing

### Context Implementation

The context implementation wraps the standard request and response objects with
additional functionality for easier handling of common web tasks.

### Routing Implementation

The routing implementation uses a tree-based router for efficient path matching,
supporting path parameters and wildcards.

## Usage Examples

### Basic Server Setup

```go
config := web.Config{
    Addr:           ":8080",
    ReadTimeout:    10 * time.Second,
    WriteTimeout:   10 * time.Second,
    IdleTimeout:    30 * time.Second,
    ShutdownTimeout: 30 * time.Second,
}

server, err := web.NewServer(config)
if err != nil {
    log.Fatal(err)
}

// Add middleware
server.Use(
    web.Recovery(),
    web.Logger(logger),
    web.CORS(),
)

// Start server
ctx := context.Background()
if err := server.Start(ctx); err != nil {
    log.Fatal(err)
}
```

### Routing

```go
router := server.Router()

// Basic routes
router.GET("/", func(ctx web.Context) error {
    return ctx.Text(http.StatusOK, "Hello, World!")
})

// Path parameters
router.GET("/users/:id", func(ctx web.Context) error {
    id := ctx.Param("id")
    return ctx.JSON(http.StatusOK, map[string]string{"id": id})
})

// Grouping
api := router.Group("/api")
{
    v1 := api.Group("/v1")
    {
        v1.GET("/users", listUsers)
        v1.POST("/users", createUser)
        v1.GET("/users/:id", getUser)
    }
}

// Static files
router.Static("/static", "./static")

// Templates
router.GET("/template", func(ctx web.Context) error {
    return ctx.Render("index.tmpl", map[string]interface{}{
        "title":   "Welcome",
        "message": "Hello, World!",
    })
})
```

### Middleware

```go
// Create a custom middleware
func AuthMiddleware(next web.HandlerFunc) web.HandlerFunc {
    return func(ctx web.Context) error {
        token := ctx.Request().Header.Get("Authorization")
        if token == "" {
            return ctx.Error(errors.New("unauthorized"))
        }

        // Validate token...

        return next(ctx)
    }
}

// Apply middleware to a group
api := router.Group("/api")
api.Use(AuthMiddleware)
```

### Request Handling

```go
func createUser(ctx web.Context) error {
    var user User

    if err := ctx.JSON(&user); err != nil {
        return ctx.Error(err)
    }

    // Validate user...

    // Save user...

    return ctx.JSON(http.StatusCreated, user)
}
```

### Template Rendering Example

```go
func renderTemplate(ctx web.Context) error {
    data := map[string]interface{}{
        "user": map[string]string{
            "name": "John Doe",
            "email": "john@example.com",
        },
        "items": []string{"Item 1", "Item 2", "Item 3"},
    }

    return ctx.Render("profile.tmpl", data)
}
```

## Testing Strategy

- Unit tests for each component
- Integration tests for request/response flow
- Mock implementations for testing handlers
- Testing utilities for common test scenarios

## Security Considerations

- HTTPS configuration and best practices
- Security headers (CSP, HSTS, X-Frame-Options, etc.)
- CORS configuration
- CSRF protection
- Authentication and authorization
- Input validation and sanitization
- Rate limiting and DoS protection

## Performance Considerations

- Connection pooling
- Response compression
- Efficient routing
- Middleware optimizations
- Template caching
- Static file optimization
- Keep-alive connections
- HTTP/2 support
