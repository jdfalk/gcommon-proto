// file: pkg/notification/channels/preferences_test.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-abcd-ef0123456789

package channels

import "testing"

func TestPreferencesSetGet(t *testing.T) {
	p := NewPreferences()
	p.Set("user1", []string{"email", "sms"})
	got := p.Get("user1")
	if len(got) != 2 || got[0] != "email" || got[1] != "sms" {
		t.Fatalf("unexpected prefs: %v", got)
	}
}
