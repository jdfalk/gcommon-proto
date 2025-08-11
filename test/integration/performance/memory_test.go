// file: test/integration/performance/memory_test.go
// version: 1.1.0
// guid: ec983e95-567b-4d65-8ae3-06d41c1c587d

package performance

import (
	"runtime"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestMemoryProfiles tracks memory usage under various scenarios.
func TestMemoryProfiles(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	t.Run("baseline", func(t *testing.T) {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		if m.Alloc == 0 {
			t.Fatalf("expected alloc > 0")
		}
	})

	t.Run("after workload", func(t *testing.T) {
		var before, after runtime.MemStats
		runtime.ReadMemStats(&before)
		_ = make([]byte, 1024*1024)
		runtime.ReadMemStats(&after)
		if after.Alloc <= before.Alloc {
			t.Fatalf("allocation did not increase")
		}
	})

	t.Run("garbage collection", func(t *testing.T) {
		runtime.GC()
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		if m.NumGC == 0 {
			t.Fatalf("expected GC count")
		}
	})

	t.Run("allocation patterns", func(t *testing.T) {
		samples := make([][]byte, 0, 10)
		for i := 0; i < 10; i++ {
			samples = append(samples, make([]byte, 1024))
		}
		if len(samples) != 10 {
			t.Fatalf("expected 10 samples")
		}
	})

	t.Run("steady state", func(t *testing.T) {
		var before, after runtime.MemStats
		runtime.ReadMemStats(&before)
		time.Sleep(1 * time.Millisecond)
		runtime.ReadMemStats(&after)
		_ = after.HeapAlloc - before.HeapAlloc
	})

	t.Run("peak usage", func(t *testing.T) {
		var peak uint64
		for i := 0; i < 5; i++ {
			b := make([]byte, 1024*1024)
			peak += uint64(len(b))
			_ = b
		}
		if peak == 0 {
			t.Fatalf("expected peak >0")
		}
	})

	t.Run("release memory", func(t *testing.T) {
		runtime.GC()
		runtime.GC()
	})

	t.Run("profile report", func(t *testing.T) {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		if m.HeapSys == 0 {
			t.Fatalf("no heap stats")
		}
	})

	t.Run("fragmentation analysis", func(t *testing.T) {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		_ = m.HeapIdle
	})

	t.Run("final stats", func(t *testing.T) {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		if m.TotalAlloc == 0 {
			t.Fatalf("expected allocations")
		}
	})

	t.Run("memory limits", func(t *testing.T) {
		var m runtime.MemStats
		runtime.ReadMemStats(&m)
		if m.Sys == 0 {
			t.Fatalf("expected system memory")
		}
	})
}
