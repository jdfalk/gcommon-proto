// file: security/monitoring/integration_test.go
// version: 1.0.0
// guid: f1a2b3c4-d5e6-47f8-9a0b-1c2d3e4f5a6b

package monitoring

import (
	"testing"
	"time"
)

// TestSecurityMonitoringIntegration exercises recorder, detector, and dispatcher together.
func TestSecurityMonitoringIntegration(t *testing.T) {
	rec := NewRecorder()
	disp := NewDispatcher()
	det := NewDetector(map[string]int{"login": 2}, time.Minute)

	alertCh := make(chan Alert, 1)
	disp.Subscribe(alertCh)

	rec.Record("login", map[string]string{"user": "alice"})
	rec.Record("login", map[string]string{"user": "bob"})
	rec.Record("login", map[string]string{"user": "charlie"})

	anomalies := det.Detect(rec.List())
	for range anomalies {
		disp.Dispatch("anomaly detected", "critical")
	}

	select {
	case a := <-alertCh:
		if a.Severity != "critical" {
			t.Fatalf("unexpected severity: %s", a.Severity)
		}
	case <-time.After(time.Second):
		t.Fatalf("no alert received")
	}
}
