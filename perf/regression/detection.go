// file: perf/regression/detection.go
// version: 1.1.0
// guid: 610f86d8-1b34-41e3-b20c-86161c182f6d

package regression

import "github.com/jdfalk/gcommon/perf/framework"

// DetectRegression returns true if a regression is detected.
func DetectRegression(current, baseline framework.PerformanceMetrics, threshold float64) bool {
	diff := CompareMetrics(current, baseline)
	return diff.ErrorRate.ErrorRate > threshold
}
