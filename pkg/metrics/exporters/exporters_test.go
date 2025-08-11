// file: pkg/metrics/exporters/exporters_test.go
// version: 1.0.1
// guid: 4e5f6071-89ab-cdef-0123-456789abcdef

package exporters

import (
	"context"
	"net/http"
	"testing"

	metrics "github.com/jdfalk/gcommon/pkg/metrics"
)

// mockProvider is a minimal metrics.Provider used for testing.
// It satisfies the interface but does not record any metrics.
type mockProvider struct{}

func (m *mockProvider) Counter(name string, options ...metrics.Option) metrics.Counter { return nil }
func (m *mockProvider) Gauge(name string, options ...metrics.Option) metrics.Gauge     { return nil }
func (m *mockProvider) Histogram(name string, options ...metrics.Option) metrics.Histogram {
	return nil
}
func (m *mockProvider) Summary(name string, options ...metrics.Option) metrics.Summary { return nil }
func (m *mockProvider) Timer(name string, options ...metrics.Option) metrics.Timer     { return nil }
func (m *mockProvider) Registry() metrics.Registry                                     { return nil }
func (m *mockProvider) Handler() http.Handler                                          { return nil }
func (m *mockProvider) Start(ctx context.Context) error                                { return nil }
func (m *mockProvider) Stop(ctx context.Context) error                                 { return nil }
func (m *mockProvider) WithTags(tags ...metrics.Tag) metrics.Provider {
	return m
}

// TestBaseExporter_WithProvider ensures that the BaseExporter correctly stores
// and retrieves the provider instance.
func TestBaseExporter_WithProvider(t *testing.T) {
	t.Run("assign provider", func(t *testing.T) {
		var b BaseExporter
		p := &mockProvider{}
		b.WithProvider(p)
		if b.Provider() != p {
			t.Fatalf("expected provider to be set")
		}
	})

	t.Run("thread safe", func(t *testing.T) {
		t.Skip("TODO: add concurrency tests for BaseExporter")
	})
}
