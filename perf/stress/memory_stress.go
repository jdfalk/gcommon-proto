// file: perf/stress/memory_stress.go
// version: 1.0.0
// guid: 24e5b2ef-d78e-4714-a6c6-64c5581116f7

// Package stress contains stress test helpers.
package stress

// AllocateMemory repeatedly allocates blocks to test memory limits.
func AllocateMemory(blocks int, size int) [][]byte {
	data := make([][]byte, 0, blocks)
	for i := 0; i < blocks; i++ {
		data = append(data, make([]byte, size))
	}
	return data
}
