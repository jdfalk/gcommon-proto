// file: pkg/plugins/examples/provider/reverse/reverse_test.go
// version: 1.0.0
// guid: 2f14309d-a2ae-4d47-b1a7-0c6c5c28b2b5

package reverse

import "testing"

func TestReverseProvider(t *testing.T) {
	p := New()
	provider := p.GetProvider().(func(string) string)
	if got := provider("abc"); got != "cba" {
		t.Fatalf("expected cba, got %s", got)
	}
}
