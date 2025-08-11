// file: pkg/grpc/client/resilience_future_test.go
// version: 1.0.0
// guid: 7f4e9c2b-3a1d-4d5e-9c0b-1e2f3a4b5c6d

package client

import (
	"context"
	"errors"
	"sync/atomic"
	"testing"
	"time"
)

// TestTokenBucket verifies the basic rate limiting behaviour of the token bucket.
func TestTokenBucket(t *testing.T) {
	tb := NewTokenBucket(1, 1)
	if !tb.Allow() {
		t.Fatalf("first call should be allowed")
	}
	if tb.Allow() {
		t.Fatalf("second call should be rate limited")
	}
	time.Sleep(time.Second)
	if !tb.Allow() {
		t.Fatalf("token bucket should refill after interval")
	}
}

// TestBulkheadLimiter ensures the bulkhead limits concurrent operations.
func TestBulkheadLimiter(t *testing.T) {
	b := NewBulkheadLimiter(2)
	if !b.Allow() || !b.Allow() {
		t.Fatalf("initial acquisitions should succeed")
	}
	if b.Allow() {
		t.Fatalf("third acquisition should be blocked")
	}
	b.Done()
	if !b.Allow() {
		t.Fatalf("slot should be available after Done")
	}
}

// TestRunWithHedging validates that hedged calls are issued when the first
// attempt is slow and succeed when a subsequent attempt completes successfully.
func TestRunWithHedging(t *testing.T) {
	opts := ResilienceOptions{
		Hedge: HedgingPolicy{MaxHedges: 2, HedgeDelay: 10 * time.Millisecond},
		Retry: RetryOptions{MaxAttempts: 1},
	}
	var calls int32
	fn := func(ctx context.Context) error {
		n := atomic.AddInt32(&calls, 1)
		if n == 1 {
			time.Sleep(100 * time.Millisecond)
			return errors.New("slow")
		}
		return nil
	}
	if err := runWithHedging(context.Background(), fn, opts); err != nil {
		t.Fatalf("expected success from hedged call, got %v", err)
	}
	if atomic.LoadInt32(&calls) < 2 {
		t.Fatalf("expected hedged attempt to execute")
	}
}
