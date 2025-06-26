// Package middleware provides gRPC interceptors for metrics collection.
package middleware

import (
	"context"
	"strings"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"google.golang.org/grpc"
	"google.golang.org/grpc/status"
)

// GRPCMetricsOptions configures the gRPC metrics interceptors.
type GRPCMetricsOptions struct {
	// Provider is the metrics provider.
	Provider metrics.Provider

	// Buckets are the histogram buckets for request duration.
	Buckets []float64

	// AdditionalTags are additional tags to include with all metrics.
	AdditionalTags []metrics.Tag

	// RequestCounterName is the name of the request counter.
	// Default: "grpc_server_requests_total".
	RequestCounterName string

	// DurationHistogramName is the name of the request duration histogram.
	// Default: "grpc_server_request_duration_seconds".
	DurationHistogramName string
}

// UnaryServerMetrics returns a unary server interceptor that records metrics.
func UnaryServerMetrics(opts GRPCMetricsOptions) grpc.UnaryServerInterceptor {
	if opts.RequestCounterName == "" {
		opts.RequestCounterName = "grpc_server_requests_total"
	}
	if opts.DurationHistogramName == "" {
		opts.DurationHistogramName = "grpc_server_request_duration_seconds"
	}
	if opts.Buckets == nil {
		opts.Buckets = metrics.DefaultBuckets
	}

	counter := opts.Provider.Counter(
		opts.RequestCounterName,
		metrics.WithDescription("Total number of gRPC requests"),
	)
	histogram := opts.Provider.Histogram(
		opts.DurationHistogramName,
		metrics.WithDescription("gRPC request duration in seconds"),
		metrics.WithBuckets(opts.Buckets),
	)

	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		start := time.Now()
		resp, err := handler(ctx, req)
		svc, method := splitFullMethod(info.FullMethod)
		code := status.Code(err).String()
		tags := append(opts.AdditionalTags, []metrics.Tag{
			{Key: "service", Value: svc},
			{Key: "method", Value: method},
			{Key: "status", Value: code},
		}...)
		counter.WithTags(tags...).Inc()
		histogram.WithTags(tags...).Observe(time.Since(start).Seconds())
		return resp, err
	}
}

// StreamServerMetrics returns a stream server interceptor that records metrics.
func StreamServerMetrics(opts GRPCMetricsOptions) grpc.StreamServerInterceptor {
	if opts.RequestCounterName == "" {
		opts.RequestCounterName = "grpc_server_requests_total"
	}
	if opts.DurationHistogramName == "" {
		opts.DurationHistogramName = "grpc_server_request_duration_seconds"
	}
	if opts.Buckets == nil {
		opts.Buckets = metrics.DefaultBuckets
	}

	counter := opts.Provider.Counter(
		opts.RequestCounterName,
		metrics.WithDescription("Total number of gRPC requests"),
	)
	histogram := opts.Provider.Histogram(
		opts.DurationHistogramName,
		metrics.WithDescription("gRPC request duration in seconds"),
		metrics.WithBuckets(opts.Buckets),
	)

	return func(srv interface{}, stream grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		start := time.Now()
		err := handler(srv, stream)
		svc, method := splitFullMethod(info.FullMethod)
		code := status.Code(err).String()
		tags := append(opts.AdditionalTags, []metrics.Tag{
			{Key: "service", Value: svc},
			{Key: "method", Value: method},
			{Key: "status", Value: code},
		}...)
		counter.WithTags(tags...).Inc()
		histogram.WithTags(tags...).Observe(time.Since(start).Seconds())
		return err
	}
}

// splitFullMethod splits a gRPC full method name into service and method.
// The input is expected in the form "/package.Service/Method".
func splitFullMethod(fullMethod string) (string, string) {
	fullMethod = strings.TrimPrefix(fullMethod, "/")
	parts := strings.SplitN(fullMethod, "/", 2)
	if len(parts) != 2 {
		return fullMethod, ""
	}
	return parts[0], parts[1]
}
