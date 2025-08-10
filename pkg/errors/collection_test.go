// file: pkg/errors/collection_test.go
// version: 1.0.0
// guid: 7d8e9f10-1112-4d0e-ef01-789012345678

package errors

import (
	"context"
	"testing"
)

// TestCollectionAdd verifies that errors can be aggregated.
func TestCollectionAdd(t *testing.T) {
	c := &Collection{}
	c.Add(NewError(context.Background(), ErrCodeInternal, "one"))
	c.Add(NewError(context.Background(), ErrCodeInternal, "two"))
	if c.Len() != 2 {
		t.Fatalf("expected 2 errors, got %d", c.Len())
	}
}

// TestCollectionError ensures concatenated error messages are produced.
func TestCollectionError(t *testing.T) {
	c := &Collection{}
	c.Add(NewError(context.Background(), ErrCodeInternal, "one"))
	c.Add(NewError(context.Background(), ErrCodeInternal, "two"))
	if c.Error() != "one; two" {
		t.Fatalf("unexpected error string: %s", c.Error())
	}
}
