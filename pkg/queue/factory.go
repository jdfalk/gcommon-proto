// file: pkg/queue/factory.go
// version: 1.0.0
// guid: b587cf14-a926-43bf-941b-3a8cf68f9357

package queue

import (
	"fmt"
	"sync"
)

type ProviderFactory func() Queue

var (
	mu        sync.RWMutex
	providers = make(map[string]ProviderFactory)
)

func RegisterProvider(name string, factory ProviderFactory) {
	mu.Lock()
	defer mu.Unlock()
	providers[name] = factory
}

func CreateProvider(name string) (Queue, error) {
	mu.RLock()
	factory, ok := providers[name]
	mu.RUnlock()
	if !ok {
		return nil, fmt.Errorf("provider %s not registered", name)
	}
	return factory(), nil
}
