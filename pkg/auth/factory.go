// file: pkg/auth/factory.go
// version: 1.0.0
// guid: 1686eee6-4b5b-4c37-9b55-b3beef6fd254

// Package auth provides authentication and authorization interfaces.
package auth

import "fmt"

// ProviderFactory constructs auth providers by name.
type ProviderFactory struct {
	providers map[string]func() AuthProvider
}

// NewProviderFactory creates a new provider factory.
func NewProviderFactory() *ProviderFactory {
	return &ProviderFactory{providers: make(map[string]func() AuthProvider)}
}

// Register adds a provider constructor with the given name.
func (f *ProviderFactory) Register(name string, constructor func() AuthProvider) {
	if f.providers == nil {
		f.providers = make(map[string]func() AuthProvider)
	}
	f.providers[name] = constructor
}

// Get returns a provider by name.
func (f *ProviderFactory) Get(name string) (AuthProvider, error) {
	constructor, ok := f.providers[name]
	if !ok {
		return nil, fmt.Errorf("provider %s not registered", name)
	}
	return constructor(), nil
}
