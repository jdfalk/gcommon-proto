// file: pkg/errors/context.go
// version: 1.0.0
// guid: 3a7a7b72-4a0d-4e0e-9f9f-0b276dbe6aa2

package errors

import "context"

// ctxKey is used to store errors within a context.Context.
type ctxKey struct{}

// NewError creates a new Error with the supplied context and message.
func NewError(ctx context.Context, code ErrorCode, message string) Error {
	return NewErrorWithDetails(ctx, code, message, map[string]interface{}{})
}

// NewErrorWithDetails creates a new Error with additional details.
func NewErrorWithDetails(ctx context.Context, code ErrorCode, message string, details map[string]interface{}) Error {
	be := newBaseError(code, componentFromContext(ctx), operationFromContext(ctx), message)
	if details != nil {
		be.details = details
	}
	return be
}

// WithError stores an Error in the context.
func WithError(ctx context.Context, err Error) context.Context {
	return context.WithValue(ctx, ctxKey{}, err)
}

// FromContext retrieves an Error from the context if present.
func FromContext(ctx context.Context) Error {
	if v := ctx.Value(ctxKey{}); v != nil {
		if err, ok := v.(Error); ok {
			return err
		}
	}
	return nil
}

// componentFromContext extracts a component name from context metadata.
// In this initial implementation the component is not derived from context,
// but the hook exists for future extensibility.
func componentFromContext(ctx context.Context) string {
	return ""
}

// operationFromContext extracts an operation name from context metadata.
// This is a placeholder for future contextual operation tracking.
func operationFromContext(ctx context.Context) string {
	return ""
}
