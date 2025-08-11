// file: examples/getting-started/first-app/main.go
// version: 1.1.0
// guid: a2eaf657-6cd4-4015-88b7-456534fdd008

package main

import (
        "context"
        "fmt"
        "net/http"
        "time"

        "github.com/jdfalk/gcommon/pkg/metrics"
        prom "github.com/jdfalk/gcommon/pkg/metrics/prometheus"
)

// server wraps the HTTP server and metrics provider so that setup and run can
// share state in a minimal way without introducing global variables.
type server struct {
        provider metrics.Provider
        counter  metrics.Counter
}

// setup initializes a Prometheus metrics provider and creates a counter for HTTP
// requests. The provider also exposes an HTTP handler at `/metrics` for scraping
// by Prometheus.
func setup(ctx context.Context) (*server, error) {
        provider, err := prom.NewProvider(metrics.Config{})
        if err != nil {
                return nil, err
        }
        if err := provider.Start(ctx); err != nil {
                return nil, err
        }
        s := &server{provider: provider, counter: provider.Counter("requests_total")}
        return s, nil
}

// run starts a simple HTTP server with a single endpoint. Each request
// increments the metrics counter to demonstrate instrumentation.
func run(ctx context.Context, s *server) error {
        mux := http.NewServeMux()
        mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
                s.counter.Inc()
                fmt.Fprintln(w, "hello from gcommon")
        })
        mux.Handle("/metrics", s.provider.Handler())

        srv := &http.Server{Addr: ":8080", Handler: mux}

        go func() {
                <-ctx.Done()
                _ = srv.Shutdown(context.Background())
        }()

        return srv.ListenAndServe()
}

func main() {
        ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
        defer cancel()

        srv, err := setup(ctx)
        if err != nil {
                panic(err)
        }
        if err := run(ctx, srv); err != nil && err != http.ErrServerClosed {
                panic(err)
        }
}
