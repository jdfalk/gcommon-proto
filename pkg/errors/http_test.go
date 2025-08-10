// file: pkg/errors/http_test.go
// version: 1.0.0
// guid: 5b6c7d8e-9f10-4b0c-cdef-567890123456

package errors

import (
	"context"
	"net/http/httptest"
	"testing"
)

// TestWriteHTTPError ensures HTTP responses use proper status codes and body.
func TestWriteHTTPError(t *testing.T) {
	err := NewError(context.Background(), ErrCodeNotFound, "missing")
	rec := httptest.NewRecorder()
	WriteHTTPError(rec, err)
	if rec.Code != 404 {
		t.Fatalf("expected 404, got %d", rec.Code)
	}
}

// TestToHTTPStatus verifies mapping between error codes and HTTP statuses.
func TestToHTTPStatus(t *testing.T) {
	cases := []struct {
		code     ErrorCode
		expected int
	}{
		{ErrCodeInvalidInput, 400},
		{ErrCodeNotFound, 404},
		{ErrCodeAlreadyExists, 409},
		{ErrCodeTimeout, 504},
		{ErrCodeUnauthorized, 401},
		{ErrCodeForbidden, 403},
	}
	for _, c := range cases {
		err := NewError(context.Background(), c.code, "msg")
		status := ToHTTPStatus(err)
		if status != c.expected {
			t.Fatalf("unexpected status for %v: got %d", c.code, status)
		}
	}
}
