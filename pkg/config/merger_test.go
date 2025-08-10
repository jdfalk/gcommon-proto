// file: pkg/config/merger_test.go
// version: 1.0.0
// guid: 66666666-7777-8888-9999-aaaaaaaaaaaa

package config

import "testing"

// TestMergerMerge verifies precedence ordering.
func TestMergerMerge(t *testing.T) {
	low := map[string]interface{}{"a": 1, "b": 1}
	high := map[string]interface{}{"b": 2, "c": 3}
	m := NewMerger(low, high)
	result := m.Merge()
	if result["b"].(int) != 2 {
		t.Fatalf("expected high precedence value 2, got %v", result["b"])
	}
	if len(result) != 3 {
		t.Fatalf("expected 3 keys, got %d", len(result))
	}
}

// TODO:
//  - Add tests for more than two configuration maps
//  - Verify behavior with empty maps and nil inputs
//  - Ensure deep merging for nested structures
//  - Test performance with large configurations
//  - Include tests for different data types and conflicts
//  - Document merge algorithm and precedence rules
//  - Consider options for conflict resolution strategies
//  - Add fuzz testing for robustness
//  - Explore merging slice and array values
//  - Validate integration with Loader and Watcher
