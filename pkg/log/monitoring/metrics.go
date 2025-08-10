// file: pkg/log/monitoring/metrics.go
// version: 1.0.0
// guid: e1f2a3b4-c5d6-47e8-9f01-234567890abc

package monitoring

import (
	"github.com/jdfalk/gcommon/pkg/log"
	prom "github.com/prometheus/client_golang/prometheus"
)

var (
	logEntries = prom.NewCounterVec(prom.CounterOpts{
		Namespace: "gcommon",
		Subsystem: "log",
		Name:      "entries_total",
		Help:      "Number of log entries by level",
	}, []string{"level"})
)

func init() {
	prom.MustRegister(logEntries)
}

// Observe records a log entry for metrics tracking.
func Observe(level log.Level) {
	logEntries.WithLabelValues(level.String()).Inc()
}
