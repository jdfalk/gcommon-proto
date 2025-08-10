// file: perf/stress/cpu_stress.go
// version: 1.0.0
// guid: c0de16cc-49e1-4959-9b4f-9f9c52a67c78

package stress

// BurnCPU performs a compute-heavy loop to stress CPU.
func BurnCPU(iterations int) int {
	x := 0
	for i := 0; i < iterations; i++ {
		x += i
	}
	return x
}
