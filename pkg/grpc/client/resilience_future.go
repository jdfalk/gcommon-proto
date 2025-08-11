// file: pkg/grpc/client/resilience_future.go
// version: 1.0.0
// guid: 8d3b5d4a-2b9c-4b0e-8d9d-8f7c6e5a4b3c

// Package client provides gRPC client utilities. This file implements
// advanced resilience features that combine multiple fault-tolerance
// strategies including retries, circuit breaking, rate limiting and
// request hedging. The goal is to offer a single interceptor that can be
// configured with the desired policies while remaining modular so that
// individual strategies can be reused independently.
package client

import (
	"context"
	"sync"
	"sync/atomic"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// RateLimiter decides whether a request is allowed to proceed based on
// current load. Implementations must be safe for concurrent use.
type RateLimiter interface {
	Allow() bool
}

// TokenBucket implements a simple token bucket rate limiter. The bucket is
// filled at a steady rate up to a maximum burst capacity. Each call to
// Allow consumes one token. If no tokens remain the call is rejected.
type TokenBucket struct {
	mu       sync.Mutex
	capacity float64
	tokens   float64
	rate     float64
	last     time.Time
}

// NewTokenBucket creates a token bucket with the given fill rate (tokens per
// second) and burst capacity. The bucket starts full.
func NewTokenBucket(rate, burst int) *TokenBucket {
	if rate <= 0 {
		rate = 1
	}
	if burst <= 0 {
		burst = rate
	}
	return &TokenBucket{
		capacity: float64(burst),
		tokens:   float64(burst),
		rate:     float64(rate),
		last:     time.Now(),
	}
}

// Allow reports whether a token is available. If so it consumes one token and
// returns true. Otherwise it returns false.
func (tb *TokenBucket) Allow() bool {
	tb.mu.Lock()
	defer tb.mu.Unlock()
	now := time.Now()
	elapsed := now.Sub(tb.last).Seconds()
	tb.last = now
	tb.tokens += elapsed * tb.rate
	if tb.tokens > tb.capacity {
		tb.tokens = tb.capacity
	}
	if tb.tokens < 1 {
		return false
	}
	tb.tokens--
	return true
}

// HedgingPolicy controls how additional hedged RPCs are issued. Hedging
// allows secondary requests to be sent if the initial call is taking too long
// which can reduce tail latency at the expense of extra load.
type HedgingPolicy struct {
	// MaxHedges is the maximum number of parallel hedged requests
	// including the original. Values less than two disable hedging.
	MaxHedges int
	// HedgeDelay is the delay before starting each additional hedge.
	HedgeDelay time.Duration
}

// ResilienceOptions configures the behaviour of the ResilientUnaryInterceptor.
// All fields are optional. Zero values will cause sensible defaults to be
// selected.
type ResilienceOptions struct {
	Retry          RetryOptions
	CircuitBreaker *CircuitBreaker
	RateLimiter    RateLimiter
	Hedge          HedgingPolicy
	Timeout        time.Duration
}

// ResilientUnaryInterceptor returns a grpc.UnaryClientInterceptor that
// composes multiple resilience strategies including retries, circuit breaking,
// rate limiting and hedging. Each component can be enabled or disabled via the
// supplied options.
func ResilientUnaryInterceptor(opts ResilienceOptions) grpc.UnaryClientInterceptor {
	if opts.RateLimiter == nil {
		opts.RateLimiter = NewTokenBucket(100, 100)
	}
	if opts.CircuitBreaker == nil {
		opts.CircuitBreaker = NewCircuitBreaker()
	}
	if opts.Retry.MaxAttempts == 0 {
		opts.Retry.MaxAttempts = 3
	}
	if opts.Retry.BackoffStrategy == nil {
		opts.Retry.BackoffStrategy = NewExponentialBackoff()
	}
	if opts.Retry.Retryable == nil {
		opts.Retry.Retryable = defaultRetryable
	}
	return func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn,
		invoker grpc.UnaryInvoker, callOpts ...grpc.CallOption) error {
		if opts.Timeout > 0 {
			var cancel context.CancelFunc
			ctx, cancel = context.WithTimeout(ctx, opts.Timeout)
			defer cancel()
		}
		if opts.RateLimiter != nil && !opts.RateLimiter.Allow() {
			return status.Error(codes.ResourceExhausted, "rate limit exceeded")
		}

		attempt := func(c context.Context) error {
			if !opts.CircuitBreaker.Allow() {
				return status.Error(codes.Unavailable, "circuit open")
			}
			err := invoker(c, method, req, reply, cc, callOpts...)
			if err != nil {
				opts.CircuitBreaker.MarkFailure()
			} else {
				opts.CircuitBreaker.MarkSuccess()
			}
			return err
		}

		if opts.Hedge.MaxHedges > 1 {
			return runWithHedging(ctx, attempt, opts)
		}
		return runWithRetry(ctx, attempt, opts)
	}
}

