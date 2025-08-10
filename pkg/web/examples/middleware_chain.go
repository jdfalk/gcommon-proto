// file: pkg/web/examples/middleware_chain.go
// version: 1.1.0
// guid: 0ff4e765-181d-4f42-b4a6-cec951f2bf0e

//go:build ignore

package main

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/web"
	"github.com/jdfalk/gcommon/pkg/web/middleware"
	proto "github.com/jdfalk/gcommon/pkg/web/proto"
)

// Example showing middleware chaining.
func main() {
	cfg := &proto.ServerConfig{}
	srv := web.NewHTTPServer(cfg)
	srv.RegisterMiddleware(middleware.Logging())
	srv.RegisterMiddleware(middleware.RecoveryMiddleware())
	srv.Start(context.Background())
	defer srv.Stop(context.Background())
}
