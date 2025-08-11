// file: security/monitoring/alerts_test.go
// version: 1.0.0
// guid: 8a7e68d0-3b39-4c47-8fd3-5e0c2668e1aa

package monitoring

import (
	"testing"
	"time"
)

// TestDispatcherDispatch verifies subscribers receive alerts.
func TestDispatcherDispatch(t *testing.T) {
	d := NewDispatcher()
	ch := make(chan Alert, 1)
	d.Subscribe(ch)
	d.Dispatch("intrusion", "high")
	select {
	case a := <-ch:
		if a.Message != "intrusion" || a.Severity != "high" {
			t.Fatalf("unexpected alert: %+v", a)
		}
	case <-time.After(time.Second):
		t.Fatalf("timeout waiting for alert")
	}
}
