// file: pkg/web/session/redis.go
// version: 1.0.0
// guid: d0f1e2c3-b4a5-4b6c-9d8e-1234567890ab

package session

import (
	"context"
	"errors"
	"time"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/redis/go-redis/v9"
	gproto "google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// RedisStore implements session storage backed by Redis.
type RedisStore struct {
	client *redis.Client
	ttl    time.Duration
}

// NewRedisStore creates a RedisStore using the provided client and TTL.
func NewRedisStore(client *redis.Client, ttl time.Duration) *RedisStore {
	return &RedisStore{client: client, ttl: ttl}
}

// CreateSession creates a new session for the user and stores it in Redis.
func (r *RedisStore) CreateSession(ctx context.Context, userID string) (*proto.SessionData, error) {
	id := generateID()
	now := time.Now()
	sess := &proto.SessionData{}
	sess.SetSessionId(id)
	sess.SetUserId(userID)
	sess.SetState(proto.SessionState_SESSION_STATE_ACTIVE)
	sess.SetCreatedAt(timestamppb.New(now))
	sess.SetLastAccessAt(timestamppb.New(now))
	sess.SetExpiresAt(timestamppb.New(now.Add(r.ttl)))
	b, err := gproto.Marshal(sess)
	if err != nil {
		return nil, err
	}
	if err := r.client.Set(ctx, id, b, r.ttl).Err(); err != nil {
		return nil, err
	}
	return sess, nil
}

// GetSession retrieves a session by ID from Redis.
func (r *RedisStore) GetSession(ctx context.Context, sessionID string) (*proto.SessionData, error) {
	b, err := r.client.Get(ctx, sessionID).Bytes()
	if err != nil {
		if errors.Is(err, redis.Nil) {
			return nil, errors.New("session not found")
		}
		return nil, err
	}
	sess := &proto.SessionData{}
	if err := gproto.Unmarshal(b, sess); err != nil {
		return nil, err
	}
	return sess, nil
}

// UpdateSession updates an existing session in Redis.
func (r *RedisStore) UpdateSession(ctx context.Context, session *proto.SessionData) error {
	b, err := gproto.Marshal(session)
	if err != nil {
		return err
	}
	return r.client.Set(ctx, session.GetSessionId(), b, r.ttl).Err()
}

// DeleteSession removes a session from Redis.
func (r *RedisStore) DeleteSession(ctx context.Context, sessionID string) error {
	return r.client.Del(ctx, sessionID).Err()
}

var _ Store = (*RedisStore)(nil)
