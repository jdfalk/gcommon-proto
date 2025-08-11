// file: templates/basic-api-service/internal/server/server.go
// version: 1.0.0
// guid: 15c27177-23ed-42e3-940a-ed14479d2e7a

// Package server provides HTTP server implementation for the basic API service
// template. The server exposes a simple health check endpoint and is intended to
// be extended with real application logic.
package server

import (
	"net/http"

	glog "github.com/jdfalk/gcommon/pkg/log"
	"github.com/jdfalk/gcommon/templates/basic-api-service/internal/config"
)

// Server wraps the dependencies required to run the HTTP server.
type Server struct {
	cfg    *config.AppConfig
	logger glog.Provider
	mux    *http.ServeMux
}

// New creates a new Server instance and configures routes.
func New(cfg *config.AppConfig, logger glog.Provider) *Server {
	s := &Server{
		cfg:    cfg,
		logger: logger,
		mux:    http.NewServeMux(),
	}
	s.routes()
	return s
}

// Handler returns the HTTP handler for serving requests.
func (s *Server) Handler() http.Handler { return s.mux }

// routes configures HTTP routes for the service.
func (s *Server) routes() {
	s.mux.HandleFunc("/healthz", s.handleHealth)
}

// handleHealth provides a basic health check endpoint.
func (s *Server) handleHealth(w http.ResponseWriter, r *http.Request) {
	s.logger.Info("health check")
	_, _ = w.Write([]byte("ok"))
}
