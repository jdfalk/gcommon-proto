// file: pkg/grpc/interceptors/metrics_stream.go
// version: 1.0.0
// guid: 0d82029d-79d6-4d1c-80ad-c6cc1ea13f26

package interceptors

import (
	"time"

	"google.golang.org/grpc"
)

// MetricsStream measures stream duration for metrics collection.
func MetricsStream(observer func(method string, d time.Duration, err error)) grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		start := time.Now()
		err := handler(srv, ss)
		if observer != nil {
			observer(info.FullMethod, time.Since(start), err)
		}
		return err
	}
}
