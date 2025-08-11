// file: pkg/cache/providers/distributed.go
// version: 1.1.0
// guid: d3e4f5a6-b7c8-49d0-1e2f-3a4b5c6d7e8f

package providers

import (
	"context"
	"time"

	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
	gproto "google.golang.org/protobuf/proto"
)

// Node represents a cache node that participates in the distributed cache.
type Node interface {
	Get(ctx context.Context, key string) (any, error)
	Set(ctx context.Context, key string, value any, ttl time.Duration) error
	Delete(ctx context.Context, key string) error
	Exists(ctx context.Context, key string) (bool, error)
	Clear(ctx context.Context) error
	GetStats() *cachepb.CacheStats
	GetMultiple(ctx context.Context, keys []string) (map[string]any, error)
	SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error
	DeleteMultiple(ctx context.Context, keys []string) error
	Increment(ctx context.Context, key string, n int64) (int64, error)
	Decrement(ctx context.Context, key string, n int64) (int64, error)
	Keys(ctx context.Context, pattern string) ([]string, error)
	Flush(ctx context.Context) error
	TouchExpiration(ctx context.Context, key string, ttl time.Duration) error
}

// DistributedCache coordinates multiple cache nodes.
type DistributedCache struct {
	nodes []Node
}

// NewDistributedCache creates a distributed cache over the given nodes.
func NewDistributedCache(nodes []Node) *DistributedCache {
	return &DistributedCache{nodes: nodes}
}

// Get tries to retrieve a value from the first node that has it.
func (d *DistributedCache) Get(ctx context.Context, key string) (any, error) {
	for _, n := range d.nodes {
		v, err := n.Get(ctx, key)
		if err != nil {
			return nil, err
		}
		if v != nil {
			return v, nil
		}
	}
	return nil, nil
}

// Set stores the value in all nodes.
func (d *DistributedCache) Set(ctx context.Context, key string, value any, ttl time.Duration) error {
	for _, n := range d.nodes {
		if err := n.Set(ctx, key, value, ttl); err != nil {
			return err
		}
	}
	return nil
}

// Delete removes the key from all nodes.
func (d *DistributedCache) Delete(ctx context.Context, key string) error {
	for _, n := range d.nodes {
		if err := n.Delete(ctx, key); err != nil {
			return err
		}
	}
	return nil
}

// Exists checks if the key exists in any node.
func (d *DistributedCache) Exists(ctx context.Context, key string) (bool, error) {
	for _, n := range d.nodes {
		ok, err := n.Exists(ctx, key)
		if err != nil {
			return false, err
		}
		if ok {
			return true, nil
		}
	}
	return false, nil
}

// Clear clears all nodes.
func (d *DistributedCache) Clear(ctx context.Context) error {
	for _, n := range d.nodes {
		if err := n.Clear(ctx); err != nil {
			return err
		}
	}
	return nil
}

// GetStats aggregates stats from all nodes.
func (d *DistributedCache) GetStats() *cachepb.CacheStats {
	var total, hits, misses int64
	for _, n := range d.nodes {
		s := n.GetStats()
		total += s.GetTotalItems()
		hits += s.GetCacheHits()
		misses += s.GetCacheMisses()
	}
	return cachepb.CacheStats_builder{TotalItems: gproto.Int64(total), CacheHits: gproto.Int64(hits), CacheMisses: gproto.Int64(misses)}.Build()
}

// InvalidatePattern is a no-op for simple distributed cache.
func (d *DistributedCache) InvalidatePattern(ctx context.Context, pattern string) error {
	return nil
}

// GetMultiple retrieves keys from first node containing them.
func (d *DistributedCache) GetMultiple(ctx context.Context, keys []string) (map[string]any, error) {
	result := make(map[string]any)
	for _, k := range keys {
		v, err := d.Get(ctx, k)
		if err != nil {
			return nil, err
		}
		if v != nil {
			result[k] = v
		}
	}
	return result, nil
}

// SetMultiple stores items on all nodes.
func (d *DistributedCache) SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error {
	for k, it := range items {
		if err := d.Set(ctx, k, it.Value, it.TTL); err != nil {
			return err
		}
	}
	return nil
}

// DeleteMultiple removes keys from all nodes.
func (d *DistributedCache) DeleteMultiple(ctx context.Context, keys []string) error {
	for _, k := range keys {
		if err := d.Delete(ctx, k); err != nil {
			return err
		}
	}
	return nil
}

// Increment increments across nodes; uses first node.
func (d *DistributedCache) Increment(ctx context.Context, key string, n int64) (int64, error) {
	if len(d.nodes) == 0 {
		return 0, nil
	}
	return d.nodes[0].Increment(ctx, key, n)
}

// Decrement decrements across nodes; uses first node.
func (d *DistributedCache) Decrement(ctx context.Context, key string, n int64) (int64, error) {
	if len(d.nodes) == 0 {
		return 0, nil
	}
	return d.nodes[0].Decrement(ctx, key, n)
}

// Keys aggregates keys from all nodes.
func (d *DistributedCache) Keys(ctx context.Context, pattern string) ([]string, error) {
	var keys []string
	for _, n := range d.nodes {
		ks, err := n.Keys(ctx, pattern)
		if err != nil {
			return nil, err
		}
		keys = append(keys, ks...)
	}
	return keys, nil
}

// Flush flushes all nodes.
func (d *DistributedCache) Flush(ctx context.Context) error {
	for _, n := range d.nodes {
		if err := n.Flush(ctx); err != nil {
			return err
		}
	}
	return nil
}

// TouchExpiration updates TTL on all nodes.
func (d *DistributedCache) TouchExpiration(ctx context.Context, key string, ttl time.Duration) error {
	for _, n := range d.nodes {
		if err := n.TouchExpiration(ctx, key, ttl); err != nil {
			return err
		}
	}
	return nil
}
