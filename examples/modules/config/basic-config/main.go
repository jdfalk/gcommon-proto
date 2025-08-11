// file: examples/modules/config/basic-config/main.go
// version: 1.1.0
// guid: ed8e57b1-20b5-4cd1-b9a8-4d2f9b12ff5a

package main

import (
        "context"
        "fmt"
        "time"

        "github.com/jdfalk/gcommon/pkg/config"
)

// setup returns a configuration merger using default values embedded in code.
// Additional sources can be layered on top in more advanced examples.
func setup(ctx context.Context) (*config.Merger, error) {
        defaults := map[string]interface{}{
                "port": 8080,
                "env":  "development",
        }
        merger := config.NewMerger(defaults)
        return merger, nil
}

// run retrieves the final configuration map and prints it.
func run(ctx context.Context, merger *config.Merger) error {
        final := merger.Merge()
        fmt.Printf("final config: %v\n", final)
        return nil
}

func main() {
        ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
        defer cancel()
        merger, err := setup(ctx)
        if err != nil {
                panic(err)
        }
        if err := run(ctx, merger); err != nil {
                panic(err)
        }
}
