// file: pkg/cache/providers/distributed_test.go
// version: 1.0.0
// guid: f1a2b3c4-d5e6-47f8-9a0b-1c2d3e4f5a6b

package providers

import (
	"context"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
)

// TestDistributedCache_Basic verifies distributed get/set.
func TestDistributedCache_Basic(t *testing.T) {
	n1 := NewMemoryCache(0, policies.NewLRU())
	n2 := NewMemoryCache(0, policies.NewLRU())
	dc := NewDistributedCache([]Node{n1, n2})
	ctx := context.Background()
	if err := dc.Set(ctx, "k", "v", time.Minute); err != nil {
		t.Fatalf("set error: %v", err)
	}
	val, err := dc.Get(ctx, "k")
	if err != nil {
		t.Fatalf("get error: %v", err)
	}
	if val != "v" {
		t.Fatalf("expected 'v', got %v", val)
	}
}
