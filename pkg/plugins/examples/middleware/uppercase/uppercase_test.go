// file: pkg/plugins/examples/middleware/uppercase/uppercase_test.go
// version: 1.0.0
// guid: 3e3f211e-2587-4ece-9432-2560f5d9e5ce

package uppercase

import (
	"context"
	"testing"
)

func TestUppercaseMiddleware(t *testing.T) {
	p := New()
	out, err := p.Handle(context.Background(), "abc")
	if err != nil {
		t.Fatalf("handle error: %v", err)
	}
	if out != "ABC" {
		t.Fatalf("expected ABC, got %v", out)
	}
}
