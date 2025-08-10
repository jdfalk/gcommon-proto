// file: pkg/cache/examples/basic_cache.go
// version: 1.0.0
// guid: a6b7c8d9-e0f1-42a3-b4c5-d6e7f8a9b0c1

//go:build ignore

package main

import (
	"context"
	"log"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
)

// Basic example of using the in-memory cache.
func main() {
	c := providers.NewMemoryCache(10, policies.NewLRU())
	ctx := context.Background()
	_ = c.Set(ctx, "foo", "bar", time.Minute)
	v, _ := c.Get(ctx, "foo")
	log.Printf("foo=%v", v)
}
