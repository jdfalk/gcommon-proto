// file: pkg/metrics/memory/provider_test.go
// version: 1.1.0
// guid: f1d1a2b3-c4d5-6789-0abc-def123456789

package memory

import (
	"testing"

	metrics "github.com/jdfalk/gcommon/pkg/metrics"
)

// TestMemoryProviderCounter verifies counter operations.
func TestMemoryProviderCounter(t *testing.T) {
	p, err := NewProvider(metrics.Config{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	c := p.Counter("requests")
	c.Inc()
	c.Add(2)

	if v := c.Value(); v != 3 {
		t.Fatalf("expected value 3, got %v", v)
	}
}

// TestMemoryProviderGauge verifies gauge operations.
func TestMemoryProviderGauge(t *testing.T) {
	p, err := NewProvider(metrics.Config{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	g := p.Gauge("temperature")
	g.Set(10)
	g.Add(5)
	g.Dec()

	if v := g.Value(); v != 14 {
		t.Fatalf("expected value 14, got %v", v)
	}
}

// TestMemoryProviderHistogram verifies histogram observations.
func TestMemoryProviderHistogram(t *testing.T) {
	p, err := NewProvider(metrics.Config{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	h := p.Histogram("latency")
	h.Observe(0.5)
	h.Observe(1.5)

	snap := p.Registry().Snapshot().Histograms()["latency"]
	if snap.Count() != 2 {
		t.Fatalf("expected count 2, got %d", snap.Count())
	}
}

// TestMemoryProviderSummary verifies summary quantiles.
func TestMemoryProviderSummary(t *testing.T) {
	p, err := NewProvider(metrics.Config{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	s := p.Summary("requests")
	s.Observe(1)
	s.Observe(2)

	snap := p.Registry().Snapshot().Summaries()["requests"]
	if q := snap.Quantile(0.5); q != 1.5 {
		t.Fatalf("expected median 1.5, got %v", q)
	}
}
