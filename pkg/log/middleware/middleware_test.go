// file: pkg/log/middleware/middleware_test.go
// version: 1.0.0
// guid: c0d1e2f3-a4b5-46c7-89d0-0123456789ff

package middleware

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/jdfalk/gcommon/pkg/log"
)

// stubLogger captures log entries for assertions.
type stubLogger struct {
	entries []log.LogEntry
}

func (s *stubLogger) Debug(msg string, fields ...log.Field)                             {}
func (s *stubLogger) DebugContext(ctx context.Context, msg string, fields ...log.Field) {}
func (s *stubLogger) Info(msg string, fields ...log.Field) {
	s.entries = append(s.entries, log.LogEntry{Message: msg, Fields: toMap(fields)})
}
func (s *stubLogger) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	s.Info(msg, fields...)
}
func (s *stubLogger) Warn(msg string, fields ...log.Field)                              {}
func (s *stubLogger) WarnContext(ctx context.Context, msg string, fields ...log.Field)  {}
func (s *stubLogger) Error(msg string, fields ...log.Field)                             {}
func (s *stubLogger) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {}
func (s *stubLogger) Fatal(msg string, fields ...log.Field)                             {}
func (s *stubLogger) FatalContext(ctx context.Context, msg string, fields ...log.Field) {}
func (s *stubLogger) With(fields ...log.Field) log.Logger                               { return s }
func (s *stubLogger) WithContext(ctx context.Context) log.Logger                        { return s }
func (s *stubLogger) SetLevel(level log.Level)                                          {}
func (s *stubLogger) GetLevel() log.Level                                               { return log.InfoLevel }

func toMap(fields []log.Field) map[string]interface{} {
	m := make(map[string]interface{}, len(fields))
	for _, f := range fields {
		m[f.Key] = f.Value
	}
	return m
}

func TestHTTPMiddleware(t *testing.T) {
	logger := &stubLogger{}
	h := HTTPMiddleware(logger, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(201)
	}))
	req := httptest.NewRequest(http.MethodGet, "/test", nil)
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)
	if rec.Code != 201 {
		t.Fatalf("expected status 201, got %d", rec.Code)
	}
	if len(logger.entries) != 1 {
		t.Fatalf("expected one log entry, got %d", len(logger.entries))
	}
	if logger.entries[0].Fields["status"].(int) != 201 {
		t.Fatalf("expected status field 201, got %v", logger.entries[0].Fields["status"])
	}
}

func TestHTTPCorrelationMiddleware(t *testing.T) {
	h := HTTPCorrelationMiddleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if CorrelationIDFromContext(r.Context()) == "" {
			t.Fatal("correlation id missing")
		}
		w.WriteHeader(200)
	}))
	req := httptest.NewRequest(http.MethodGet, "/test", nil)
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)
	if rec.Code != 200 {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
}
