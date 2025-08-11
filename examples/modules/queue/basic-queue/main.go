// file: examples/modules/queue/basic-queue/main.go
// version: 1.1.0
// guid: f7b5c457-5a6f-418a-936d-ce03d61051eb

package main

import (
        "context"
        "fmt"
        "time"

        "github.com/jdfalk/gcommon/pkg/queue/providers"
)

// queueApp holds the in-memory queue used in this basic example.
type queueApp struct {
        q providers.Queue
}

// setup initializes a memory-backed queue with capacity for ten messages.
func setup(ctx context.Context) (*queueApp, error) {
        q := providers.NewMemoryQueue(10)
        return &queueApp{q: q}, nil
}

// run publishes and consumes a single message.
func run(ctx context.Context, app *queueApp) error {
        msg := &providers.Message{Body: "hello queue"}
        if err := app.q.Publish(ctx, msg); err != nil {
                return err
        }
        received, err := app.q.Consume(ctx)
        if err != nil {
                return err
        }
        fmt.Printf("received message: %s\n", received.Body)
        return nil
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
