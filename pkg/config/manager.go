// file: pkg/config/manager.go
// version: 1.1.0
// guid: 1a9b0cdd-9e19-4dba-89c4-6e4a1a111111

package config

import (
	"fmt"
	"sync"
)

// ConfigSource loads configuration values.
type ConfigSource interface {
	Load() (map[string]interface{}, error)
}

// ConfigManager defines the unified configuration interface for gcommon.
type ConfigManager interface {
	Load(sources ...ConfigSource) error
	Get(key string) (interface{}, error)
	GetString(key string) (string, error)
	GetInt(key string) (int, error)
	GetBool(key string) (bool, error)
	Set(key string, value interface{}) error
	Watch(key string, callback func(interface{})) error
	Validate() error
	Merge(configs ...Config) error
}

// Config defines methods for accessing module and global configuration.
type Config interface {
	GetModuleConfig(module string) (ModuleConfig, error)
	SetModuleConfig(module string, cfg ModuleConfig) error
	GetGlobalConfig() (GlobalConfig, error)
}

// ModuleConfig represents configuration for a single module.
type ModuleConfig interface{}

// Manager implements ConfigManager with basic in-memory storage.
type Manager struct {
	mu       sync.RWMutex
	data     map[string]interface{}
	watchers map[string][]func(interface{})
}

// NewManager creates a new Manager instance.
func NewManager() *Manager {
	return &Manager{
		data:     make(map[string]interface{}),
		watchers: make(map[string][]func(interface{})),
	}
}

// Load reads configuration from provided sources.
func (m *Manager) Load(sources ...ConfigSource) error {
	for _, src := range sources {
		cfg, err := src.Load()
		if err != nil {
			return err
		}
		for k, v := range cfg {
			if err := m.Set(k, v); err != nil {
				return err
			}
		}
	}
	return nil
}

// Get retrieves a value by key.
func (m *Manager) Get(key string) (interface{}, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	v, ok := m.data[key]
	if !ok {
		return nil, fmt.Errorf("key %s not found", key)
	}
	return v, nil
}

// GetString retrieves a string value.
func (m *Manager) GetString(key string) (string, error) {
	v, err := m.Get(key)
	if err != nil {
		return "", err
	}
	s, ok := v.(string)
	if !ok {
		return "", fmt.Errorf("key %s not a string", key)
	}
	return s, nil
}

// GetInt retrieves an int value.
func (m *Manager) GetInt(key string) (int, error) {
	v, err := m.Get(key)
	if err != nil {
		return 0, err
	}
	i, ok := v.(int)
	if !ok {
		return 0, fmt.Errorf("key %s not an int", key)
	}
	return i, nil
}

// GetBool retrieves a bool value.
func (m *Manager) GetBool(key string) (bool, error) {
	v, err := m.Get(key)
	if err != nil {
		return false, err
	}
	b, ok := v.(bool)
	if !ok {
		return false, fmt.Errorf("key %s not a bool", key)
	}
	return b, nil
}

// Set stores a value and notifies watchers.
func (m *Manager) Set(key string, value interface{}) error {
	m.mu.Lock()
	m.data[key] = value
	callbacks := m.watchers[key]
	m.mu.Unlock()
	for _, cb := range callbacks {
		cb(value)
	}
	return nil
}

// Watch registers a callback for key changes.
func (m *Manager) Watch(key string, callback func(interface{})) error {
	m.mu.Lock()
	m.watchers[key] = append(m.watchers[key], callback)
	m.mu.Unlock()
	return nil
}

// Validate performs configuration validation.
func (m *Manager) Validate() error {
	return ValidateMap(m.data)
}

// Merge merges additional configurations.
func (m *Manager) Merge(configs ...Config) error {
	for _, cfg := range configs {
		g, err := cfg.GetGlobalConfig()
		if err != nil {
			return err
		}
		_ = g // TODO: merge global config values
	}
	return nil
}
