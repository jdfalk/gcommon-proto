// file: test/e2e/scenarios/basic_test.go
// version: 1.1.0
// guid: bd76514d-1944-48a6-9f39-71ebe2bffbdf

package scenarios

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	_ "github.com/jdfalk/gcommon/pkg/auth/proto"
	authpb "github.com/jdfalk/gcommon/pkg/auth/proto"
	authproviders "github.com/jdfalk/gcommon/pkg/auth/providers"
	cacheproviders "github.com/jdfalk/gcommon/pkg/cache/providers"
	"github.com/jdfalk/gcommon/pkg/config"
	_ "github.com/jdfalk/gcommon/pkg/config/proto"
	metrics "github.com/jdfalk/gcommon/pkg/metrics"
	metricsmem "github.com/jdfalk/gcommon/pkg/metrics/memory"
	notification "github.com/jdfalk/gcommon/pkg/notification"
	notifpb "github.com/jdfalk/gcommon/pkg/notification/proto"
	_ "github.com/jdfalk/gcommon/pkg/notification/providers"
	queuepkg "github.com/jdfalk/gcommon/pkg/queue"
	queuepb "github.com/jdfalk/gcommon/pkg/queue/proto"
	queueproviders "github.com/jdfalk/gcommon/pkg/queue/providers"
	webmw "github.com/jdfalk/gcommon/pkg/web/middleware"
	_ "github.com/jdfalk/gcommon/pkg/web/proto"
	"github.com/jdfalk/gcommon/test/integration/framework"
)

type mapSource struct{ data map[string]any }

func (m mapSource) Load() (map[string]any, error) { return m.data, nil }

// TestBasicScenario runs a simple end-to-end scenario across modules.
func TestBasicScenario(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	ctx := context.Background()
	var token string

	t.Run("config module", func(t *testing.T) {
		mgr := config.NewManager()
		src := mapSource{data: map[string]any{"feature": true}}
		if err := mgr.Load(src); err != nil {
			t.Fatalf("load failed: %v", err)
		}
		v, err := mgr.GetBool("feature")
		if err != nil || !v {
			t.Fatalf("expected true got %v err %v", v, err)
		}
	})

	t.Run("cache module", func(t *testing.T) {
		cache := cacheproviders.NewMemoryCache(10, nil)
		if err := cache.Set(ctx, "k", "v", time.Minute); err != nil {
			t.Fatalf("set failed: %v", err)
		}
		got, err := cache.Get(ctx, "k")
		if err != nil || got != "v" {
			t.Fatalf("expected v got %v err %v", got, err)
		}
	})

	t.Run("metrics module", func(t *testing.T) {
		mp, err := metricsmem.NewProvider(metrics.Config{})
		if err != nil {
			t.Fatalf("new provider failed: %v", err)
		}
		counter := mp.Counter("requests")
		counter.Inc()
		snap := mp.Registry().Snapshot()
		if snap.Counters()["requests"] != 1 {
			t.Fatalf("expected counter 1 got %v", snap.Counters()["requests"])
		}
	})

	t.Run("auth module", func(t *testing.T) {
		provider := authproviders.NewLocalProvider([]byte("secret"), map[string]string{"alice": "password"}, map[string]string{"alice": "admin"}, nil)
		creds := &authpb.PasswordCredentials{}
		creds.SetUsername("alice")
		creds.SetPassword("password")
		req := &authpb.AuthenticateRequest{}
		req.SetPassword(creds)
		resp, err := provider.Authenticate(ctx, req)
		if err != nil {
			t.Fatalf("authenticate failed: %v", err)
		}
		token = resp.GetAccessToken()
		vreq := &authpb.ValidateTokenRequest{}
		vreq.SetAccessToken(token)
		vresp, err := provider.ValidateToken(ctx, vreq)
		if err != nil || !vresp.GetValid() {
			t.Fatalf("validate failed: %v", err)
		}
	})

	t.Run("queue module", func(t *testing.T) {
		mq := queueproviders.NewMemoryQueue(10)
		received := make(chan struct{}, 1)
		subCtx, cancel := context.WithCancel(ctx)
		if err := mq.Subscribe(queuepkg.WithQueueName(subCtx, "default"), func(ctx context.Context, msg *queuepb.QueueMessage) error {
			received <- struct{}{}
			return nil
		}); err != nil {
			t.Fatalf("subscribe failed: %v", err)
		}
		if err := mq.Publish(queuepkg.WithQueueName(ctx, "default"), &queuepb.QueueMessage{}); err != nil {
			t.Fatalf("publish failed: %v", err)
		}
		select {
		case <-received:
		case <-time.After(time.Second):
			t.Fatalf("message not received")
		}
		cancel()
		mq.Shutdown(ctx)
	})

	t.Run("notification module", func(t *testing.T) {
		prov, err := notification.NewProvider("email", map[string]any{"host": "localhost"})
		if err != nil {
			t.Fatalf("provider failed: %v", err)
		}
		msg := &notifpb.NotificationMessage{}
		msg.SetSubject("test")
		msg.SetBody("body")
		_, err = prov.Send(ctx, msg)
		if err != nil {
			t.Fatalf("send failed: %v", err)
		}
	})

	t.Run("web module", func(t *testing.T) {
		mw := webmw.NewAuthMiddleware(token)
		handler := mw.Handle(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			w.WriteHeader(http.StatusOK)
		}))
		srv := httptest.NewServer(handler)
		defer srv.Close()

		req, _ := http.NewRequest("GET", srv.URL, nil)
		req.Header.Set("Authorization", "Bearer "+token)
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		if res.StatusCode != http.StatusOK {
			t.Fatalf("expected 200 got %d", res.StatusCode)
		}
	})
}
