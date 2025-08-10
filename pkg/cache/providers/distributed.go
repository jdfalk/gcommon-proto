// file: pkg/cache/providers/distributed.go
// version: 1.0.0
// guid: d3e4f5a6-b7c8-49d0-1e2f-3a4b5c6d7e8f

package providers

import (
	"context"
	"time"

	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
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

// BulkGet retrieves multiple keys across nodes.
func (d *DistributedCache) BulkGet(ctx context.Context, keys []string) (map[string]any, error) {
	result := make(map[string]any)
	for _, key := range keys {
		v, err := d.Get(ctx, key)
		if err != nil {
			return nil, err
		}
		if v != nil {
			result[key] = v
		}
	}
	return result, nil
}

// BulkSet stores items on all nodes.
type CacheItem struct {
	Value any
	TTL   time.Duration
}

func (d *DistributedCache) BulkSet(ctx context.Context, items map[string]CacheItem) error {
	for k, it := range items {
		if err := d.Set(ctx, k, it.Value, it.TTL); err != nil {
			return err
		}
	}
	return nil
}
