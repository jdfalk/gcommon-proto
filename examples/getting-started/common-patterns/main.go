//go:build ignore

// file: examples/getting-started/common-patterns/main.go
// version: 1.1.0
// guid: 30361479-35e5-4d3f-b9a8-b990d37a2ae3

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/sources"
	"github.com/jdfalk/gcommon/pkg/metrics"
	prom "github.com/jdfalk/gcommon/pkg/metrics/prometheus"
	"github.com/jdfalk/gcommon/pkg/queue/providers"
)

// app encapsulates commonly used components that appear across many examples:
// configuration loading, metrics collection, and queue publishing.
type app struct {
	loader   *config.Loader
	metrics  metrics.Provider
	messages chan string
}

// setup wires together configuration, metrics, and a memory queue provider.
func setup(ctx context.Context) (*app, error) {
	// Load configuration from environment with APP_ prefix
	env := sources.EnvSource{Prefix: "APP_"}
	loader := config.NewLoader(nil, config.ConfigSource(env))

	// Metrics provider for instrumentation
	provider, err := prom.NewProvider(metrics.Config{})
	if err != nil {
		return nil, err
	}
	if err := provider.Start(ctx); err != nil {
		return nil, err
	}

	// Simple memory queue used for demonstration
	q := providers.NewMemoryQueue(5)
	ch := make(chan string, 1)
	go func() {
		for {
			msg, err := q.Consume(ctx)
			if err != nil {
				return
			}
			ch <- msg.Body
		}
	}()

	return &app{loader: loader, metrics: provider, messages: ch}, nil
}

// run publishes a message to the queue and prints the loaded configuration.
func run(ctx context.Context, a *app) error {
	cfg, err := a.loader.Load()
	if err != nil {
		return err
	}
	fmt.Printf("config: %v\n", cfg)

	counter := a.metrics.Counter("processed_messages_total")
	queue := providers.NewMemoryQueue(5)
	_ = queue.Publish(ctx, &providers.Message{Body: "hello"})
	select {
	case msg := <-a.messages:
		fmt.Println("received:", msg)
		counter.Inc()
	case <-time.After(time.Second):
		fmt.Println("no message received")
	}
	return nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	a, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, a); err != nil {
		panic(err)
	}
}
