// file: pkg/cache/providers/memory.go
// version: 1.0.0
// guid: 3459121b-810a-4ab1-b49a-3475999d27f8

package providers

import (
	"context"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/metrics"
	"github.com/jdfalk/gcommon/pkg/cache/policies"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	gproto "google.golang.org/protobuf/proto"
)

type item struct {
	value   any
	expires time.Time
}

// MemoryCache is an in-memory cache implementation.
type MemoryCache struct {
	mu      sync.RWMutex
	data    map[string]item
	policy  policies.Policy
	metrics *metrics.Collector
	cap     int
}

// NewMemoryCache creates a new MemoryCache with optional capacity and policy.
func NewMemoryCache(capacity int, policy policies.Policy) *MemoryCache {
	return &MemoryCache{data: make(map[string]item), cap: capacity, policy: policy, metrics: &metrics.Collector{}}
}

// Get retrieves a value by key.
func (m *MemoryCache) Get(ctx context.Context, key string) (any, error) {
	m.mu.RLock()
	it, ok := m.data[key]
	m.mu.RUnlock()
	if !ok || (!it.expires.IsZero() && time.Now().After(it.expires)) {
		if m.metrics != nil {
			m.metrics.Miss()
		}
		if m.policy != nil {
			m.policy.OnGet(key)
		}
		return nil, nil
	}
	if m.metrics != nil {
		m.metrics.Hit()
	}
	if m.policy != nil {
		m.policy.OnGet(key)
	}
	return it.value, nil
}

// Set stores a value with optional TTL.
func (m *MemoryCache) Set(ctx context.Context, key string, value any, ttl time.Duration) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if m.cap > 0 && len(m.data) >= m.cap {
		if m.policy != nil {
			if evict := m.policy.Evict(); evict != "" {
				delete(m.data, evict)
			}
		}
	}
	var exp time.Time
	if ttl > 0 {
		exp = time.Now().Add(ttl)
		if t, ok := m.policy.(*policies.TTL); ok {
			t.OnSetWithTTL(key, ttl)
		}
	}
	m.data[key] = item{value: value, expires: exp}
	if m.policy != nil {
		m.policy.OnSet(key)
	}
	return nil
}

// Delete removes a key.
func (m *MemoryCache) Delete(ctx context.Context, key string) error {
	m.mu.Lock()
	delete(m.data, key)
	m.mu.Unlock()
	if m.policy != nil {
		m.policy.OnDelete(key)
	}
	return nil
}

// Exists checks if key exists and is not expired.
func (m *MemoryCache) Exists(ctx context.Context, key string) (bool, error) {
	m.mu.RLock()
	it, ok := m.data[key]
	m.mu.RUnlock()
	if !ok {
		if m.metrics != nil {
			m.metrics.Miss()
		}
		return false, nil
	}
	if !it.expires.IsZero() && time.Now().After(it.expires) {
		if m.metrics != nil {
			m.metrics.Miss()
		}
		return false, nil
	}
	if m.metrics != nil {
		m.metrics.Hit()
	}
	return true, nil
}

// Clear removes all keys.
func (m *MemoryCache) Clear(ctx context.Context) error {
	m.mu.Lock()
	m.data = make(map[string]item)
	m.mu.Unlock()
	return nil
}

// GetStats returns basic cache statistics.
func (m *MemoryCache) GetStats() *cachepb.CacheStats {
	total := int64(len(m.data))
	stats := m.metrics.Stats()
	return cachepb.CacheStats_builder{TotalItems: gproto.Int64(total), CacheHits: gproto.Int64(stats.Hits), CacheMisses: gproto.Int64(stats.Misses)}.Build()
}
