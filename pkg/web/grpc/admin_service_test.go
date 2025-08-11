// file: pkg/web/grpc/admin_service_test.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7a8b-9c0d-1234567890ab

package grpc

import (
	"context"
	"testing"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

func TestAdminServiceConfigLifecycle(t *testing.T) {
	svc := NewAdminService()
	ctx := context.Background()

	// Initially not found
	if _, err := svc.GetCacheConfig(ctx, &proto.GetCacheConfigRequest{}); status.Code(err) != codes.NotFound {
		t.Fatalf("expected NotFound")
	}

	cfg := &proto.CacheConfig{}
	req := &proto.UpdateCacheConfigRequest{}
	req.SetConfig(cfg)
	if _, err := svc.UpdateCacheConfig(ctx, req); err != nil {
		t.Fatalf("update: %v", err)
	}

	resp, err := svc.GetCacheConfig(ctx, &proto.GetCacheConfigRequest{})
	if err != nil {
		t.Fatalf("get: %v", err)
	}
	if resp.GetConfig() == nil {
		t.Fatalf("expected config")
	}

	flushResp, err := svc.FlushCache(ctx, &proto.FlushCacheRequest{})
	if err != nil {
		t.Fatalf("flush: %v", err)
	}
	if !flushResp.GetSuccess() {
		t.Fatalf("expected success true")
	}
}
