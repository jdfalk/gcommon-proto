// file: test/integration/cross_module/config_all_test.go
// version: 1.1.0
// guid: f3f48567-c788-401f-88b2-d7261aca8054

package crossmodule

import (
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	_ "github.com/jdfalk/gcommon/pkg/cache/proto"
	"github.com/jdfalk/gcommon/pkg/config"
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

	mgr := config.NewManager()
	_ = mgr.Set("web.port", 80)
	_ = mgr.Set("cache.size", 10)
	modules := map[string]string{"web.port": "80", "cache.size": "10"}
	for key, expect := range modules {
		t.Run(key, func(t *testing.T) {
			v, err := mgr.GetString(key)
			if err != nil || v != expect {
				t.Fatalf("expected %s got %s err %v", expect, v, err)
			}
		})
	}

	t.Run("dynamic reload", func(t *testing.T) {
		_ = mgr.Set("web.port", 81)
		v, _ := mgr.GetInt("web.port")
		if v != 81 {
			t.Fatalf("expected 81 got %d", v)
		}
	})
}
