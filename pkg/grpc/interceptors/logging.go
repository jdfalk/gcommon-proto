// file: pkg/grpc/interceptors/logging.go
// version: 1.0.0
// guid: 9d891769-7a3a-4624-816d-25f7ed0a0fd1

package interceptors

import (
	"context"
	"log"

	"google.golang.org/grpc"
)

// LoggingUnary logs basic request information.
func LoggingUnary(logger *log.Logger) grpc.UnaryServerInterceptor {
	if logger == nil {
		logger = log.Default()
	}
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		logger.Printf("%s called", info.FullMethod)
		return handler(ctx, req)
	}
}
