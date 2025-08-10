// file: pkg/errors/context_test.go
// version: 1.0.0
// guid: 8e9f1011-1213-4e0f-f012-890123456789

package errors

import (
	"context"
	"testing"
)

// TestContextStorage verifies storing and retrieving errors in context.
func TestContextStorage(t *testing.T) {
	err := NewError(context.Background(), ErrCodeInternal, "ctx")
	ctx := WithError(context.Background(), err)
	retrieved := FromContext(ctx)
	if retrieved == nil || retrieved.Error() != "ctx" {
		t.Fatalf("expected to retrieve error")
	}
}

// TestContextStorageMissing verifies retrieval when no error stored.
func TestContextStorageMissing(t *testing.T) {
	if FromContext(context.Background()) != nil {
		t.Fatalf("expected nil error")
	}
}
