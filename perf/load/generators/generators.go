// file: perf/load/generators/generators.go
// version: 1.1.0
// guid: 9e819fd0-172f-46fd-9a3c-1ff30221fceb

// Package generators provides load generators.
package generators

import (
	"context"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/perf/framework"
)

// Generator produces load against the system under test.
type Generator interface {
	Start(ctx context.Context, workers int) error
	Stop() error
	Metrics() <-chan framework.PerformanceMetrics
}

// BasicGenerator implements a simple work generator using a function callback.
type BasicGenerator struct {
	work     func() framework.PerformanceMetrics
	metricsC chan framework.PerformanceMetrics
	cancel   context.CancelFunc
	wg       sync.WaitGroup
}

// NewBasicGenerator creates a generator using provided work function.
func NewBasicGenerator(work func() framework.PerformanceMetrics) *BasicGenerator {
	return &BasicGenerator{work: work, metricsC: make(chan framework.PerformanceMetrics, 100)}
}

// Start begins generating load with given number of workers.
func (g *BasicGenerator) Start(ctx context.Context, workers int) error {
	ctx, g.cancel = context.WithCancel(ctx)
	g.wg.Add(workers)
	for i := 0; i < workers; i++ {
		go func() {
			defer g.wg.Done()
			ticker := time.NewTicker(10 * time.Millisecond)
			defer ticker.Stop()
			for {
				select {
				case <-ctx.Done():
					return
				case <-ticker.C:
					g.metricsC <- g.work()
				}
			}
		}()
	}
	return nil
}

// Stop halts all workers.
func (g *BasicGenerator) Stop() error {
	if g.cancel != nil {
		g.cancel()
	}
	g.wg.Wait()
	close(g.metricsC)
	return nil
}

// Metrics returns channel of performance metrics produced by workers.
func (g *BasicGenerator) Metrics() <-chan framework.PerformanceMetrics {
	return g.metricsC
}
