// file: pkg/web/examples/basic_server.go
// version: 1.1.0
// guid: 3d84c605-64d0-4c35-96d9-72c246b193ab

//go:build ignore

package main

import (
	"context"
	"log"

	"github.com/jdfalk/gcommon/pkg/web"
	"github.com/jdfalk/gcommon/pkg/web/handlers"
	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// Basic example starting an HTTP server.
func main() {
	cfg := &proto.ServerConfig{}
	srv := web.NewHTTPServer(cfg)
	srv.RegisterHandler("/health", handlers.HealthHandler())
	if err := srv.Start(context.Background()); err != nil {
		log.Fatal(err)
	}
	defer srv.Stop(context.Background())
}
