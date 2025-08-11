// file: perf/load/analyzers/analyzers.go
// version: 1.1.0
// guid: 377b1d5b-a9ef-4ddc-b2f6-cbabcae4845e

// Package analyzers evaluates load test results.
package analyzers

import (
	"errors"
	"sync"

	"github.com/jdfalk/gcommon/perf/framework"
)

// Analyzer processes load test metrics.
type Analyzer interface {
	AddSample(m framework.PerformanceMetrics) error
	Analyze() (framework.PerformanceMetrics, error)
}

// MemoryAnalyzer stores metrics in memory for later analysis.
type MemoryAnalyzer struct {
	collector *framework.MetricsCollector
	once      sync.Once
}

// NewMemoryAnalyzer creates a MemoryAnalyzer using provided collector.
func NewMemoryAnalyzer(c *framework.MetricsCollector) *MemoryAnalyzer {
	return &MemoryAnalyzer{collector: c}
}

// AddSample records metrics sample into collector.
func (m *MemoryAnalyzer) AddSample(pm framework.PerformanceMetrics) error {
	if m.collector == nil {
		return errors.New("nil collector")
	}
	m.collector.Merge(pm)
	return nil
}

// Analyze returns aggregated metrics.
func (m *MemoryAnalyzer) Analyze() (framework.PerformanceMetrics, error) {
	if m.collector == nil {
		return framework.PerformanceMetrics{}, errors.New("nil collector")
	}
	return m.collector.Snapshot(), nil
}
