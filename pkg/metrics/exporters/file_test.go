// file: pkg/metrics/exporters/file_test.go
// version: 1.0.0
// guid: 7189abcd-ef01-2345-6789-abcdef012345

package exporters

import (
	"context"
	"os"
	"testing"
	"time"
)

// TestFileExporter_StartStop ensures that the file exporter starts and stops
// without error and creates the output file.
func TestFileExporter_StartStop(t *testing.T) {
	tmp := t.TempDir() + "/metrics.log"
	exp := NewFileExporter(tmp, time.Millisecond)
	if err := exp.Start(context.Background()); err != nil {
		t.Fatalf("start error: %v", err)
	}
	// allow one write cycle
	time.Sleep(2 * time.Millisecond)
	stopCtx, cancel := context.WithTimeout(context.Background(), time.Millisecond)
	defer cancel()
	if err := exp.Stop(stopCtx); err != nil {
		t.Fatalf("stop error: %v", err)
	}
	if _, err := os.Stat(tmp); err != nil {
		t.Fatalf("expected file to exist: %v", err)
	}
}

// TODO: add tests for file rotation, error handling, and snapshot content.
