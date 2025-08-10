// file: pkg/web/session/manager.go
// version: 1.0.0
// guid: 9c0de4e5-7f2a-4f9e-9a2c-d5279a2dd1b4

package session

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/web"
	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// Manager implements web.SessionManager using a Store.
type Manager struct {
	store Store
}

// NewManager creates a Manager with the provided store.
func NewManager(store Store) *Manager {
	return &Manager{store: store}
}

func (m *Manager) CreateSession(ctx context.Context, userID string) (*proto.SessionData, error) {
	return m.store.CreateSession(ctx, userID)
}

func (m *Manager) GetSession(ctx context.Context, sessionID string) (*proto.SessionData, error) {
	return m.store.GetSession(ctx, sessionID)
}

func (m *Manager) UpdateSession(ctx context.Context, session *proto.SessionData) error {
	return m.store.UpdateSession(ctx, session)
}

func (m *Manager) DeleteSession(ctx context.Context, sessionID string) error {
	return m.store.DeleteSession(ctx, sessionID)
}

var _ web.SessionManager = (*Manager)(nil)
