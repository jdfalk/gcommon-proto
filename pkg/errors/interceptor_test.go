// file: pkg/errors/interceptor_test.go
// version: 1.0.0
// guid: a0b1c2d3-1415-4f11-f234-0123456789ab

package errors

import (
	"context"
	"testing"

	"google.golang.org/grpc"
)

// TestErrorHandlingInterceptor ensures unary interceptor converts errors.
func TestErrorHandlingInterceptor(t *testing.T) {
	interceptor := ErrorHandlingInterceptor()
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return nil, NewError(ctx, ErrCodeInvalidInput, "bad")
	}
	_, err := interceptor(context.Background(), nil, &grpc.UnaryServerInfo{}, handler)
	if err == nil {
		t.Fatalf("expected error")
	}
}

// TestErrorHandlingStreamInterceptor ensures stream interceptor converts errors.
func TestErrorHandlingStreamInterceptor(t *testing.T) {
	interceptor := ErrorHandlingStreamInterceptor()
	handler := func(srv interface{}, ss grpc.ServerStream) error {
		return NewError(ss.Context(), ErrCodeInvalidInput, "bad")
	}
	err := interceptor(nil, &noopServerStream{ctx: context.Background()}, &grpc.StreamServerInfo{}, handler)
	if err == nil {
		t.Fatalf("expected error")
	}
}

type noopServerStream struct {
	grpc.ServerStream
	ctx context.Context
}

func (n *noopServerStream) Context() context.Context { return n.ctx }
