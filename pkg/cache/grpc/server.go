// file: pkg/cache/grpc/server.go
// version: 1.0.0
// guid: f5a6b7c8-d9e0-4f1a-2b3c-4d5e6f7a8b9c

package cachegrpc

import (
	"net"

	cachepkg "github.com/jdfalk/gcommon/pkg/cache"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	"google.golang.org/grpc"
)

// NewServer creates a gRPC server with cache services registered.
func NewServer(c cachepkg.Cache) *grpc.Server {
	s := grpc.NewServer()
	cachepb.RegisterCacheServiceServer(s, NewCacheService(c))
	cachepb.RegisterCacheAdminServiceServer(s, NewCacheAdminService(c))
	return s
}

// ListenAndServe starts the server on the given address.
func ListenAndServe(addr string, c cachepkg.Cache) error {
	lis, err := net.Listen("tcp", addr)
	if err != nil {
		return err
	}
	srv := NewServer(c)
	return srv.Serve(lis)
}
