// file: pkg/grpc/client/resilience.go
// version: 1.0.0
// guid: 5f1c5d7e-8a9b-4f0a-93d2-bc2752e78d10

package client

import (
	"context"
	"time"

	"google.golang.org/grpc"
)

// ResiliencePolicy configures combined retry and circuit breaker behaviour.
type ResiliencePolicy struct {
	// CircuitBreaker guards against repeated failures. If nil a default breaker is used.
	CircuitBreaker *CircuitBreaker
	// Retry controls retry attempts. Zero values use sensible defaults.
	Retry RetryOptions
	// Timeout caps the total time allowed for a call. Zero disables the timeout.
	Timeout time.Duration
	// Fallback is invoked when the call fails after all retries or when the
	// circuit is open. If nil the last error is returned.
	Fallback func(ctx context.Context, method string, req, reply interface{}, err error) error
}

// DefaultResiliencePolicy returns a policy with sensible defaults.
func DefaultResiliencePolicy() ResiliencePolicy {
	return ResiliencePolicy{
		CircuitBreaker: NewCircuitBreaker(),
		Retry: RetryOptions{
			MaxAttempts:     3,
			BackoffStrategy: NewExponentialBackoff(),
			Retryable:       defaultRetryable,
		},
	}
}

// UnaryResilienceInterceptor returns an interceptor that applies retry logic,
// circuit breaking and optional fallbacks using the provided policy.
func UnaryResilienceInterceptor(p ResiliencePolicy) grpc.UnaryClientInterceptor {
	if p.CircuitBreaker == nil {
		p.CircuitBreaker = NewCircuitBreaker()
	}
	if p.Retry.MaxAttempts == 0 {
		p.Retry.MaxAttempts = 3
	}
	if p.Retry.BackoffStrategy == nil {
		p.Retry.BackoffStrategy = NewExponentialBackoff()
	}
	if p.Retry.Retryable == nil {
		p.Retry.Retryable = defaultRetryable
	}
	return func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, callOpts ...grpc.CallOption) error {
		if p.Timeout > 0 {
			var cancel context.CancelFunc
			ctx, cancel = context.WithTimeout(ctx, p.Timeout)
			defer cancel()
		}
		var lastErr error
		for attempt := uint(0); attempt < p.Retry.MaxAttempts; attempt++ {
			if !p.CircuitBreaker.Allow() {
				if p.Fallback != nil {
					return p.Fallback(ctx, method, req, reply, grpc.ErrClientConnClosing)
				}
				return grpc.ErrClientConnClosing
			}
			if attempt > 0 {
				d := p.Retry.BackoffStrategy.Next(attempt - 1)
				select {
				case <-time.After(d):
				case <-ctx.Done():
					return ctx.Err()
				}
			}
			lastErr = invoker(ctx, method, req, reply, cc, callOpts...)
			if lastErr == nil {
				p.CircuitBreaker.MarkSuccess()
				return nil
			}
			p.CircuitBreaker.MarkFailure()
			if !p.Retry.Retryable(lastErr) {
				break
			}
		}
		if p.Fallback != nil {
			return p.Fallback(ctx, method, req, reply, lastErr)
		}
		return lastErr
	}
}

// ResilientExecutor executes functions with resilience policy outside gRPC.
type ResilientExecutor struct {
	policy ResiliencePolicy
}

// NewResilientExecutor creates an executor with the given policy.
func NewResilientExecutor(policy ResiliencePolicy) *ResilientExecutor {
	if policy.CircuitBreaker == nil {
		policy.CircuitBreaker = NewCircuitBreaker()
	}
	if policy.Retry.MaxAttempts == 0 {
		policy.Retry.MaxAttempts = 3
	}
	if policy.Retry.BackoffStrategy == nil {
		policy.Retry.BackoffStrategy = NewExponentialBackoff()
	}
	if policy.Retry.Retryable == nil {
		policy.Retry.Retryable = defaultRetryable
	}
	return &ResilientExecutor{policy: policy}
}

// Do executes fn with the configured policy, providing the same semantics as
// the unary interceptor but for arbitrary operations.
func (e *ResilientExecutor) Do(ctx context.Context, fn func(context.Context) error) error {
	p := e.policy
	if p.Timeout > 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, p.Timeout)
		defer cancel()
	}
	var lastErr error
	for attempt := uint(0); attempt < p.Retry.MaxAttempts; attempt++ {
		if !p.CircuitBreaker.Allow() {
			if p.Fallback != nil {
				return p.Fallback(ctx, "", nil, nil, grpc.ErrClientConnClosing)
			}
			return grpc.ErrClientConnClosing
		}
		if attempt > 0 {
			d := p.Retry.BackoffStrategy.Next(attempt - 1)
			select {
			case <-time.After(d):
			case <-ctx.Done():
				return ctx.Err()
			}
		}
		lastErr = fn(ctx)
		if lastErr == nil {
			p.CircuitBreaker.MarkSuccess()
			return nil
		}
		p.CircuitBreaker.MarkFailure()
		if !p.Retry.Retryable(lastErr) {
			break
		}
	}
	if p.Fallback != nil {
		return p.Fallback(ctx, "", nil, nil, lastErr)
	}
	return lastErr
}

// ResilienceStats tracks successes and failures when using a ResilientExecutor.
type ResilienceStats struct {
	Successes int
	Failures  int
}

// DoWithStats executes fn and records success/failure counts in stats.
func (e *ResilientExecutor) DoWithStats(ctx context.Context, fn func(context.Context) error, stats *ResilienceStats) error {
	err := e.Do(ctx, fn)
	if stats != nil {
		if err != nil {
			stats.Failures++
		} else {
			stats.Successes++
		}
	}
	return err
}
