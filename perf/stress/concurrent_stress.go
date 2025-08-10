// file: perf/stress/concurrent_stress.go
// version: 1.0.0
// guid: fe674fd3-b43c-406f-ba93-854dfac52654

package stress

import "sync"

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
