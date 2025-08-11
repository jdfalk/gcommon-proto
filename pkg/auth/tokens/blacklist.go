// file: pkg/auth/tokens/blacklist.go
// version: 1.0.0
// guid: 1c2d3e4f-5a6b-7081-92a3-b4c5d6e7f8a9

// Package tokens provides JWT utilities for the auth module.
package tokens

import (
	"sync"
	"time"
)

// Blacklist stores revoked tokens until their expiration.
type Blacklist struct {
	mu      sync.RWMutex
	revoked map[string]time.Time
}

// NewBlacklist creates an empty token blacklist.
func NewBlacklist() *Blacklist {
	return &Blacklist{revoked: make(map[string]time.Time)}
}

// Revoke marks a token as revoked until the given expiration time.
func (b *Blacklist) Revoke(tokenID string, exp time.Time) {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.revoked[tokenID] = exp
}

// IsRevoked checks whether the token ID is currently revoked.
func (b *Blacklist) IsRevoked(tokenID string) bool {
	b.mu.RLock()
	exp, ok := b.revoked[tokenID]
	b.mu.RUnlock()
	if !ok {
		return false
	}
	if time.Now().After(exp) {
		b.mu.Lock()
		delete(b.revoked, tokenID)
		b.mu.Unlock()
		return false
	}
	return true
}

// Cleanup removes expired tokens from the blacklist.
func (b *Blacklist) Cleanup() {
	b.mu.Lock()
	for id, exp := range b.revoked {
		if time.Now().After(exp) {
			delete(b.revoked, id)
		}
	}
	b.mu.Unlock()
}
