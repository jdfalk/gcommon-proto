// file: pkg/cache/policies/ttl.go
// version: 1.0.0
// guid: 4d5e6f7a-8b9c-41d2-0e1f-2a3b4c5d6e7f

package policies

import "time"

// TTL implements a time-to-live eviction policy.
type TTL struct {
	expirations map[string]time.Time
}

// NewTTL creates a new TTL policy.
func NewTTL() *TTL {
	return &TTL{expirations: make(map[string]time.Time)}
}

// OnGet removes the key if expired.
func (t *TTL) OnGet(key string) {
	if exp, ok := t.expirations[key]; ok && time.Now().After(exp) {
		delete(t.expirations, key)
	}
}

// OnSet sets the expiration for the key using provided ttl.
func (t *TTL) OnSetWithTTL(key string, ttl time.Duration) {
	if ttl > 0 {
		t.expirations[key] = time.Now().Add(ttl)
	}
}

// OnSet satisfies Policy but requires a TTL, so it sets no expiration.
func (t *TTL) OnSet(key string) {}

// OnDelete removes the expiration tracking for the key.
func (t *TTL) OnDelete(key string) {
	delete(t.expirations, key)
}

// Evict returns an expired key if any.
func (t *TTL) Evict() string {
	now := time.Now()
	for k, exp := range t.expirations {
		if now.After(exp) {
			delete(t.expirations, k)
			return k
		}
	}
	return ""
}
