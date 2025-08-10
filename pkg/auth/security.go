// file: pkg/auth/security.go
// version: 1.0.0
// guid: 24dbd8a3-2ec0-4e8b-8b6a-82f6efaa1c5b

package auth

import (
	"errors"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/security/tools"
)

// TokenManager handles creation and validation of authentication tokens.
type TokenManager struct {
	expiry time.Duration
}

// NewTokenManager creates a token manager with specified token lifetime.
func NewTokenManager(expiry time.Duration) *TokenManager {
	return &TokenManager{expiry: expiry}
}

// Generate creates a new random token string.
func (t *TokenManager) Generate() (string, error) {
	return tools.RandomToken(32)
}

// Validate checks whether the token issue time is within expiry window.
func (t *TokenManager) Validate(issued time.Time) bool {
	return time.Since(issued) <= t.expiry
}

// HashPassword hashes a password using repository crypto tools.
func HashPassword(pw string) (string, error) {
	return tools.HashPassword(pw)
}

// CheckPassword verifies a password against hashed value.
func CheckPassword(hash, pw string) bool {
	return tools.VerifyPassword(hash, pw)
}

// Session represents an authenticated user session.
type Session struct {
	Token     string
	UserID    string
	CreatedAt time.Time
}

// SessionManager manages active sessions.
type SessionManager struct {
	mu       sync.RWMutex
	sessions map[string]Session
	tokens   *TokenManager
}

// NewSessionManager creates a session manager.
func NewSessionManager(tokens *TokenManager) *SessionManager {
	return &SessionManager{sessions: map[string]Session{}, tokens: tokens}
}

// CreateSession creates a session for a user ID and returns token.
func (s *SessionManager) CreateSession(userID string) (Session, error) {
	token, err := s.tokens.Generate()
	if err != nil {
		return Session{}, err
	}
	sess := Session{Token: token, UserID: userID, CreatedAt: time.Now().UTC()}
	s.mu.Lock()
	s.sessions[token] = sess
	s.mu.Unlock()
	return sess, nil
}

// ValidateSession ensures token exists and not expired.
func (s *SessionManager) ValidateSession(token string) bool {
	s.mu.RLock()
	sess, ok := s.sessions[token]
	s.mu.RUnlock()
	if !ok {
		return false
	}
	if !s.tokens.Validate(sess.CreatedAt) {
		s.DestroySession(token)
		return false
	}
	return true
}

// DestroySession removes a session.
func (s *SessionManager) DestroySession(token string) {
	s.mu.Lock()
	delete(s.sessions, token)
	s.mu.Unlock()
}

// Authorization middleware example to prevent bypass.
func Authorize(isAllowed func(token string) bool) func(token string) error {
	return func(token string) error {
		if !isAllowed(token) {
			return errors.New("unauthorized")
		}
		return nil
	}
}
