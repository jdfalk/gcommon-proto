// file: pkg/config/interfaces.go
// version: 1.0.0
// guid: db2655ec-cb40-404c-ae61-af296e7f636f

package config

import (
	"context"

	proto "github.com/jdfalk/gcommon/pkg/config/proto"
)

// Provider defines the configuration provider interface.
type Provider interface {
	Get(key string) (interface{}, error)
	Set(key string, value interface{}) error
	Watch(key string, callback func(interface{})) error
	Close() error
}

// ConfigService defines the main configuration service operations.
type ConfigService interface {
	Get(ctx context.Context, req *proto.GetConfigRequest) (*proto.GetConfigResponse, error)
	Set(ctx context.Context, req *proto.SetConfigRequest) (*proto.SetConfigResponse, error)
	Watch(req *proto.WatchConfigRequest, stream proto.ConfigService_WatchServer) error
}
