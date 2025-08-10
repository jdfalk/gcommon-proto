// file: pkg/cache/examples/performance.go
// version: 1.0.0
// guid: c8d9e0f1-a2b3-44c5-d6e7-f8a9b0c1d2e3

//go:build ignore

package main

import (
	"context"
	"log"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
)

// Simple performance check performing many writes and reads.
func main() {
	c := providers.NewMemoryCache(0, policies.NewLFU())
	ctx := context.Background()
	for i := 0; i < 1000; i++ {
		_ = c.Set(ctx, "k", i, time.Minute)
		_, _ = c.Get(ctx, "k")
	}
	stats := c.GetStats()
	log.Printf("hits=%d misses=%d", stats.GetCacheHits(), stats.GetCacheMisses())
}
