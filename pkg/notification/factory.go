// file: pkg/notification/factory.go
// version: 1.1.0
// guid: 6f75be17-2ad5-4fdb-b8c1-cbc5e6f9654a

package notification

import "fmt"

// ProviderConstructor creates a Provider from config.
type ProviderConstructor func(cfg map[string]any) (Provider, error)

var registry = map[string]ProviderConstructor{}

// RegisterProvider registers a provider constructor by name.
func RegisterProvider(name string, ctor ProviderConstructor) {
	if name == "" || ctor == nil {
		return
	}
	registry[name] = ctor
}

// NewProvider returns a provider by name using supplied config.
func NewProvider(name string, cfg map[string]any) (Provider, error) {
	ctor, ok := registry[name]
	if !ok {
		return nil, fmt.Errorf("unknown provider: %s", name)
	}
	p, err := ctor(cfg)
	if err != nil {
		return nil, err
	}
	return p, p.ValidateConfig(cfg)
}

// Providers register themselves in their init functions.
