// file: pkg/grpc/client/resolver.go
// version: 1.0.0
// guid: 7742ff84-6c2d-4e04-9e85-5896fb9b8d39

package client

import "sync"

// Resolver adds watch capability on top of Discovery.
type Resolver struct {
	mu          sync.RWMutex
	discovery   *Discovery
	subscribers map[string][]chan string
}

// NewResolver creates a resolver using an existing discovery instance.
func NewResolver(d *Discovery) *Resolver {
	if d == nil {
		d = NewDiscovery()
	}
	return &Resolver{discovery: d, subscribers: make(map[string][]chan string)}
}

// Update sets the service address and notifies subscribers.
func (r *Resolver) Update(name, addr string) {
	r.discovery.Register(name, addr)
	r.mu.RLock()
	subs := append([]chan string(nil), r.subscribers[name]...)
	r.mu.RUnlock()
	for _, ch := range subs {
		select {
		case ch <- addr:
		default:
		}
	}
}

// Resolve returns the current address for the service.
func (r *Resolver) Resolve(name string) (string, bool) {
	return r.discovery.Lookup(name)
}

// Watch returns a channel notified when the service address changes.
func (r *Resolver) Watch(name string) <-chan string {
	ch := make(chan string, 1)
	r.mu.Lock()
	r.subscribers[name] = append(r.subscribers[name], ch)
	r.mu.Unlock()
	if addr, ok := r.discovery.Lookup(name); ok {
		ch <- addr
	}
	return ch
}

// Close unsubscribes all watchers.
func (r *Resolver) Close() {
	r.mu.Lock()
	defer r.mu.Unlock()
	for _, subs := range r.subscribers {
		for _, ch := range subs {
			close(ch)
		}
	}
	r.subscribers = make(map[string][]chan string)
}
