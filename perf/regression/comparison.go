// file: perf/regression/comparison.go
// version: 1.1.0
// guid: 40ae2f0e-0dda-4c37-85a9-41710f07aa51

package regression

import "github.com/jdfalk/gcommon/perf/framework"

// CompareMetrics compares current metrics with baseline and returns difference metrics.
func CompareMetrics(current, baseline framework.PerformanceMetrics) framework.PerformanceMetrics {
	return framework.CombineMetrics(current, baseline)
}
