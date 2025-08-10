// file: perf/regression/comparison.go
// version: 1.0.0
// guid: 40ae2f0e-0dda-4c37-85a9-41710f07aa51

package regression

// CompareMetrics compares current metrics with baseline.
func CompareMetrics(current, baseline float64) float64 {
	return current - baseline
}
