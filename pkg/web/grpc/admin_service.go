// file: pkg/web/grpc/admin_service.go
// version: 1.1.0
// guid: 4e6ed2bb-7871-4c61-8815-7e71d2342635

package grpc

import (
	"context"
	"sync"

	proto "github.com/jdfalk/gcommon/pkg/web/proto"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// AdminService implements proto.WebAdminServiceServer.
type AdminService struct {
	proto.UnimplementedWebAdminServiceServer
	mu     sync.RWMutex
	config *proto.CacheConfig
}

// NewAdminService creates a new AdminService.
func NewAdminService() *AdminService { return &AdminService{} }

// GetCacheConfig returns the current cache configuration.
func (a *AdminService) GetCacheConfig(ctx context.Context, _ *proto.GetCacheConfigRequest) (*proto.GetCacheConfigResponse, error) {
	a.mu.RLock()
	defer a.mu.RUnlock()
	if a.config == nil {
		return nil, status.Error(codes.NotFound, "cache config not set")
	}
	resp := &proto.GetCacheConfigResponse{}
	resp.SetConfig(a.config)
	return resp, nil
}

// UpdateCacheConfig sets the cache configuration.
func (a *AdminService) UpdateCacheConfig(ctx context.Context, req *proto.UpdateCacheConfigRequest) (*proto.UpdateCacheConfigResponse, error) {
	if req.GetConfig() == nil {
		return nil, status.Error(codes.InvalidArgument, "config required")
	}
	a.mu.Lock()
	a.config = req.GetConfig()
	a.mu.Unlock()
	resp := &proto.UpdateCacheConfigResponse{}
	resp.SetSuccess(true)
	return resp, nil
}

// FlushCache is a placeholder that reports success.
func (a *AdminService) FlushCache(ctx context.Context, _ *proto.FlushCacheRequest) (*proto.FlushCacheResponse, error) {
	resp := &proto.FlushCacheResponse{}
	resp.SetSuccess(true)
	resp.SetEntriesFlushed(0)
	return resp, nil
}

var _ proto.WebAdminServiceServer = (*AdminService)(nil)
