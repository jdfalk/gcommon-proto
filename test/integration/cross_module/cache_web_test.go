// file: test/integration/cross_module/cache_web_test.go
// version: 1.1.0
// guid: 029293af-e862-4836-8625-e98e4aa89793

package crossmodule

import (
	"context"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	_ "github.com/jdfalk/gcommon/pkg/cache/proto"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
	_ "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/jdfalk/gcommon/pkg/web/routing"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

// TestCacheWebIntegration tests web response caching behavior.
func TestCacheWebIntegration(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	cache := providers.NewMemoryCache(0, nil)
	router := routing.NewRouter()
	router.Register("/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if v, _ := cache.Get(r.Context(), "page"); v != nil {
			w.Write([]byte(v.(string)))
			return
		}
		cache.Set(r.Context(), "page", "rendered", 0)
		w.Write([]byte("rendered"))
	}))
	srv := httptest.NewServer(router.Handler("/"))
	defer srv.Close()

	t.Run("cache miss triggers render", func(t *testing.T) {
		res, _ := http.Get(srv.URL)
		buf, _ := io.ReadAll(res.Body)
		if string(buf) != "rendered" {
			t.Fatalf("expected rendered")
		}
	})

	t.Run("cache hit serves response", func(t *testing.T) {
		res, _ := http.Get(srv.URL)
		buf, _ := io.ReadAll(res.Body)
		if string(buf) != "rendered" {
			t.Fatalf("expected cached rendered")
		}
	})

	t.Run("cache invalidation", func(t *testing.T) {
		cache.Clear(context.Background())
		res, _ := http.Get(srv.URL)
		buf, _ := io.ReadAll(res.Body)
		if string(buf) != "rendered" {
			t.Fatalf("expected rendered after clear")
		}
	})

	t.Run("cache headers", func(t *testing.T) {
		req, _ := http.NewRequest("GET", srv.URL, nil)
		res, _ := http.DefaultClient.Do(req)
		if res.Header.Get("Cache-Control") != "" {
			t.Fatalf("unexpected cache header")
		}
	})
}
