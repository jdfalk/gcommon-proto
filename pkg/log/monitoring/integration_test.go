// file: pkg/log/monitoring/integration_test.go
// version: 1.0.0
// guid: a4b5c6d7-e8f9-40a1-b2c3-d4e5f6a7b8c9

package monitoring

import (
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
	prom "github.com/prometheus/client_golang/prometheus"
)

// TestLogMonitoringIntegration wires together metrics, alerts, and analysis.
func TestLogMonitoringIntegration(t *testing.T) {
	prom.Unregister(logEntries)
	prom.MustRegister(logEntries)

	fired := make(chan int64, 1)
	am := NewAlertManager(2, 10*time.Millisecond, func(c int64) { fired <- c })

	entries := []log.LogEntry{}
	for i := 0; i < 3; i++ {
		am.Notify(log.ErrorLevel)
		Observe(log.ErrorLevel)
		entries = append(entries, log.LogEntry{Level: log.ErrorLevel, Message: "err"})
	}

	analyzer := Analyzer{}
	counts := analyzer.CountByLevel(entries)
	if counts[log.ErrorLevel] != 3 {
		t.Fatalf("expected 3 error entries, got %d", counts[log.ErrorLevel])
	}
	select {
	case <-fired:
	case <-time.After(time.Second):
		t.Fatalf("alert manager did not fire")
	}
}
