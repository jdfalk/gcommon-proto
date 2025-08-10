// file: pkg/cache/grpc/admin_service.go
// version: 1.0.0
// guid: e4f5a6b7-c8d9-4e0f-1a2b-3c4d5e6f7a8b

package cachegrpc

import (
	"context"

	cachepkg "github.com/jdfalk/gcommon/pkg/cache"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	gproto "google.golang.org/protobuf/proto"
)

// CacheAdminService implements cachepb.CacheAdminServiceServer.
type CacheAdminService struct {
	cachepb.UnimplementedCacheAdminServiceServer
	cache cachepkg.Cache
}

// NewCacheAdminService creates a new admin service.
func NewCacheAdminService(c cachepkg.Cache) *CacheAdminService {
	return &CacheAdminService{cache: c}
}

// Flush clears the cache.
func (s *CacheAdminService) Flush(ctx context.Context, req *cachepb.FlushRequest) (*cachepb.FlushResponse, error) {
	if err := s.cache.Clear(ctx); err != nil {
		return nil, err
	}
	return cachepb.FlushResponse_builder{Success: gproto.Bool(true)}.Build(), nil
}

// GetStats returns cache statistics.
func (s *CacheAdminService) GetStats(ctx context.Context, req *cachepb.GetStatsRequest) (*cachepb.GetStatsResponse, error) {
	stats := s.cache.GetStats()
	return cachepb.GetStatsResponse_builder{TotalItems: gproto.Int64(stats.GetTotalItems()), Success: gproto.Bool(true)}.Build(), nil
}
