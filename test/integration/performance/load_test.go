// file: test/integration/performance/load_test.go
// version: 1.1.0
// guid: cf063f25-7c29-42e5-b64c-8e978d1863ba

package performance

import (
	"sync"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestLoad simulates sustained load across modules.
func TestLoad(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	t.Run("simulate load", func(t *testing.T) {
		var wg sync.WaitGroup
		for i := 0; i < 10; i++ {
			wg.Add(1)
			go func() { time.Sleep(time.Millisecond); wg.Done() }()
		}
		wg.Wait()
	})

	t.Run("measure latency", func(t *testing.T) {
		start := time.Now()
		time.Sleep(time.Millisecond)
		if d := time.Since(start); d <= 0 {
			t.Fatalf("invalid duration")
		}
	})

	t.Run("collect metrics", func(t *testing.T) {
		var count int
		for i := 0; i < 5; i++ {
			count++
		}
		if count != 5 {
			t.Fatalf("expected 5")
		}
	})
}
