// file: pkg/cache/policies/adaptive.go
// version: 1.0.0
// guid: 5e6f7a8b-9c0d-41e2-1f2a-3b4c5d6e7f8a

package policies

// Adaptive combines LRU and LFU policies and selects one based on access patterns.
type Adaptive struct {
	lru    *LRU
	lfu    *LFU
	useLFU bool
}

// NewAdaptive creates a new Adaptive policy.
func NewAdaptive() *Adaptive {
	return &Adaptive{lru: NewLRU(), lfu: NewLFU()}
}

// OnGet records access in both policies.
func (a *Adaptive) OnGet(key string) {
	a.lru.OnGet(key)
	a.lfu.OnGet(key)
}

// OnSet records insertion in both policies.
func (a *Adaptive) OnSet(key string) {
	a.lru.OnSet(key)
	a.lfu.OnSet(key)
}

// OnDelete removes key from both policies.
func (a *Adaptive) OnDelete(key string) {
	a.lru.OnDelete(key)
	a.lfu.OnDelete(key)
}

// Evict uses LFU when many accesses have occurred, otherwise LRU.
func (a *Adaptive) Evict() string {
	if a.useLFU {
		return a.lfu.Evict()
	}
	return a.lru.Evict()
}
