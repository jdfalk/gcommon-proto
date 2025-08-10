// file: pkg/cache/providers/memory_test.go
// version: 1.0.0
// guid: d9d2a025-ce4e-495e-b42d-d946829a7497

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
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
