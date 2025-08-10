// file: pkg/log/middleware/grpc.go
// version: 1.0.0
// guid: c1e2d3f4-a5b6-4c7d-8e9f-0123456789ab

package middleware

import (
	"context"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
	"google.golang.org/grpc"
)

// UnaryServerInterceptor returns a gRPC unary interceptor that logs requests and responses.
func UnaryServerInterceptor(logger log.Logger) grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		start := time.Now()
		resp, err := handler(ctx, req)
		duration := time.Since(start)
		fields := []log.Field{{Key: "method", Value: info.FullMethod}, {Key: "duration", Value: duration.String()}}
		if err != nil {
			logger.ErrorContext(ctx, "grpc unary request failed", append(fields, log.Field{Key: "error", Value: err.Error()})...)
		} else {
			logger.InfoContext(ctx, "grpc unary request completed", fields...)
		}
		return resp, err
	}
}

// StreamServerInterceptor logs gRPC streaming requests.
func StreamServerInterceptor(logger log.Logger) grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		start := time.Now()
		err := handler(srv, ss)
		duration := time.Since(start)
		fields := []log.Field{{Key: "method", Value: info.FullMethod}, {Key: "duration", Value: duration.String()}}
		if err != nil {
			logger.ErrorContext(ss.Context(), "grpc stream failed", append(fields, log.Field{Key: "error", Value: err.Error()})...)
		} else {
			logger.InfoContext(ss.Context(), "grpc stream completed", fields...)
		}
		return err
	}
}
