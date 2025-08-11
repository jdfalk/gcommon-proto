// file: test/integration/cross_module/metrics_all_test.go
// version: 1.1.0
// guid: 1c01742c-f4b5-4917-9a5e-9d0fde0716ba

package crossmodule

import (
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	_ "github.com/jdfalk/gcommon/pkg/cache/proto"
	_ "github.com/jdfalk/gcommon/pkg/config/proto"
	metrics "github.com/jdfalk/gcommon/pkg/metrics"
	memory "github.com/jdfalk/gcommon/pkg/metrics/memory"
	_ "github.com/jdfalk/gcommon/pkg/metrics/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/organization/proto"
	_ "github.com/jdfalk/gcommon/pkg/queue/proto"
	_ "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestMetricsAcrossModules verifies that metrics integrate with all modules.
func TestMetricsAcrossModules(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	provider, _ := memory.NewProvider(metrics.Config{})
	modules := []string{"config", "queue", "metrics", "auth", "web", "cache", "organization", "notification"}
	for _, m := range modules {
		t.Run(m, func(t *testing.T) {
			c := provider.Counter(m)
			c.Inc()
			if c.Value() != 1 {
				t.Fatalf("expected counter 1 got %v", c.Value())
			}
		})
	}

	t.Run("aggregate metrics", func(t *testing.T) {
		total := 0.0
		for _, m := range modules {
			total += provider.Counter(m).Value()
		}
		if total != float64(len(modules)) {
			t.Fatalf("expected %d got %v", len(modules), total)
		}
	})
}
