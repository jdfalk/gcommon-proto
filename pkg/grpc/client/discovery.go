// file: pkg/grpc/client/discovery.go
// version: 1.1.0
// guid: 129fc533-97d8-4e8a-86d1-77dd2474035b

package client

import "sync"

// Discovery provides a simple registry for service addresses.
type Discovery struct {
	mu       sync.RWMutex
	services map[string]string
}

// NewDiscovery creates an empty discovery registry.
func NewDiscovery() *Discovery {
	return &Discovery{services: make(map[string]string)}
}

// Register records a service name and address.
func (d *Discovery) Register(name, addr string) {
	d.mu.Lock()
	d.services[name] = addr
	d.mu.Unlock()
}

// Lookup returns the address for a service name.
func (d *Discovery) Lookup(name string) (string, bool) {
	d.mu.RLock()
	addr, ok := d.services[name]
	d.mu.RUnlock()
	return addr, ok
}
