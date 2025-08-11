// file: cmd/microservice-template/main_test.go
// version: 1.0.0
// guid: 5d1bbb30-719e-415b-a87b-45f19fa281b0

package main

import (
	"os"
	"path/filepath"
	"testing"
)

func TestCopyTemplate(t *testing.T) {
	src := filepath.Join("..", "..", "templates", "basic-api-service")
	dst := t.TempDir()
	if err := copyTemplate(src, dst, "basic-api-service", "example-service"); err != nil {
		t.Fatalf("copyTemplate failed: %v", err)
	}
	// Ensure a known file exists in target
	if _, err := os.Stat(filepath.Join(dst, "main.go")); err != nil {
		t.Fatalf("expected file not found: %v", err)
	}
}
