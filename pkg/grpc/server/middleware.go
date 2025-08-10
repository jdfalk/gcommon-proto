// file: pkg/grpc/server/middleware.go
// version: 1.0.0
// guid: e816bc12-3528-4515-8007-8df0d951c42d

package server

import (
	"context"
	"google.golang.org/grpc"
)

// ChainUnary creates a single unary interceptor from a list.
func ChainUnary(interceptors ...grpc.UnaryServerInterceptor) grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		var chained grpc.UnaryHandler = handler
		for i := len(interceptors) - 1; i >= 0; i-- {
			inter := interceptors[i]
			next := chained
			chained = func(c context.Context, r interface{}) (interface{}, error) {
				return inter(c, r, info, next)
			}
		}
		return chained(ctx, req)
	}
}

// ChainStream creates a single stream interceptor from a list.
func ChainStream(interceptors ...grpc.StreamServerInterceptor) grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		var chained grpc.StreamHandler = handler
		for i := len(interceptors) - 1; i >= 0; i-- {
			inter := interceptors[i]
			next := chained
			chained = func(current interface{}, stream grpc.ServerStream) error {
				return inter(current, stream, info, next)
			}
		}
		return chained(srv, ss)
	}
}
