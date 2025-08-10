// file: pkg/auth/middleware/grpc.go
// version: 1.0.0
// guid: e1f2a3b4-c5d6-7e8f-901a-b2c3d4e5f6a7

package middleware

import (
	"context"

	auth "github.com/jdfalk/gcommon/pkg/auth"
	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
	"google.golang.org/grpc"
)

// UnaryServerInterceptor validates auth tokens on incoming gRPC requests.
func UnaryServerInterceptor(p auth.AuthProvider) grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		if v, ok := req.(*proto.ValidateTokenRequest); ok {
			if _, err := p.ValidateToken(ctx, v); err != nil {
				return nil, err
			}
		}
		return handler(ctx, req)
	}
}
