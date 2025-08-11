// file: templates/auth-service/internal/server/server.go
// version: 1.0.0
// guid: 16d821b0-fdf1-457a-b866-80b94570602e

package server

import (
	"net/http"

	glog "github.com/jdfalk/gcommon/pkg/log"
	"github.com/jdfalk/gcommon/templates/auth-service/internal/config"
)

type Server struct {
	cfg    *config.AppConfig
	logger glog.Provider
	mux    *http.ServeMux
}

func New(cfg *config.AppConfig, l glog.Provider) *Server {
	s := &Server{cfg: cfg, logger: l, mux: http.NewServeMux()}
	s.mux.HandleFunc("/login", s.handleLogin)
	return s
}

func (s *Server) Handler() http.Handler { return s.mux }

func (s *Server) handleLogin(w http.ResponseWriter, r *http.Request) {
	s.logger.Info("login called")
	w.WriteHeader(http.StatusOK)
}
