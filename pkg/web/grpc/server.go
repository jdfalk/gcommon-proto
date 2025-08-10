// file: pkg/web/grpc/server.go
// version: 1.0.0
// guid: b9921eb5-3ce3-451f-9f48-8ce274235a8e

package grpc

import (
	"net"

	"google.golang.org/grpc"
)

// Server wraps a gRPC server for the web module.
type Server struct {
	grpc *grpc.Server
}

// NewServer creates a new gRPC server with default options.
func NewServer(opts ...grpc.ServerOption) *Server {
	return &Server{grpc: grpc.NewServer(opts...)}
}

// Serve listens on the given address.
func (s *Server) Serve(l net.Listener) error {
	return s.grpc.Serve(l)
}

// GracefulStop gracefully stops the server.
func (s *Server) GracefulStop() {
	s.grpc.GracefulStop()
}
