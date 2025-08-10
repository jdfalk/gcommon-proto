// file: pkg/config/watcher_test.go
// version: 1.0.0
// guid: 77777777-8888-9999-aaaa-bbbbbbbbbbbb

package config

import (
	"sync"
	"testing"
	"time"
)

// TestWatcherStartStop ensures watcher applies fetched configuration.
func TestWatcherStartStop(t *testing.T) {
	w := NewWatcher(10 * time.Millisecond)
	var mu sync.Mutex
	applied := 0
	fetch := func() (map[string]interface{}, error) {
		return map[string]interface{}{"count": 1}, nil
	}
	apply := func(map[string]interface{}) {
		mu.Lock()
		applied++
		mu.Unlock()
	}
	w.Start(fetch, apply)
	time.Sleep(25 * time.Millisecond)
	w.Stop()
	mu.Lock()
	n := applied
	mu.Unlock()
	if n == 0 {
		t.Fatalf("watcher did not apply configuration")
	}
}

// TODO:
//  - Test multiple watchers running concurrently
//  - Verify stop behaviour when not started
//  - Add tests for error handling in fetch function
//  - Benchmark watcher overhead at different intervals
//  - Ensure watcher recovers from panics in apply
//  - Simulate long-running apply callbacks
//  - Add integration tests with Loader and Merger
//  - Validate thread-safety under heavy load
//  - Use context to cancel watcher in tests
//  - Document edge cases and race conditions
