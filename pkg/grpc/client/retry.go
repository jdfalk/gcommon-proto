// file: pkg/grpc/client/retry.go
// version: 1.0.0
// guid: 945f1877-1b2e-4aa6-9011-3aebb9e3f4d8

package client

import (
	"context"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// RetryOptions configures retry behaviour for client calls.
type RetryOptions struct {
	// MaxAttempts is the maximum number of retry attempts (including first call).
	MaxAttempts uint
	// BackoffStrategy calculates the backoff delay.
	BackoffStrategy Backoff
	// Retryable decides whether to retry for the given error.
	Retryable func(error) bool
}

// defaultRetryable retries on all errors.
func defaultRetryable(err error) bool { return err != nil }

// UnaryRetryInterceptor returns a grpc.UnaryClientInterceptor with retry logic.
func UnaryRetryInterceptor(opts RetryOptions) grpc.UnaryClientInterceptor {
	if opts.MaxAttempts == 0 {
		opts.MaxAttempts = 3
	}
	if opts.BackoffStrategy == nil {
		opts.BackoffStrategy = NewExponentialBackoff()
	}
	if opts.Retryable == nil {
		opts.Retryable = defaultRetryable
	}
	return func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, callOpts ...grpc.CallOption) error {
		var lastErr error
		for attempt := uint(0); attempt < opts.MaxAttempts; attempt++ {
			if attempt > 0 {
				d := opts.BackoffStrategy.Next(attempt - 1)
				select {
				case <-time.After(d):
				case <-ctx.Done():
					return ctx.Err()
				}
			}
			lastErr = invoker(ctx, method, req, reply, cc, callOpts...)
			if lastErr == nil || !opts.Retryable(lastErr) {
				return lastErr
			}
			if s, ok := status.FromError(lastErr); ok && s.Code() == codes.Unauthenticated {
				return lastErr
			}
		}
		return lastErr
	}
}
