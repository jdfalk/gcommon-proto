// file: pkg/cache/policies/lru.go
// version: 1.0.0
// guid: 2b3c4d5e-6f7a-41b2-8c9d-0e1f2a3b4c5d

package policies

import "container/list"

// LRU implements a least recently used eviction policy.
type LRU struct {
	ll   *list.List
	keys map[string]*list.Element
}

// NewLRU creates a new LRU policy.
func NewLRU() *LRU {
	return &LRU{ll: list.New(), keys: make(map[string]*list.Element)}
}

// OnGet moves the accessed key to the front.
func (l *LRU) OnGet(key string) {
	if e, ok := l.keys[key]; ok {
		l.ll.MoveToFront(e)
	}
}

// OnSet inserts or updates the key position.
func (l *LRU) OnSet(key string) {
	if e, ok := l.keys[key]; ok {
		l.ll.MoveToFront(e)
		return
	}
	e := l.ll.PushFront(key)
	l.keys[key] = e
}

// OnDelete removes the key from tracking.
func (l *LRU) OnDelete(key string) {
	if e, ok := l.keys[key]; ok {
		l.ll.Remove(e)
		delete(l.keys, key)
	}
}

// Evict returns the least recently used key.
func (l *LRU) Evict() string {
	e := l.ll.Back()
	if e == nil {
		return ""
	}
	key := e.Value.(string)
	l.ll.Remove(e)
	delete(l.keys, key)
	return key
}
