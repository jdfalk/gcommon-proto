// file: pkg/notification/channels/preferences.go
// version: 1.0.0
// guid: eeeeeeee-ffff-0000-1111-222222222222

package channels

import "sync"

// Preferences stores user notification channel preferences.
type Preferences struct {
	mu    sync.RWMutex
	prefs map[string][]string
}

// NewPreferences creates a Preferences store.
func NewPreferences() *Preferences {
	return &Preferences{prefs: make(map[string][]string)}
}

// Set sets preferred channels for a user.
func (p *Preferences) Set(user string, channels []string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.prefs[user] = channels
}

// Get retrieves preferred channels for a user.
func (p *Preferences) Get(user string) []string {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return p.prefs[user]
}
