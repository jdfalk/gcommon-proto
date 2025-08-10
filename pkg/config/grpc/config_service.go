// file: pkg/config/grpc/config_service.go
// version: 1.0.0
// guid: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

package grpc

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/config"
	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// ConfigServiceServer implements ConfigService gRPC interface
// TODO: Inject provider and validation components
// TODO: Add logging and metrics
// TODO: Implement business logic
// TODO: Handle streaming errors
// TODO: Ensure thread safety
// TODO: Provide tracing hooks
// TODO: Add authorization checks
// TODO: Validate requests
// TODO: Support batching operations
// TODO: End TODO list

type ConfigServiceServer struct {
	configpb.UnimplementedConfigServiceServer
	Provider config.Provider
}

// Get retrieves configuration value for key
func (s *ConfigServiceServer) Get(ctx context.Context, req *configpb.GetConfigRequest) (*configpb.GetConfigResponse, error) {
	if s.Provider == nil {
		return nil, status.Error(codes.Unimplemented, "provider not configured")
	}
	if _, err := s.Provider.Get(req.GetKey()); err != nil {
		return nil, status.Errorf(codes.NotFound, "%v", err)
	}
	return &configpb.GetConfigResponse{}, nil
}

// Set stores configuration value
func (s *ConfigServiceServer) Set(ctx context.Context, req *configpb.SetConfigRequest) (*configpb.SetConfigResponse, error) {
	if s.Provider == nil {
		return nil, status.Error(codes.Unimplemented, "provider not configured")
	}
	if err := s.Provider.Set(req.GetKey(), req.GetValue()); err != nil {
		return nil, status.Errorf(codes.Internal, "%v", err)
	}
	return &configpb.SetConfigResponse{}, nil
}

// Watch streams updates for a key pattern
func (s *ConfigServiceServer) Watch(req *configpb.WatchConfigRequest, stream grpc.ServerStreamingServer[configpb.WatchConfigResponse]) error {
	if s.Provider == nil {
		return status.Error(codes.Unimplemented, "provider not configured")
	}
	return s.Provider.Watch(req.GetKeyPattern(), func(v interface{}) {
		_ = stream.Send(&configpb.WatchConfigResponse{})
	})
}

var _ configpb.ConfigServiceServer = (*ConfigServiceServer)(nil)

// EOF
