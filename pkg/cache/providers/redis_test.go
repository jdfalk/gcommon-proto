// file: pkg/cache/providers/redis_test.go
// version: 1.1.0
// guid: e0f1a2b3-c4d5-46e7-8f9a-0b1c2d3e4f5a

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/alicebob/miniredis/v2"
	"github.com/go-redis/redis/v8"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
)

// TestRedisCache_GetSet verifies basic operations.
func TestRedisCache_GetSet(t *testing.T) {
	mr, err := miniredis.Run()
	if err != nil {
		t.Fatalf("miniredis: %v", err)
	}
	defer mr.Close()

	client := redis.NewClient(&redis.Options{Addr: mr.Addr()})
	cache := NewRedisCache(client)
	ctx := context.Background()

	if err := cache.Set(ctx, "k", "v", time.Minute); err != nil {
		t.Fatalf("set error: %v", err)
	}
	val, err := cache.Get(ctx, "k")
	if err != nil {
		t.Fatalf("get error: %v", err)
	}
	if val != "v" {
		t.Fatalf("expected 'v', got %v", val)
	}
}

// TestRedisCache_Batch verifies batch operations.
func TestRedisCache_Batch(t *testing.T) {
	mr, _ := miniredis.Run()
	defer mr.Close()
	client := redis.NewClient(&redis.Options{Addr: mr.Addr()})
	cache := NewRedisCache(client)
	ctx := context.Background()

	items := map[string]cachetypes.CacheItem{
		"a": {Value: "1", TTL: 0},
		"b": {Value: "2", TTL: 0},
	}
	if err := cache.SetMultiple(ctx, items); err != nil {
		t.Fatalf("set multiple: %v", err)
	}
	vals, err := cache.GetMultiple(ctx, []string{"a", "b"})
	if err != nil || len(vals) != 2 {
		t.Fatalf("get multiple failed")
	}
}
