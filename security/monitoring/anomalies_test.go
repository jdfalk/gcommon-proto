// file: security/monitoring/anomalies_test.go
// version: 1.0.0
// guid: b2d9aef5-3c7e-40e4-8e5d-2a0b741d3c69

package monitoring

import (
	"testing"
	"time"
)

// TestDetectorDetect verifies anomaly detection based on thresholds.
func TestDetectorDetect(t *testing.T) {
	r := NewRecorder()
	r.Record("login", nil)
	r.Record("login", nil)
	det := NewDetector(map[string]int{"login": 1}, time.Minute)
	anomalies := det.Detect(r.List())
	if len(anomalies) != 1 {
		t.Fatalf("expected one anomaly, got %d", len(anomalies))
	}
}
