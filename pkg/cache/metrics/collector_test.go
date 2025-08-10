// file: pkg/cache/metrics/collector_test.go
// version: 1.0.0
// guid: e6f7a8b9-c0d1-42e3-f4a5-b6c7d8e9f0a1

package metrics

import "testing"

// TestCollector verifies hit/miss tracking.
func TestCollector(t *testing.T) {
	var c Collector
	c.Hit()
	c.Miss()
	s := c.Stats()
	if s.Hits != 1 || s.Misses != 1 {
		t.Fatalf("unexpected stats: %+v", s)
	}
}
