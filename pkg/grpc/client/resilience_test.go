// file: pkg/grpc/client/resilience_test.go
// version: 1.0.0
// guid: 4a2b6a15-8c38-4b1d-81f9-707e6a2c20e1

package client

import (
	"context"
	"errors"
	"testing"
	"time"

	"google.golang.org/grpc"
)

// TestUnaryResilienceInterceptor_RetrySuccess verifies retry and breaker reset behaviour.
func TestUnaryResilienceInterceptor_RetrySuccess(t *testing.T) {
	policy := DefaultResiliencePolicy()
	attempts := 0
	invoker := func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn, opts ...grpc.CallOption) error {
		attempts++
		if attempts < 2 {
			return errors.New("temp failure")
		}
		return nil
	}
	interceptor := UnaryResilienceInterceptor(policy)
	err := interceptor(context.Background(), "/svc/Op", nil, nil, nil, invoker)
	if err != nil {
		t.Fatalf("expected success, got %v", err)
	}
	if attempts != 2 {
		t.Fatalf("expected 2 attempts, got %d", attempts)
	}
}

// TestUnaryResilienceInterceptor_CircuitOpenFallback ensures fallback executes when circuit is open.
func TestUnaryResilienceInterceptor_CircuitOpenFallback(t *testing.T) {
	cb := NewCircuitBreaker()
	cb.failureThresh = 1
	var fallbackCalled bool
	policy := ResiliencePolicy{
		CircuitBreaker: cb,
		Retry:          RetryOptions{MaxAttempts: 1, BackoffStrategy: ConstantBackoff{Delay: time.Millisecond}},
		Fallback: func(ctx context.Context, method string, req, reply interface{}, err error) error {
			fallbackCalled = true
			return err
		},
	}
	invoker := func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn, opts ...grpc.CallOption) error {
		return errors.New("fail")
	}
	interceptor := UnaryResilienceInterceptor(policy)
	err := interceptor(context.Background(), "/svc/Op", nil, nil, nil, invoker)
	if err == nil {
		t.Fatalf("expected error on failure")
	}
	if !fallbackCalled {
		t.Fatalf("expected fallback to be called")
	}
	if cb.state != Open {
		t.Fatalf("expected circuit to be open")
	}
	err = interceptor(context.Background(), "/svc/Op", nil, nil, nil, invoker)
	if err == nil {
		t.Fatalf("expected immediate error when circuit open")
	}
}

// TestResilientExecutor_DoWithStats validates stats tracking with retries.
func TestResilientExecutor_DoWithStats(t *testing.T) {
	exec := NewResilientExecutor(DefaultResiliencePolicy())
	stats := &ResilienceStats{}
	attempts := 0
	err := exec.DoWithStats(context.Background(), func(ctx context.Context) error {
		attempts++
		if attempts == 1 {
			return errors.New("boom")
		}
		return nil
	}, stats)
	if err != nil {
		t.Fatalf("expected success after retry, got %v", err)
	}
	if stats.Successes != 1 || stats.Failures != 0 {
		t.Fatalf("expected 1 success and 0 failures, got %d success and %d failure", stats.Successes, stats.Failures)
	}
}
