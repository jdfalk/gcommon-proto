// file: perf/stress/cpu_stress.go
// version: 1.1.0
// guid: c0de16cc-49e1-4959-9b4f-9f9c52a67c78

package stress

import (
	"context"
	"math"
	"time"
)

// BurnCPU performs a compute-heavy loop to stress CPU.
func BurnCPU(iterations int) int {
	x := 0
	for i := 0; i < iterations; i++ {
		x += int(math.Sqrt(float64(i)))
	}
	return x
}

// SpinCPU spins the CPU for the specified duration.
func SpinCPU(ctx context.Context, d time.Duration) {
	deadline := time.Now().Add(d)
	for {
		select {
		case <-ctx.Done():
			return
		default:
			if time.Now().After(deadline) {
				return
			}
			_ = BurnCPU(1000)
		}
	}
}
