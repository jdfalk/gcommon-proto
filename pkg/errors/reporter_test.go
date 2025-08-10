// file: pkg/errors/reporter_test.go
// version: 1.0.0
// guid: 6c7d8e9f-1011-4c0d-def0-678901234567

package errors

import (
	"context"
	"testing"
)

// TestMemoryReporter verifies basic statistics collection.
func TestMemoryReporter(t *testing.T) {
	r := NewMemoryReporter()
	r.ReportError(context.Background(), NewError(context.Background(), ErrCodeInternal, "boom"))
	r.ReportErrorWithTags(context.Background(), NewError(context.Background(), ErrCodeInternal, "boom2"), map[string]string{"env": "test"})
	stats := r.GetErrorStats()
	if stats.TotalErrors != 2 {
		t.Fatalf("expected 2, got %d", stats.TotalErrors)
	}
	if stats.ErrorsByCode[ErrCodeInternal] != 2 {
		t.Fatalf("expected code count 2")
	}
	r.Reset()
	stats = r.GetErrorStats()
	if stats.TotalErrors != 0 {
		t.Fatalf("expected reset stats")
	}
}
