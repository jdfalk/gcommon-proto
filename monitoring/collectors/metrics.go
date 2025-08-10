// file: monitoring/collectors/metrics.go
// version: 1.1.0
// guid: c00734ab-0f41-411b-8348-9029a65d8a53

package collectors

import (
	"context"
	"fmt"
	"runtime"
	"sync"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	otelprom "go.opentelemetry.io/otel/exporters/prometheus"
	"go.opentelemetry.io/otel/metric"
)

// MetricsCollector provides an abstraction around collecting application and
// system metrics. It exposes helper methods for recording counters, gauges,
// and histograms while also reporting basic runtime statistics. The collector
// is safe for concurrent use and is intended to be embedded or shared across
// services that require observability.
type MetricsCollector struct {
	registry   *prometheus.Registry
	meter      metric.Meter
	mu         sync.RWMutex
	counters   map[string]metric.Int64Counter
	gauges     map[string]metric.Int64UpDownCounter
	histograms map[string]metric.Float64Histogram
}

// NewMetricsCollector creates a MetricsCollector backed by a fresh Prometheus
// registry and OpenTelemetry meter. A custom registry is used so that services
// embedding this package can export only the metrics they register.
func NewMetricsCollector() (*MetricsCollector, error) {
	reg := prometheus.NewRegistry()
	exp, err := otelprom.New(otelprom.WithRegisterer(reg))
	if err != nil {
		return nil, fmt.Errorf("create prometheus exporter: %w", err)
	}
	otel.SetMeterProvider(exp.MeterProvider())
	m := otel.Meter("gcommon/monitoring")
	mc := &MetricsCollector{
		registry:   reg,
		meter:      m,
		counters:   make(map[string]metric.Int64Counter),
		gauges:     make(map[string]metric.Int64UpDownCounter),
		histograms: make(map[string]metric.Float64Histogram),
	}
	return mc, nil
}

// RegisterCounter registers a new counter metric with the given name and
// description. Subsequent calls with the same name return the existing counter.
func (m *MetricsCollector) RegisterCounter(name, description string) metric.Int64Counter {
	m.mu.Lock()
	defer m.mu.Unlock()
	if c, ok := m.counters[name]; ok {
		return c
	}
	counter, err := m.meter.Int64Counter(name, metric.WithDescription(description))
	if err != nil {
		panic(fmt.Sprintf("unable to create counter %s: %v", name, err))
	}
	m.counters[name] = counter
	return counter
}

// RegisterGauge registers a new up/down counter which is used to represent a
// gauge value. This simplifies tracking values that can increase and decrease.
func (m *MetricsCollector) RegisterGauge(name, description string) metric.Int64UpDownCounter {
	m.mu.Lock()
	defer m.mu.Unlock()
	if g, ok := m.gauges[name]; ok {
		return g
	}
	gauge, err := m.meter.Int64UpDownCounter(name, metric.WithDescription(description))
	if err != nil {
		panic(fmt.Sprintf("unable to create gauge %s: %v", name, err))
	}
	m.gauges[name] = gauge
	return gauge
}

// RegisterHistogram registers a histogram metric which can be used for
// recording latency or size distributions.
func (m *MetricsCollector) RegisterHistogram(name, description, unit string) metric.Float64Histogram {
	m.mu.Lock()
	defer m.mu.Unlock()
	if h, ok := m.histograms[name]; ok {
		return h
	}
	hist, err := m.meter.Float64Histogram(name, metric.WithDescription(description), metric.WithUnit(unit))
	if err != nil {
		panic(fmt.Sprintf("unable to create histogram %s: %v", name, err))
	}
	m.histograms[name] = hist
	return hist
}

// Increment increments the named counter by the provided value. The metric will
// be lazily registered if it does not already exist.
func (m *MetricsCollector) Increment(name string, value int64, attrs ...attribute.KeyValue) {
	counter := m.RegisterCounter(name, fmt.Sprintf("auto-generated counter %s", name))
	counter.Add(context.Background(), value, metric.WithAttributes(attrs...))
}

// GaugeAdd increments or decrements the named gauge by the provided value.
func (m *MetricsCollector) GaugeAdd(name string, delta int64, attrs ...attribute.KeyValue) {
	gauge := m.RegisterGauge(name, fmt.Sprintf("auto-generated gauge %s", name))
	gauge.Add(context.Background(), delta, metric.WithAttributes(attrs...))
}

// Observe records a value in the specified histogram. The histogram will be
// lazily registered if required.
func (m *MetricsCollector) Observe(name string, value float64, attrs ...attribute.KeyValue) {
	hist := m.RegisterHistogram(name, fmt.Sprintf("auto-generated histogram %s", name), "")
	hist.Record(context.Background(), value, metric.WithAttributes(attrs...))
}

// StartRuntimeMetrics begins a goroutine that periodically records Go runtime
// statistics such as memory usage and number of goroutines. The metrics are
// updated every interval until the context is cancelled.
func (m *MetricsCollector) StartRuntimeMetrics(ctx context.Context, interval time.Duration) {
	gGauge := m.RegisterGauge("runtime_goroutines", "Number of running goroutines")
	mGauge := m.RegisterGauge("runtime_memory_bytes", "Number of bytes in use")
	gcCounter := m.RegisterCounter("runtime_gc_cycles_total", "Total GC cycles")

	go func() {
		ticker := time.NewTicker(interval)
		defer ticker.Stop()
		var lastGC uint32
		for {
			select {
			case <-ctx.Done():
				return
			case <-ticker.C:
				gGauge.Add(ctx, int64(runtime.NumGoroutine()))
				var ms runtime.MemStats
				runtime.ReadMemStats(&ms)
				mGauge.Add(ctx, int64(ms.Alloc))
				if ms.NumGC != lastGC {
					gcCounter.Add(ctx, int64(ms.NumGC-lastGC))
					lastGC = ms.NumGC
				}
			}
		}
	}()
}

// Registry exposes the underlying Prometheus registry for HTTP handlers or
// custom exporters.
func (m *MetricsCollector) Registry() *prometheus.Registry {
	return m.registry
}

// Example usage of MetricsCollector demonstrating registering custom metrics
// and recording values. This function is not called anywhere but serves as
// documentation for developers integrating with the collector.
func example() {
	mc, _ := NewMetricsCollector()
	requests := mc.RegisterCounter("requests_total", "number of processed requests")
	latency := mc.RegisterHistogram("request_latency_seconds", "request latency", "s")

	ctx := context.Background()
	requests.Add(ctx, 1, metric.WithAttributes(attribute.String("module", "example")))
	latency.Record(ctx, 0.35)
}
