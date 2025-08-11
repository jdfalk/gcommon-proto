// file: pkg/log/monitoring/metrics_test.go
// version: 1.0.0
// guid: 3e0f24c9-64f2-4f4b-93e1-b60e4f3a92b2

package monitoring

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/log"
	prom "github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/testutil"
)

// TestObserve increments the counter for log entries.
func TestObserve(t *testing.T) {
	prom.Unregister(logEntries)
	prom.MustRegister(logEntries)
	Observe(log.InfoLevel)
	if testutil.ToFloat64(logEntries.WithLabelValues(log.InfoLevel.String())) != 1 {
		t.Fatalf("counter not incremented")
	}
}
