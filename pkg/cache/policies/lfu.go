// file: pkg/cache/policies/lfu.go
// version: 1.0.0
// guid: 3c4d5e6f-7a8b-41c2-9d0e-1f2a3b4c5d6e

package policies

// LFU implements a least frequently used eviction policy.
type LFU struct {
	counts map[string]int
}

// NewLFU creates a new LFU policy.
func NewLFU() *LFU {
	return &LFU{counts: make(map[string]int)}
}

// OnGet increments the access count for the key.
func (l *LFU) OnGet(key string) {
	l.counts[key]++
}

// OnSet initializes the count for the key.
func (l *LFU) OnSet(key string) {
	l.counts[key] = 1
}

// OnDelete removes tracking for the key.
func (l *LFU) OnDelete(key string) {
	delete(l.counts, key)
}

// Evict returns the least frequently used key.
func (l *LFU) Evict() string {
	var minKey string
	minCount := int(^uint(0) >> 1)
	for k, c := range l.counts {
		if c < minCount {
			minCount = c
			minKey = k
		}
	}
	if minKey != "" {
		delete(l.counts, minKey)
	}
	return minKey
}
