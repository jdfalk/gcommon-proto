// file: monitoring/exporters/jaeger_test.go
// version: 1.0.0
// guid: 5d7e0c9a-1b2d-4e3f-9a4b-6c7d8e9f0a1b

package exporters

import (
	"context"
	"testing"

	sdktrace "go.opentelemetry.io/otel/sdk/trace"
)

// TestJaegerExporter verifies exporter integration with tracer provider.
func TestJaegerExporter(t *testing.T) {
	exp, err := NewJaegerExporter("http://localhost:14268/api/traces")
	if err != nil {
		t.Fatalf("NewJaegerExporter: %v", err)
	}
	tp := sdktrace.NewTracerProvider()
	exp.Export(tp)
	if err := exp.Shutdown(context.Background()); err != nil {
		t.Fatalf("Shutdown: %v", err)
	}
}
