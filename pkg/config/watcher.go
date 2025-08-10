// file: pkg/config/watcher.go
// version: 1.1.0
// guid: 33333333-4444-5555-6666-777777777777

package config

import (
	"context"
	"sync"
	"time"
)

// Watcher monitors configuration changes and notifies callbacks.
// Supports both polling-based and provider-based watching.
type Watcher struct {
	mu       sync.RWMutex
	interval time.Duration
	stopCh   chan struct{}
	running  bool
	watches  map[string][]func(interface{})
	provider Provider
}

// NewWatcher creates a polling-based watcher with specified interval.
func NewWatcher(interval time.Duration) *Watcher {
	return &Watcher{interval: interval, stopCh: make(chan struct{})}
}

// NewProviderWatcher creates a provider-based watcher.
func NewProviderWatcher(p Provider) *Watcher {
	return &Watcher{provider: p, watches: make(map[string][]func(interface{}))}
}

// Start begins polling using provided fetch and apply functions.
// Only works for polling-based watchers created with NewWatcher.
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

// Stop halts the polling watcher.
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

// Watch registers a callback for a key with provider-based watcher.
// Only works for provider-based watchers created with NewProviderWatcher.
func (w *Watcher) Watch(ctx context.Context, key string, cb func(interface{})) error {
	if w.provider == nil {
		return ErrProviderNotFound
	}
	w.mu.Lock()
	w.watches[key] = append(w.watches[key], cb)
	w.mu.Unlock()
	return w.provider.Watch(key, func(v interface{}) {
		for _, f := range w.copyCallbacks(key) {
			f(v)
		}
	})
}

func (w *Watcher) copyCallbacks(key string) []func(interface{}) {
	w.mu.RLock()
	cbs := append([]func(interface{}){}, w.watches[key]...)
	w.mu.RUnlock()
	return cbs
}

// Close stops the watcher and cleans up resources.
func (w *Watcher) Close() error {
	if w.provider != nil {
		w.mu.Lock()
		w.watches = make(map[string][]func(interface{}))
		w.mu.Unlock()
		return w.provider.Close()
	}
	w.Stop()
	return nil
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
//  - Implement efficient subscription handling
//  - Support wildcard subscriptions
//  - Add backoff strategies for reconnecting
//  - Provide metrics for watcher events
//  - Integrate with notification module
//  - Add persistent queue for missed events
//  - Provide examples for watcher usage
//  - Support external event sources
//  - Document thread safety guarantees
//  - Add ability to pause/resume watchers
//  - Provide cleanup of stale subscriptions
//  - Use generics for typed callbacks when available
//  - Include tracing information
//  - Provide automatic reconnection for network providers
//  - Add tests covering concurrent watchers
//  - Ensure graceful shutdown
//  - Provide health checks for watcher subsystem
//  - Add configuration for watcher buffer sizes
//  - Document latency expectations
//  - Provide benchmarking tools
//  - Support filtering events by type
//  - Add access control for watch operations
//  - Implement watchers for remote providers
//  - Provide event replay capabilities
//  - Support batched change notifications
//  - Include event deduplication
//  - Add debug logging
//  - Provide alerting hooks
//  - Ensure watchers survive provider restarts
//  - Add documentation for extending watcher functionality
//  - Evaluate using channels vs callback approach
//  - Provide context propagation
//  - Add sample implementations in examples
//  - Add support for patterns in Watch method
//  - Return cancellation function from Watch
//  - Handle provider watch errors properly
//  - Ensure provider watchers are cleaned up on Close
//  - Notify subscribers of closure
