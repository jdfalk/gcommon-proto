// file: monitoring/alerts/sla_test.go
// version: 1.0.0
// guid: 7e6f5b47-9f39-4cfa-8a5d-06b8d1d89888

package alerts

import (
	"context"
	"testing"
	"time"
)

// TestSLAAlertEvaluate verifies uptime calculation.
func TestSLAAlertEvaluate(t *testing.T) {
	a := NewSLAAlert(time.Minute, 90)
	now := time.Now()
	for i := 0; i < 5; i++ {
		a.Record(now.Add(-time.Duration(i)*10*time.Second), true)
	}
	a.Record(now.Add(-15*time.Second), false)
	if !a.Evaluate(now) {
		t.Fatalf("expected SLA alert to trigger")
	}
}

// TestSLAAlertMonitor ensures callback is invoked when uptime drops.
func TestSLAAlertMonitor(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	a := NewSLAAlert(time.Minute, 100)
	a.Record(time.Now(), false)
	fired := make(chan float64, 1)
	go a.Monitor(ctx, 10*time.Millisecond, func(u float64) { fired <- u })
	select {
	case <-fired:
	case <-time.After(time.Second):
		t.Fatalf("monitor did not fire")
	}
}
