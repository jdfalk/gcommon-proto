package log

import (
	"errors"
	"testing"
)

// TestRegisterProvider verifies provider registration.
func TestRegisterProvider(t *testing.T) {
	defer func() { providerRegistry.constructors = make(map[string]ProviderConstructor) }()

	RegisterProvider("test", func(config Config) (Provider, error) { return &noopProvider{}, nil })
	if _, ok := providerRegistry.constructors["test"]; !ok {
		t.Error("expected provider to be registered")
	}
}

// TestNewProvider verifies provider creation.
func TestNewProvider(t *testing.T) {
	defer func() { providerRegistry.constructors = make(map[string]ProviderConstructor) }()

	if _, err := NewProvider(Config{Provider: "missing"}); err == nil {
		t.Error("expected error for unknown provider")
	}

	RegisterProvider("err", func(c Config) (Provider, error) { return nil, errors.New("bad") })
	if _, err := NewProvider(Config{Provider: "err"}); err == nil {
		t.Error("expected error from provider")
	}

	mock := &noopProvider{}
	RegisterProvider("ok", func(c Config) (Provider, error) { return mock, nil })
	p, err := NewProvider(Config{Provider: "ok"})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if p != mock {
		t.Error("expected returned provider")
	}

	p, err = NewProvider(Config{})
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, ok := p.(*noopProvider); !ok {
		t.Error("expected noop provider when provider name empty")
	}
}
