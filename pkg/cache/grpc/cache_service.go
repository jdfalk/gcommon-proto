// file: pkg/cache/grpc/cache_service.go
// version: 1.0.0
// guid: 887175af-36ad-491a-aa36-b40741b29935

package cachegrpc

import (
	"context"
	"time"

	cachepkg "github.com/jdfalk/gcommon/pkg/cache"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	gproto "google.golang.org/protobuf/proto"
)

// CacheService implements cachepb.CacheServiceServer.
type CacheService struct {
	cachepb.UnimplementedCacheServiceServer
	cache cachepkg.Cache
}

// NewCacheService creates a new CacheService.
func NewCacheService(c cachepkg.Cache) *CacheService {
	return &CacheService{cache: c}
}

// Get retrieves a value from the underlying cache.
func (s *CacheService) Get(ctx context.Context, req *cachepb.GetRequest) (*cachepb.GetResponse, error) {
	val, err := s.cache.Get(ctx, req.GetKey())
	if err != nil {
		return nil, err
	}
	return cachepb.GetResponse_builder{Found: gproto.Bool(val != nil)}.Build(), nil
}

// Set stores a value in the cache.
func (s *CacheService) Set(ctx context.Context, req *cachepb.SetRequest) (*cachepb.SetResponse, error) {
	var ttl time.Duration
	if req.GetTtl() != nil {
		ttl = req.GetTtl().AsDuration()
	}
	if err := s.cache.Set(ctx, req.GetKey(), req.GetValue(), ttl); err != nil {
		return nil, err
	}
	return &cachepb.SetResponse{}, nil
}

// Delete removes a key.
func (s *CacheService) Delete(ctx context.Context, req *cachepb.DeleteRequest) (*cachepb.DeleteResponse, error) {
	if err := s.cache.Delete(ctx, req.GetKey()); err != nil {
		return nil, err
	}
	return cachepb.DeleteResponse_builder{Success: gproto.Bool(true), DeletedCount: gproto.Int32(1)}.Build(), nil
}

// Exists checks if a key exists.
func (s *CacheService) Exists(ctx context.Context, req *cachepb.ExistsRequest) (*cachepb.ExistsResponse, error) {
	exists, err := s.cache.Exists(ctx, req.GetKey())
	if err != nil {
		return nil, err
	}
	return cachepb.ExistsResponse_builder{Exists: gproto.Bool(exists)}.Build(), nil
}

// Clear clears the cache.
func (s *CacheService) Clear(ctx context.Context, req *cachepb.ClearRequest) (*cachepb.ClearResponse, error) {
	if err := s.cache.Clear(ctx); err != nil {
		return nil, err
	}
	return cachepb.ClearResponse_builder{Success: gproto.Bool(true)}.Build(), nil
}

// GetStats returns cache statistics.
func (s *CacheService) GetStats(ctx context.Context, req *cachepb.GetStatsRequest) (*cachepb.GetStatsResponse, error) {
	stats := s.cache.GetStats()
	return cachepb.GetStatsResponse_builder{TotalItems: gproto.Int64(stats.GetTotalItems()), Success: gproto.Bool(true)}.Build(), nil
}
