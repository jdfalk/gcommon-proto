// file: pkg/web/session/store.go
// version: 1.0.0
// guid: e2f1bbf5-6f0d-4c8c-9d4f-7b026c093894

package session

import (
	"context"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// Store defines persistence for sessions.
type Store interface {
	CreateSession(ctx context.Context, userID string) (*proto.SessionData, error)
	GetSession(ctx context.Context, sessionID string) (*proto.SessionData, error)
	UpdateSession(ctx context.Context, session *proto.SessionData) error
	DeleteSession(ctx context.Context, sessionID string) error
}
