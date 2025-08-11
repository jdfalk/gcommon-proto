// file: monitoring/alerts/errors_test.go
// version: 1.0.0
// guid: 3f4d6e21-bfd3-44a8-9e5c-93ec5af1fce3

package alerts

import (
	"context"
	"testing"
	"time"
)

// TestErrorAlertEvaluate verifies error rate calculation.
func TestErrorAlertEvaluate(t *testing.T) {
	a := NewErrorAlert(time.Minute, 0.1)
	now := time.Now()
	for i := 0; i < 10; i++ {
		a.Record(now)
	}
	if !a.Evaluate(now) {
		t.Fatalf("expected alert to trigger")
	}
}

// TestErrorAlertMonitor ensures callback fires when threshold exceeded.
func TestErrorAlertMonitor(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	a := NewErrorAlert(time.Minute, 0)
	a.Record(time.Now())
	fired := make(chan float64, 1)
	go a.Monitor(ctx, 10*time.Millisecond, func(r float64) { fired <- r })
	select {
	case <-fired:
	case <-time.After(time.Second):
		t.Fatalf("monitor did not fire")
	}
}
