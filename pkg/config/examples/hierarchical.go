// file: pkg/config/examples/hierarchical.go
// version: 1.0.0
// guid: 33333333-4444-5555-6666-cccccccccccc
//go:build ignore

package main

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

// This example demonstrates hierarchical configuration loading with precedence.
// The default map provides baseline values, while file and environment sources
// override as needed. The example is simplified for illustration and does not
// handle errors or advanced scenarios. Real applications should include
// thorough error handling and validation steps.
//
// Configuration hierarchy (lowest to highest precedence):
//   1. Defaults embedded in code
//   2. Global configuration file
//   3. Environment variables
//   4. Command line arguments (not shown)
//   5. Runtime updates

func main() {
	defaults := map[string]interface{}{"port": 80}
	file := sources.FileSource{Path: "config.yaml"}
	env := sources.EnvSource{Prefix: "APP_"}

	loader := config.NewLoader(nil, config.ConfigSource(file), config.ConfigSource(env))
	cfg, _ := loader.Load()
	merger := config.NewMerger(defaults, cfg)
	final := merger.Merge()
	fmt.Println(final)
}

// TODO:
//  - Demonstrate merging module-specific configuration files
//  - Show how command-line flags override environment variables
//  - Include validation step ensuring required keys present
//  - Add example for dynamic overrides using Watcher
//  - Provide diagrams explaining configuration resolution order
//  - Document best practices for organizing configuration directories
//  - Include test verifying hierarchy precedence
//  - Explore using templates for generating configuration
//  - Add support for remote sources like Consul
//  - Highlight potential security pitfalls in configuration files
