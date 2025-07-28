package middleware

import (
	"context"
	"net/http"
	"testing"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"google.golang.org/grpc"
)

// mockCounter implements metrics.Counter for testing.
type mockCounter struct {
	value float64
	tags  []metrics.Tag
}

func (c *mockCounter) Inc()          { c.value++ }
func (c *mockCounter) Add(v float64) { c.value += v }
func (c *mockCounter) WithTags(tags ...metrics.Tag) metrics.Counter {
	return &mockCounter{tags: append(c.tags, tags...)}
}
func (c *mockCounter) Value() float64 { return c.value }

// mockHistogram implements metrics.Histogram for testing.
type mockHistogram struct {
	observations []float64
	tags         []metrics.Tag
}

func (h *mockHistogram) Observe(v float64) { h.observations = append(h.observations, v) }
func (h *mockHistogram) WithTags(tags ...metrics.Tag) metrics.Histogram {
	return &mockHistogram{observations: h.observations, tags: append(h.tags, tags...)}
}
func (h *mockHistogram) Snapshot() metrics.HistogramSnapshot { return nil }

// mockProvider implements metrics.Provider for testing.
type mockProvider struct {
	counter   *mockCounter
	histogram *mockHistogram
}

func newMockProvider() *mockProvider {
	return &mockProvider{
		counter:   &mockCounter{},
		histogram: &mockHistogram{},
	}
}

func (p *mockProvider) Counter(name string, options ...metrics.Option) metrics.Counter {
	return p.counter
}
func (p *mockProvider) Gauge(name string, options ...metrics.Option) metrics.Gauge { return nil }
func (p *mockProvider) Histogram(name string, options ...metrics.Option) metrics.Histogram {
	return p.histogram
}
func (p *mockProvider) Summary(name string, options ...metrics.Option) metrics.Summary { return nil }
func (p *mockProvider) Timer(name string, options ...metrics.Option) metrics.Timer     { return nil }
func (p *mockProvider) Registry() metrics.Registry                                     { return nil }
func (p *mockProvider) Handler() http.Handler                                          { return nil }
func (p *mockProvider) Start(ctx context.Context) error                                { return nil }
func (p *mockProvider) Stop(ctx context.Context) error                                 { return nil }
func (p *mockProvider) WithTags(tags ...metrics.Tag) metrics.Provider                  { return p }

// dummy unary handler
func dummyUnary(ctx context.Context, req interface{}) (interface{}, error) {
	return "ok", nil
}

func TestUnaryServerMetrics(t *testing.T) {
	p := newMockProvider()
	interceptor := UnaryServerMetrics(GRPCMetricsOptions{Provider: p})

	_, err := interceptor(context.Background(), struct{}{}, &grpc.UnaryServerInfo{FullMethod: "/pkg.Service/Method"}, dummyUnary)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}

	if p.counter.value != 1 {
		t.Errorf("expected counter to be 1, got %f", p.counter.value)
	}
	if len(p.histogram.observations) != 1 {
		t.Errorf("expected one observation, got %d", len(p.histogram.observations))
	}
}

// dummy stream handler
func dummyStream(srv interface{}, stream grpc.ServerStream) error { return nil }

type dummyServerStream struct{ grpc.ServerStream }

func TestStreamServerMetrics(t *testing.T) {
	p := newMockProvider()
	interceptor := StreamServerMetrics(GRPCMetricsOptions{Provider: p})

	ds := &dummyServerStream{}
	err := interceptor(nil, ds, &grpc.StreamServerInfo{FullMethod: "/pkg.Service/Stream"}, dummyStream)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if p.counter.value != 1 {
		t.Errorf("expected counter to be 1, got %f", p.counter.value)
	}
	if len(p.histogram.observations) != 1 {
		t.Errorf("expected one observation, got %d", len(p.histogram.observations))
	}
}
