// file: pkg/grpc/interceptors/auth.go
// version: 1.0.0
// guid: 2a603731-2dd9-4498-906d-b0f0e951d199

package interceptors

import (
	"context"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// AuthUnary returns a unary interceptor performing basic authorization checks.
func AuthUnary(check func(context.Context) error) grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		if check != nil {
			if err := check(ctx); err != nil {
				return nil, status.Error(codes.PermissionDenied, err.Error())
			}
		}
		return handler(ctx, req)
	}
}
