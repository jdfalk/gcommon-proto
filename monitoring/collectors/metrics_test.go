// file: monitoring/collectors/metrics_test.go
// version: 1.0.0
// guid: 5c9d4a97-8ae6-41e7-a5f3-9a5e5fd4f111

package collectors

import (
	"context"
	"testing"
	"time"

	"github.com/prometheus/client_golang/prometheus/testutil"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/metric"
)

// TestMetricsCollectorCounter verifies counter registration and increment.
func TestMetricsCollectorCounter(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	counter := mc.RegisterCounter("test_counter", "a test counter")
	counter.Add(context.Background(), 5)
	if got := testutil.ToFloat64(counter); got != 5 {
		t.Fatalf("counter value = %v, want 5", got)
	}
}

// TestMetricsCollectorGauge verifies gauge registration and updates.
func TestMetricsCollectorGauge(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	gauge := mc.RegisterGauge("test_gauge", "a test gauge")
	gauge.Add(context.Background(), 3)
	gauge.Add(context.Background(), -1)
	if got := testutil.ToFloat64(gauge); got != 2 {
		t.Fatalf("gauge value = %v, want 2", got)
	}
}

// TestMetricsCollectorHistogram verifies histogram registration and observation.
func TestMetricsCollectorHistogram(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	hist := mc.RegisterHistogram("test_hist", "a test histogram", "ms")
	hist.Record(context.Background(), 10, metric.WithAttributes(attribute.String("type", "test")))
	if count := testutil.CollectAndCount(hist); count == 0 {
		t.Fatalf("expected histogram to record value")
	}
}

// TestStartRuntimeMetrics ensures runtime metrics are recorded.
func TestStartRuntimeMetrics(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	ctx, cancel := context.WithCancel(context.Background())
	mc.StartRuntimeMetrics(ctx, 10*time.Millisecond)
	time.Sleep(25 * time.Millisecond)
	cancel()
	if got := testutil.ToFloat64(mc.RegisterGauge("runtime_goroutines", "")); got == 0 {
		t.Fatalf("runtime_goroutines not recorded")
	}
}
