// file: pkg/grpc/server/monitoring_test.go
// version: 1.0.0
// guid: 6048c9ee-fb6e-4b5d-8c08-79cd13e341fa

package server

import (
	"testing"
)

// TestMonitorRecord verifies request and error counting.
func TestMonitorRecord(t *testing.T) {
	m := NewMonitor()
	m.Record(nil)
	m.Record(nil)
	m.Record(errExample{})
	req, errs, _ := m.Snapshot()
	if req != 3 || errs != 1 {
		t.Fatalf("unexpected stats: %d %d", req, errs)
	}
}

type errExample struct{}

func (errExample) Error() string { return "example" }
