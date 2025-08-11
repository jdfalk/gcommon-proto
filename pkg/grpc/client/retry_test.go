// file: pkg/grpc/client/retry_test.go
// version: 1.0.0
// guid: 89d8f36a-4547-4de7-b9de-2a6577854e04

package client

import (
	"context"
	"errors"
	"testing"
	"time"

	"google.golang.org/grpc"
)

// TestUnaryRetryInterceptor retries until success.
func TestUnaryRetryInterceptor(t *testing.T) {
	attempts := 0
	invoker := func(context.Context, string, interface{}, interface{}, *grpc.ClientConn, ...grpc.CallOption) error {
		attempts++
		if attempts < 3 {
			return errors.New("fail")
		}
		return nil
	}
	interceptor := UnaryRetryInterceptor(RetryOptions{MaxAttempts: 5, BackoffStrategy: ConstantBackoff{Delay: time.Millisecond}})
	err := interceptor(context.Background(), "", nil, nil, nil, invoker)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if attempts != 3 {
		t.Fatalf("expected 3 attempts, got %d", attempts)
	}
}
