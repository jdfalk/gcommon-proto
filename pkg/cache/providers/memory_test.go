// file: pkg/cache/providers/memory_test.go
// version: 1.1.0
// guid: d9d2a025-ce4e-495e-b42d-d946829a7497

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
)

// TestMemoryCache_GetSet verifies basic get and set behavior.
func TestMemoryCache_GetSet(t *testing.T) {
	// Arrange
	cache := NewMemoryCache(0, policies.NewLRU())
	ctx := context.Background()

	// Act
	if err := cache.Set(ctx, "k", "v", time.Minute); err != nil {
		t.Fatalf("unexpected set error: %v", err)
	}
	val, err := cache.Get(ctx, "k")

	// Assert
	if err != nil {
		t.Fatalf("unexpected get error: %v", err)
	}
	if val != "v" {
		t.Fatalf("expected 'v', got %v", val)
	}
}

// TestMemoryCache_TTL ensures values expire after TTL.
func TestMemoryCache_TTL(t *testing.T) {
	// Arrange
	cache := NewMemoryCache(0, policies.NewLRU())
	ctx := context.Background()

	// Act
	if err := cache.Set(ctx, "k", "v", time.Millisecond); err != nil {
		t.Fatalf("set error: %v", err)
	}
	time.Sleep(2 * time.Millisecond)
	val, err := cache.Get(ctx, "k")

	// Assert
	if err != nil {
		t.Fatalf("get error: %v", err)
	}
	if val != nil {
		t.Fatalf("expected nil, got %v", val)
	}
}

// TestMemoryCache_LRUEviction verifies LRU eviction when capacity exceeded.
func TestMemoryCache_LRUEviction(t *testing.T) {
	cache := NewMemoryCache(1, policies.NewLRU())
	ctx := context.Background()
	if err := cache.Set(ctx, "a", 1, 0); err != nil {
		t.Fatalf("set error: %v", err)
	}
	if err := cache.Set(ctx, "b", 2, 0); err != nil {
		t.Fatalf("set error: %v", err)
	}
	if val, _ := cache.Get(ctx, "a"); val != nil {
		t.Fatalf("expected 'a' to be evicted, got %v", val)
	}
}

// TestMemoryCache_LFUEviction verifies LFU eviction logic.
func TestMemoryCache_LFUEviction(t *testing.T) {
	cache := NewMemoryCache(2, policies.NewLFU())
	ctx := context.Background()
	if err := cache.Set(ctx, "a", 1, 0); err != nil {
		t.Fatalf("set a: %v", err)
	}
	if err := cache.Set(ctx, "b", 2, 0); err != nil {
		t.Fatalf("set b: %v", err)
	}
	// Access 'a' to increase frequency.
	if _, err := cache.Get(ctx, "a"); err != nil {
		t.Fatalf("get a: %v", err)
	}
	// Adding 'c' should evict 'b'.
	if err := cache.Set(ctx, "c", 3, 0); err != nil {
		t.Fatalf("set c: %v", err)
	}
	if val, _ := cache.Get(ctx, "b"); val != nil {
		t.Fatalf("expected 'b' to be evicted, got %v", val)
	}
}

// TestMemoryCache_AdvancedOps verifies batch and counter operations.
func TestMemoryCache_AdvancedOps(t *testing.T) {
	cache := NewMemoryCache(0, policies.NewLRU())
	ctx := context.Background()

	// SetMultiple and GetMultiple
	items := map[string]cachetypes.CacheItem{
		"a": {Value: []byte("1"), TTL: 0},
		"b": {Value: []byte("2"), TTL: 0},
	}
	if err := cache.SetMultiple(ctx, items); err != nil {
		t.Fatalf("set multiple: %v", err)
	}
	vals, err := cache.GetMultiple(ctx, []string{"a", "b", "c"})
	if err != nil {
		t.Fatalf("get multiple: %v", err)
	}
	if len(vals) != 2 {
		t.Fatalf("expected 2 values, got %d", len(vals))
	}

	// Increment/Decrement
	if v, err := cache.Increment(ctx, "counter", 2); err != nil || v != 2 {
		t.Fatalf("increment: %v %d", err, v)
	}
	if v, err := cache.Decrement(ctx, "counter", 1); err != nil || v != 1 {
		t.Fatalf("decrement: %v %d", err, v)
	}

	// Keys
	keys, err := cache.Keys(ctx, "")
	if err != nil || len(keys) < 3 {
		t.Fatalf("keys: %v len=%d", err, len(keys))
	}

	// TouchExpiration
	if err := cache.TouchExpiration(ctx, "a", time.Millisecond); err != nil {
		t.Fatalf("touch: %v", err)
	}
	time.Sleep(2 * time.Millisecond)
	if v, _ := cache.Get(ctx, "a"); v != nil {
		t.Fatalf("expected 'a' expired")
	}

	// DeleteMultiple and Flush
	if err := cache.DeleteMultiple(ctx, []string{"b", "counter"}); err != nil {
		t.Fatalf("delete multiple: %v", err)
	}
	if err := cache.Flush(ctx); err != nil {
		t.Fatalf("flush: %v", err)
	}
	keys, _ = cache.Keys(ctx, "")
	if len(keys) != 0 {
		t.Fatalf("expected empty cache after flush")
	}
}
