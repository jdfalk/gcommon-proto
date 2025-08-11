// file: perf/benchmarks/config_bench.go
// version: 1.1.0
// guid: 311a5d69-2fc9-48e2-adeb-6490a46ab222

// Package benchmarks provides module benchmark stubs.
package benchmarks

import (
	"encoding/json"
	"sync"
	"testing"
)

// BenchmarkConfigRetrieval measures configuration retrieval performance.
func BenchmarkConfigRetrieval(b *testing.B) {
	cfg := map[string]string{"key": "value"}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = cfg["key"]
	}
}

// BenchmarkConfigParsing measures configuration parsing speed.
func BenchmarkConfigParsing(b *testing.B) {
	data := []byte(`{"name":"test","value":42}`)
	var out struct {
		Name  string
		Value int
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		if err := json.Unmarshal(data, &out); err != nil {
			b.Fatalf("parse: %v", err)
		}
	}
}

// BenchmarkConfigConcurrentAccess measures concurrent configuration access.
func BenchmarkConfigConcurrentAccess(b *testing.B) {
	cfg := map[string]int{"a": 1, "b": 2, "c": 3}
	var mu sync.RWMutex
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			mu.RLock()
			_ = cfg["a"]
			mu.RUnlock()
		}
	})
}

// BenchmarkConfigWatchingOverhead measures configuration watching overhead.
func BenchmarkConfigWatchingOverhead(b *testing.B) {
	ch := make(chan struct{}, 1)
	go func() {
		for range ch {
		}
	}()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		select {
		case ch <- struct{}{}:
		default:
		}
	}
	close(ch)
}
