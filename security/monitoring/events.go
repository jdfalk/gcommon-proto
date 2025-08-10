// file: security/monitoring/events.go
// version: 1.1.0
// guid: 9beb19f6-dceb-47fe-b4a3-8c17a8755503

package monitoring

import (
	"sync"
	"time"
)

// Event represents a security relevant action in the system.
type Event struct {
	Name      string            `json:"name"`
	Timestamp time.Time         `json:"timestamp"`
	Metadata  map[string]string `json:"metadata"`
}

// Recorder stores events in memory and allows queries.
type Recorder struct {
	mu     sync.RWMutex
	events []Event
}

// NewRecorder creates an empty event recorder.
func NewRecorder() *Recorder {
	return &Recorder{events: []Event{}}
}

// Record logs a new event with optional metadata.
func (r *Recorder) Record(name string, metadata map[string]string) {
	r.mu.Lock()
	defer r.mu.Unlock()
	if metadata == nil {
		metadata = map[string]string{}
	}
	r.events = append(r.events, Event{Name: name, Timestamp: time.Now().UTC(), Metadata: metadata})
}

// List returns a copy of all recorded events.
func (r *Recorder) List() []Event {
	r.mu.RLock()
	defer r.mu.RUnlock()
	out := make([]Event, len(r.events))
	copy(out, r.events)
	return out
}

// Filter returns events that satisfy the predicate.
func (r *Recorder) Filter(pred func(Event) bool) []Event {
	r.mu.RLock()
	defer r.mu.RUnlock()
	result := []Event{}
	for _, e := range r.events {
		if pred(e) {
			result = append(result, e)
		}
	}
	return result
}
