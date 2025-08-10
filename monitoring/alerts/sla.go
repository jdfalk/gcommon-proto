// file: monitoring/alerts/sla.go
// version: 1.1.0
// guid: d50dfbb6-6cb1-4bf4-88d3-03bce8bcbe5b

package alerts

import (
	"context"
	"time"
)

// SLAAlert checks that a service maintains a minimum uptime percentage over a
// rolling window.
type SLAAlert struct {
	window    time.Duration
	minUptime float64
	events    []slaEvent
}

type slaEvent struct {
	ts time.Time
	up bool
}

// NewSLAAlert creates an SLA alert with the given window and minimum uptime
// percentage (0-100).
func NewSLAAlert(window time.Duration, minUptime float64) *SLAAlert {
	return &SLAAlert{window: window, minUptime: minUptime}
}

// Record notes whether the system was up or down at the given time.
func (a *SLAAlert) Record(ts time.Time, up bool) {
	a.events = append(a.events, slaEvent{ts: ts, up: up})
}

// Evaluate calculates the uptime percentage within the window and returns true
// if the uptime drops below the minimum.
func (a *SLAAlert) Evaluate(now time.Time) bool {
	cutoff := now.Add(-a.window)
	idx := 0
	for i, e := range a.events {
		if e.ts.After(cutoff) {
			idx = i
			break
		}
	}
	a.events = a.events[idx:]
	if len(a.events) == 0 {
		return false
	}
	upCount := 0
	for _, e := range a.events {
		if e.up {
			upCount++
		}
	}
	uptime := (float64(upCount) / float64(len(a.events))) * 100
	return uptime < a.minUptime
}

// Monitor periodically evaluates the SLA and triggers the callback if the
// uptime percentage falls below the minimum.
func (a *SLAAlert) Monitor(ctx context.Context, interval time.Duration, cb func(float64)) {
	ticker := time.NewTicker(interval)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			return
		case t := <-ticker.C:
			if a.Evaluate(t) {
				upCount := 0
				for _, e := range a.events {
					if e.up {
						upCount++
					}
				}
				uptime := (float64(upCount) / float64(len(a.events))) * 100
				cb(uptime)
			}
		}
	}
}
