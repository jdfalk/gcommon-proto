// file: monitoring/exporters/otlp_test.go
// version: 1.2.0
// guid: 123e4567-e89b-12d3-a456-426614174001

package exporters

import (
	"context"
	"testing"

	sdktrace "go.opentelemetry.io/otel/sdk/trace"
)

// TestOTLPExporter verifies exporter integration with tracer provider.
func TestOTLPExporter(t *testing.T) {
	exp, err := NewOTLPExporter("http://localhost:4318/v1/traces")
	if err != nil {
		t.Fatalf("NewOTLPExporter: %v", err)
	}

	tp := sdktrace.NewTracerProvider()
	exp.Export(tp)

	ctx := context.Background()
	if err := exp.Shutdown(ctx); err != nil {
		t.Errorf("shutdown error: %v", err)
	}
}
