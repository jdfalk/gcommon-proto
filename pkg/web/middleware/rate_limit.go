// file: pkg/web/middleware/rate_limit.go
// version: 1.0.0
// guid: 1e4a6a54-ae7c-46b6-9074-f0ac8e2c120e

package middleware

import (
	"net"
	"net/http"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/web"
)

type clientCounter struct {
	count int
	start time.Time
}

// RateLimitMiddleware limits requests per client within a window.
type RateLimitMiddleware struct {
	limit  int
	window time.Duration
	mu     sync.Mutex
	counts map[string]*clientCounter
}

// NewRateLimitMiddleware creates a RateLimitMiddleware.
func NewRateLimitMiddleware(limit int, window time.Duration) *RateLimitMiddleware {
	return &RateLimitMiddleware{
		limit:  limit,
		window: window,
		counts: make(map[string]*clientCounter),
	}
}

// Handle enforces the rate limit per remote IP.
func (m *RateLimitMiddleware) Handle(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ip, _, _ := net.SplitHostPort(r.RemoteAddr)
		m.mu.Lock()
		c, ok := m.counts[ip]
		now := time.Now()
		if !ok || now.Sub(c.start) > m.window {
			c = &clientCounter{start: now}
			m.counts[ip] = c
		}
		if c.count >= m.limit {
			m.mu.Unlock()
			w.WriteHeader(http.StatusTooManyRequests)
			return
		}
		c.count++
		m.mu.Unlock()
		next.ServeHTTP(w, r)
	})
}

var _ web.Middleware = (*RateLimitMiddleware)(nil)
