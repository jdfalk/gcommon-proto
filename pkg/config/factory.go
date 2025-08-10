// file: pkg/config/factory.go
// version: 1.0.0
// guid: fe2737c0-4fd4-43e4-8d7d-12cd4f4daaa9

package config

import "fmt"

// ProviderConstructor constructs a Provider from configuration options.
type ProviderConstructor func(map[string]interface{}) (Provider, error)

var providerRegistry = make(map[string]ProviderConstructor)

// RegisterProvider registers a provider constructor by name.
func RegisterProvider(name string, constructor ProviderConstructor) {
	providerRegistry[name] = constructor
}

// NewProvider creates a Provider based on its registered type.
func NewProvider(providerType string, cfg map[string]interface{}) (Provider, error) {
	constructor, exists := providerRegistry[providerType]
	if !exists {
		return nil, fmt.Errorf("unknown provider type: %s", providerType)
	}
	return constructor(cfg)
}
