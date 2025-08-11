// file: test/integration/modules/metrics_test.go
// version: 1.1.0
// guid: 6cb68b18-f75f-423c-bd42-13148c14fc71

package modules

import (
	"testing"

	metrics "github.com/jdfalk/gcommon/pkg/metrics"
	memory "github.com/jdfalk/gcommon/pkg/metrics/memory"
	_ "github.com/jdfalk/gcommon/pkg/metrics/proto"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestMetricsModuleIntegration checks metrics collection and export.
func TestMetricsModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	provider, err := memory.NewProvider(metrics.Config{})
	if err != nil {
		t.Fatalf("provider error: %v", err)
	}

	t.Run("record counter", func(t *testing.T) {
		c := provider.Counter("requests")
		c.Inc()
		c.Add(2)
		if v := c.Value(); v != 3 {
			t.Fatalf("expected 3 got %v", v)
		}
	})

	t.Run("record gauge", func(t *testing.T) {
		g := provider.Gauge("load")
		g.Set(5)
		g.Dec()
		if v := g.Value(); v != 4 {
			t.Fatalf("expected 4 got %v", v)
		}
	})

	t.Run("record histogram", func(t *testing.T) {
		h := provider.Histogram("latency")
		h.Observe(1)
		h.Observe(5)
		s := h.Snapshot()
		if s.Count() != 2 {
			t.Fatalf("expected 2 samples got %d", s.Count())
		}
	})

	t.Run("export metrics", func(t *testing.T) {
		if provider.Handler() != nil {
			t.Fatalf("memory provider handler should be nil")
		}
	})

	t.Run("reset metrics", func(t *testing.T) {
		c := provider.Counter("requests")
		c.Add(-c.Value())
		if v := c.Value(); v != 0 {
			t.Fatalf("expected reset to 0, got %v", v)
		}
	})
}
