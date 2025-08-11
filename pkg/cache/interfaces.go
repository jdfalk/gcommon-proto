// file: pkg/cache/interfaces.go
// version: 1.1.0
// guid: 234f51b5-07a9-40e0-a00e-b83139c62244

package cache

import (
	"context"
	"time"

	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
)

// Cache defines the basic caching operations.
type Cache interface {
	Get(ctx context.Context, key string) (any, error)
	Set(ctx context.Context, key string, value any, ttl time.Duration) error
	Delete(ctx context.Context, key string) error
	Exists(ctx context.Context, key string) (bool, error)
	Clear(ctx context.Context) error
	GetStats() *cachepb.CacheStats

	// GetMultiple retrieves multiple values by keys.
	GetMultiple(ctx context.Context, keys []string) (map[string]any, error)
	// SetMultiple stores multiple key-value pairs atomically.
	SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error
	// DeleteMultiple removes multiple keys atomically.
	DeleteMultiple(ctx context.Context, keys []string) error
	// Increment atomically increments a numeric value by n and returns the new value.
	Increment(ctx context.Context, key string, n int64) (int64, error)
	// Decrement atomically decrements a numeric value by n and returns the new value.
	Decrement(ctx context.Context, key string, n int64) (int64, error)
	// Keys lists all keys matching the pattern.
	Keys(ctx context.Context, pattern string) ([]string, error)
	// Flush persists or clears cache depending on backend.
	Flush(ctx context.Context) error
	// TouchExpiration updates the TTL for the given key.
	TouchExpiration(ctx context.Context, key string, ttl time.Duration) error
}

// DistributedCache extends Cache with distributed operations.
type DistributedCache interface {
	Cache
	InvalidatePattern(ctx context.Context, pattern string) error
}
