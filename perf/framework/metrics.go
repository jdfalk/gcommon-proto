// file: perf/framework/metrics.go
// version: 1.0.0
// guid: 4e9b2dc2-9853-459b-9c81-a190eaf138a8

// Package framework provides utilities for performance testing.
package framework

import "time"

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
