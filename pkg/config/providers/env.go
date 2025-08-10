// file: pkg/config/providers/env.go
// version: 1.0.1
// guid: 1782fede-2351-4201-a56d-76073ef4fd87

package providers

import (
	"errors"
	"fmt"
	"os"
	"strings"

	"github.com/jdfalk/gcommon/pkg/config"
)

// EnvProvider reads configuration from environment variables with optional prefix
// TODO: Document naming conventions and prefix behavior
// TODO: Support complex types via serialization
// TODO: Add caching for lookups
// TODO: Provide case sensitivity options
// TODO: Support watching for changes using polling
// TODO: Add metrics for access frequency
// TODO: Implement batching for Set operations
// TODO: Integrate with secrets management for sensitive variables
// TODO: Include validation hooks
// TODO: Add ability to map env vars to nested keys
type EnvProvider struct {
	Prefix string
}

// NewEnvProvider creates a new EnvProvider with optional prefix
func NewEnvProvider(prefix string) (*EnvProvider, error) {
	// TODO: Validate prefix format
	return &EnvProvider{Prefix: prefix}, nil
}

// Get retrieves a value by key from environment variables
func (p *EnvProvider) Get(key string) (interface{}, error) {
	fullKey := p.Prefix + key
	if val, ok := os.LookupEnv(fullKey); ok {
		return val, nil
	}
	return nil, fmt.Errorf("key not found: %s", fullKey)
}

// Set sets an environment variable value
func (p *EnvProvider) Set(key string, value interface{}) error {
	str, ok := value.(string)
	if !ok {
		return errors.New("value must be a string")
	}
	fullKey := p.Prefix + key
	return os.Setenv(fullKey, strings.TrimSpace(str))
}

// Watch registers callback for key changes using polling
func (p *EnvProvider) Watch(key string, callback func(interface{})) error {
	// TODO: Implement efficient polling or OS notifications
	go func() {
		fullKey := p.Prefix + key
		last := os.Getenv(fullKey)
		for {
			current := os.Getenv(fullKey)
			if current != last {
				callback(current)
				last = current
			}
		}
	}()
	return nil
}

// Close cleans up resources
func (p *EnvProvider) Close() error { return nil }

// Compile time check for interface implementation
var _ config.Provider = (*EnvProvider)(nil)
