// file: pkg/log/factory.go

package log

import (
	"context"
	"fmt"
	"io"
	"sync"
)

// ProviderConstructor creates a Provider from a Config.
type ProviderConstructor func(config Config) (Provider, error)

// providerRegistry stores provider constructors keyed by name.
var providerRegistry = struct {
	sync.RWMutex
	constructors map[string]ProviderConstructor
}{constructors: make(map[string]ProviderConstructor)}

// RegisterProvider registers a provider constructor.
func RegisterProvider(name string, constructor ProviderConstructor) {
	providerRegistry.Lock()
	defer providerRegistry.Unlock()
	providerRegistry.constructors[name] = constructor
}

// NewProvider creates a new provider from the given config.
func NewProvider(config Config) (Provider, error) {
	providerRegistry.RLock()
	constructor, ok := providerRegistry.constructors[config.Provider]
	providerRegistry.RUnlock()
	if !ok {
		if config.Provider == "" || config.Provider == "noop" {
			return newNoopProvider(), nil
		}
		return nil, fmt.Errorf("unknown log provider: %s", config.Provider)
	}
	return constructor(config)
}

// noopProvider is a provider that discards all logs.
type noopProvider struct{}

func newNoopProvider() Provider { return &noopProvider{} }

func (p *noopProvider) Name() string          { return "noop" }
func (p *noopProvider) Close() error          { return nil }
func (p *noopProvider) Sync() error           { return nil }
func (p *noopProvider) SetOutput(w io.Writer) {}
func (p *noopProvider) AddHook(h Hook) error  { return nil }

// Logger methods for noopProvider
func (p *noopProvider) Debug(msg string, fields ...Field)                             {}
func (p *noopProvider) DebugContext(ctx context.Context, msg string, fields ...Field) {}
func (p *noopProvider) Info(msg string, fields ...Field)                              {}
func (p *noopProvider) InfoContext(ctx context.Context, msg string, fields ...Field)  {}
func (p *noopProvider) Warn(msg string, fields ...Field)                              {}
func (p *noopProvider) WarnContext(ctx context.Context, msg string, fields ...Field)  {}
func (p *noopProvider) Error(msg string, fields ...Field)                             {}
func (p *noopProvider) ErrorContext(ctx context.Context, msg string, fields ...Field) {}
func (p *noopProvider) Fatal(msg string, fields ...Field)                             {}
func (p *noopProvider) FatalContext(ctx context.Context, msg string, fields ...Field) {}
func (p *noopProvider) With(fields ...Field) Logger                                   { return p }
func (p *noopProvider) WithContext(ctx context.Context) Logger                        { return p }
func (p *noopProvider) SetLevel(level Level)                                          {}
func (p *noopProvider) GetLevel() Level                                               { return InfoLevel }
