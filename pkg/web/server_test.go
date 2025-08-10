// file: pkg/web/server_test.go
// version: 1.0.0
// guid: 4fce088c-0af6-4f3f-bd3d-148053d0a20f

package web

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

func TestRegisterHandlerAndMiddleware(t *testing.T) {
	cfg := &proto.ServerConfig{}
	srv := NewHTTPServer(cfg)
	srv.RegisterMiddleware(MiddlewareFunc(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			w.Header().Set("X-Test", "1")
			next.ServeHTTP(w, r)
		})
	}))
	srv.RegisterHandler("/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	}))
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	rec := httptest.NewRecorder()
	srv.mux.ServeHTTP(rec, req)
	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
	if rec.Header().Get("X-Test") != "1" {
		t.Fatalf("middleware not applied")
	}
}

func TestStartStop(t *testing.T) {
	cfg := &proto.ServerConfig{}
	cfg.SetHost("127.0.0.1")
	cfg.SetPort(0)
	srv := NewHTTPServer(cfg)
	srv.RegisterHandler("/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {}))
	if err := srv.Start(context.Background()); err != nil {
		t.Fatalf("start failed: %v", err)
	}
	time.Sleep(50 * time.Millisecond)
	if err := srv.Stop(context.Background()); err != nil {
		t.Fatalf("stop failed: %v", err)
	}
}
