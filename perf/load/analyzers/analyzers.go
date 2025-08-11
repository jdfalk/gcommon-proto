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
	mu      sync.Mutex
	metrics framework.PerformanceMetrics
	once    sync.Once
}

// NewMemoryAnalyzer creates a MemoryAnalyzer with zeroed metrics.
func NewMemoryAnalyzer() *MemoryAnalyzer {
	return &MemoryAnalyzer{}
}

// AddSample records metrics sample into internal storage.
func (m *MemoryAnalyzer) AddSample(pm framework.PerformanceMetrics) error {
	m.mu.Lock()
	defer m.mu.Unlock()
	m.metrics.Merge(pm)
	return nil
}

// Analyze returns aggregated metrics.
func (m *MemoryAnalyzer) Analyze() (framework.PerformanceMetrics, error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	if (m.metrics == framework.PerformanceMetrics{}) {
		return framework.PerformanceMetrics{}, errors.New("no samples")
	}
	return m.metrics.Clone(), nil
}
