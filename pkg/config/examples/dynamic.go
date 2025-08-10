// file: pkg/config/examples/dynamic.go
// version: 1.0.0
// guid: 44444444-5555-6666-7777-dddddddddddd
//go:build ignore

package main

import (
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/config"
)

// This example illustrates dynamic configuration updates using the Watcher.
// A mock fetch function returns a map with an incrementing counter to simulate
// configuration changes. The watcher polls every 100 milliseconds and applies
// the updates, printing the new configuration each time.

func main() {
	counter := 0
	fetch := func() (map[string]interface{}, error) {
		counter++
		return map[string]interface{}{"counter": counter}, nil
	}
	apply := func(cfg map[string]interface{}) {
		fmt.Println("updated", cfg)
	}
	w := config.NewWatcher(100 * time.Millisecond)
	w.Start(fetch, apply)
	time.Sleep(350 * time.Millisecond)
	w.Stop()
}

// TODO:
//  - Replace mock fetch with real configuration source
//  - Demonstrate rollback when validation fails
//  - Show concurrent watchers for different modules
//  - Expose metrics for update frequency
//  - Handle network failures gracefully
//  - Add context cancellation example
//  - Integrate with command-line tool for manual trigger
//  - Provide unit tests covering race conditions
//  - Explore event-based update propagation
//  - Document best practices for safe dynamic reconfiguration
