// file: monitoring/alerts/performance.go
// version: 1.1.0
// guid: b5cf4418-c058-4e06-9756-0b95cb0d01c3

package alerts

import (
	"context"
	"time"
)

// PerformanceAlert tracks latency measurements and fires when the percentile of
// interest exceeds a threshold. It uses a sliding window of recent values.
type PerformanceAlert struct {
	window    time.Duration
	threshold time.Duration
	values    []measurement
}

type measurement struct {
	ts    time.Time
	value time.Duration
}

// NewPerformanceAlert creates a new alert configured with the time window and
// latency threshold.
func NewPerformanceAlert(window time.Duration, threshold time.Duration) *PerformanceAlert {
	return &PerformanceAlert{window: window, threshold: threshold}
}

// Record adds a latency measurement.
func (a *PerformanceAlert) Record(value time.Duration) {
	a.values = append(a.values, measurement{ts: time.Now(), value: value})
}

// Evaluate returns true when the 95th percentile latency exceeds the threshold.
func (a *PerformanceAlert) Evaluate(now time.Time) bool {
	cutoff := now.Add(-a.window)
	idx := 0
	for i, m := range a.values {
		if m.ts.After(cutoff) {
			idx = i
			break
		}
	}
	a.values = a.values[idx:]
	if len(a.values) == 0 {
		return false
	}
	vals := make([]time.Duration, len(a.values))
	for i, m := range a.values {
		vals[i] = m.value
	}
	// Simple selection sort for deterministic percentile calculation.
	for i := 0; i < len(vals); i++ {
		for j := i + 1; j < len(vals); j++ {
			if vals[j] < vals[i] {
				vals[i], vals[j] = vals[j], vals[i]
			}
		}
	}
	p95 := vals[(95*len(vals))/100]
	return p95 > a.threshold
}

// Monitor evaluates the alert at the given interval and triggers the callback
// when the latency threshold is exceeded.
func (a *PerformanceAlert) Monitor(ctx context.Context, interval time.Duration, cb func(time.Duration)) {
	ticker := time.NewTicker(interval)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			return
		case t := <-ticker.C:
			if a.Evaluate(t) {
				vals := make([]time.Duration, len(a.values))
				for i, m := range a.values {
					vals[i] = m.value
				}
				cb(vals[(95*len(vals))/100])
			}
		}
	}
}
