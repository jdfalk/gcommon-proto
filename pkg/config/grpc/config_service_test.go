// file: pkg/config/grpc/config_service_test.go
// version: 1.0.0
// guid: 04040404-0404-0404-0404-040404040404

package grpc

import (
	"context"
	"testing"

	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"github.com/jdfalk/gcommon/pkg/config/providers"
	gproto "google.golang.org/protobuf/proto"
)

// TestGet ensures basic get works
func TestGet(t *testing.T) {
	p, _ := providers.NewEnvProvider("T_")
	_ = p.Set("A", "B")
	svc := &ConfigServiceServer{Provider: p}
	req := configpb.GetConfigRequest_builder{Key: gproto.String("A")}.Build()
	if _, err := svc.Get(context.Background(), req); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
}

// TODO: Add tests for Set and Watch

// EOF
