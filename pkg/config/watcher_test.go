// file: pkg/config/watcher_test.go
// version: 1.0.1
// guid: 77777777-8888-9999-aaaa-bbbbbbbbbbbb

package config

import (
	"context"
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

// TestWatcherWithProvider ensures callbacks are triggered with provider-based watcher
func TestWatcherWithProvider(t *testing.T) {
	// Create a mock provider for testing
	mockProvider := &mockProvider{data: make(map[string]interface{})}
	w := NewProviderWatcher(mockProvider)
	ch := make(chan string, 1)
	if err := w.Watch(context.Background(), "A", func(v interface{}) {
		if str, ok := v.(string); ok {
			ch <- str
		}
	}); err != nil {
		t.Fatalf("watch error: %v", err)
	}
	go func() {
		time.Sleep(10 * time.Millisecond)
		_ = mockProvider.Set("A", "1")
	}()
	select {
	case <-ch:
	case <-time.After(time.Millisecond * 100):
		t.Fatalf("callback not triggered")
	}
	_ = w.Close()
}

// mockProvider for testing
type mockProvider struct {
	data      map[string]interface{}
	callbacks map[string][]func(interface{})
	mu        sync.RWMutex
}

func (m *mockProvider) Get(key string) (interface{}, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	return m.data[key], nil
}

func (m *mockProvider) Set(key string, value interface{}) error {
	m.mu.Lock()
	m.data[key] = value
	callbacks := append([]func(interface{}){}, m.callbacks[key]...)
	m.mu.Unlock()

	for _, cb := range callbacks {
		cb(value)
	}
	return nil
}

func (m *mockProvider) Watch(key string, callback func(interface{})) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	if m.callbacks == nil {
		m.callbacks = make(map[string][]func(interface{}))
	}
	m.callbacks[key] = append(m.callbacks[key], callback)
	return nil
}

func (m *mockProvider) Close() error { return nil }

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
//  - Add tests for multiple watchers
//  - Add tests for unsubscribe functionality
