// file: perf/framework/analysis.go
// version: 1.0.0
// guid: d63d6247-5c21-4f6a-9f3a-dbf7ef42d5c4

package framework

import "time"

// TrendPoint represents a single data point in a performance trend.
type TrendPoint struct {
	Timestamp time.Time
	Metrics   PerformanceMetrics
}

// Trend stores historical metrics for analysis.
type Trend struct {
	Points []TrendPoint
}

// Add adds a new point to the trend.
func (t *Trend) Add(p TrendPoint) {
	t.Points = append(t.Points, p)
}

// Latest returns the most recent metrics.
func (t *Trend) Latest() PerformanceMetrics {
	if len(t.Points) == 0 {
		return PerformanceMetrics{}
	}
	return t.Points[len(t.Points)-1].Metrics
}

// GrowthRate calculates growth rate of operations per second.
func (t *Trend) GrowthRate() float64 {
	if len(t.Points) < 2 {
		return 0
	}
	first := t.Points[0].Metrics.Throughput.OperationsPerSecond
	last := t.Points[len(t.Points)-1].Metrics.Throughput.OperationsPerSecond
	if first == 0 {
		return 0
	}
	return (last - first) / first
}

// ExceedsLatency checks if latest latency exceeds limit.
func (t *Trend) ExceedsLatency(limit time.Duration) bool {
	return t.Latest().Latency.P99 > limit
}

// Reset clears all trend points.
func (t *Trend) Reset() {
	t.Points = nil
}

// MergeTrends combines two trends.
func MergeTrends(a, b Trend) Trend {
	merged := Trend{Points: append([]TrendPoint{}, a.Points...)}
	merged.Points = append(merged.Points, b.Points...)
	return merged
}

// RollingAverage returns average P99 latency of last n points.
func (t *Trend) RollingAverage(n int) time.Duration {
	if n <= 0 || len(t.Points) == 0 {
		return 0
	}
	if n > len(t.Points) {
		n = len(t.Points)
	}
	var sum time.Duration
	for i := len(t.Points) - n; i < len(t.Points); i++ {
		sum += t.Points[i].Metrics.Latency.P99
	}
	return sum / time.Duration(n)
}

// DetectSpike checks if latest point is spike relative to average.
func (t *Trend) DetectSpike(multiplier float64) bool {
	avg := t.RollingAverage(len(t.Points))
	latest := t.Latest().Latency.P99
	return float64(latest) > float64(avg)*multiplier
}

// Trim keeps only last n points.
func (t *Trend) Trim(n int) {
	if n >= len(t.Points) {
		return
	}
	t.Points = t.Points[len(t.Points)-n:]
}
