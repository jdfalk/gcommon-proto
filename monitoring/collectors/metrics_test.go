// file: monitoring/collectors/metrics_test.go
// version: 1.0.0
// guid: 5c9d4a97-8ae6-41e7-a5f3-9a5e5fd4f111

package collectors

import (
	"context"
	"testing"
	"time"

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
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("counter.Add panicked: %v", r)
		}
	}()
	counter.Add(context.Background(), 5)
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}

// TestMetricsCollectorGauge verifies gauge registration and updates.
func TestMetricsCollectorGauge(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	gauge := mc.RegisterGauge("test_gauge", "a test gauge")
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("gauge.Add panicked: %v", r)
		}
	}()
	gauge.Add(context.Background(), 3)
	gauge.Add(context.Background(), -1)
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}

// TestMetricsCollectorHistogram verifies histogram registration and observation.
func TestMetricsCollectorHistogram(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	hist := mc.RegisterHistogram("test_hist", "a test histogram", "ms")
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("hist.Record panicked: %v", r)
		}
	}()
	hist.Record(context.Background(), 10, metric.WithAttributes(attribute.String("type", "test")))
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}

// TestStartRuntimeMetrics ensures runtime metrics are recorded.
func TestStartRuntimeMetrics(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	ctx, cancel := context.WithCancel(context.Background())
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("StartRuntimeMetrics panicked: %v", r)
		}
	}()
	mc.StartRuntimeMetrics(ctx, 10*time.Millisecond)
	time.Sleep(25 * time.Millisecond)
	cancel()
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}
