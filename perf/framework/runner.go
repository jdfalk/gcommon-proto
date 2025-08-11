// file: perf/framework/runner.go
// version: 0.1.0
// guid: 39830806-921a-4985-ba8e-37e2a166d00a

package framework

import (
	"context"
	"errors"
	"time"
)

// Runner coordinates execution of benchmarks, load tests, and stress tests. It
// is intended to be extended with more sophisticated scheduling and reporting
// capabilities. The current implementation is a placeholder that provides the
// structure for future work.
type Runner struct {
	// ctx allows coordinated cancellation of running tests.
	ctx context.Context
	// cancel stops any running operations when invoked.
	cancel context.CancelFunc
	// metrics holds aggregated performance metrics from executed tests.
	metrics PerformanceMetrics
	// TODO: Add fields for configuration, test suites, and reporting sinks.
}

// NewRunner creates a new Runner with a background context. Callers can supply
// their own context to integrate with larger systems if necessary.
func NewRunner(parent context.Context) *Runner {
	if parent == nil {
		parent = context.Background()
	}
	ctx, cancel := context.WithCancel(parent)
	return &Runner{ctx: ctx, cancel: cancel, metrics: NewPerformanceMetrics()}
}

// Run executes a set of named test functions sequentially. Each function should
// perform its work and return an error if it fails. The runner collects metrics
// between tests and stops execution if a test returns an error.
func (r *Runner) Run(tests map[string]func(context.Context) error) error {
	if tests == nil {
		return errors.New("tests map is nil")
	}
	for name, fn := range tests {
		if fn == nil {
			return errors.New("nil test function: " + name)
		}
		start := time.Now()
		if err := fn(r.ctx); err != nil {
			return err
		}
		_ = start // TODO: Record elapsed time into metrics.
		// TODO: Aggregate metrics for each test execution.
		// TODO: Implement logging and reporting hooks per test.
	}
	return nil
}

// Metrics returns the aggregated metrics collected during all executed tests.
func (r *Runner) Metrics() PerformanceMetrics {
	// TODO: Return a copy of metrics to prevent external modification.
	return r.metrics
}

// Stop cancels any running tests and prevents further execution.
func (r *Runner) Stop() {
	// TODO: Flush any buffered metrics or logs before stopping.
	if r.cancel != nil {
		r.cancel()
	}
}

// Reset clears accumulated metrics and establishes a new context for additional
// test executions.
func (r *Runner) Reset() {
	if r.cancel != nil {
		r.cancel()
	}
	r.ctx, r.cancel = context.WithCancel(context.Background())
	r.metrics.Reset()
	// TODO: Reset internal test state and configuration once implemented.
}

// RegisterBenchmark registers a benchmark with the runner. This is a placeholder
// demonstrating how benchmarks might be added dynamically.
func (r *Runner) RegisterBenchmark(name string, fn func(context.Context) error) {
	// TODO: Store benchmarks in internal structures for execution ordering.
	_ = name
	_ = fn
}

// RunAsync executes tests in a separate goroutine, returning immediately. Errors
// are sent to the provided channel. This skeleton is intentionally simple.
func (r *Runner) RunAsync(tests map[string]func(context.Context) error, errs chan<- error) {
	go func() {
		errs <- r.Run(tests)
	}()
}

// TODO: Add support for concurrent test execution with worker pools.
// TODO: Add CLI integration for running benchmarks from the command line.
// TODO: Add result persistence to disk for historical comparison.
// TODO: Integrate with regression package once completed.
