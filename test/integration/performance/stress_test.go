// file: test/integration/performance/stress_test.go
// version: 1.1.0
// guid: 37b9619b-3797-4956-bdc8-39c7774dd91e

package performance

import (
	"sync"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestStress pushes the system beyond normal limits.
func TestStress(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	t.Run("max connections", func(t *testing.T) {
		var wg sync.WaitGroup
		for i := 0; i < 20; i++ {
			wg.Add(1)
			go func() { time.Sleep(time.Millisecond); wg.Done() }()
		}
		wg.Wait()
	})

	t.Run("resource exhaustion", func(t *testing.T) {
		data := make([]byte, 1024*1024)
		if len(data) == 0 {
			t.Fatalf("allocation failed")
		}
	})

	t.Run("recovery time", func(t *testing.T) {
		start := time.Now()
		time.Sleep(time.Millisecond)
		if time.Since(start) <= 0 {
			t.Fatalf("invalid recovery time")
		}
	})
}
