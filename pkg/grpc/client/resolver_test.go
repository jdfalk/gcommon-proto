// file: pkg/grpc/client/resolver_test.go
// version: 1.0.0
// guid: b1a8dfcd-f606-4cf2-b1ce-13d6c3471dbe

package client

import (
	"testing"
)

// TestResolverWatch notifies watchers on updates.
func TestResolverWatch(t *testing.T) {
	r := NewResolver(nil)
	ch := r.Watch("svc")
	r.Update("svc", "a")
	if addr := <-ch; addr != "a" {
		t.Fatalf("expected address 'a', got %s", addr)
	}
	r.Close()
}
