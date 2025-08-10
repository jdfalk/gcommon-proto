// file: perf/framework/reporting.go
// version: 1.0.0
// guid: cae403f2-401c-4d19-b1de-b6e9cd16df1e

package framework

import "encoding/json"

// Report wraps performance metrics for output.
type Report struct {
	Metrics PerformanceMetrics `json:"metrics"`
}

// GenerateReport returns metrics as formatted JSON.
func GenerateReport(m PerformanceMetrics) ([]byte, error) {
	r := Report{Metrics: m}
	return json.MarshalIndent(r, "", "  ")
}
