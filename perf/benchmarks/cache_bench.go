// file: perf/benchmarks/cache_bench.go
// version: 1.1.0
// guid: dbd85aa4-ce87-4d30-9b6f-4881edd6cb12

package benchmarks

import (
	"sync"
	"testing"
)

// BenchmarkCacheLatency measures cache hit/miss latency.
func BenchmarkCacheLatency(b *testing.B) {
	cache := map[string]string{"a": "1"}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = cache["a"]
	}
}

// BenchmarkCacheThroughput measures cache throughput.
func BenchmarkCacheThroughput(b *testing.B) {
	cache := make(map[int]int)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		cache[i] = i
		_ = cache[i]
	}
}

// BenchmarkCacheEviction measures eviction policy performance.
func BenchmarkCacheEviction(b *testing.B) {
	cache := make(map[int]int)
	capacity := 1024
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		cache[i] = i
		if len(cache) > capacity {
			for k := range cache {
				delete(cache, k)
				break
			}
		}
	}
}

// BenchmarkConcurrentCacheAccess measures concurrent cache access.
func BenchmarkConcurrentCacheAccess(b *testing.B) {
	cache := make(map[int]int)
	var mu sync.RWMutex
	b.RunParallel(func(pb *testing.PB) {
		i := 0
		for pb.Next() {
			mu.Lock()
			cache[i] = i
			mu.Unlock()
			mu.RLock()
			_ = cache[i]
			mu.RUnlock()
			i++
		}
	})
}
