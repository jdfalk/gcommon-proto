// file: perf/framework/runner.go
// version: 1.1.0
// guid: b6ba8daf-d498-45da-8fbc-92f4bddfc1c0

// Package framework provides utilities for performance testing.
package framework

import (
	"context"
	"os"
	"runtime"
	"testing"
	"time"
)

// BenchmarkFunc represents a benchmark operation.
type BenchmarkFunc func(ctx context.Context, i int) error

// Runner executes benchmarks and collects metrics.
type Runner struct {
	collector *MetricsCollector
	options   RunnerOptions
}

// RunnerOptions defines configurable options for the Runner.
type RunnerOptions struct {
	WarmupIterations int
	Profiling        bool
}

// NewRunner creates a Runner with the provided options.
func NewRunner(opts RunnerOptions) *Runner {
	return &Runner{collector: NewMetricsCollector(), options: opts}
}

// Run executes a benchmark function and returns collected metrics.
func (r *Runner) Run(b *testing.B, fn BenchmarkFunc) PerformanceMetrics {
	ctx := context.Background()
	for i := 0; i < r.options.WarmupIterations; i++ {
		_ = fn(ctx, i) // Warmup phase
	}

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		iterStart := time.Now()
		if err := fn(ctx, i); err != nil {
			r.collector.RecordError()
		}
		r.collector.RecordLatency(time.Since(iterStart))
		r.collector.RecordThroughput(0, 1)
	}

	// Capture resource usage after benchmark
	r.collector.mu.Lock()
	r.collector.mu.Unlock()
	m := r.collector.Snapshot()

	var mem runtime.MemStats
	runtime.ReadMemStats(&mem)
	m.MemoryUsage = MemoryMetrics{AllocatedBytes: mem.Alloc, TotalBytes: mem.TotalAlloc}
	m.ResourceUsage = ResourceMetrics{Goroutines: runtime.NumGoroutine()}
	return m
}

// RunWithProfiling executes the benchmark with CPU profiling enabled.
func (r *Runner) RunWithProfiling(b *testing.B, profilePath string, fn BenchmarkFunc) (PerformanceMetrics, error) {
	var (
		profFile *os.File
		err      error
	)
	if r.options.Profiling {
		profFile, err = StartCPUProfile(profilePath)
		if err != nil {
			return PerformanceMetrics{}, err
		}
		defer StopCPUProfile(profFile)
	}
	return r.Run(b, fn), nil
}

// Reset clears any metrics collected by the runner.
func (r *Runner) Reset() {
	r.collector.Reset()
}
