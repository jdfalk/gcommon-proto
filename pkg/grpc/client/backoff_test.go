// file: pkg/grpc/client/backoff_test.go
// version: 1.0.0
// guid: 6623baec-92ad-4f61-9d4b-833295673eee

package client

import (
	"testing"
	"time"
)

// TestExponentialBackoff verifies delays increase exponentially.
func TestExponentialBackoff(t *testing.T) {
	b := NewExponentialBackoff()
	first := b.Next(0)
	second := b.Next(1)
	third := b.Next(2)
	if !(first < second && second < third) {
		t.Fatalf("expected increasing delays: %v %v %v", first, second, third)
	}
}

// TestConstantBackoff verifies constant delay is returned.
func TestConstantBackoff(t *testing.T) {
	c := ConstantBackoff{Delay: time.Second}
	if d := c.Next(10); d != time.Second {
		t.Fatalf("unexpected delay: %v", d)
	}
}
