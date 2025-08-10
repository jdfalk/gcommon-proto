// file: pkg/config/watcher.go
// version: 1.0.0
// guid: 33333333-4444-5555-6666-777777777777

package config

import (
	"sync"
	"time"
)

// Watcher monitors configuration changes and notifies callbacks.
type Watcher struct {
	mu       sync.Mutex
	interval time.Duration
	stopCh   chan struct{}
	running  bool
}

// NewWatcher creates a watcher with polling interval.
func NewWatcher(interval time.Duration) *Watcher {
	return &Watcher{interval: interval, stopCh: make(chan struct{})}
}

// Start begins polling using provided function.
func (w *Watcher) Start(fetch func() (map[string]interface{}, error), apply func(map[string]interface{})) {
	w.mu.Lock()
	if w.running {
		w.mu.Unlock()
		return
	}
	w.running = true
	w.mu.Unlock()
	go func() {
		ticker := time.NewTicker(w.interval)
		defer ticker.Stop()
		for {
			select {
			case <-w.stopCh:
				return
			case <-ticker.C:
				cfg, err := fetch()
				if err == nil {
					apply(cfg)
				}
			}
		}
	}()
}

// Stop halts the watcher.
func (w *Watcher) Stop() {
	w.mu.Lock()
	if !w.running {
		w.mu.Unlock()
		return
	}
	w.running = false
	close(w.stopCh)
	w.stopCh = make(chan struct{})
	w.mu.Unlock()
}

// TODO:
//  - Support file system notifications using fsnotify
//  - Allow per-key watch subscriptions with fine-grained control
//  - Provide jitter to reduce thundering herd on updates
//  - Expose metrics for watch latency and error counts
//  - Implement backpressure to handle slow consumers
//  - Integrate with context for cancellation and deadlines
//  - Offer pluggable fetch strategies (pull, push, streaming)
//  - Add security checks for source authenticity
//  - Document strategies for rolling back failed updates
//  - Provide example for cluster-wide configuration propagation
//  - Support batching multiple updates into a single callback
//  - Enable filtering of unchanged configurations
//  - Handle panic recovery in apply callbacks
//  - Write unit tests covering concurrent start/stop scenarios
//  - Ensure idempotent application of configuration changes
//  - Investigate use of channels for event streaming
//  - Provide CLI for manually triggering reloads
//  - Allow dynamic adjustment of polling interval
//  - Support multiple fetch functions for segmented configs
//  - Explore integration with message queues for updates
