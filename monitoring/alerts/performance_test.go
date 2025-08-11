// file: monitoring/alerts/performance_test.go
// version: 1.0.0
// guid: 6a1d842c-3e55-4efb-9f76-c1ee1bb4b3e4

package alerts

import (
	"context"
	"testing"
	"time"
)

// TestPerformanceAlertEvaluate verifies percentile logic.
func TestPerformanceAlertEvaluate(t *testing.T) {
	a := NewPerformanceAlert(time.Minute, 50*time.Millisecond)
	now := time.Now()
	for i := 0; i < 100; i++ {
		a.Record(time.Duration(i) * time.Millisecond)
	}
	if !a.Evaluate(now) {
		t.Fatalf("expected alert to trigger")
	}
}

// TestPerformanceAlertMonitor ensures callback triggers when latency too high.
func TestPerformanceAlertMonitor(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	a := NewPerformanceAlert(time.Minute, 0)
	a.Record(10 * time.Millisecond)
	fired := make(chan time.Duration, 1)
	go a.Monitor(ctx, 10*time.Millisecond, func(d time.Duration) { fired <- d })
	select {
	case <-fired:
	case <-time.After(time.Second):
		t.Fatalf("monitor did not fire")
	}
}
