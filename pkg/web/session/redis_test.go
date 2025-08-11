// file: pkg/web/session/redis_test.go
// version: 1.0.0
// guid: e4f1b2c3-d4e5-6f7a-8b9c-1234567890ab

package session

import (
	"context"
	"testing"
	"time"

	miniredis "github.com/alicebob/miniredis/v2"
	proto "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/redis/go-redis/v9"
)

func TestRedisStoreCreateGet(t *testing.T) {
	ctx := context.Background()
	s := miniredis.RunT(t)
	defer s.Close()
	client := redis.NewClient(&redis.Options{Addr: s.Addr()})
	store := NewRedisStore(client, time.Minute)

	sess, err := store.CreateSession(ctx, "user1")
	if err != nil {
		t.Fatalf("create session: %v", err)
	}

	got, err := store.GetSession(ctx, sess.GetSessionId())
	if err != nil {
		t.Fatalf("get session: %v", err)
	}
	if got.GetUserId() != "user1" {
		t.Fatalf("unexpected user id: %s", got.GetUserId())
	}
}

func TestRedisStoreUpdateDelete(t *testing.T) {
	ctx := context.Background()
	s := miniredis.RunT(t)
	defer s.Close()
	client := redis.NewClient(&redis.Options{Addr: s.Addr()})
	store := NewRedisStore(client, time.Minute)

	sess := &proto.SessionData{}
	sess.SetSessionId("abc")

	if err := store.UpdateSession(ctx, sess); err != nil {
		t.Fatalf("update session: %v", err)
	}

	if err := store.DeleteSession(ctx, "abc"); err != nil {
		t.Fatalf("delete session: %v", err)
	}

	if _, err := store.GetSession(ctx, "abc"); err == nil {
		t.Fatalf("expected error getting deleted session")
	}
}
