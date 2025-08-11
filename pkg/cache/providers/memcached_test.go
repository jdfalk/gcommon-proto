// file: pkg/cache/providers/memcached_test.go
// version: 1.0.0
// guid: f2a3b4c5-d6e7-48f9-0a1b-2c3d4e5f6a7b

package providers

import (
	"context"
	"os/exec"
	"testing"
	"time"

	"github.com/bradfitz/gomemcache/memcache"
)

// TestMemcachedCache_GetSet verifies basic operations with a real memcached server.
func TestMemcachedCache_GetSet(t *testing.T) {
	cmd := exec.Command("memcached", "-p", "11212")
	if err := cmd.Start(); err != nil {
		t.Skip("memcached not installed")
	}
	defer cmd.Process.Kill()
	time.Sleep(500 * time.Millisecond)

	client := memcache.New("127.0.0.1:11212")
	cache := NewMemcachedCache(client)
	ctx := context.Background()

	if err := cache.Set(ctx, "k", []byte("v"), time.Minute); err != nil {
		t.Skipf("memcached not available: %v", err)
	}
	val, err := cache.Get(ctx, "k")
	if err != nil {
		t.Fatalf("get: %v", err)
	}
	if string(val.([]byte)) != "v" {
		t.Fatalf("expected v got %v", val)
	}
}
