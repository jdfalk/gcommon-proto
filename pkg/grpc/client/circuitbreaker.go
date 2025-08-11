// file: pkg/grpc/client/circuitbreaker.go
// version: 1.0.0
// guid: d4e278a4-7fb4-4c4e-8e7b-73d9aa70f8f2

package client

import (
	"context"
	"sync"
	"time"

	"google.golang.org/grpc"
)

// CircuitState represents the state of a circuit breaker.
type CircuitState int

const (
	// Closed allows all requests.
	Closed CircuitState = iota
	// Open rejects requests immediately.
	Open
	// HalfOpen allows a limited number of trial requests.
	HalfOpen
)

// CircuitBreaker implements a simple failure-count circuit breaker.
type CircuitBreaker struct {
	mu              sync.Mutex
	failures        uint
	state           CircuitState
	openedAt        time.Time
	failureThresh   uint
	openTimeout     time.Duration
	halfOpenMaxSucc uint
	halfOpenSucc    uint
}

// NewCircuitBreaker creates a CircuitBreaker with defaults.
func NewCircuitBreaker() *CircuitBreaker {
	return &CircuitBreaker{
		failureThresh:   5,
		openTimeout:     time.Second * 30,
		halfOpenMaxSucc: 2,
	}
}

// Allow returns whether a request should proceed.
func (cb *CircuitBreaker) Allow() bool {
	cb.mu.Lock()
	defer cb.mu.Unlock()

	switch cb.state {
	case Open:
		if time.Since(cb.openedAt) > cb.openTimeout {
			cb.state = HalfOpen
			cb.halfOpenSucc = 0
			return true
		}
		return false
	case HalfOpen:
		if cb.halfOpenSucc < cb.halfOpenMaxSucc {
			cb.halfOpenSucc++
			return true
		}
		cb.state = Open
		cb.openedAt = time.Now()
		return false
	default:
		return true
	}
}

// MarkSuccess resets failure counters on successful call.
func (cb *CircuitBreaker) MarkSuccess() {
	cb.mu.Lock()
	defer cb.mu.Unlock()
	cb.failures = 0
	if cb.state == HalfOpen {
		cb.state = Closed
	}
}

// MarkFailure increments failure count and potentially opens circuit.
func (cb *CircuitBreaker) MarkFailure() {
	cb.mu.Lock()
	defer cb.mu.Unlock()
	cb.failures++
	if cb.failures >= cb.failureThresh {
		cb.state = Open
		cb.openedAt = time.Now()
	}
}

// UnaryCircuitBreakerInterceptor returns an interceptor enforcing circuit breaking.
func UnaryCircuitBreakerInterceptor(cb *CircuitBreaker) grpc.UnaryClientInterceptor {
	if cb == nil {
		cb = NewCircuitBreaker()
	}
	return func(ctx context.Context, method string, req, reply interface{}, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, callOpts ...grpc.CallOption) error {
		if !cb.Allow() {
			return grpc.ErrClientConnClosing
		}
		err := invoker(ctx, method, req, reply, cc, callOpts...)
		if err != nil {
			cb.MarkFailure()
		} else {
			cb.MarkSuccess()
		}
		return err
	}
}
