// file: test/integration/cross_module/metrics_all_test.go
// version: 1.0.0
// guid: 1c01742c-f4b5-4917-9a5e-9d0fde0716ba

package crossmodule

import (
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	_ "github.com/jdfalk/gcommon/pkg/cache/proto"
	_ "github.com/jdfalk/gcommon/pkg/config/proto"
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

	modules := []string{"config", "queue", "metrics", "auth", "web", "cache", "organization", "notification"}
	for _, m := range modules {
		t.Run(m, func(t *testing.T) {
			// TODO: emit metrics from module and validate collection
			t.Skip("integration test not implemented")
		})
	}

	t.Run("aggregate metrics", func(t *testing.T) {
		// TODO: ensure metrics aggregation across modules
		t.Skip("integration test not implemented")
	})
}
