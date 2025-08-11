// file: pkg/config/logging.go
// version: 1.0.0
// guid: 016b30e1-ec33-4273-84f8-fec3bffb6714

package config

import (
	"context"

	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"github.com/jdfalk/gcommon/pkg/log"
)

// LoggedProvider wraps a Provider adding structured logging for all operations.
type LoggedProvider struct {
	provider Provider
	logger   log.Logger
}

// NewLoggedProvider creates a new LoggedProvider.
func NewLoggedProvider(p Provider, l log.Logger) *LoggedProvider {
	return &LoggedProvider{provider: p, logger: l}
}

// Get retrieves a configuration value and logs the operation.
func (l *LoggedProvider) Get(key string) (interface{}, error) {
	l.logger.Info("config get", log.Field{Key: "key", Value: key})
	v, err := l.provider.Get(key)
	if err != nil {
		l.logger.Error("config get failed", log.Field{Key: "key", Value: key}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.Info("config get success", log.Field{Key: "key", Value: key})
	return v, nil
}

// Set stores a configuration value and logs the result.
func (l *LoggedProvider) Set(key string, value interface{}) error {
	l.logger.Info("config set", log.Field{Key: "key", Value: key})
	if err := l.provider.Set(key, value); err != nil {
		l.logger.Error("config set failed", log.Field{Key: "key", Value: key}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.Info("config set success", log.Field{Key: "key", Value: key})
	return nil
}

// Watch registers a callback and logs registration errors.
func (l *LoggedProvider) Watch(key string, callback func(interface{})) error {
	l.logger.Info("config watch", log.Field{Key: "key", Value: key})
	if err := l.provider.Watch(key, callback); err != nil {
		l.logger.Error("config watch failed", log.Field{Key: "key", Value: key}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.Info("config watch registered", log.Field{Key: "key", Value: key})
	return nil
}

// Close closes the provider and logs any error.
func (l *LoggedProvider) Close() error {
	l.logger.Info("config provider close")
	if err := l.provider.Close(); err != nil {
		l.logger.Error("config provider close failed", log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.Info("config provider closed")
	return nil
}

// LoggedConfigService adds logging to ConfigService operations.
type LoggedConfigService struct {
	svc    ConfigService
	logger log.Logger
}

// NewLoggedConfigService wraps a ConfigService with logging.
func NewLoggedConfigService(svc ConfigService, l log.Logger) *LoggedConfigService {
	return &LoggedConfigService{svc: svc, logger: l}
}

// Get retrieves configuration via gRPC and logs the request.
func (l *LoggedConfigService) Get(ctx context.Context, req *configpb.GetConfigRequest) (*configpb.GetConfigResponse, error) {
	l.logger.InfoContext(ctx, "config service get", log.Field{Key: "key", Value: req.GetKey()})
	resp, err := l.svc.Get(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "config service get failed", log.Field{Key: "key", Value: req.GetKey()}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "config service get success", log.Field{Key: "key", Value: req.GetKey()})
	return resp, nil
}

// Set updates configuration and logs the operation.
func (l *LoggedConfigService) Set(ctx context.Context, req *configpb.SetConfigRequest) (*configpb.SetConfigResponse, error) {
	l.logger.InfoContext(ctx, "config service set", log.Field{Key: "key", Value: req.GetKey()})
	resp, err := l.svc.Set(ctx, req)
	if err != nil {
		l.logger.ErrorContext(ctx, "config service set failed", log.Field{Key: "key", Value: req.GetKey()}, log.Field{Key: "error", Value: err.Error()})
		return nil, err
	}
	l.logger.InfoContext(ctx, "config service set success", log.Field{Key: "key", Value: req.GetKey()})
	return resp, nil
}

// Watch streams configuration updates and logs start and errors.
func (l *LoggedConfigService) Watch(req *configpb.WatchConfigRequest, stream configpb.ConfigService_WatchServer) error {
	l.logger.Info("config service watch", log.Field{Key: "key", Value: req.GetKeyPattern()})
	if err := l.svc.Watch(req, stream); err != nil {
		l.logger.Error("config service watch failed", log.Field{Key: "key", Value: req.GetKeyPattern()}, log.Field{Key: "error", Value: err.Error()})
		return err
	}
	l.logger.Info("config service watch completed", log.Field{Key: "key", Value: req.GetKeyPattern()})
	return nil
}
