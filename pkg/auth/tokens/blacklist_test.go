// file: pkg/auth/tokens/blacklist_test.go
// version: 1.0.0
// guid: 4f5e6d7c-8b9a-1c2d-3e4f-5a6b7c8d9e0f

package tokens

import (
	"testing"
	"time"
)

func TestBlacklist(t *testing.T) {
	bl := NewBlacklist()
	bl.Revoke("t1", time.Now().Add(time.Second))
	if !bl.IsRevoked("t1") {
		t.Fatal("expected token to be revoked")
	}
	time.Sleep(2 * time.Second)
	if bl.IsRevoked("t1") {
		t.Fatal("expected token to expire")
	}
}

func TestCleanup(t *testing.T) {
	bl := NewBlacklist()
	bl.Revoke("t1", time.Now().Add(-time.Second))
	bl.Revoke("t2", time.Now().Add(time.Hour))
	bl.Cleanup()
	if bl.IsRevoked("t1") {
		t.Fatalf("cleanup should remove expired tokens")
	}
	if !bl.IsRevoked("t2") {
		t.Fatalf("active token removed unexpectedly")
	}
}
