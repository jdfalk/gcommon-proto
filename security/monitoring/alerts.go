// file: security/monitoring/alerts.go
// version: 1.1.0
// guid: 2b8b7c1d-6fdd-4092-a95e-79dd1aaf4e86

package monitoring

import "time"

// Alert represents a notification that something needs attention.
type Alert struct {
	Message   string    `json:"message"`
	Severity  string    `json:"severity"`
	Timestamp time.Time `json:"timestamp"`
}

// Dispatcher notifies subscribers of alerts.
type Dispatcher struct {
	subs []chan Alert
}

// NewDispatcher creates a new alert dispatcher.
func NewDispatcher() *Dispatcher {
	return &Dispatcher{subs: []chan Alert{}}
}

// Subscribe registers a channel to receive alerts.
func (d *Dispatcher) Subscribe(ch chan Alert) {
	d.subs = append(d.subs, ch)
}

// Dispatch sends the alert to all subscribers.
func (d *Dispatcher) Dispatch(message, severity string) {
	alert := Alert{Message: message, Severity: severity, Timestamp: time.Now().UTC()}
	for _, ch := range d.subs {
		select {
		case ch <- alert:
		default:
			// drop alert if subscriber not ready
		}
	}
}
