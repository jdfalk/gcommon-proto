// file: perf/framework/metrics.go
// version: 1.1.0
// guid: 4e9b2dc2-9853-459b-9c81-a190eaf138a8

// Package framework provides utilities for performance testing.
package framework

import (
	"sort"
	"sync"
	"time"
)

// PerformanceMetrics captures collected metrics for a benchmark run.
type PerformanceMetrics struct {
	Latency       LatencyMetrics
	Throughput    ThroughputMetrics
	MemoryUsage   MemoryMetrics
	CPUUsage      CPUMetrics
	ErrorRate     ErrorRateMetrics
	ResourceUsage ResourceMetrics
}

// LatencyMetrics represents latency distribution metrics.
type LatencyMetrics struct {
	P50, P95, P99, P999 time.Duration
	Mean, Max, Min      time.Duration
}

// ThroughputMetrics represents throughput measurements.
type ThroughputMetrics struct {
	RequestsPerSecond   float64
	OperationsPerSecond float64
	BytesPerSecond      float64
}

// MemoryMetrics reports memory usage statistics.
type MemoryMetrics struct {
	AllocatedBytes uint64
	TotalBytes     uint64
}

// CPUMetrics reports CPU usage percentages.
type CPUMetrics struct {
	UserPercent   float64
	SystemPercent float64
}

// ErrorRateMetrics captures error counts and rate.
type ErrorRateMetrics struct {
	Errors    int64
	ErrorRate float64
}

// ResourceMetrics tracks system resource utilization.
type ResourceMetrics struct {
	OpenFiles  int
	Goroutines int
}

// MetricsCollector aggregates raw samples into PerformanceMetrics.
type MetricsCollector struct {
	mu        sync.Mutex
	latencies []time.Duration
	bytes     int64
	ops       int64
	errors    int64
	start     time.Time
}

// NewMetricsCollector returns an initialized MetricsCollector.
func NewMetricsCollector() *MetricsCollector {
	return &MetricsCollector{start: time.Now()}
}

// RecordLatency stores a latency sample.
func (c *MetricsCollector) RecordLatency(d time.Duration) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.latencies = append(c.latencies, d)
}

// RecordThroughput adds bytes and operations counters.
func (c *MetricsCollector) RecordThroughput(bytes int64, ops int64) {
	c.mu.Lock()
	c.bytes += bytes
	c.ops += ops
	c.mu.Unlock()
}

// RecordError increments the error counter.
func (c *MetricsCollector) RecordError() {
	c.mu.Lock()
	c.errors++
	c.mu.Unlock()
}

// Snapshot converts collected samples into PerformanceMetrics.
func (c *MetricsCollector) Snapshot() PerformanceMetrics {
	c.mu.Lock()
	defer c.mu.Unlock()

	elapsed := time.Since(c.start)
	m := PerformanceMetrics{}
	m.Latency = calculateLatencyMetrics(c.latencies)

	if elapsed > 0 {
		m.Throughput = ThroughputMetrics{
			RequestsPerSecond:   float64(c.ops) / elapsed.Seconds(),
			OperationsPerSecond: float64(c.ops) / elapsed.Seconds(),
			BytesPerSecond:      float64(c.bytes) / elapsed.Seconds(),
		}
	}

	if c.ops > 0 {
		m.ErrorRate = ErrorRateMetrics{
			Errors:    c.errors,
			ErrorRate: float64(c.errors) / float64(c.ops),
		}
	} else {
		m.ErrorRate = ErrorRateMetrics{Errors: c.errors}
	}

	m.ResourceUsage = ResourceMetrics{}
	return m
}

// calculateLatencyMetrics computes percentile and summary statistics.
func calculateLatencyMetrics(samples []time.Duration) LatencyMetrics {
	if len(samples) == 0 {
		return LatencyMetrics{}
	}

	sort.Slice(samples, func(i, j int) bool { return samples[i] < samples[j] })
	n := len(samples)

	lm := LatencyMetrics{
		P50:  samples[(50*n)/100],
		P95:  samples[(95*n)/100],
		P99:  samples[(99*n)/100],
		P999: samples[(999*n)/1000],
		Min:  samples[0],
		Max:  samples[n-1],
	}

	var total time.Duration
	for _, s := range samples {
		total += s
	}
	lm.Mean = total / time.Duration(n)
	return lm
}

// Merge combines another PerformanceMetrics into this collector.
func (c *MetricsCollector) Merge(other PerformanceMetrics) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.latencies = append(c.latencies, other.Latency.P50)
	c.bytes += int64(other.Throughput.BytesPerSecond)
	c.ops += int64(other.Throughput.OperationsPerSecond)
	c.errors += other.ErrorRate.Errors
}

// Reset clears collected samples.
func (c *MetricsCollector) Reset() {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.latencies = nil
	c.bytes = 0
	c.ops = 0
	c.errors = 0
	c.start = time.Now()
}

// CombineMetrics merges two PerformanceMetrics and returns result.
func CombineMetrics(a, b PerformanceMetrics) PerformanceMetrics {
	mc := NewMetricsCollector()
	mc.RecordThroughput(int64(a.Throughput.BytesPerSecond), int64(a.Throughput.OperationsPerSecond))
	mc.RecordThroughput(int64(b.Throughput.BytesPerSecond), int64(b.Throughput.OperationsPerSecond))
	mc.RecordLatency(a.Latency.Mean)
	mc.RecordLatency(b.Latency.Mean)
	mc.errors = a.ErrorRate.Errors + b.ErrorRate.Errors
	return mc.Snapshot()
}
