// file: examples/getting-started/basic-setup/main.go
// version: 1.1.0
// guid: f47dcc6d-2d49-421d-bfce-b39ae5779d50

package main

import (
        "context"
        "fmt"
        "time"

        "github.com/jdfalk/gcommon/pkg/config"
        "github.com/jdfalk/gcommon/pkg/config/sources"
)

// setup creates a simple configuration loader that reads from a YAML file.
//
// The loader is returned so that run can demonstrate how to use it. In a real
// application additional sources (environment variables, command line flags,
// remote stores) would be provided.
func setup(ctx context.Context) (*config.Loader, error) {
        file := sources.FileSource{Path: "config.yaml"}
        loader := config.NewLoader(nil, config.ConfigSource(file))
        return loader, nil
}

// run loads the configuration and prints it to stdout. This function serves as
// the minimal "Hello World" style demonstration of using gcommon's config
// package.
func run(ctx context.Context, loader *config.Loader) error {
        cfg, err := loader.Load()
        if err != nil {
                return err
        }
        fmt.Printf("loaded config: %v\n", cfg)
        return nil
}

func main() {
        ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
        defer cancel()

        loader, err := setup(ctx)
        if err != nil {
                panic(err)
        }
        if err := run(ctx, loader); err != nil {
                panic(err)
        }
}
