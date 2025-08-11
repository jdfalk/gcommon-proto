// file: perf/benchmarks/queue_bench.go
// version: 1.1.0
// guid: b40d8fa6-78a7-4405-a2bb-94865f4c5a36

package benchmarks

import (
	"strconv"
	"sync"
	"testing"
)

// BenchmarkQueuePublishing measures message publishing throughput.
func BenchmarkQueuePublishing(b *testing.B) {
	ch := make(chan int, b.N)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ch <- i
	}
	close(ch)
}

// BenchmarkQueueConsumption measures message consumption latency.
func BenchmarkQueueConsumption(b *testing.B) {
	ch := make(chan int, b.N)
	for i := 0; i < b.N; i++ {
		ch <- i
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		<-ch
	}
}

// BenchmarkQueueDepthHandling measures queue depth handling.
func BenchmarkQueueDepthHandling(b *testing.B) {
	for depth := 1; depth <= 1024; depth *= 2 {
		b.Run("depth"+strconv.Itoa(depth), func(b *testing.B) {
			ch := make(chan int, depth)
			for i := 0; i < b.N; i++ {
				select {
				case ch <- i:
				default:
					<-ch
					ch <- i
				}
			}
		})
	}
}

// BenchmarkQueueConcurrent measures concurrent producer/consumer performance.
func BenchmarkQueueConcurrent(b *testing.B) {
	ch := make(chan int, 1024)
	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		defer wg.Done()
		for i := 0; i < b.N; i++ {
			ch <- i
		}
		close(ch)
	}()
	go func() {
		defer wg.Done()
		for range ch {
		}
	}()
	wg.Wait()
}
