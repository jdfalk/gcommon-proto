// file: pkg/config/providers/file.go
// version: 1.0.0
// guid: 0bf1a8f9-ac21-438a-9f20-bc0d3b237f6a

package providers

import (
	"encoding/json"
	"fmt"
	"os"
	"sync"

	"github.com/jdfalk/gcommon/pkg/config"
)

// FileProvider stores configuration in a JSON file.
type FileProvider struct {
	path     string
	mu       sync.RWMutex
	data     map[string]interface{}
	watchers map[string][]func(interface{})
}

// NewFileProvider creates a FileProvider from the given config map.
func NewFileProvider(cfg map[string]interface{}) (config.Provider, error) {
	path, ok := cfg["path"].(string)
	if !ok || path == "" {
		return nil, fmt.Errorf("path is required")
	}
	fp := &FileProvider{path: path, data: map[string]interface{}{}, watchers: map[string][]func(interface{}){}}
	if err := fp.load(); err != nil {
		return nil, err
	}
	return fp, nil
}

func (p *FileProvider) load() error {
	p.mu.Lock()
	defer p.mu.Unlock()
	b, err := os.ReadFile(p.path)
	if err != nil {
		if os.IsNotExist(err) {
			p.data = map[string]interface{}{}
			return nil
		}
		return err
	}
	return json.Unmarshal(b, &p.data)
}

func (p *FileProvider) save() error {
	b, err := json.MarshalIndent(p.data, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(p.path, b, 0o600)
}

// Get retrieves a value from the file store.
func (p *FileProvider) Get(key string) (interface{}, error) {
	p.mu.RLock()
	defer p.mu.RUnlock()
	v, ok := p.data[key]
	if !ok {
		return nil, fmt.Errorf("key not found: %s", key)
	}
	return v, nil
}

// Set writes a value to the file store.
func (p *FileProvider) Set(key string, value interface{}) error {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.data[key] = value
	if err := p.save(); err != nil {
		return err
	}
	for _, cb := range p.watchers[key] {
		cb(value)
	}
	return nil
}

// Watch registers a callback for key changes.
func (p *FileProvider) Watch(key string, callback func(interface{})) error {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.watchers[key] = append(p.watchers[key], callback)
	return nil
}

// Close is a no-op for FileProvider.
func (p *FileProvider) Close() error { return nil }

func init() {
	config.RegisterProvider("file", NewFileProvider)
}
