// file: pkg/cache/grpc/cache_service.go
// version: 1.1.0
// guid: 887175af-36ad-491a-aa36-b40741b29935

package cachegrpc

import (
	"context"
	"time"

	cachepkg "github.com/jdfalk/gcommon/pkg/cache"
	cachepb "github.com/jdfalk/gcommon/pkg/cache/proto"
	cachetypes "github.com/jdfalk/gcommon/pkg/cache/types"
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

// GetMultiple retrieves multiple values.
func (s *CacheService) GetMultiple(ctx context.Context, req *cachepb.GetMultipleRequest) (*cachepb.GetMultipleResponse, error) {
	vals, err := s.cache.GetMultiple(ctx, req.GetKeys())
	if err != nil {
		return nil, err
	}
	resp := cachepb.GetMultipleResponse_builder{}
	for k, v := range vals {
		if b, ok := v.([]byte); ok {
			resp.Values[k] = b
		}
	}
	return resp.Build(), nil
}

// SetMultiple stores multiple values.
func (s *CacheService) SetMultiple(ctx context.Context, req *cachepb.SetMultipleRequest) (*cachepb.SetMultipleResponse, error) {
	ttl := time.Duration(0)
	if req.GetTtl() != nil {
		ttl = req.GetTtl().AsDuration()
	}
	items := make(map[string]cachetypes.CacheItem, len(req.GetValues()))
	for k, v := range req.GetValues() {
		items[k] = cachetypes.CacheItem{Value: v, TTL: ttl}
	}
	if err := s.cache.SetMultiple(ctx, items); err != nil {
		return nil, err
	}
	return cachepb.SetMultipleResponse_builder{Success: gproto.Bool(true), SetCount: gproto.Int32(int32(len(items)))}.Build(), nil
}

// DeleteMultiple removes multiple keys.
func (s *CacheService) DeleteMultiple(ctx context.Context, req *cachepb.DeleteMultipleRequest) (*cachepb.DeleteMultipleResponse, error) {
	if err := s.cache.DeleteMultiple(ctx, req.GetKeys()); err != nil {
		return nil, err
	}
	return cachepb.DeleteMultipleResponse_builder{DeletedCount: gproto.Int32(int32(len(req.GetKeys())))}.Build(), nil
}

// Increment increments a counter.
func (s *CacheService) Increment(ctx context.Context, req *cachepb.IncrementRequest) (*cachepb.IncrementResponse, error) {
	ttl := time.Duration(0)
	if req.GetTtl() != nil {
		ttl = req.GetTtl().AsDuration()
	}
	// Ensure key exists with initial value if provided
	if req.GetInitialValue() != 0 {
		_ = s.cache.Set(ctx, req.GetKey(), req.GetInitialValue(), ttl)
	}
	val, err := s.cache.Increment(ctx, req.GetKey(), req.GetDelta())
	if err != nil {
		return nil, err
	}
	return cachepb.IncrementResponse_builder{NewValue: gproto.Int64(val), Success: gproto.Bool(true)}.Build(), nil
}

// Decrement decrements a counter.
func (s *CacheService) Decrement(ctx context.Context, req *cachepb.DecrementRequest) (*cachepb.DecrementResponse, error) {
	val, err := s.cache.Decrement(ctx, req.GetKey(), req.GetDelta())
	if err != nil {
		return nil, err
	}
	return cachepb.DecrementResponse_builder{NewValue: gproto.Int64(val), Success: gproto.Bool(true)}.Build(), nil
}

// Keys lists keys matching a pattern.
func (s *CacheService) Keys(ctx context.Context, req *cachepb.KeysRequest) (*cachepb.KeysResponse, error) {
	keys, err := s.cache.Keys(ctx, req.GetPattern())
	if err != nil {
		return nil, err
	}
	return cachepb.KeysResponse_builder{Keys: keys, TotalCount: gproto.Int64(int64(len(keys))), Success: gproto.Bool(true)}.Build(), nil
}

// Flush flushes cache contents.
func (s *CacheService) Flush(ctx context.Context, req *cachepb.FlushRequest) (*cachepb.FlushResponse, error) {
	if err := s.cache.Flush(ctx); err != nil {
		return nil, err
	}
	return cachepb.FlushResponse_builder{Success: gproto.Bool(true)}.Build(), nil
}

// TouchExpiration updates TTL for a key.
func (s *CacheService) TouchExpiration(ctx context.Context, req *cachepb.TouchExpirationRequest) (*cachepb.TouchExpirationResponse, error) {
	var ttl time.Duration
	if req.GetTtl() != nil {
		ttl = req.GetTtl().AsDuration()
	}
	if err := s.cache.TouchExpiration(ctx, req.GetKey(), ttl); err != nil {
		return nil, err
	}
	return cachepb.TouchExpirationResponse_builder{Success: gproto.Bool(true), KeyExisted: gproto.Bool(true)}.Build(), nil
}
