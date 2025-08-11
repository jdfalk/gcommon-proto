// file: perf/framework/reporting.go
// version: 1.1.0
// guid: cae403f2-401c-4d19-b1de-b6e9cd16df1e

package framework

import (
	"encoding/json"
	"errors"
	"io/ioutil"
	"os"
	"path/filepath"
	"time"
)

// Report wraps performance metrics for output.
type Report struct {
	GeneratedAt time.Time          `json:"generated_at"`
	Metrics     PerformanceMetrics `json:"metrics"`
}

// GenerateReport returns metrics as formatted JSON.
func GenerateReport(m PerformanceMetrics) ([]byte, error) {
	r := Report{GeneratedAt: time.Now(), Metrics: m}
	return json.MarshalIndent(r, "", "  ")
}

// SaveReport writes metrics to the specified path in JSON format.
func SaveReport(path string, m PerformanceMetrics) error {
	data, err := GenerateReport(m)
	if err != nil {
		return err
	}
	if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
		return err
	}
	return ioutil.WriteFile(path, data, 0o644)
}

// LoadReport loads metrics from a JSON file.
func LoadReport(path string) (PerformanceMetrics, error) {
	b, err := ioutil.ReadFile(path)
	if err != nil {
		return PerformanceMetrics{}, err
	}
	var r Report
	if err := json.Unmarshal(b, &r); err != nil {
		return PerformanceMetrics{}, err
	}
	return r.Metrics, nil
}

// CompareReports returns the difference between two metrics.
func CompareReports(a, b PerformanceMetrics) PerformanceMetrics {
	mc := NewMetricsCollector()
	mc.RecordLatency(a.Latency.Mean)
	mc.RecordLatency(b.Latency.Mean)
	mc.RecordThroughput(int64(a.Throughput.BytesPerSecond-b.Throughput.BytesPerSecond),
		int64(a.Throughput.OperationsPerSecond-b.Throughput.OperationsPerSecond))
	if a.ErrorRate.Errors > b.ErrorRate.Errors {
		mc.errors = a.ErrorRate.Errors - b.ErrorRate.Errors
	} else {
		mc.errors = b.ErrorRate.Errors - a.ErrorRate.Errors
	}
	return mc.Snapshot()
}

// ValidateReport ensures report file contains valid JSON.
func ValidateReport(path string) error {
	b, err := ioutil.ReadFile(path)
	if err != nil {
		return err
	}
	var r Report
	if err := json.Unmarshal(b, &r); err != nil {
		return err
	}
	if r.GeneratedAt.IsZero() {
		return errors.New("missing generated_at")
	}
	return nil
}
