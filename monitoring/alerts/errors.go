// file: monitoring/alerts/errors.go
// version: 1.1.0
// guid: 1b9a6c7d-9e8f-4c1b-9a2e-7d0c3b71c4f2

package alerts

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// ErrorAlert monitors error rates within a specific window and triggers when the
// rate exceeds a configured threshold.
type ErrorAlert struct {
	mu        sync.Mutex
	window    time.Duration
	threshold float64
	errors    []time.Time
}

// NewErrorAlert creates an ErrorAlert with the provided time window and
// threshold. The threshold represents errors per second.
func NewErrorAlert(window time.Duration, threshold float64) *ErrorAlert {
	return &ErrorAlert{window: window, threshold: threshold}
}

// Record logs an occurrence of an error at the current time.
func (a *ErrorAlert) Record(now time.Time) {
	a.mu.Lock()
	defer a.mu.Unlock()
	a.errors = append(a.errors, now)
}

// Evaluate determines whether the error rate has exceeded the threshold.
func (a *ErrorAlert) Evaluate(now time.Time) bool {
	a.mu.Lock()
	defer a.mu.Unlock()
	cutoff := now.Add(-a.window)
	idx := 0
	for i, t := range a.errors {
		if t.After(cutoff) {
			idx = i
			break
		}
	}
	a.errors = a.errors[idx:]
	rate := float64(len(a.errors)) / a.window.Seconds()
	return rate > a.threshold
}

// Monitor runs Evaluate on the provided interval and invokes the callback when
// the alert is triggered. It stops when the context is cancelled.
func (a *ErrorAlert) Monitor(ctx context.Context, interval time.Duration, cb func(float64)) {
	ticker := time.NewTicker(interval)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			return
		case t := <-ticker.C:
			if a.Evaluate(t) {
				rate := float64(len(a.errors)) / a.window.Seconds()
				cb(rate)
			}
		}
	}
}

// Example demonstrates the error alert by injecting artificial errors and
// printing when the threshold is crossed.
func exampleErrorAlert() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	alert := NewErrorAlert(1*time.Minute, 0.5)
	go alert.Monitor(ctx, 5*time.Second, func(rate float64) {
		fmt.Printf("error rate too high: %.2f errors/s\n", rate)
	})

	for i := 0; i < 10; i++ {
		alert.Record(time.Now())
		time.Sleep(5 * time.Second)
	}
}
