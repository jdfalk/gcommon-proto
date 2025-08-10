// file: pkg/cache/serialization/json_test.go
// version: 1.0.0
// guid: d5e6f7a8-b9c0-41d2-3e4f-5a6b7c8d9e0f

package serialization

import "testing"

// TestJSONSerializer verifies JSON marshal/unmarshal.
func TestJSONSerializer(t *testing.T) {
	s := JSON{}
	type sample struct{ A int }
	data, err := s.Marshal(sample{A: 1})
	if err != nil {
		t.Fatalf("marshal: %v", err)
	}
	var out sample
	if err := s.Unmarshal(data, &out); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	if out.A != 1 {
		t.Fatalf("expected 1 got %d", out.A)
	}
}
