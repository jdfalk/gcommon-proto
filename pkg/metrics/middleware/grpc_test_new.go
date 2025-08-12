package middleware

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/mock"
	"github.com/stretchr/testify/assert"
	"google.golang.org/grpc"
)

func TestGRPCMetricsInterceptor(t *testing.T) {
	// Create mock provider and metrics
	mockProvider := mock.NewMockProvider(t)
	mockCounter := mock.NewMockCounter(t)
	mockHistogram := mock.NewMockHistogram(t)

	// Setup expectations
	mockProvider.On("Counter", "grpc_requests_total", []metrics.Option(nil)).Return(mockCounter)
	mockProvider.On("Histogram", "grpc_request_duration_seconds", []metrics.Option(nil)).Return(mockHistogram)

	mockCounter.On("WithTags", []metrics.Tag{{Key: "method", Value: "/test"}, {Key: "status", Value: "OK"}}).Return(mockCounter)
	mockCounter.On("Inc").Return()

	mockHistogram.On("WithTags", []metrics.Tag{{Key: "method", Value: "/test"}}).Return(mockHistogram)
	mockHistogram.On("Observe", float64(0.1)).Return()

	// Create interceptor
	interceptor := NewGRPCMetricsInterceptor(mockProvider)
	assert.NotNil(t, interceptor)

	// Test unary interceptor
	unaryHandler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return "response", nil
	}

	info := &grpc.UnaryServerInfo{
		FullMethod: "/test",
	}

	resp, err := interceptor.UnaryServerInterceptor()(context.Background(), "request", info, unaryHandler)
	assert.NoError(t, err)
	assert.Equal(t, "response", resp)

	// Verify expectations
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockHistogram.AssertExpectations(t)
}

// dummy unary handler
func dummyUnary(ctx context.Context, req interface{}) (interface{}, error) {
	return "ok", nil
}

func TestUnaryServerMetrics(t *testing.T) {
	// Create mock provider and metrics
	mockProvider := mock.NewMockProvider(t)
	mockCounter := mock.NewMockCounter(t)
	mockHistogram := mock.NewMockHistogram(t)

	// Setup expectations
	mockProvider.On("Counter", "grpc_requests_total", []metrics.Option(nil)).Return(mockCounter)
	mockProvider.On("Histogram", "grpc_request_duration_seconds", []metrics.Option(nil)).Return(mockHistogram)

	mockCounter.On("WithTags", []metrics.Tag{{Key: "method", Value: "/pkg.Service/Method"}, {Key: "status", Value: "OK"}}).Return(mockCounter)
	mockCounter.On("Inc").Return()

	mockHistogram.On("WithTags", []metrics.Tag{{Key: "method", Value: "/pkg.Service/Method"}}).Return(mockHistogram)
	mockHistogram.On("Observe", mock.AnythingOfType("float64")).Return()

	interceptor := UnaryServerMetrics(GRPCMetricsOptions{Provider: mockProvider})

	_, err := interceptor(context.Background(), struct{}{}, &grpc.UnaryServerInfo{FullMethod: "/pkg.Service/Method"}, dummyUnary)
	assert.NoError(t, err)

	// Verify expectations
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockHistogram.AssertExpectations(t)
}

// dummy stream handler
func dummyStream(srv interface{}, stream grpc.ServerStream) error { return nil }

type dummyServerStream struct{ grpc.ServerStream }

func TestStreamServerMetrics(t *testing.T) {
	// Create mock provider and metrics
	mockProvider := mock.NewMockProvider(t)
	mockCounter := mock.NewMockCounter(t)
	mockHistogram := mock.NewMockHistogram(t)

	// Setup expectations
	mockProvider.On("Counter", "grpc_requests_total", []metrics.Option(nil)).Return(mockCounter)
	mockProvider.On("Histogram", "grpc_request_duration_seconds", []metrics.Option(nil)).Return(mockHistogram)

	mockCounter.On("WithTags", []metrics.Tag{{Key: "method", Value: "/pkg.Service/Stream"}, {Key: "status", Value: "OK"}}).Return(mockCounter)
	mockCounter.On("Inc").Return()

	mockHistogram.On("WithTags", []metrics.Tag{{Key: "method", Value: "/pkg.Service/Stream"}}).Return(mockHistogram)
	mockHistogram.On("Observe", mock.AnythingOfType("float64")).Return()

	interceptor := StreamServerMetrics(GRPCMetricsOptions{Provider: mockProvider})

	ds := &dummyServerStream{}
	err := interceptor(nil, ds, &grpc.StreamServerInfo{FullMethod: "/pkg.Service/Stream"}, dummyStream)
	assert.NoError(t, err)

	// Verify expectations
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockHistogram.AssertExpectations(t)
}
