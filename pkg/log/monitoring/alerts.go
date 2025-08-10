// file: pkg/log/monitoring/alerts.go
// version: 1.0.0
// guid: f3a2b1c4-d5e6-4789-0f12-34567890abcd

package monitoring

import (
	"sync/atomic"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
)

// AlertManager triggers callbacks when error counts exceed thresholds.
type AlertManager struct {
	threshold int64
	interval  time.Duration
	counter   int64
	callback  func(int64)
}

// NewAlertManager creates an AlertManager.
func NewAlertManager(threshold int64, interval time.Duration, cb func(int64)) *AlertManager {
	am := &AlertManager{threshold: threshold, interval: interval, callback: cb}
	go am.run()
	return am
}

// Notify increments the error counter.
func (a *AlertManager) Notify(level log.Level) {
	if level >= log.ErrorLevel {
		atomic.AddInt64(&a.counter, 1)
	}
}

func (a *AlertManager) run() {
	ticker := time.NewTicker(a.interval)
	defer ticker.Stop()
	for range ticker.C {
		c := atomic.SwapInt64(&a.counter, 0)
		if c >= a.threshold {
			a.callback(c)
		}
	}
}
