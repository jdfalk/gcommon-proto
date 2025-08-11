// file: test/integration/modules/config_test.go
// version: 1.1.0
// guid: 031edbd2-005b-4e10-9e35-9cba218514f3

package modules

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/config"
	_ "github.com/jdfalk/gcommon/pkg/config/proto"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

type mapSource struct{ data map[string]interface{} }

func (m mapSource) Load() (map[string]interface{}, error) { return m.data, nil }

// TestConfigModuleIntegration verifies basic configuration workflows.
func TestConfigModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}

	mgr := config.NewManager()

	t.Run("load configuration", func(t *testing.T) {
		src := mapSource{data: map[string]interface{}{"host": "localhost", "port": 8080}}
		if err := mgr.Load(src); err != nil {
			t.Fatalf("load failed: %v", err)
		}
		host, err := mgr.GetString("host")
		if err != nil || host != "localhost" {
			t.Fatalf("expected host localhost got %s err %v", host, err)
		}
		port, err := mgr.GetInt("port")
		if err != nil || port != 8080 {
			t.Fatalf("expected port 8080 got %d err %v", port, err)
		}
	})

	t.Run("update configuration", func(t *testing.T) {
		if err := mgr.Set("debug", true); err != nil {
			t.Fatalf("set failed: %v", err)
		}
		val, err := mgr.GetBool("debug")
		if err != nil || !val {
			t.Fatalf("expected debug true got %v err %v", val, err)
		}
		var watched interface{}
		if err := mgr.Watch("debug", func(v interface{}) { watched = v }); err != nil {
			t.Fatalf("watch failed: %v", err)
		}
		_ = mgr.Set("debug", false)
		if watched != false {
			t.Fatalf("watcher not triggered: %v", watched)
		}
	})

	t.Run("validate configuration", func(t *testing.T) {
		if err := mgr.Validate(); err != nil {
			t.Fatalf("validate returned error: %v", err)
		}
	})

	t.Run("reload configuration", func(t *testing.T) {
		src := mapSource{data: map[string]interface{}{"host": "example.com"}}
		if err := mgr.Load(src); err != nil {
			t.Fatalf("reload failed: %v", err)
		}
		host, _ := mgr.GetString("host")
		if host != "example.com" {
			t.Fatalf("expected example.com got %s", host)
		}
	})

	t.Run("cleanup", func(t *testing.T) {
		if err := env.Cleanup(); err != nil {
			t.Fatalf("cleanup failed: %v", err)
		}
		// Recreate env to ensure cleanup removed resources
		if _, err := framework.SetupTestEnvironment(); err != nil {
			t.Fatalf("failed to recreate env: %v", err)
		}
	})
}
