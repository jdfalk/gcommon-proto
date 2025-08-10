// file: pkg/auth/security_test.go
// version: 1.0.0
// guid: 2ab57552-3b9c-4c1e-a6e0-14fb4f6d06c3

package auth

import (
	"testing"
	"time"
)

func TestSessionLifecycle(t *testing.T) {
	tm := NewTokenManager(time.Minute)
	sm := NewSessionManager(tm)
	sess, err := sm.CreateSession("user1")
	if err != nil {
		t.Fatalf("create session: %v", err)
	}
	if !sm.ValidateSession(sess.Token) {
		t.Fatalf("session should be valid")
	}
	sm.DestroySession(sess.Token)
	if sm.ValidateSession(sess.Token) {
		t.Fatalf("session should be destroyed")
	}
}
