// file: pkg/web/session/memory.go
// version: 1.1.0
// guid: 78b88f98-8aec-4cc3-9164-337dfeee1faa

package session

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"errors"
	"sync"
	"time"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// MemoryStore implements in-memory session storage.
type MemoryStore struct {
	mu       sync.RWMutex
	sessions map[string]*proto.SessionData
	ttl      time.Duration
}

// NewMemoryStore creates a MemoryStore with the given TTL.
func NewMemoryStore(ttl time.Duration) *MemoryStore {
	return &MemoryStore{
		sessions: make(map[string]*proto.SessionData),
		ttl:      ttl,
	}
}

// CreateSession creates a new session for the user.
func (m *MemoryStore) CreateSession(ctx context.Context, userID string) (*proto.SessionData, error) {
	id := generateID()
	now := time.Now()
	sess := &proto.SessionData{}
	sess.SetSessionId(id)
	sess.SetUserId(userID)
	sess.SetState(proto.SessionState_SESSION_STATE_ACTIVE)
	sess.SetCreatedAt(timestamppb.New(now))
	sess.SetLastAccessAt(timestamppb.New(now))
	sess.SetExpiresAt(timestamppb.New(now.Add(m.ttl)))
	m.mu.Lock()
	m.sessions[id] = sess
	m.mu.Unlock()
	return sess, nil
}

// GetSession retrieves a session by ID.
func (m *MemoryStore) GetSession(ctx context.Context, sessionID string) (*proto.SessionData, error) {
	m.mu.RLock()
	sess, ok := m.sessions[sessionID]
	m.mu.RUnlock()
	if !ok {
		return nil, errors.New("session not found")
	}
	if sess.GetExpiresAt().AsTime().Before(time.Now()) {
		m.DeleteSession(ctx, sessionID)
		return nil, errors.New("session expired")
	}
	return sess, nil
}

// UpdateSession updates an existing session.
func (m *MemoryStore) UpdateSession(ctx context.Context, session *proto.SessionData) error {
	m.mu.Lock()
	m.sessions[session.GetSessionId()] = session
	m.mu.Unlock()
	return nil
}

// DeleteSession removes a session.
func (m *MemoryStore) DeleteSession(ctx context.Context, sessionID string) error {
	m.mu.Lock()
	delete(m.sessions, sessionID)
	m.mu.Unlock()
	return nil
}

// generateID creates a random session ID.
func generateID() string {
	b := make([]byte, 16)
	_, err := rand.Read(b)
	if err != nil {
		return hex.EncodeToString([]byte(time.Now().Format(time.RFC3339Nano)))
	}
	return hex.EncodeToString(b)
}

var _ Store = (*MemoryStore)(nil)
