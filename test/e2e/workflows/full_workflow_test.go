// file: test/e2e/workflows/full_workflow_test.go
// version: 1.1.0
// guid: f615b648-f1a9-4bfd-b403-12ee88d5f3ab

package workflows

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

// workflowState holds state shared across workflow stages.
type workflowState struct {
	token    string
	server   *httptest.Server
	queue    *queueproviders.MemoryQueue
	metrics  metrics.Provider
	cache    *cacheproviders.MemoryCache
	notifier notification.Provider
	received chan *queuepb.QueueMessage
	cancel   context.CancelFunc
}

// TestFullWorkflow executes a representative end-to-end workflow.
func TestFullWorkflow(t *testing.T) {
	env, err := framework.SetupTestEnvironment()
	if err != nil {
		t.Fatalf("setup failed: %v", err)
	}
	defer env.Cleanup()

	ctx := context.Background()
	state := &workflowState{received: make(chan *queuepb.QueueMessage, 1)}
	t.Cleanup(func() {
		if state.cancel != nil {
			state.cancel()
		}
		if state.server != nil {
			state.server.Close()
		}
	})

	t.Run("initialize modules", func(t *testing.T) {
		mgr := config.NewManager()
		if err := mgr.Load(mapSource{data: map[string]any{"welcome": "hello"}}); err != nil {
			t.Fatalf("config load failed: %v", err)
		}
		state.cache = cacheproviders.NewMemoryCache(0, nil)
		mp, err := metricsmem.NewProvider(metrics.Config{})
		if err != nil {
			t.Fatalf("metrics provider failed: %v", err)
		}
		state.metrics = mp
		authProv := authproviders.NewLocalProvider([]byte("secret"), map[string]string{"bob": "pwd"}, map[string]string{}, nil)
		creds := &authpb.PasswordCredentials{}
		creds.SetUsername("bob")
		creds.SetPassword("pwd")
		areq := &authpb.AuthenticateRequest{}
		areq.SetPassword(creds)
		resp, err := authProv.Authenticate(ctx, areq)
		if err != nil {
			t.Fatalf("authenticate failed: %v", err)
		}
		state.token = resp.GetAccessToken()
		state.queue = queueproviders.NewMemoryQueue(10)
		cfg := &queuepb.QueueConfig{}
		cfg.SetName("notifications")
		if err := state.queue.CreateQueue(ctx, cfg); err != nil {
			t.Fatalf("create queue failed: %v", err)
		}
		subCtx, cancel := context.WithCancel(ctx)
		state.cancel = cancel
		if err := state.queue.Subscribe(queuepkg.WithQueueName(subCtx, "notifications"), func(ctx context.Context, msg *queuepb.QueueMessage) error {
			state.received <- msg
			return nil
		}); err != nil {
			t.Fatalf("subscribe failed: %v", err)
		}
		notif, err := notification.NewProvider("email", map[string]any{"host": "localhost"})
		if err != nil {
			t.Fatalf("notifier failed: %v", err)
		}
		state.notifier = notif
		handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			state.metrics.Counter("requests").Inc()
			_ = state.cache.Set(r.Context(), "welcome", "hello", time.Minute)
			_ = state.queue.Publish(queuepkg.WithQueueName(r.Context(), "notifications"), &queuepb.QueueMessage{})
			msg := &notifpb.NotificationMessage{}
			msg.SetSubject("hi")
			_, _ = state.notifier.Send(r.Context(), msg)
			w.WriteHeader(http.StatusOK)
		})
		mw := webmw.NewAuthMiddleware(state.token)
		state.server = httptest.NewServer(mw.Handle(handler))
	})

	t.Run("process workflow", func(t *testing.T) {
		req, _ := http.NewRequest("GET", state.server.URL, nil)
		req.Header.Set("Authorization", "Bearer "+state.token)
		res, err := http.DefaultClient.Do(req)
		if err != nil {
			t.Fatalf("request failed: %v", err)
		}
		if res.StatusCode != http.StatusOK {
			t.Fatalf("expected 200 got %d", res.StatusCode)
		}
	})

	t.Run("finalize workflow", func(t *testing.T) {
		select {
		case <-state.received:
		case <-time.After(time.Second):
			t.Fatalf("queue message not received")
		}
		snap := state.metrics.Registry().Snapshot()
		if snap.Counters()["requests"] != 1 {
			t.Fatalf("expected 1 request got %v", snap.Counters()["requests"])
		}
		val, err := state.cache.Get(ctx, "welcome")
		if err != nil || val != "hello" {
			t.Fatalf("cache check failed: %v %v", val, err)
		}
	})
}
