// file: perf/load/scenarios/scenarios.go
// version: 1.1.0
// guid: f80b7f6b-0bdc-4c33-96f2-0d226ae78c62

// Package scenarios defines load test scenarios.
package scenarios

import (
	"context"
	"time"

	"github.com/jdfalk/gcommon/perf/framework"
	"github.com/jdfalk/gcommon/perf/load/analyzers"
	"github.com/jdfalk/gcommon/perf/load/generators"
)

// Scenario defines a load test scenario.
type Scenario struct {
	Name        string
	Duration    time.Duration
	Concurrency int
	Generator   generators.Generator
	Analyzer    analyzers.Analyzer
	Description string
}

// Run executes the scenario using the configured generator and analyzer.
func (s *Scenario) Run(ctx context.Context) error {
	ctx, cancel := context.WithTimeout(ctx, s.Duration)
	defer cancel()

	err := s.Generator.Start(ctx, s.Concurrency)
	if err != nil {
		return err
	}

	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			s.Generator.Stop()
			return ctx.Err()
		case m := <-s.Generator.Metrics():
			if err := s.Analyzer.AddSample(m); err != nil {
				return err
			}
		case <-ticker.C:
			// Periodic tick for long-running scenarios
		}
	}
}

// NewScenario constructs a Scenario with default analyzer.
func NewScenario(name string, duration time.Duration, conc int, gen generators.Generator, an analyzers.Analyzer) *Scenario {
	return &Scenario{
		Name:        name,
		Duration:    duration,
		Concurrency: conc,
		Generator:   gen,
		Analyzer:    an,
	}
}

// BaselineScenarios returns common predefined scenarios.
func BaselineScenarios(gen generators.Generator, an analyzers.Analyzer) []*Scenario {
	return []*Scenario{
		NewScenario("normal", 1*time.Minute, 10, gen, an),
		NewScenario("peak", 30*time.Second, 100, gen, an),
		NewScenario("burst", 10*time.Second, 500, gen, an),
		NewScenario("sustained", 5*time.Minute, 50, gen, an),
	}
}

// RecordBaseline runs the scenario and returns captured metrics.
func RecordBaseline(ctx context.Context, s *Scenario) (framework.PerformanceMetrics, error) {
	collector := framework.NewMetricsCollector()
	an := analyzers.NewMemoryAnalyzer(collector)
	s.Analyzer = an
	if err := s.Run(ctx); err != nil && err != context.DeadlineExceeded {
		return framework.PerformanceMetrics{}, err
	}
	return collector.Snapshot(), nil
}
