// file: pkg/plugins/registry.go
// version: 1.0.0
// guid: 81f00222-ba03-4912-9606-6aaa3c836d32

package plugins

import (
	"context"
	"errors"
	"sync"
)

// HealthStatus represents basic plugin health information.
type HealthStatus struct {
	OK   bool
	Info string
}

// Plugin defines the core behavior for all plugins.
type Plugin interface {
	Name() string
	Version() string
	Initialize(config map[string]interface{}) error
	Start(ctx context.Context) error
	Stop(ctx context.Context) error
	Health() HealthStatus
}

// ProviderPlugin exposes a provider implementation.
type ProviderPlugin interface {
	Plugin
	GetProvider() interface{}
}

// Registry manages registered plugins and their metadata.
type Registry struct {
	mu       sync.RWMutex
	plugins  map[string]Plugin
	metadata map[string]Metadata
}

// NewRegistry creates a new plugin registry.
func NewRegistry() *Registry {
	return &Registry{plugins: make(map[string]Plugin), metadata: make(map[string]Metadata)}
}

// Register adds a plugin with metadata to the registry.
func (r *Registry) Register(p Plugin, md Metadata) error {
	r.mu.Lock()
	defer r.mu.Unlock()
	if _, exists := r.plugins[p.Name()]; exists {
		return errors.New("plugin already registered")
	}
	r.plugins[p.Name()] = p
	r.metadata[p.Name()] = md
	return nil
}

// Get retrieves a plugin by name.
func (r *Registry) Get(name string) (Plugin, Metadata, bool) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	p, ok := r.plugins[name]
	if !ok {
		return nil, Metadata{}, false
	}
	md := r.metadata[name]
	return p, md, true
}

// List returns all registered plugins.
func (r *Registry) List() []Plugin {
	r.mu.RLock()
	defer r.mu.RUnlock()
	result := make([]Plugin, 0, len(r.plugins))
	for _, p := range r.plugins {
		result = append(result, p)
	}
	return result
}

// ListByType returns all plugins matching the specified type.
func (r *Registry) ListByType(t Type) []Plugin {
	r.mu.RLock()
	defer r.mu.RUnlock()
	var result []Plugin
	for name, p := range r.plugins {
		if md := r.metadata[name]; md.Type == t {
			result = append(result, p)
		}
	}
	return result
}
