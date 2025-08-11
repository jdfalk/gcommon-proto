// file: pkg/grpc/client/pool.go
// version: 1.0.0
// guid: 1550e9bf-a852-4038-921d-f918aaf5933d

package client

import (
	"context"
	"sync"

	"google.golang.org/grpc"
)

// Pool manages connections to a set of service addresses.
type Pool struct {
	mu       sync.Mutex
	manager  *Manager
	balancer *RoundRobin
	resolver *Resolver
	opts     []grpc.DialOption
}

// NewPool creates a Pool using resolver addresses.
func NewPool(res *Resolver, opts ...grpc.DialOption) *Pool {
	p := &Pool{manager: NewManager(), resolver: res, opts: opts}
	if res != nil {
		// initialize balancer with current addresses
		var addrs []string
		res.discovery.mu.RLock()
		for _, addr := range res.discovery.services {
			addrs = append(addrs, addr)
		}
		res.discovery.mu.RUnlock()
		p.balancer = NewRoundRobin(addrs)
	}
	return p
}

// Get returns a connection using round-robin balancing.
func (p *Pool) Get(ctx context.Context) (*grpc.ClientConn, error) {
	p.mu.Lock()
	bal := p.balancer
	res := p.resolver
	p.mu.Unlock()
	if bal == nil || res == nil {
		return p.manager.Get(ctx, "", p.opts...)
	}
	addr := bal.Next()
	if addr == "" {
		return nil, grpc.ErrClientConnClosing
	}
	return p.manager.Get(ctx, addr, p.opts...)
}

// UpdateAddresses sets new addresses for load balancing.
func (p *Pool) UpdateAddresses(addrs []string) {
	p.mu.Lock()
	p.balancer = NewRoundRobin(addrs)
	p.mu.Unlock()
}

// Close closes all pooled connections.
func (p *Pool) Close() error {
	return p.manager.Close()
}
