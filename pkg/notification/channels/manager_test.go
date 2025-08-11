// file: pkg/notification/channels/manager_test.go
// version: 1.0.0
// guid: f1234567-89ab-cdef-0123-456789abcdef

package channels

import "testing"

func TestManagerEnableDisable(t *testing.T) {
	m := NewManager()
	m.Enable("email")
	if !m.IsEnabled("email") {
		t.Fatalf("expected email enabled")
	}
	m.Disable("email")
	if m.IsEnabled("email") {
		t.Fatalf("expected email disabled")
	}
}
