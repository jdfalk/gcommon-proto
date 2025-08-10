// file: pkg/config/loader_test.go
// version: 1.0.0
// guid: 55555555-6666-7777-8888-999999999999

package config

import "testing"

// memorySource implements ConfigSource for tests.
type memorySource struct{ data map[string]interface{} }

// Load returns stored data.
func (m memorySource) Load() (map[string]interface{}, error) { return m.data, nil }

// TestLoaderLoad verifies loading from multiple sources.
func TestLoaderLoad(t *testing.T) {
	src1 := memorySource{data: map[string]interface{}{"a": 1}}
	src2 := memorySource{data: map[string]interface{}{"b": 2}}
	l := NewLoader(nil, src1, src2)
	cfg, err := l.Load()
	if err != nil {
		t.Fatalf("Load returned error: %v", err)
	}
	if len(cfg) != 2 {
		t.Fatalf("expected 2 keys, got %d", len(cfg))
	}
}

// TODO:
//  - Test error handling when a source fails
//  - Verify precedence when sources overlap
//  - Benchmark loading performance with many sources
//  - Add table-driven tests for various source combinations
//  - Include tests for decoder integration
//  - Mock formats to simulate parse errors
//  - Test concurrent loading scenarios
//  - Validate integration with Validator and Merger
//  - Add examples for real file sources
//  - Ensure coverage for edge cases and empty configurations
