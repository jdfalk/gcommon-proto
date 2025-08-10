// file: pkg/config/providers/env.go
// version: 1.0.0
// guid: 1782fede-2351-4201-a56d-76073ef4fd87

package providers

import (
	"errors"
	"fmt"
	"os"

	"github.com/jdfalk/gcommon/pkg/config"
)

// EnvProvider reads configuration from environment variables.
type EnvProvider struct{}

// NewEnvProvider creates a new EnvProvider.
func NewEnvProvider(cfg map[string]interface{}) (config.Provider, error) {
	return &EnvProvider{}, nil
}

// Get retrieves a value by key from environment variables.
func (p *EnvProvider) Get(key string) (interface{}, error) {
	if val, ok := os.LookupEnv(key); ok {
		return val, nil
	}
	return nil, fmt.Errorf("key not found: %s", key)
}

// Set sets an environment variable value.
func (p *EnvProvider) Set(key string, value interface{}) error {
	str, ok := value.(string)
	if !ok {
		return errors.New("value must be a string")
	}
	return os.Setenv(key, str)
}

// Watch is not supported for environment variables.
func (p *EnvProvider) Watch(key string, callback func(interface{})) error {
	return errors.New("watch not supported for env provider")
}

// Close is a no-op for EnvProvider.
func (p *EnvProvider) Close() error { return nil }

func init() {
	config.RegisterProvider("env", NewEnvProvider)
}
