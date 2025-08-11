// file: examples/modules/config/file-config/main.go
// version: 1.1.0
// guid: 0d9d21f6-2818-47ce-84f7-40c736b13de2

package main

import (
        "context"
        "fmt"
        "time"

        "github.com/jdfalk/gcommon/pkg/config"
        "github.com/jdfalk/gcommon/pkg/config/sources"
)

// setup creates a loader that reads configuration from `config.yaml` and merges
// it with defaults.
func setup(ctx context.Context) (*config.Merger, error) {
        defaults := map[string]interface{}{"timeout": 5}
        file := sources.FileSource{Path: "config.yaml"}
        loader := config.NewLoader(nil, config.ConfigSource(file))
        cfg, err := loader.Load()
        if err != nil {
                return nil, err
        }
        merger := config.NewMerger(defaults, cfg)
        return merger, nil
}

// run prints the merged configuration demonstrating that file values override
// defaults.
func run(ctx context.Context, merger *config.Merger) error {
        fmt.Printf("merged: %v\n", merger.Merge())
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
