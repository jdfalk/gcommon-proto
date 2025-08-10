// file: pkg/config/factory_test.go
// version: 1.0.1
// guid: 9783f849-cb18-4969-bf72-5d420dcaa31f

package config

import "testing"

type dummyProvider struct{}

func (d *dummyProvider) Get(key string) (interface{}, error)                { return nil, nil }
func (d *dummyProvider) Set(key string, value interface{}) error            { return nil }
func (d *dummyProvider) Watch(key string, callback func(interface{})) error { return nil }
func (d *dummyProvider) Close() error                                       { return nil }

func TestNewProvider_Unknown(t *testing.T) {
	t.Parallel()
	if _, err := NewProvider("missing", nil); err == nil {
		t.Fatalf("expected error for unknown provider")
	}
}

func TestRegisterAndCreateProvider(t *testing.T) {
	t.Parallel()
	RegisterProvider("dummy", func(cfg map[string]interface{}) (Provider, error) {
		return &dummyProvider{}, nil
	})
	if p, err := NewProvider("dummy", nil); err != nil || p == nil {
		t.Fatalf("expected provider, got %v", err)
	}
}

// TestFactoryRegistration tests provider registration and creation
func TestFactoryRegistration(t *testing.T) {
	RegisterProvider("env", func(cfg map[string]interface{}) (Provider, error) {
		prefix := ""
		if cfg != nil {
			if p, ok := cfg["prefix"].(string); ok {
				prefix = p
			}
		}
		// Note: This would need to be adapted once env provider is fixed
		// Using prefix in dummy provider to avoid unused variable error
		_ = prefix
		return &dummyProvider{}, nil
	})
	p, err := NewProvider("env", nil)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if p == nil {
		t.Fatalf("expected provider instance")
	}
}

// TODO: Add negative tests for unknown provider
// TODO: Add concurrency tests
// TODO: Add benchmark for provider creation
