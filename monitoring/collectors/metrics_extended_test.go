// file: monitoring/collectors/metrics_extended_test.go
// version: 1.0.0
// guid: c5e3b2d1-8a4b-4f9e-9a6d-7d8c9e0f1a2b

package collectors

import (
	"context"
	"sync"
	"testing"
	"time"

	"github.com/prometheus/client_golang/prometheus/testutil"
)

// TestConcurrentIncrement validates counter correctness under concurrency.
func TestConcurrentIncrement(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	counter := mc.RegisterCounter("conc_counter", "")
	var wg sync.WaitGroup
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter.Add(context.Background(), 1)
		}()
	}
	wg.Wait()
	if got := testutil.ToFloat64(counter); got != 50 {
		t.Fatalf("counter value = %v, want 50", got)
	}
}

// TestGaugeConcurrency checks gauge updates from multiple goroutines.
func TestGaugeConcurrency(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	gauge := mc.RegisterGauge("conc_gauge", "")
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			gauge.Add(context.Background(), 1)
			time.Sleep(1 * time.Millisecond)
			gauge.Add(context.Background(), -1)
		}()
	}
	wg.Wait()
	if got := testutil.ToFloat64(gauge); got != 0 {
		t.Fatalf("gauge value = %v, want 0", got)
	}
}

// TestObserveDistribution ensures histogram records multiple values.
func TestObserveDistribution(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	hist := mc.RegisterHistogram("dist_hist", "", "ms")
	for i := 0; i < 100; i++ {
		hist.Record(context.Background(), float64(i))
	}
	if count := testutil.CollectAndCount(hist); count == 0 {
		t.Fatalf("expected histogram values")
	}
}
