// file: pkg/metrics/grpc_snapshot.go
// version: 1.0.0
// guid: 3f4e5d6c-7b8a-9c0d-1e2f-3a4b5c6d7e8f

package metrics

// grpcSnapshot implements Snapshot interface for gRPC-based metrics
type grpcSnapshot struct {
	registry *grpcRegistry
}

// Counters returns all counters in the snapshot
func (s *grpcSnapshot) Counters() map[string]float64 {
	counters := make(map[string]float64)
	for key, metric := range s.registry.metrics {
		if counter, ok := metric.(*grpcCounter); ok {
			name := s.extractNameFromKey(key)
			counters[name] = counter.Value()
		}
	}
	return counters
}

// Gauges returns all gauges in the snapshot
func (s *grpcSnapshot) Gauges() map[string]float64 {
	gauges := make(map[string]float64)
	for key, metric := range s.registry.metrics {
		if gauge, ok := metric.(*grpcGauge); ok {
			name := s.extractNameFromKey(key)
			gauges[name] = gauge.Value()
		}
	}
	return gauges
}

// Histograms returns all histograms in the snapshot
func (s *grpcSnapshot) Histograms() map[string]HistogramSnapshot {
	histograms := make(map[string]HistogramSnapshot)
	for key, metric := range s.registry.metrics {
		if histogram, ok := metric.(*grpcHistogram); ok {
			name := s.extractNameFromKey(key)
			histograms[name] = histogram.Snapshot()
		}
	}
	return histograms
}

// Summaries returns all summaries in the snapshot
func (s *grpcSnapshot) Summaries() map[string]SummarySnapshot {
	summaries := make(map[string]SummarySnapshot)
	for key, metric := range s.registry.metrics {
		if summary, ok := metric.(*grpcSummary); ok {
			name := s.extractNameFromKey(key)
			summaries[name] = summary.Snapshot()
		}
	}
	return summaries
}

// extractNameFromKey extracts the metric name from the registry key
// Key format: "name:type"
func (s *grpcSnapshot) extractNameFromKey(key string) string {
	for i := len(key) - 1; i >= 0; i-- {
		if key[i] == ':' {
			return key[:i]
		}
	}
	return key
}
