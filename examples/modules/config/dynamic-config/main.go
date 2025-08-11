//go:build ignore

// file: examples/modules/config/dynamic-config/main.go
// version: 1.1.0
// guid: afadb93b-48ce-446c-82e2-e951a01f7ef2

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

// setup creates a watcher that reloads configuration when the underlying file
// changes. For simplicity this example uses a temporary file.
func setup(ctx context.Context) (*config.Watcher, error) {
	file := sources.FileSource{Path: "config.yaml"}
	loader := config.NewLoader(nil, config.ConfigSource(file))
	watcher := config.NewWatcher(loader, time.Second)
	return watcher, nil
}

// run starts the watcher and prints configuration updates until the context is
// canceled.
func run(ctx context.Context, watcher *config.Watcher) error {
	updates := watcher.Start(ctx)
	go func() {
		for cfg := range updates {
			fmt.Printf("updated config: %v\n", cfg)
		}
	}()
	<-ctx.Done()
	return watcher.Stop(context.Background())
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	watcher, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, watcher); err != nil {
		panic(err)
	}
}
