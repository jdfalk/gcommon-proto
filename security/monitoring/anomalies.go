// file: security/monitoring/anomalies.go
// version: 1.1.0
// guid: 490c7f8f-9d88-47cd-b95d-060ca134d64f

package monitoring

import "time"

// Anomaly represents a detected unusual pattern.
type Anomaly struct {
	Event  Event  `json:"event"`
	Reason string `json:"reason"`
}

// Detector analyzes events and reports anomalies based on thresholds.
type Detector struct {
	Thresholds map[string]int
	Window     time.Duration
}

// NewDetector creates a detector with event thresholds and a time window.
func NewDetector(thresholds map[string]int, window time.Duration) *Detector {
	return &Detector{Thresholds: thresholds, Window: window}
}

// Detect inspects events and returns anomalies.
func (d *Detector) Detect(events []Event) []Anomaly {
	cutoff := time.Now().Add(-d.Window)
	counts := map[string]int{}
	result := []Anomaly{}
	for _, e := range events {
		if e.Timestamp.Before(cutoff) {
			continue
		}
		counts[e.Name]++
		if threshold, ok := d.Thresholds[e.Name]; ok && counts[e.Name] > threshold {
			result = append(result, Anomaly{Event: e, Reason: "threshold exceeded"})
		}
	}
	return result
}
