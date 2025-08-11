// file: monitoring/alerts/combined_test.go
// version: 1.0.0
// guid: e7f9a1b2-c3d4-4e5f-a6b7-c8d9e0f1a2b3

package alerts

import (
	"context"
	"testing"
	"time"
)

// TestCombinedAlerts runs all alert types together to ensure no interference.
func TestCombinedAlerts(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	sla := NewSLAAlert(time.Minute, 100)
	errA := NewErrorAlert(time.Minute, 0)
	perf := NewPerformanceAlert(time.Minute, 0)

	sla.Record(time.Now(), false)
	errA.Record(time.Now())
	perf.Record(1 * time.Millisecond)

	slaFired := make(chan float64, 1)
	errFired := make(chan float64, 1)
	perfFired := make(chan time.Duration, 1)

	go sla.Monitor(ctx, 10*time.Millisecond, func(u float64) { slaFired <- u })
	go errA.Monitor(ctx, 10*time.Millisecond, func(r float64) { errFired <- r })
	go perf.Monitor(ctx, 10*time.Millisecond, func(d time.Duration) { perfFired <- d })

	timeout := time.After(time.Second)
	for i := 0; i < 3; i++ {
		select {
		case <-slaFired:
		case <-errFired:
		case <-perfFired:
		case <-timeout:
			t.Fatalf("timeout waiting for alerts")
		}
	}
}
