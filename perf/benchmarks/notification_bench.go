// file: perf/benchmarks/notification_bench.go
// version: 1.1.0
// guid: 76f64712-9442-44d5-9f74-360028e0b6e0

package benchmarks

import (
	"strconv"
	"sync"
	"testing"
)

// BenchmarkNotificationSend measures notification send throughput.
func BenchmarkNotificationSend(b *testing.B) {
	ch := make(chan string, b.N)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ch <- "msg"
	}
	close(ch)
}

// BenchmarkNotificationDelivery measures delivery latency.
func BenchmarkNotificationDelivery(b *testing.B) {
	ch := make(chan string, 1)
	go func() {
		for msg := range ch {
			_ = msg
		}
	}()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ch <- "msg"
	}
	close(ch)
}

// BenchmarkNotificationQueueDepth measures queue depth handling.
func BenchmarkNotificationQueueDepth(b *testing.B) {
	for depth := 1; depth <= 1024; depth *= 2 {
		b.Run("depth"+strconv.Itoa(depth), func(b *testing.B) {
			ch := make(chan string, depth)
			for i := 0; i < b.N; i++ {
				select {
				case ch <- "msg":
				default:
					<-ch
					ch <- "msg"
				}
			}
		})
	}
}

// BenchmarkConcurrentNotifications measures concurrent notification handling.
func BenchmarkConcurrentNotifications(b *testing.B) {
	ch := make(chan string, 1024)
	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		defer wg.Done()
		for i := 0; i < b.N; i++ {
			ch <- "msg"
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
