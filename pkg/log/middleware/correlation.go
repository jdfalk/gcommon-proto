// file: pkg/log/middleware/correlation.go
// version: 1.0.0
// guid: f4e3d2c1-b0a9-48f7-8e65-dcba98765432

package middleware

import (
	"context"
	"github.com/google/uuid"
	"net/http"
)

// ContextKey is the type used for correlation ID context keys.
type ContextKey string

const (
	// CorrelationIDKey is the key used to store correlation IDs in contexts.
	CorrelationIDKey ContextKey = "correlation_id"
)

// WithCorrelationID returns a new context with a correlation ID.
func WithCorrelationID(ctx context.Context) context.Context {
	if id, ok := ctx.Value(CorrelationIDKey).(string); ok && id != "" {
		return ctx
	}
	return context.WithValue(ctx, CorrelationIDKey, uuid.New().String())
}

// CorrelationIDFromContext extracts the correlation ID from context.
func CorrelationIDFromContext(ctx context.Context) string {
	if id, ok := ctx.Value(CorrelationIDKey).(string); ok {
		return id
	}
	return ""
}

// HTTPCorrelationMiddleware adds correlation IDs to incoming HTTP requests.
func HTTPCorrelationMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		id := r.Header.Get("X-Correlation-ID")
		if id == "" {
			id = uuid.New().String()
		}
		ctx := context.WithValue(r.Context(), CorrelationIDKey, id)
		next.ServeHTTP(w, r.WithContext(ctx))
	})
}
