//go:build ignore

// file: examples/modules/queue/worker-pool/main.go
// version: 1.1.0
// guid: 917ed822-710c-48b4-b1b0-309696429460

package main

import (
	"context"
	"fmt"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/queue/providers"
)

// poolApp demonstrates a simple worker pool consuming messages concurrently.
type poolApp struct {
	q providers.Queue
}

// setup creates a memory queue and publishes a few messages to be processed.
func setup(ctx context.Context) (*poolApp, error) {
	q := providers.NewMemoryQueue(100)
	for i := 0; i < 5; i++ {
		_ = q.Publish(ctx, &providers.Message{Body: fmt.Sprintf("job-%d", i)})
	}
	return &poolApp{q: q}, nil
}

// run starts a fixed number of workers that consume messages from the queue.
func run(ctx context.Context, app *poolApp) error {
	var wg sync.WaitGroup
	workers := 3
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			for {
				msg, err := app.q.Consume(ctx)
				if err != nil {
					return
				}
				fmt.Printf("worker %d processed %s\n", id, msg.Body)
			}
		}(i)
	}

	// Allow workers time to process then cancel
	time.Sleep(500 * time.Millisecond)
	cancelCtx, cancel := context.WithCancel(ctx)
	cancel()
	wg.Wait()
	return app.q.Close(cancelCtx)
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()
	app, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	if err := run(ctx, app); err != nil {
		panic(err)
	}
}
