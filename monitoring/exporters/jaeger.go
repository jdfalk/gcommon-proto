// file: monitoring/exporters/otlp.go
// version: 1.2.0
// guid: 123e4567-e89b-12d3-a456-426614174000

package exporters

import (
	"context"

	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	"go.opentelemetry.io/otel/sdk/trace"
)

// OTLPExporter wraps the OpenTelemetry OTLP HTTP exporter.
type OTLPExporter struct {
	exporter trace.SpanExporter
}

// NewOTLPExporter creates a new exporter that sends data to the provided
// OTLP collector endpoint URL.
func NewOTLPExporter(endpoint string) (*OTLPExporter, error) {
	exp, err := otlptracehttp.New(context.Background(),
		otlptracehttp.WithEndpoint(endpoint),
		otlptracehttp.WithInsecure(), // Use WithTLSClientConfig for secure connections
	)
	if err != nil {
		return nil, err
	}
	return &OTLPExporter{exporter: exp}, nil
}

// Export spans using the provided tracer provider.
func (e *OTLPExporter) Export(tp *sdktrace.TracerProvider) {
	tp.RegisterSpanProcessor(sdktrace.NewBatchSpanProcessor(e.exporter))
}

// Shutdown closes the exporter.
func (e *OTLPExporter) Shutdown(ctx context.Context) error {
	return e.exporter.Shutdown(ctx)
}