// runWithRetry executes the provided function using the retry policy defined in
// ResilienceOptions. Retries are attempted with the configured backoff
// strategy. The function stops retrying once it succeeds or the retry policy is
// exhausted.
func runWithRetry(ctx context.Context, fn func(context.Context) error, opts ResilienceOptions) error {
	if opts.Retry.BackoffStrategy == nil {
		opts.Retry.BackoffStrategy = NewExponentialBackoff()
	}
	if opts.Retry.Retryable == nil {
		opts.Retry.Retryable = defaultRetryable
	}
	var lastErr error
	for attempt := uint(0); attempt < opts.Retry.MaxAttempts; attempt++ {
		if attempt > 0 {
			d := opts.Retry.BackoffStrategy.Next(attempt - 1)
			select {
			case <-time.After(d):
			case <-ctx.Done():
				return ctx.Err()
			}
		}
		lastErr = fn(ctx)
		if lastErr == nil || !opts.Retry.Retryable(lastErr) {
			return lastErr
		}
		if s, ok := status.FromError(lastErr); ok && s.Code() == codes.Unauthenticated {
			return lastErr
		}
	}
	return lastErr
}

// runWithHedging executes the function with request hedging. The initial
// attempt is started immediately and additional hedged attempts are launched
// after the configured delay. The first successful attempt returns and all
// others are canceled. Retries are still applied within each hedged attempt.
func runWithHedging(ctx context.Context, fn func(context.Context) error, opts ResilienceOptions) error {
	var (
		wg      sync.WaitGroup
		cancel  context.CancelFunc
		hedges  = opts.Hedge.MaxHedges
		results = make(chan error, hedges)
	)
	ctx, cancel = context.WithCancel(ctx)
	defer cancel()

	startAttempt := func() {
		wg.Add(1)
		go func() {
			defer wg.Done()
			err := runWithRetry(ctx, fn, opts)
			if err == nil {
				select {
				case results <- nil:
				default:
				}
				cancel()
			} else {
				results <- err
			}
		}()
	}

	startAttempt() // initial request

	for i := 1; i < hedges; i++ {
		select {
		case <-ctx.Done():
			break
		case <-time.After(opts.Hedge.HedgeDelay):
			startAttempt()
		}
	}

	var lastErr error
	for i := 0; i < hedges; i++ {
		select {
		case err := <-results:
			if err == nil {
				wg.Wait()
				return nil
			}
			lastErr = err
		case <-ctx.Done():
			wg.Wait()
			return lastErr
		}
	}

	wg.Wait()
	return lastErr
}

// BulkheadLimiter limits the number of concurrent operations. It implements the
// RateLimiter interface but enforces a concurrency ceiling rather than a
// throughput rate. Once the limit is reached additional calls are rejected
// until running operations complete.
type BulkheadLimiter struct {
	capacity int32
	current  int32
}

// NewBulkheadLimiter creates a BulkheadLimiter with the specified capacity.
func NewBulkheadLimiter(capacity int) *BulkheadLimiter {
	if capacity <= 0 {
		capacity = 1
	}
	return &BulkheadLimiter{capacity: int32(capacity)}
}

// Allow attempts to reserve one slot. It returns true if capacity permits the
// operation and false otherwise.
func (b *BulkheadLimiter) Allow() bool {
	for {
		cur := atomic.LoadInt32(&b.current)
		if cur >= b.capacity {
			return false
		}
		if atomic.CompareAndSwapInt32(&b.current, cur, cur+1) {
			return true
		}
	}
}

// Done releases a previously reserved slot. It should be called when the
// operation completes.
func (b *BulkheadLimiter) Done() {
	atomic.AddInt32(&b.current, -1)
}
