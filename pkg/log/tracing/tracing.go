// file: pkg/log/tracing/tracing.go
// version: 1.0.0
// guid: 378b3c31-793c-4f26-b5d7-40f41fe8f209

package tracing

import (
	"context"

	"github.com/google/uuid"
	"github.com/jdfalk/gcommon/pkg/log"
	"github.com/jdfalk/gcommon/pkg/log/middleware"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/trace"
)

const tracerName = "github.com/jdfalk/gcommon/pkg/log/tracing"

// StartSpan starts a new trace span, attaches a correlation ID, and returns a logger
// enriched with trace information.
func StartSpan(ctx context.Context, logger log.Logger, name string) (context.Context, trace.Span, log.Logger) {
	tracer := otel.Tracer(tracerName)
	ctx, span := tracer.Start(ctx, name)
	cid := uuid.New().String()
	ctx = context.WithValue(ctx, middleware.CorrelationIDKey, cid)
	span.SetAttributes(attribute.String("correlation_id", cid))
	l := logger.With(
		log.Field{Key: "trace_id", Value: span.SpanContext().TraceID().String()},
		log.Field{Key: "span_id", Value: span.SpanContext().SpanID().String()},
		log.Field{Key: "correlation_id", Value: cid},
	)
	return ctx, span, l
}

// EndSpan ends the span and records an error if present.
func EndSpan(span trace.Span, err error) {
	if err != nil {
		span.RecordError(err)
	}
	span.End()
}

// LoggerFromContext returns a logger enriched with the correlation ID from context if present.
func LoggerFromContext(ctx context.Context, logger log.Logger) log.Logger {
	if v := ctx.Value(middleware.CorrelationIDKey); v != nil {
		if id, ok := v.(string); ok {
			return logger.With(log.Field{Key: "correlation_id", Value: id})
		}
	}
	return logger
}
