// file: monitoring/exporters/jaeger.go
// version: 1.1.0
// guid: 123e4567-e89b-12d3-a456-426614174000

package exporters

import (
	"context"

	"go.opentelemetry.io/otel/exporters/jaeger"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
)

// JaegerExporter wraps the OpenTelemetry Jaeger exporter.
type JaegerExporter struct {
	exporter *jaeger.Exporter
}

// NewJaegerExporter creates a new exporter that sends data to the provided
// collector endpoint URL.
func NewJaegerExporter(endpoint string) (*JaegerExporter, error) {
	exp, err := jaeger.New(jaeger.WithCollectorEndpoint(jaeger.WithEndpoint(endpoint)))
	if err != nil {
		return nil, err
	}
	return &JaegerExporter{exporter: exp}, nil
}

// Export spans using the provided tracer provider.
func (e *JaegerExporter) Export(tp *sdktrace.TracerProvider) {
	tp.RegisterSpanProcessor(sdktrace.NewBatchSpanProcessor(e.exporter))
}

// Shutdown closes the exporter.
func (e *JaegerExporter) Shutdown(ctx context.Context) error {
	return e.exporter.Shutdown(ctx)
}
