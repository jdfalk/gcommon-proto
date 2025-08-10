// file: pkg/cache/examples/distributed.go
// version: 1.0.0
// guid: b7c8d9e0-f1a2-43b4-c5d6-e7f8a9b0c1d2

//go:build ignore

package main

import (
	"context"
	"log"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
)

// Example demonstrating distributed cache usage.
func main() {
	n1 := providers.NewMemoryCache(10, policies.NewLRU())
	n2 := providers.NewMemoryCache(10, policies.NewLRU())
	dc := providers.NewDistributedCache([]providers.Node{n1, n2})
	ctx := context.Background()
	_ = dc.Set(ctx, "k", "v", time.Minute)
	v, _ := dc.Get(ctx, "k")
	log.Printf("k=%v", v)
}
