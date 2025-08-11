// file: test/integration/modules/cache_test.go
// version: 1.1.0
// guid: 328d387a-6e25-42e8-a4e9-b560e1f93c7c

package modules

import (
	"context"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	_ "github.com/jdfalk/gcommon/pkg/cache/proto"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestCacheModuleIntegration validates cache operations.
func TestCacheModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	cache := providers.NewMemoryCache(0, policies.NewLRU(10))
	ctx := context.Background()

	t.Run("set value", func(t *testing.T) {
		if err := cache.Set(ctx, "foo", "bar", 0); err != nil {
			t.Fatalf("set failed: %v", err)
		}
	})

	t.Run("get value", func(t *testing.T) {
		v, err := cache.Get(ctx, "foo")
		if err != nil || v != "bar" {
			t.Fatalf("expected bar got %v err %v", v, err)
		}
	})

	t.Run("delete value", func(t *testing.T) {
		if err := cache.Delete(ctx, "foo"); err != nil {
			t.Fatalf("delete failed: %v", err)
		}
		v, _ := cache.Get(ctx, "foo")
		if v != nil {
			t.Fatalf("expected nil after delete")
		}
	})

	t.Run("cache expiration", func(t *testing.T) {
		_ = cache.Set(ctx, "exp", "v", time.Millisecond)
		time.Sleep(2 * time.Millisecond)
		v, _ := cache.Get(ctx, "exp")
		if v != nil {
			t.Fatalf("expected expired value to be nil")
		}
	})

	t.Run("cache statistics", func(t *testing.T) {
		stats := cache.GetStats()
		if stats.GetTotalItems() < 0 {
			t.Fatalf("invalid stats")
		}
	})
}
