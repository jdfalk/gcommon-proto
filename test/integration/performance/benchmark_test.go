// file: test/integration/performance/benchmark_test.go
// version: 1.1.0
// guid: eec239de-9516-4cbe-8b1a-848833a1b2ea

package performance

import (
	"testing"

	"github.com/jdfalk/gcommon/test/integration/framework"
)

// BenchmarkThroughput measures basic operation throughput.
func BenchmarkThroughput(b *testing.B) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		b.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	b.Run("benchmark operation", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			_ = i * i
		}
	})
}
