// file: pkg/web/examples/api_server.go
// version: 1.1.0
// guid: 5e7b96e4-00a6-4c4b-bf59-7a86e73bc94e

//go:build ignore

package main

import (
	"context"
	"net/http"

	"github.com/jdfalk/gcommon/pkg/web"
	"github.com/jdfalk/gcommon/pkg/web/handlers"
	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// APIServer example with a single route.
func main() {
	cfg := &proto.ServerConfig{}
	srv := web.NewHTTPServer(cfg)
	srv.RegisterHandler("/api", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	}))
	srv.RegisterHandler("/health", handlers.HealthHandler())
	srv.Start(context.Background())
	defer srv.Stop(context.Background())
}
