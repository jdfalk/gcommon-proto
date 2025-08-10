// file: pkg/config/examples/grpc_server.go
// version: 1.0.0
// guid: dddddddd-dddd-dddd-dddd-dddddddddddd

package examples

import (
	"net"

	cfggrpc "github.com/jdfalk/gcommon/pkg/config/grpc"
	"github.com/jdfalk/gcommon/pkg/config/providers"
)

// ExampleGRPCServer demonstrates starting a gRPC server with config services
// TODO: Include full client-server interaction
// TODO: Handle errors and context cancellation
// TODO: Add TLS setup example
func ExampleGRPCServer() {
	p, _ := providers.NewEnvProvider("APP_")
	svc := &cfggrpc.ConfigServiceServer{Provider: p}
	server := cfggrpc.NewServer(svc, nil)
	l, _ := net.Listen("tcp", ":0")
	go server.Serve(l)
	server.Stop()
}

// EOF
