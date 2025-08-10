// file: pkg/auth/grpc/server.go
// version: 1.0.0
// guid: 7b8c9d0e-1f2a-3b4c-5d6e-7f8a9b0c1d2e

package grpc

import (
	"net"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"google.golang.org/grpc"
)

// Server wraps a gRPC server for auth services.
type Server struct {
	*grpc.Server
}

// NewServer creates and registers auth services on a new gRPC server.
func NewServer(authProv auth.AuthProvider, authzProv auth.AuthorizationProvider) *Server {
	srv := grpc.NewServer()
	proto.RegisterAuthServiceServer(srv, NewAuthService(authProv))
	proto.RegisterAuthorizationServiceServer(srv, NewAuthzService(authzProv))
	proto.RegisterAuthAdminServiceServer(srv, NewAdminService(authzProv))
	return &Server{Server: srv}
}

// ListenAndServe starts the server on the given address.
func (s *Server) ListenAndServe(addr string) error {
	lis, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}
	return s.Serve(lis)
}
