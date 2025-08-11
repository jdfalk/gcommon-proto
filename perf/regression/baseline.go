// file: perf/regression/baseline.go
// version: 1.1.0
// guid: c5fa1a50-68cd-4820-9956-aa7757ccc010

// Package regression provides performance regression detection.
package regression

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path/filepath"

	"github.com/jdfalk/gcommon/perf/framework"
)

// Baseline represents stored performance metrics for comparison.
type Baseline struct {
	Metrics framework.PerformanceMetrics `json:"metrics"`
}

// Save writes the baseline to the given path.
func (b Baseline) Save(path string) error {
	data, err := json.MarshalIndent(b, "", "  ")
	if err != nil {
		return err
	}
	if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
		return err
	}
	return ioutil.WriteFile(path, data, 0o644)
}

// LoadBaseline reads baseline metrics from path.
func LoadBaseline(path string) (Baseline, error) {
	b, err := ioutil.ReadFile(path)
	if err != nil {
		return Baseline{}, err
	}
	var base Baseline
	if err := json.Unmarshal(b, &base); err != nil {
		return Baseline{}, err
	}
	return base, nil
}
