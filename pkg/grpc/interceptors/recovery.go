// file: pkg/grpc/interceptors/recovery.go
// version: 1.0.0
// guid: dd905d5e-5d3d-4aa5-b47e-7519638ee1d0

package interceptors

import (
	"context"
	"fmt"

	"google.golang.org/grpc"
)

// RecoveryUnary intercepts panics and returns an error instead.
func RecoveryUnary() grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (resp interface{}, err error) {
		defer func() {
			if r := recover(); r != nil {
				err = fmt.Errorf("panic: %v", r)
			}
		}()
		return handler(ctx, req)
	}
}
