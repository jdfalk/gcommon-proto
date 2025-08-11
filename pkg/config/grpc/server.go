// file: pkg/config/grpc/server.go
// version: 1.0.0
// guid: 99999999-9999-9999-9999-999999999999

package grpc

import (
	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"google.golang.org/grpc"
)

// NewServer creates a gRPC server with config services registered
// TODO: Add options for middleware and interceptors
// TODO: Support TLS and authentication
// TODO: Integrate with metrics and tracing
// TODO: Allow registering additional services
// TODO: Provide health checks
// TODO: Support reflection and debugging
// TODO: Add graceful shutdown support
// TODO: Document server configuration options
// TODO: Allow injecting existing grpc.Server
// TODO: End TODO list

func NewServer(cfgSvc configpb.ConfigServiceServer, adminSvc configpb.ConfigAdminServiceServer) *grpc.Server {
	s := grpc.NewServer()
	if cfgSvc != nil {
		configpb.RegisterConfigServiceServer(s, cfgSvc)
	}
	if adminSvc != nil {
		configpb.RegisterConfigAdminServiceServer(s, adminSvc)
	}
	return s
}

// EOF
