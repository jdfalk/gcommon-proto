//go:build ignore

// file: pkg/config/examples/production.go
// version: 1.0.0
// guid: 55555555-6666-7777-8888-eeeeeeeeeeee

package main

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

// This example sketches a production configuration setup using a YAML file and
// environment variables. In a real deployment, additional sources such as
// Consul or Vault would be added for secrets and dynamic configuration.

func main() {
	dec := formats.YAMLDecoder{}
	file := sources.FileSource{Path: "/etc/app/config.yaml", Decoder: dec}
	env := sources.EnvSource{Prefix: "APP_"}
	loader := config.NewLoader(dec, config.ConfigSource(file), config.ConfigSource(env))
	cfg, err := loader.Load()
	if err != nil {
		panic(err)
	}
	fmt.Println("loaded", cfg)
}

// TODO:
//  - Integrate ConsulSource and VaultSource for distributed configuration
//  - Add command-line flags for overriding critical settings
//  - Demonstrate merging multiple environment-specific files
//  - Show validation errors and graceful shutdown on failures
//  - Provide example for hot reloading using Watcher
//  - Document deployment steps for containerized environments
//  - Include metrics and tracing initialization based on config
//  - Securely handle secrets using dedicated secret sources
//  - Offer fallback to defaults when external systems unreachable
//  - Illustrate structured logging configuration
//  - Use context for loader and watcher operations
//  - Provide test suite verifying production setup
//  - Benchmark configuration load times on startup
//  - Explain configuration hierarchy with diagrams
//  - Support configuration diffing for troubleshooting
//  - Add health checks dependent on config values
//  - Implement graceful reload on SIGHUP
//  - Validate that required directories exist
//  - Document disaster recovery and backup strategies
//  - Include localization support for messages
