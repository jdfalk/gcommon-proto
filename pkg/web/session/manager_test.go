// file: pkg/web/session/manager_test.go
// version: 1.0.0
// guid: d77b31bb-a2b4-41ba-9f2d-6c0d5857a1f4

package session

import (
	"context"
	"testing"
	"time"
)

func TestManagerDelegatesToStore(t *testing.T) {
	store := NewMemoryStore(time.Minute)
	mgr := NewManager(store)
	sess, err := mgr.CreateSession(context.Background(), "u1")
	if err != nil {
		t.Fatalf("create session: %v", err)
	}
	got, err := mgr.GetSession(context.Background(), sess.GetSessionId())
	if err != nil {
		t.Fatalf("get session: %v", err)
	}
	if got.GetUserId() != "u1" {
		t.Fatalf("unexpected user id: %s", got.GetUserId())
	}
}
