// file: pkg/cache/providers/memcached.go
// version: 1.0.0
// guid: e1f2a3b4-c5d6-47e8-9f0a-b1c2d3e4f5a6

package providers

import (
	"context"
	"errors"
	"time"

	"github.com/bradfitz/gomemcache/memcache"
	"github.com/jdfalk/gcommon/pkg/cache/metrics"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
	gproto "google.golang.org/protobuf/proto"
)

// MemcachedCache implements Cache using a memcached backend.
//
// NOTE: This is a basic implementation and does not cover the entire
// memcached feature set. More advanced features should be added.
type MemcachedCache struct {
	client  *memcache.Client
	metrics *metrics.Collector
}

// NewMemcachedCache creates a new MemcachedCache. If client is nil, it will
// connect to a local memcached instance at 127.0.0.1:11211.
func NewMemcachedCache(client *memcache.Client) *MemcachedCache {
	if client == nil {
		client = memcache.New("127.0.0.1:11211")
	}
	return &MemcachedCache{client: client, metrics: &metrics.Collector{}}
}

// Get retrieves a value by key.
func (m *MemcachedCache) Get(ctx context.Context, key string) (any, error) {
	it, err := m.client.Get(key)
	if errors.Is(err, memcache.ErrCacheMiss) {
		m.metrics.Miss()
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	m.metrics.Hit()
	return it.Value, nil
}

// Set stores a value with optional TTL.
func (m *MemcachedCache) Set(ctx context.Context, key string, value any, ttl time.Duration) error {
	b, ok := value.([]byte)
	if !ok {
		return errors.New("memcached only supports byte values")
	}
	return m.client.Set(&memcache.Item{Key: key, Value: b, Expiration: int32(ttl.Seconds())})
}

// Delete removes a key.
func (m *MemcachedCache) Delete(ctx context.Context, key string) error {
	err := m.client.Delete(key)
	if errors.Is(err, memcache.ErrCacheMiss) {
		return nil
	}
	return err
}

// Exists checks if a key exists.
func (m *MemcachedCache) Exists(ctx context.Context, key string) (bool, error) {
	_, err := m.client.Get(key)
	if errors.Is(err, memcache.ErrCacheMiss) {
		m.metrics.Miss()
		return false, nil
	}
	if err != nil {
		return false, err
	}
	m.metrics.Hit()
	return true, nil
}

// Clear flushes all keys from memcached.
func (m *MemcachedCache) Clear(ctx context.Context) error {
	return m.client.FlushAll()
}

// GetStats returns cache statistics collected locally.
func (m *MemcachedCache) GetStats() *cachepb.CacheStats {
	stats := m.metrics.Stats()
	return cachepb.CacheStats_builder{CacheHits: gproto.Int64(stats.Hits), CacheMisses: gproto.Int64(stats.Misses)}.Build()
}

// GetMultiple retrieves multiple values by keys.
func (m *MemcachedCache) GetMultiple(ctx context.Context, keys []string) (map[string]any, error) {
	items, err := m.client.GetMulti(keys)
	if err != nil {
		return nil, err
	}
	res := make(map[string]any, len(items))
	for k, it := range items {
		res[k] = it.Value
		m.metrics.Hit()
	}
	// memcache library does not return missing keys, count misses
	m.metrics.Miss()
	return res, nil
}

// SetMultiple stores multiple key-value pairs.
func (m *MemcachedCache) SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error {
	for k, it := range items {
		if err := m.Set(ctx, k, it.Value, it.TTL); err != nil {
			return err
		}
	}
	return nil
}

// DeleteMultiple removes multiple keys.
func (m *MemcachedCache) DeleteMultiple(ctx context.Context, keys []string) error {
	for _, k := range keys {
		if err := m.Delete(ctx, k); err != nil {
			return err
		}
	}
	return nil
}

// Increment increments a counter and returns the new value.
func (m *MemcachedCache) Increment(ctx context.Context, key string, n int64) (int64, error) {
	val, err := m.client.Increment(key, uint64(n))
	if errors.Is(err, memcache.ErrCacheMiss) {
		// memcache can't auto-create on increment with expiration, so set initial
		if err := m.client.Set(&memcache.Item{Key: key, Value: []byte("0")}); err != nil {
			return 0, err
		}
		val, err = m.client.Increment(key, uint64(n))
	}
	return int64(val), err
}

// Decrement decrements a counter and returns the new value.
func (m *MemcachedCache) Decrement(ctx context.Context, key string, n int64) (int64, error) {
	val, err := m.client.Decrement(key, uint64(n))
	if errors.Is(err, memcache.ErrCacheMiss) {
		if err := m.client.Set(&memcache.Item{Key: key, Value: []byte("0")}); err != nil {
			return 0, err
		}
		val, err = m.client.Decrement(key, uint64(n))
	}
	return int64(val), err
}

// Keys returns an error as memcached does not support listing keys.
func (m *MemcachedCache) Keys(ctx context.Context, pattern string) ([]string, error) {
	return nil, errors.New("memcached: keys listing not supported")
}

// Flush flushes the cache.
func (m *MemcachedCache) Flush(ctx context.Context) error { return m.client.FlushAll() }

// TouchExpiration updates the TTL for a key.
func (m *MemcachedCache) TouchExpiration(ctx context.Context, key string, ttl time.Duration) error {
	return m.client.Touch(key, int32(ttl.Seconds()))
}
