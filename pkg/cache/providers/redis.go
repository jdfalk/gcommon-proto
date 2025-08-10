// file: pkg/cache/providers/redis.go
// version: 1.0.0
// guid: c2d3e4f5-a6b7-48c9-0d1e-2f3a4b5c6d7e

package providers

import (
	"context"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/cache/metrics"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	gproto "google.golang.org/protobuf/proto"
)

// RedisCache implements Cache using Redis.
type RedisCache struct {
	client  *redis.Client
	metrics *metrics.Collector
}

// NewRedisCache creates a new RedisCache. If client is nil, a default client is used.
func NewRedisCache(client *redis.Client) *RedisCache {
	if client == nil {
		client = redis.NewClient(&redis.Options{Addr: "localhost:6379"})
	}
	return &RedisCache{client: client, metrics: &metrics.Collector{}}
}

// Get retrieves a value by key.
func (r *RedisCache) Get(ctx context.Context, key string) (any, error) {
	val, err := r.client.Get(ctx, key).Result()
	if err == redis.Nil {
		r.metrics.Miss()
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	r.metrics.Hit()
	return val, nil
}

// Set stores a value with optional TTL.
func (r *RedisCache) Set(ctx context.Context, key string, value any, ttl time.Duration) error {
	return r.client.Set(ctx, key, value, ttl).Err()
}

// Delete removes a key.
func (r *RedisCache) Delete(ctx context.Context, key string) error {
	return r.client.Del(ctx, key).Err()
}

// Exists checks if a key exists.
func (r *RedisCache) Exists(ctx context.Context, key string) (bool, error) {
	n, err := r.client.Exists(ctx, key).Result()
	if err != nil {
		return false, err
	}
	if n == 0 {
		r.metrics.Miss()
	} else {
		r.metrics.Hit()
	}
	return n == 1, nil
}

// Clear removes all keys in the current database.
func (r *RedisCache) Clear(ctx context.Context) error {
	return r.client.FlushDB(ctx).Err()
}

// GetStats returns basic cache statistics.
func (r *RedisCache) GetStats() *cachepb.CacheStats {
	stats := r.metrics.Stats()
	return cachepb.CacheStats_builder{CacheHits: gproto.Int64(stats.Hits), CacheMisses: gproto.Int64(stats.Misses)}.Build()
}
