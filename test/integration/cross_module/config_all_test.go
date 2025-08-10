// file: test/integration/cross_module/config_all_test.go
// version: 1.0.0
// guid: f3f48567-c788-401f-88b2-d7261aca8054

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

// TestConfigAcrossModules ensures configuration is accessible to all modules.
func TestConfigAcrossModules(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	modules := []string{"config", "queue", "metrics", "auth", "web", "cache", "organization", "notification"}
	for _, m := range modules {
		t.Run(m, func(t *testing.T) {
			// TODO: load module configuration from central store
			t.Skip("integration test not implemented")
		})
	}

	t.Run("dynamic reload", func(t *testing.T) {
		// TODO: change configuration and verify module picks it up
		t.Skip("integration test not implemented")
	})
}
