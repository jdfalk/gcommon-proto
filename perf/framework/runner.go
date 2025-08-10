// file: perf/framework/runner.go
// version: 1.0.0
// guid: b6ba8daf-d498-45da-8fbc-92f4bddfc1c0

// Package framework provides utilities for performance testing.
package framework

import "testing"

// Runner executes benchmarks and collects metrics.
type Runner struct{}

// Run executes a benchmark and returns collected metrics.
func (r *Runner) Run(b *testing.B, fn func(b *testing.B) PerformanceMetrics) PerformanceMetrics {
	return fn(b)
}
