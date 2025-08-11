// file: pkg/cache/providers/memory.go
// version: 1.1.0
// guid: 3459121b-810a-4ab1-b49a-3475999d27f8

package providers

import (
	"context"
	"strings"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/metrics"
	"github.com/jdfalk/gcommon/pkg/cache/policies"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
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

// GetMultiple retrieves multiple values.
func (m *MemoryCache) GetMultiple(ctx context.Context, keys []string) (map[string]any, error) {
	result := make(map[string]any, len(keys))
	for _, k := range keys {
		v, _ := m.Get(ctx, k)
		if v != nil {
			result[k] = v
		}
	}
	return result, nil
}

// SetMultiple sets multiple key-value pairs.
func (m *MemoryCache) SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error {
	for k, it := range items {
		if err := m.Set(ctx, k, it.Value, it.TTL); err != nil {
			return err
		}
	}
	return nil
}

// DeleteMultiple removes multiple keys.
func (m *MemoryCache) DeleteMultiple(ctx context.Context, keys []string) error {
	for _, k := range keys {
		if err := m.Delete(ctx, k); err != nil {
			return err
		}
	}
	return nil
}

// Increment increments numeric value by n.
func (m *MemoryCache) Increment(ctx context.Context, key string, n int64) (int64, error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	it, ok := m.data[key]
	var val int64
	if ok {
		switch v := it.value.(type) {
		case int:
			val = int64(v)
		case int64:
			val = v
		case int32:
			val = int64(v)
		default:
			val = 0
		}
	}
	val += n
	it.value = val
	m.data[key] = it
	return val, nil
}

// Decrement decrements numeric value by n.
func (m *MemoryCache) Decrement(ctx context.Context, key string, n int64) (int64, error) {
	return m.Increment(ctx, key, -n)
}

// Keys returns all keys that match prefix pattern.
func (m *MemoryCache) Keys(ctx context.Context, pattern string) ([]string, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	keys := make([]string, 0, len(m.data))
	for k := range m.data {
		if pattern == "" || strings.HasPrefix(k, pattern) {
			keys = append(keys, k)
		}
	}
	return keys, nil
}

// Flush clears all entries.
func (m *MemoryCache) Flush(ctx context.Context) error { return m.Clear(ctx) }

// TouchExpiration updates TTL of key.
func (m *MemoryCache) TouchExpiration(ctx context.Context, key string, ttl time.Duration) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	it, ok := m.data[key]
	if !ok {
		return nil
	}
	if ttl > 0 {
		it.expires = time.Now().Add(ttl)
	} else {
		it.expires = time.Time{}
	}
	m.data[key] = it
	if t, ok := m.policy.(*policies.TTL); ok {
		t.OnSetWithTTL(key, ttl)
	}
	return nil
}
