// file: pkg/grpc/client/circuitbreaker_test.go
// version: 1.0.0
// guid: a5cc3d77-c598-42cd-ab2c-a793bcee6645

package client

import (
	"testing"
	"time"
)

// TestCircuitBreaker verifies basic state transitions.
func TestCircuitBreaker(t *testing.T) {
	cb := NewCircuitBreaker()
	cb.failureThresh = 2
	if !cb.Allow() {
		t.Fatalf("expected allow in closed state")
	}
	cb.MarkFailure()
	cb.MarkFailure()
	if cb.Allow() {
		t.Fatalf("expected block when open")
	}
	cb.openedAt = time.Now().Add(-time.Hour)
	if !cb.Allow() {
		t.Fatalf("expected allow in half-open after timeout")
	}
	cb.MarkSuccess()
	if !cb.Allow() {
		t.Fatalf("expected closed after success")
	}
}
