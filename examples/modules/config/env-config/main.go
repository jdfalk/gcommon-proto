// file: examples/modules/config/env-config/main.go
// version: 1.1.0
// guid: 162bfea1-d138-49f1-91b0-6132fe2e9e91

package main

import (
        "context"
        "fmt"
        "os"
        "time"

        "github.com/jdfalk/gcommon/pkg/config"
        "github.com/jdfalk/gcommon/pkg/config/sources"
)

// setup configures a loader that reads environment variables prefixed with
// `APP_`.
func setup(ctx context.Context) (*config.Loader, error) {
        env := sources.EnvSource{Prefix: "APP_"}
        loader := config.NewLoader(nil, config.ConfigSource(env))
        return loader, nil
}

// run demonstrates reading environment variables via the configuration loader.
func run(ctx context.Context, loader *config.Loader) error {
        _ = os.Setenv("APP_GREETING", "hello")
        cfg, err := loader.Load()
        if err != nil {
                return err
        }
        fmt.Printf("environment config: %v\n", cfg)
        return nil
}

func main() {
        ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
        defer cancel()
        loader, err := setup(ctx)
        if err != nil {
                panic(err)
        }
        if err := run(ctx, loader); err != nil {
                panic(err)
        }
}
