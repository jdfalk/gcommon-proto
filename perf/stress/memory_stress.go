// file: perf/stress/memory_stress.go
// version: 1.1.0
// guid: 24e5b2ef-d78e-4714-a6c6-64c5581116f7

// Package stress contains stress test helpers.
package stress

import (
	"context"
	"runtime"
	"time"
)

// AllocateMemory repeatedly allocates blocks to test memory limits.
func AllocateMemory(blocks int, size int) [][]byte {
	data := make([][]byte, 0, blocks)
	for i := 0; i < blocks; i++ {
		data = append(data, make([]byte, size))
	}
	return data
}

// ExhaustMemory gradually consumes memory until context cancellation or limit.
func ExhaustMemory(ctx context.Context, step, limit int) [][]byte {
	var allocated [][]byte
	ticker := time.NewTicker(50 * time.Millisecond)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			return allocated
		case <-ticker.C:
			if len(allocated)*step >= limit {
				return allocated
			}
			allocated = append(allocated, make([]byte, step))
		}
	}
}

// MonitorMemory returns current allocated and total bytes from runtime.
func MonitorMemory() (uint64, uint64) {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	return m.Alloc, m.TotalAlloc
}
