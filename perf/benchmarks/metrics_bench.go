// file: perf/benchmarks/metrics_bench.go
// version: 1.1.0
// guid: ada49c78-cfee-48e9-8940-19fa6aba772b

package benchmarks

import (
	"testing"
	"time"

	"github.com/jdfalk/gcommon/perf/framework"
)

// BenchmarkMetricCollection measures metric collection overhead.
func BenchmarkMetricCollection(b *testing.B) {
	c := framework.NewMetricsCollector()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		c.RecordLatency(time.Millisecond)
	}
}

// BenchmarkMetricAggregation measures metric aggregation performance.
func BenchmarkMetricAggregation(b *testing.B) {
	c := framework.NewMetricsCollector()
	for i := 0; i < 1000; i++ {
		c.RecordLatency(time.Duration(i) * time.Microsecond)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = c.Snapshot()
	}
}

// BenchmarkMetricExport measures export performance.
func BenchmarkMetricExport(b *testing.B) {
	m := framework.PerformanceMetrics{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		if _, err := framework.GenerateReport(m); err != nil {
			b.Fatalf("report: %v", err)
		}
	}
}

// BenchmarkConcurrentMetricRecording measures concurrent metric recording.
func BenchmarkConcurrentMetricRecording(b *testing.B) {
	c := framework.NewMetricsCollector()
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			c.RecordLatency(time.Millisecond)
		}
	})
	_ = c.Snapshot()
}
