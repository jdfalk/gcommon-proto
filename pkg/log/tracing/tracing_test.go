// file: pkg/log/tracing/tracing_test.go
// version: 1.0.0
// guid: 2d8b204a-bde3-4f6d-9e91-673a0dada252

package tracing

import (
	"context"
	"testing"

	"github.com/jdfalk/gcommon/pkg/log/middleware"
	"github.com/jdfalk/gcommon/pkg/log/testlogger"
)

func TestStartSpan(t *testing.T) {
	tl := testlogger.New()
	ctx, span, l := StartSpan(context.Background(), tl, "op")
	if span == nil {
		t.Fatal("span is nil")
	}
	if ctx.Value(middleware.CorrelationIDKey) == nil {
		t.Fatal("correlation id missing")
	}
	l.Info("hello")
	EndSpan(span, nil)
	entries := tl.Entries()
	if len(entries) != 1 {
		t.Fatalf("expected 1 entry, got %d", len(entries))
	}
	foundTrace := false
	for _, f := range entries[0].Fields {
		if f.Key == "trace_id" {
			foundTrace = true
		}
	}
	if !foundTrace {
		t.Fatalf("trace_id field missing: %+v", entries[0])
	}
}

func TestLoggerFromContext(t *testing.T) {
	tl := testlogger.New()
	ctx := context.WithValue(context.Background(), middleware.CorrelationIDKey, "cid")
	l := LoggerFromContext(ctx, tl)
	l.Info("msg")
	entries := tl.Entries()
	if len(entries) != 1 {
		t.Fatalf("expected 1 entry, got %d", len(entries))
	}
	found := false
	for _, f := range entries[0].Fields {
		if f.Key == "correlation_id" && f.Value == "cid" {
			found = true
		}
	}
	if !found {
		t.Fatalf("correlation_id not found in fields: %+v", entries[0])
	}
}
