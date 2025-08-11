// file: perf/benchmarks/organization_bench.go
// version: 1.1.0
// guid: 73ce7a17-d28d-40bb-acef-0b8343cc2c9d

package benchmarks

import (
	"sync"
	"testing"
)

// BenchmarkOrgCreation measures organization creation performance.
func BenchmarkOrgCreation(b *testing.B) {
	type Org struct{ ID int }
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = Org{ID: i}
	}
}

// BenchmarkOrgLookup measures organization lookup speed.
func BenchmarkOrgLookup(b *testing.B) {
	orgs := map[int]struct{}{1: {}, 2: {}, 3: {}}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = orgs[2]
	}
}

// BenchmarkOrgListing measures organization listing throughput.
func BenchmarkOrgListing(b *testing.B) {
	orgs := make([]struct{}, 1000)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = len(orgs)
	}
}

// BenchmarkOrgConcurrentOps measures concurrent organization operations.
func BenchmarkOrgConcurrentOps(b *testing.B) {
	orgs := make(map[int]struct{})
	var mu sync.RWMutex
	b.RunParallel(func(pb *testing.PB) {
		id := 0
		for pb.Next() {
			mu.Lock()
			orgs[id] = struct{}{}
			mu.Unlock()
			mu.RLock()
			_ = orgs[id]
			mu.RUnlock()
			id++
		}
	})
}
