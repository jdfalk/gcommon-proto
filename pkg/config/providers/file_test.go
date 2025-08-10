// file: pkg/config/providers/file_test.go
// version: 1.0.0
// guid: 02020202-0202-0202-0202-020202020202

package providers

import (
	"os"
	"testing"
)

// TestFileProvider basic set/get
func TestFileProvider(t *testing.T) {
	f, err := os.CreateTemp("", "cfg*.json")
	if err != nil {
		t.Fatalf("tmp error: %v", err)
	}
	f.Close()
	defer os.Remove(f.Name())
	p, err := NewFileProvider(f.Name())
	if err != nil {
		t.Fatalf("new error: %v", err)
	}
	if err := p.Set("key", "value"); err != nil {
		t.Fatalf("set error: %v", err)
	}
	v, err := p.Get("key")
	if err != nil || v.(string) != "value" {
		t.Fatalf("unexpected get: %v %v", v, err)
	}
}

// TODO: Add tests for persistence across reloads
// TODO: Add tests for concurrent access

// EOF
