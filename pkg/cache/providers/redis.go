// file: pkg/cache/providers/redis.go
// version: 1.1.0
// guid: c2d3e4f5-a6b7-48c9-0d1e-2f3a4b5c6d7e

package providers

import (
	"context"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/cache/metrics"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
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

// GetMultiple retrieves multiple values.
func (r *RedisCache) GetMultiple(ctx context.Context, keys []string) (map[string]any, error) {
	vals, err := r.client.MGet(ctx, keys...).Result()
	if err != nil {
		return nil, err
	}
	res := make(map[string]any)
	for i, v := range vals {
		if v != nil {
			res[keys[i]] = v
			r.metrics.Hit()
		} else {
			r.metrics.Miss()
		}
	}
	return res, nil
}

// SetMultiple sets multiple key-value pairs.
func (r *RedisCache) SetMultiple(ctx context.Context, items map[string]cachetypes.CacheItem) error {
	pipe := r.client.TxPipeline()
	for k, it := range items {
		pipe.Set(ctx, k, it.Value, it.TTL)
	}
	_, err := pipe.Exec(ctx)
	return err
}

// DeleteMultiple deletes multiple keys.
func (r *RedisCache) DeleteMultiple(ctx context.Context, keys []string) error {
	return r.client.Del(ctx, keys...).Err()
}

// Increment increments by n.
func (r *RedisCache) Increment(ctx context.Context, key string, n int64) (int64, error) {
	return r.client.IncrBy(ctx, key, n).Result()
}

// Decrement decrements by n.
func (r *RedisCache) Decrement(ctx context.Context, key string, n int64) (int64, error) {
	return r.client.DecrBy(ctx, key, n).Result()
}

// Keys lists keys matching pattern.
func (r *RedisCache) Keys(ctx context.Context, pattern string) ([]string, error) {
	return r.client.Keys(ctx, pattern).Result()
}

// Flush flushes database.
func (r *RedisCache) Flush(ctx context.Context) error {
	return r.client.FlushDB(ctx).Err()
}

// TouchExpiration updates TTL of key.
func (r *RedisCache) TouchExpiration(ctx context.Context, key string, ttl time.Duration) error {
	return r.client.Expire(ctx, key, ttl).Err()
}
