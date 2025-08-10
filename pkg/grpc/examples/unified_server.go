// file: pkg/grpc/examples/unified_server.go
// version: 1.0.0
// guid: 33ef035a-8fe1-4893-8115-b3893260681b

package examples

import (
	"context"
	"log"

	"github.com/jdfalk/gcommon/pkg/grpc/server"
)

// UnifiedServerExample demonstrates constructing and starting a server.
func UnifiedServerExample(ctx context.Context) {
	cfg := server.Config{Address: ":50051"}
	srv := cfg.Build()
	if err := srv.Start(ctx); err != nil {
		log.Printf("start failed: %v", err)
	}
}
