// file: pkg/errors/grpc_test.go
// version: 1.0.0
// guid: 4a5b6c7d-8e9f-4a0b-bcde-456789012345

package errors

import (
	"context"
	"testing"

	"google.golang.org/grpc/codes"
)

// TestToFromGRPCStatus verifies conversion between Error and gRPC status.
func TestToFromGRPCStatus(t *testing.T) {
	err := NewError(context.Background(), ErrCodeInvalidInput, "bad")
	st := ToGRPCStatus(err)
	if st.Code() != codes.InvalidArgument {
		t.Fatalf("expected InvalidArgument, got %v", st.Code())
	}
	restored := FromGRPCStatus(st)
	if restored.Code() != ErrCodeInvalidInput {
		t.Fatalf("expected ErrCodeInvalidInput, got %v", restored.Code())
	}
}
