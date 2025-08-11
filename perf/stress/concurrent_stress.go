// file: perf/stress/concurrent_stress.go
// version: 1.1.0
// guid: fe674fd3-b43c-406f-ba93-854dfac52654

package stress

import (
	"context"
	"sync"
	"time"
)

// SpawnWorkers launches goroutines to test concurrency limits.
func SpawnWorkers(workers int, work func()) {
	var wg sync.WaitGroup
	wg.Add(workers)
	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			work()
		}()
	}
	wg.Wait()
}

// RunWithContext executes workers until context cancellation.
func RunWithContext(ctx context.Context, workers int, work func()) {
	var wg sync.WaitGroup
	wg.Add(workers)
	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			for {
				select {
				case <-ctx.Done():
					return
				default:
					work()
				}
			}
		}()
	}
	wg.Wait()
}

// ThrottleWorkers limits execution rate of work function.
func ThrottleWorkers(workers int, interval time.Duration, work func()) {
	var wg sync.WaitGroup
	wg.Add(workers)
	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			ticker := time.NewTicker(interval)
			defer ticker.Stop()
			for range ticker.C {
				work()
			}
		}()
	}
	wg.Wait()
}
