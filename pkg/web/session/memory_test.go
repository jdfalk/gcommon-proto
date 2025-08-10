// file: pkg/web/session/memory_test.go
// version: 1.0.0
// guid: 9059fbcb-01cc-4e36-9781-8ede9140395a

package session

import (
	"context"
	"testing"
	"time"
)

func TestMemoryStoreSessionLifecycle(t *testing.T) {
	store := NewMemoryStore(time.Minute)
	sess, err := store.CreateSession(context.Background(), "user1")
	if err != nil {
		t.Fatalf("create session: %v", err)
	}
	got, err := store.GetSession(context.Background(), sess.GetSessionId())
	if err != nil {
		t.Fatalf("get session: %v", err)
	}
	if got.GetUserId() != "user1" {
		t.Fatalf("unexpected user id: %s", got.GetUserId())
	}
	if err := store.DeleteSession(context.Background(), sess.GetSessionId()); err != nil {
		t.Fatalf("delete session: %v", err)
	}
	if _, err := store.GetSession(context.Background(), sess.GetSessionId()); err == nil {
		t.Fatalf("expected error for deleted session")
	}
}
