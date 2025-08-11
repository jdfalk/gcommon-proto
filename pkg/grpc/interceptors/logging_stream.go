// file: pkg/grpc/interceptors/logging_stream.go
// version: 1.0.0
// guid: 2836eb7d-0d34-4276-9126-6e9d901b577b

package interceptors

import (
	"log"

	"google.golang.org/grpc"
)

// LoggingStream logs stream method invocations.
func LoggingStream(logger *log.Logger) grpc.StreamServerInterceptor {
	if logger == nil {
		logger = log.Default()
	}
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		logger.Printf("stream %s called", info.FullMethod)
		return handler(srv, ss)
	}
}
