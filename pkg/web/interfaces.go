// file: pkg/web/interfaces.go
// version: 1.0.0
// guid: 56b0b666-a31b-4e2f-882e-36e005e41ca5

package web

import (
	"context"
	"net/http"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// Server defines the interface for HTTP servers.
type Server interface {
	Start(ctx context.Context) error
	Stop(ctx context.Context) error
	RegisterHandler(pattern string, handler http.Handler)
	RegisterMiddleware(middleware Middleware)
	GetConfig() *proto.ServerConfig
}

// Middleware processes HTTP requests.
type Middleware interface {
	Handle(next http.Handler) http.Handler
}

// MiddlewareFunc adapts a function to the Middleware interface.
type MiddlewareFunc func(next http.Handler) http.Handler

// Handle calls m(next).
func (m MiddlewareFunc) Handle(next http.Handler) http.Handler {
	return m(next)
}

// SessionManager manages user sessions.
type SessionManager interface {
	CreateSession(ctx context.Context, userID string) (*proto.SessionData, error)
	GetSession(ctx context.Context, sessionID string) (*proto.SessionData, error)
	UpdateSession(ctx context.Context, session *proto.SessionData) error
	DeleteSession(ctx context.Context, sessionID string) error
}
