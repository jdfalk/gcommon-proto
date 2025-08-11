// file: pkg/grpc/interceptors/auth_stream.go
// version: 1.0.0
// guid: 391d4e5f-82df-4d89-bb86-d2e58f7b4371

package interceptors

import (
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// AuthStream returns a stream interceptor performing basic authorization checks.
func AuthStream(check func(stream grpc.ServerStream) error) grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		if check != nil {
			if err := check(ss); err != nil {
				return status.Error(codes.PermissionDenied, err.Error())
			}
		}
		return handler(srv, ss)
	}
}
