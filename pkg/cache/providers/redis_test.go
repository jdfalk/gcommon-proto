// file: pkg/cache/providers/redis_test.go
// version: 1.0.0
// guid: e0f1a2b3-c4d5-46e7-8f9a-0b1c2d3e4f5a

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/alicebob/miniredis/v2"
	"github.com/go-redis/redis/v8"
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
