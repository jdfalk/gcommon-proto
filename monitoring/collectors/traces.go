// file: monitoring/collectors/traces.go
// version: 1.1.0
// guid: 98f7e0de-06cc-4b2d-9d02-6dbffd1b707c

package collectors

import (
	"context"
	"fmt"
	"sync"
	"time"

	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/codes"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	"go.opentelemetry.io/otel/trace"
)

// TracesCollector manages creation of tracer providers and spans for distributed
// tracing. It wraps configuration for exporters and provides helper methods to
// start and end spans with common attributes.
type TracesCollector struct {
	mu     sync.Mutex
	tp     *sdktrace.TracerProvider
	tracer trace.Tracer
}

// NewTracesCollector creates a new collector configured to export spans to the
// provided OTLP endpoint. serviceName is used to tag spans with the service
// attribute for easier filtering in tracing backends.
func NewTracesCollector(serviceName, otlpEndpoint string) (*TracesCollector, error) {
	exp, err := otlptracehttp.New(context.Background(),
		otlptracehttp.WithEndpoint(otlpEndpoint),
		otlptracehttp.WithInsecure(), // Use WithTLSClientConfig for secure connections
	)
	if err != nil {
		return nil, fmt.Errorf("create OTLP exporter: %w", err)
	}
	res, err := resource.Merge(resource.Default(), resource.NewWithAttributes(
		"",
		attribute.String("service.name", serviceName),
	))
	if err != nil {
		return nil, fmt.Errorf("create resource: %w", err)
	}
	tp := sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(exp),
		sdktrace.WithResource(res),
	)
	otel.SetTracerProvider(tp)
	return &TracesCollector{tp: tp, tracer: tp.Tracer(serviceName)}, nil
}

// StartSpan starts a new span with the given name and returns a context that
// should be used for any child operations. Attributes can be provided to enrich
// the span.
func (t *TracesCollector) StartSpan(ctx context.Context, name string, attrs ...attribute.KeyValue) (context.Context, trace.Span) {
	return t.tracer.Start(ctx, name, trace.WithAttributes(attrs...))
}

// EndSpan ends the provided span, recording any error if present and setting a
// status based on the error.
func (t *TracesCollector) EndSpan(span trace.Span, err error) {
	if err != nil {
		span.RecordError(err)
		span.SetStatus(codes.Error, err.Error())
	}
	span.End()
}

// Shutdown flushes and closes the underlying tracer provider.
func (t *TracesCollector) Shutdown(ctx context.Context) error {
	t.mu.Lock()
	defer t.mu.Unlock()
	if t.tp == nil {
		return nil
	}
	err := t.tp.Shutdown(ctx)
	t.tp = nil
	return err
}

// Example demonstrates usage of the traces collector by creating a simple span
// and exporting it to Jaeger.
func exampleTracesCollector() {
	collector, err := NewTracesCollector("example", "http://localhost:14268/api/traces")
	if err != nil {
		panic(err)
	}
	defer collector.Shutdown(context.Background())

	ctx, span := collector.StartSpan(context.Background(), "operation", attribute.String("component", "demo"))
	time.Sleep(10 * time.Millisecond)
	_, child := collector.StartSpan(ctx, "child")
	time.Sleep(5 * time.Millisecond)
	collector.EndSpan(child, nil)
	collector.EndSpan(span, nil)
}
