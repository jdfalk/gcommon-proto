// file: pkg/grpc/client/balancer.go
// version: 1.0.0
// guid: e4b1f03e-6cd6-4bf4-ab25-b04a22172853

package client

import "sync/atomic"

// RoundRobin implements a simple round-robin balancer over addresses.
type RoundRobin struct {
	addrs []string
	idx   uint32
}

// NewRoundRobin creates a new balancer with provided addresses.
func NewRoundRobin(addrs []string) *RoundRobin {
	return &RoundRobin{addrs: append([]string(nil), addrs...)}
}

// Next returns the next address in sequence.
func (r *RoundRobin) Next() string {
	if len(r.addrs) == 0 {
		return ""
	}
	i := atomic.AddUint32(&r.idx, 1)
	return r.addrs[int(i)%len(r.addrs)]
}
