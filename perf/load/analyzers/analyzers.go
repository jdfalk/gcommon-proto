// file: perf/load/analyzers/analyzers.go
// version: 1.0.0
// guid: 377b1d5b-a9ef-4ddc-b2f6-cbabcae4845e

// Package analyzers evaluates load test results.
package analyzers

// Analyzer processes load test metrics.
type Analyzer interface {
	Analyze() error
}
