// file: pkg/grpc/interceptors/metrics.go
// version: 1.0.0
// guid: 715446ee-c03f-4f96-a128-e6737a860e18

package interceptors

import (
	"context"
	"time"

	"google.golang.org/grpc"
)

// MetricsUnary measures request duration for metrics collection.
func MetricsUnary(observer func(method string, d time.Duration, err error)) grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		start := time.Now()
		resp, err := handler(ctx, req)
		if observer != nil {
			observer(info.FullMethod, time.Since(start), err)
		}
		return resp, err
	}
}
