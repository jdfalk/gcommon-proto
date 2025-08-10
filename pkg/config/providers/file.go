// file: pkg/config/providers/file.go
// version: 1.0.1
// guid: 0bf1a8f9-ac21-438a-9f20-bc0d3b237f6a

package providers

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"sync"

	"github.com/jdfalk/gcommon/pkg/config"
)

// FileProvider loads configuration from a JSON file with enhanced functionality
// TODO: Support YAML and other formats
// TODO: Add file watching using fsnotify
// TODO: Implement atomic writes
// TODO: Provide schema validation before write
// TODO: Add encryption for sensitive fields
// TODO: Support partial updates
// TODO: Integrate with versioning and history
// TODO: Provide examples for complex structures
// TODO: Add backup and restore capabilities
// TODO: Add caching layer
type FileProvider struct {
	path     string
	mu       sync.RWMutex
	data     map[string]interface{}
	watchers map[string][]func(interface{})
}

// NewFileProvider creates a FileProvider from the given file path or config map
func NewFileProvider(pathOrConfig interface{}) (*FileProvider, error) {
	var path string
	switch v := pathOrConfig.(type) {
	case string:
		path = v
	case map[string]interface{}:
		p, ok := v["path"].(string)
		if !ok || p == "" {
			return nil, fmt.Errorf("path is required")
		}
		path = p
	default:
		return nil, fmt.Errorf("invalid config type")
	}

	fp := &FileProvider{
		path:     path,
		data:     map[string]interface{}{},
		watchers: map[string][]func(interface{}){},
	}
	if err := fp.load(); err != nil {
		return nil, err
	}
	return fp, nil
}

func (p *FileProvider) load() error {
	p.mu.Lock()
	defer p.mu.Unlock()
	b, err := ioutil.ReadFile(p.path)
	if err != nil {
		if errors.Is(err, os.ErrNotExist) {
			p.data = map[string]interface{}{}
			return nil
		}
		return err
	}
	if len(b) == 0 {
		p.data = map[string]interface{}{}
		return nil
	}
	return json.Unmarshal(b, &p.data)
}

func (p *FileProvider) save() error {
	p.mu.RLock()
	b, err := json.MarshalIndent(p.data, "", "  ")
	p.mu.RUnlock()
	if err != nil {
		return err
	}
	return ioutil.WriteFile(p.path, b, 0644)
}

// Get retrieves a value from the file store
func (p *FileProvider) Get(key string) (interface{}, error) {
	p.mu.RLock()
	defer p.mu.RUnlock()
	v, ok := p.data[key]
	if !ok {
		return nil, fmt.Errorf("key not found: %s", key)
	}
	return v, nil
}

// Set writes a value to the file store and notifies watchers
func (p *FileProvider) Set(key string, value interface{}) error {
	p.mu.Lock()
	p.data[key] = value
	watchers := append([]func(interface{}){}, p.watchers[key]...)
	p.mu.Unlock()

	if err := p.save(); err != nil {
		return err
	}

	for _, cb := range watchers {
		cb(value)
	}
	return nil
}

// Watch registers a callback for key changes
func (p *FileProvider) Watch(key string, callback func(interface{})) error {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.watchers[key] = append(p.watchers[key], callback)
	return nil
}

// Close cleans up resources
func (p *FileProvider) Close() error { return nil }

var _ config.Provider = (*FileProvider)(nil)
