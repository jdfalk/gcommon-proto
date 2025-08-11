// file: perf/load/scenarios/scenario.go
// version: 0.1.0
// guid: aa2b23dd-b4f8-4fe8-a2b0-506afa03cc86

package scenarios

import (
	"context"
	"errors"
	"time"

	"github.com/jdfalk/gcommon/perf/load/analyzers"
	"github.com/jdfalk/gcommon/perf/load/generators"
)

// Scenario defines a load test scenario using a generator and analyzer.
type Scenario struct {
	// Name identifies the scenario in reports.
	Name string
	// Duration specifies how long the scenario should run.
	Duration time.Duration
	// Concurrency indicates how many workers to start.
	Concurrency int
	// Generator produces load against the system under test.
	Generator generators.Generator
	// Analyzer processes metrics produced by the generator.
	Analyzer analyzers.Analyzer
}

// Run executes the scenario. This placeholder invokes the generator and feeds
// a single metric sample to the analyzer.
func (s *Scenario) Run(ctx context.Context) error {
	if s.Generator == nil || s.Analyzer == nil {
		return errors.New("missing generator or analyzer")
	}
	if err := s.Generator.Start(ctx, s.Concurrency); err != nil {
		return err
	}
	defer s.Generator.Stop()
	select {
	case <-ctx.Done():
		return ctx.Err()
	case m := <-s.Generator.Metrics():
		return s.Analyzer.AddSample(m)
	}
}

// TODO: Support multiple metric samples and duration-based execution.
// TODO: Add scenario configuration loading from files.
