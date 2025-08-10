// file: perf/regression/detection.go
// version: 1.0.0
// guid: 610f86d8-1b34-41e3-b20c-86161c182f6d

package regression

// DetectRegression returns true if a regression is detected.
func DetectRegression(diff float64, threshold float64) bool {
	return diff > threshold
}
