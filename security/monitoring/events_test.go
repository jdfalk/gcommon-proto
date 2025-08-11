// file: security/monitoring/events_test.go
// version: 1.0.0
// guid: 1d1f7b2e-7f5c-4e88-8d04-a91ccee4da8d

package monitoring

import "testing"

// TestRecorder verifies event recording and listing.
func TestRecorder(t *testing.T) {
	r := NewRecorder()
	r.Record("login", map[string]string{"user": "alice"})
	events := r.List()
	if len(events) != 1 || events[0].Name != "login" {
		t.Fatalf("unexpected events: %+v", events)
	}
	filtered := r.Filter(func(e Event) bool { return e.Metadata["user"] == "alice" })
	if len(filtered) != 1 {
		t.Fatalf("expected one filtered event")
	}
}
