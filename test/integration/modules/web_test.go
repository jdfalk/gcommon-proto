// file: test/integration/modules/web_test.go
// version: 1.1.0
// guid: fc1f100f-10b7-4130-8a4b-3a9817c80b94

package modules

import (
	"io/fs"
	"net/http"
	"net/http/httptest"
	"os"
	"testing"

	"github.com/jdfalk/gcommon/pkg/web/middleware"
	_ "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/jdfalk/gcommon/pkg/web/routing"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestWebModuleIntegration validates web service behavior.
func TestWebModuleIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	router := routing.NewRouter()
	router.Register("/hello", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("world"))
	}))
	auth := middleware.NewAuthMiddleware("token")
	handler := auth.Handle(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		router.Handler(r.URL.Path).ServeHTTP(w, r)
	}))
	srv := httptest.NewServer(handler)
	defer srv.Close()

	t.Run("handle request", func(t *testing.T) {
		req, _ := http.NewRequest("GET", srv.URL+"/hello", nil)
		req.Header.Set("Authorization", "Bearer token")
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		defer res.Body.Close()
		if res.StatusCode != http.StatusOK {
			t.Fatalf("unexpected status: %d", res.StatusCode)
		}
	})

	t.Run("middleware flow", func(t *testing.T) {
		req, _ := http.NewRequest("GET", srv.URL+"/hello", nil)
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		if res.StatusCode != http.StatusUnauthorized {
			t.Fatalf("expected unauthorized, got %d", res.StatusCode)
		}
	})

	t.Run("static assets", func(t *testing.T) {
		fsys := fs.FS(os.DirFS("."))
		fileSrv := http.FileServer(http.FS(fsys))
		router.Register("/file", fileSrv)
		req, _ := http.NewRequest("GET", srv.URL+"/file", nil)
		req.Header.Set("Authorization", "Bearer token")
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("file request failed: %v", err)
		}
		if res.StatusCode != http.StatusOK {
			t.Fatalf("expected OK got %d", res.StatusCode)
		}
	})

	t.Run("shutdown server", func(t *testing.T) {
		srv.CloseClientConnections()
	})
}
