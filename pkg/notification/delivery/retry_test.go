// file: pkg/notification/delivery/retry_test.go
// version: 1.0.0
// guid: 1e2f3a4b-5c6d-7e8f-9012-3456789abcde

package delivery

import (
	"context"
	"errors"
	"testing"
	"time"
)

func TestRetrySuccess(t *testing.T) {
	attempts := 0
	err := Retry(context.Background(), 3, time.Millisecond, func() error {
		attempts++
		if attempts < 2 {
			return errors.New("fail")
		}
		return nil
	})
	if err != nil {
		t.Fatalf("Retry: %v", err)
	}
	if attempts != 2 {
		t.Fatalf("expected 2 attempts, got %d", attempts)
	}
}

func TestRetryContextCancel(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	if err := Retry(ctx, 3, time.Millisecond, func() error { return errors.New("x") }); err == nil {
		t.Fatalf("expected context error")
	}
}
