// file: pkg/web/server.go
// version: 1.1.0
// guid: 13f51b3e-b522-448a-a499-4b7852262b5c

package web

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"sync"

	"golang.org/x/net/http2"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// HTTPServer implements the Server interface.
type HTTPServer struct {
	config      *proto.ServerConfig
	mux         *http.ServeMux
	middlewares []Middleware
	server      *http.Server
	mu          sync.Mutex
}

// NewHTTPServer creates a new HTTPServer.
func NewHTTPServer(config *proto.ServerConfig) *HTTPServer {
	return &HTTPServer{
		config: config,
		mux:    http.NewServeMux(),
	}
}

// Start begins serving HTTP requests.
func (s *HTTPServer) Start(ctx context.Context) error {
	addr := fmt.Sprintf("%s:%d", s.config.GetHost(), s.config.GetPort())
	s.mu.Lock()
	s.server = &http.Server{Addr: addr, Handler: s.mux}
	if err := http2.ConfigureServer(s.server, &http2.Server{}); err != nil {
		s.mu.Unlock()
		return err
	}
	s.mu.Unlock()
	go func() {
		var err error
		if s.config.GetEnableTls() {
			err = s.server.ListenAndServeTLS(s.config.GetTlsCertPath(), s.config.GetTlsKeyPath())
		} else {
			err = s.server.ListenAndServe()
		}
		if err != nil && err != http.ErrServerClosed {
			log.Printf("web server error: %v", err)
		}
	}()
	return nil
}

// Stop gracefully shuts down the server.
func (s *HTTPServer) Stop(ctx context.Context) error {
	s.mu.Lock()
	defer s.mu.Unlock()
	if s.server == nil {
		return nil
	}
	return s.server.Shutdown(ctx)
}

// RegisterHandler registers a handler with the server.
func (s *HTTPServer) RegisterHandler(pattern string, handler http.Handler) {
	wrapped := handler
	for i := len(s.middlewares) - 1; i >= 0; i-- {
		wrapped = s.middlewares[i].Handle(wrapped)
	}
	s.mux.Handle(pattern, wrapped)
}

// RegisterMiddleware adds middleware to the server.
func (s *HTTPServer) RegisterMiddleware(m Middleware) {
	s.middlewares = append(s.middlewares, m)
}

// GetConfig returns the server configuration.
func (s *HTTPServer) GetConfig() *proto.ServerConfig {
	return s.config
}
