package metrics

import (
	"errors"
	"testing"
)

// TestRegisterProvider tests the registration of a provider constructor.
func TestRegisterProvider(t *testing.T) {
	// Reset providers for this test
	defer func() {
		providers = make(map[string]ProviderFactory)
	}()

	// Register a test provider
	RegisterProvider("test", func(config Config) (Provider, error) {
		return nil, nil
	})

	// Check that the provider was registered
	if _, ok := providers["test"]; !ok {
		t.Error("Expected provider to be registered")
	}

	// Try registering the same provider again (should panic)
	defer func() {
		if r := recover(); r == nil {
			t.Error("Expected panic when registering duplicate provider")
		}
	}()
	RegisterProvider("test", func(config Config) (Provider, error) {
		return nil, nil
	})
}

// TestNewProvider tests the creation of a provider.
func TestNewProvider(t *testing.T) {
	// Reset providers for this test
	defer func() {
		providers = make(map[string]ProviderFactory)
	}()

	// Test with no providers registered
	_, err := NewProvider(Config{Provider: "test"})
	if err == nil {
		t.Error("Expected error when no providers registered")
	}

	// Register a test provider that returns an error
	RegisterProvider("error", func(config Config) (Provider, error) {
		return nil, errors.New("test error")
	})

	// Test with a provider that returns an error
	_, err = NewProvider(Config{Provider: "error"})
	if err == nil {
		t.Error("Expected error from provider factory")
	}

	// Register a successful test provider
	mockProvider := &mockProvider{}
	RegisterProvider("success", func(config Config) (Provider, error) {
		return mockProvider, nil
	})

	// Test with a successful provider
	provider, err := NewProvider(Config{Provider: "success"})
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if provider != mockProvider {
		t.Error("Expected provider to be the mock provider")
	}

	// Test with disabled metrics
	provider, err = NewProvider(Config{Provider: "success", Enabled: false})
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if _, ok := provider.(*noopProvider); !ok {
		t.Error("Expected provider to be a noop provider when disabled")
	}

	// Test with empty provider name
	provider, err = NewProvider(Config{})
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if _, ok := provider.(*noopProvider); !ok {
		t.Error("Expected provider to be a noop provider with empty provider name")
	}
}

// mockProvider is a mock implementation of Provider for testing
type mockProvider struct{}

func (p *mockProvider) Counter(name string, options ...Option) Counter {
	return nil
}

func (p *mockProvider) Gauge(name string, options ...Option) Gauge {
	return nil
}

func (p *mockProvider) Histogram(name string, options ...Option) Histogram {
	return nil
}

func (p *mockProvider) Summary(name string, options ...Option) Summary {
	return nil
}

func (p *mockProvider) Timer(name string, options ...Option) Timer {
	return nil
}

func (p *mockProvider) Registry() Registry {
	return nil
}

func (p *mockProvider) Handler() Handler {
	return nil
}

func (p *mockProvider) Start(ctx Context) error {
	return nil
}

func (p *mockProvider) Stop(ctx Context) error {
	return nil
}

func (p *mockProvider) WithTags(tags ...Tag) Provider {
	return p
}
