// file: monitoring/collectors/traces_test.go
// version: 1.0.0
// guid: 2c7c5a2e-bd4c-43bb-a19e-42e1b8d5c0de

package collectors

import (
	"context"
	"testing"
	"time"

	"go.opentelemetry.io/otel/attribute"
)

// TestTracesCollectorStartEnd ensures spans can be started and ended without error.
func TestTracesCollectorStartEnd(t *testing.T) {
	tc, err := NewTracesCollector("test-service", "http://localhost:14268/api/traces")
	if err != nil {
		t.Fatalf("NewTracesCollector: %v", err)
	}
	defer tc.Shutdown(context.Background())

	ctx, span := tc.StartSpan(context.Background(), "parent", attribute.String("k", "v"))
	time.Sleep(1 * time.Millisecond)
	ctx2, child := tc.StartSpan(ctx, "child")
	time.Sleep(1 * time.Millisecond)
	tc.EndSpan(child, nil)
	tc.EndSpan(span, nil)
	if ctx2 == nil {
		t.Fatalf("expected non-nil context from child span")
	}
}
