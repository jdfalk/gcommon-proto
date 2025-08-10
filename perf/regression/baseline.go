// file: perf/regression/baseline.go
// version: 1.0.0
// guid: c5fa1a50-68cd-4820-9956-aa7757ccc010

// Package regression provides performance regression detection.
package regression

import "github.com/jdfalk/gcommon/perf/framework"

// Baseline represents stored performance metrics for comparison.
type Baseline struct {
	Metrics framework.PerformanceMetrics
}
