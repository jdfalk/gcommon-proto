// file: pkg/cache/interfaces.go
// version: 1.0.0
// guid: 234f51b5-07a9-40e0-a00e-b83139c62244

package cache

import (
	"context"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	"time"
)

// Cache defines the basic caching operations.
type Cache interface {
	Get(ctx context.Context, key string) (any, error)
	Set(ctx context.Context, key string, value any, ttl time.Duration) error
	Delete(ctx context.Context, key string) error
	Exists(ctx context.Context, key string) (bool, error)
	Clear(ctx context.Context) error
	GetStats() *cachepb.CacheStats
}

// DistributedCache extends Cache with distributed operations.
type DistributedCache interface {
	Cache
	InvalidatePattern(ctx context.Context, pattern string) error
	BulkGet(ctx context.Context, keys []string) (map[string]any, error)
	BulkSet(ctx context.Context, items map[string]CacheItem) error
}

// CacheItem represents a cache item for bulk operations.
type CacheItem struct {
	Value any
	TTL   time.Duration
}
