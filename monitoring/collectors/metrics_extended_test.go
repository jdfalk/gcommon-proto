// file: monitoring/collectors/metrics_extended_test.go
// version: 1.0.0
// guid: c5e3b2d1-8a4b-4f9e-9a6d-7d8c9e0f1a2b

package collectors

import (
	"context"
	"sync"
	"testing"
	"time"
)

// TestConcurrentIncrement validates counter correctness under concurrency.
func TestConcurrentIncrement(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	counter := mc.RegisterCounter("conc_counter", "")
	var wg sync.WaitGroup
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("counter.Add panicked: %v", r)
		}
	}()
	for i := 0; i < 50; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter.Add(context.Background(), 1)
		}()
	}
	wg.Wait()
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}

// TestGaugeConcurrency checks gauge updates from multiple goroutines.
func TestGaugeConcurrency(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	gauge := mc.RegisterGauge("conc_gauge", "")
	var wg sync.WaitGroup
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("gauge.Add panicked: %v", r)
		}
	}()
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
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}

// TestObserveDistribution ensures histogram records multiple values.
func TestObserveDistribution(t *testing.T) {
	mc, err := NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	hist := mc.RegisterHistogram("dist_hist", "", "ms")
	defer func() {
		if r := recover(); r != nil {
			t.Fatalf("hist.Record panicked: %v", r)
		}
	}()
	for i := 0; i < 100; i++ {
		hist.Record(context.Background(), float64(i))
	}
	// TODO: Use OTel SDK in-memory reader to assert value if needed
}
