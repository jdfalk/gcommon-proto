// file: pkg/errors/formatting_test.go
// version: 1.0.0
// guid: 9f10a1b2-1314-4e10-f123-901234567890

package errors

import (
	"context"
	"strings"
	"testing"
)

// TestFormatError ensures formatted output contains key information.
func TestFormatError(t *testing.T) {
	err := WrapWithCode(NewError(context.Background(), ErrCodeInternal, "boom"), ErrCodeInternal, "comp", "op")
	err = WrapWithDetails(err, map[string]interface{}{"k": "v"})
	out := FormatError(err)
	if !strings.Contains(out, "comp") || !strings.Contains(out, "k=v") {
		t.Fatalf("unexpected format: %s", out)
	}
}
