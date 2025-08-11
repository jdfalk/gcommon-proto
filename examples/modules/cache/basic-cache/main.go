// file: examples/modules/cache/basic-cache/main.go
// version: 1.0.0
// guid: c64487d9-7a76-47f4-8f49-a022a1b21f4a

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
)

// cacheApp wraps the cache provider used in this example.
type cacheApp struct {
	cache *providers.MemoryCache
}

// setup initializes an in-memory cache with LRU eviction.
func setup(ctx context.Context) (*cacheApp, error) {
	return &cacheApp{cache: providers.NewMemoryCache(10, policies.NewLRU())}, nil
}

// run stores and retrieves a value to demonstrate basic cache operations.
func run(ctx context.Context, app *cacheApp) error {
	if err := app.cache.Set(ctx, "foo", "bar", time.Minute); err != nil {
		return err
	}
	val, err := app.cache.Get(ctx, "foo")
	if err != nil {
		return err
	}
	fmt.Printf("foo=%v\n", val)
	return nil
}

func main() {
	ctx := context.Background()
	app, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, app); err != nil {
		panic(err)
	}
}
