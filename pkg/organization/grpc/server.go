// file: pkg/organization/grpc/server.go
// version: 1.0.0
// guid: 7a6b4ad3-d481-47d1-9ba2-fa0a391e287b

package grpc

import (
	orgpb "github.com/jdfalk/gcommon/pkg/organization/proto"
	"google.golang.org/grpc"
)

// Register registers organization gRPC services with the server.
func Register(s *grpc.Server, ts orgpb.TenantServiceServer) {
	orgpb.RegisterTenantServiceServer(s, ts)
}
