// file: pkg/metrics/grpc_provider.go
// version: 1.0.0
// guid: a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8

package metrics

import (
	"context"
	"fmt"
	"net/http"
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
	"google.golang.org/grpc"
)

// grpcProvider implements the Provider interface using the protobuf gRPC client
type grpcProvider struct {
	client proto.MetricsServiceClient
	conn   *grpc.ClientConn
	mu     sync.RWMutex
	tags   []Tag
}

// NewGRPCProvider creates a new metrics provider that uses the gRPC service
func NewGRPCProvider(client proto.MetricsServiceClient, conn *grpc.ClientConn) Provider {
	return &grpcProvider{
		client: client,
		conn:   conn,
		tags:   make([]Tag, 0),
	}
}

// Counter creates or retrieves a counter using the gRPC service
func (p *grpcProvider) Counter(name string, options ...Option) Counter {
	opts := &Options{}
	for _, opt := range options {
		opt(opts)
	}

	return &grpcCounter{
		client: p.client,
		name:   name,
		tags:   append(p.tags, opts.Tags...),
		help:   opts.Help,
	}
}

// Gauge creates or retrieves a gauge using the gRPC service
func (p *grpcProvider) Gauge(name string, options ...Option) Gauge {
	opts := &Options{}
	for _, opt := range options {
		opt(opts)
	}

	return &grpcGauge{
		client: p.client,
		name:   name,
		tags:   append(p.tags, opts.Tags...),
		help:   opts.Help,
	}
}

// Histogram creates or retrieves a histogram using the gRPC service
func (p *grpcProvider) Histogram(name string, options ...Option) Histogram {
	opts := &Options{}
	for _, opt := range options {
		opt(opts)
	}

	return &grpcHistogram{
		client:  p.client,
		name:    name,
		tags:    append(p.tags, opts.Tags...),
		help:    opts.Help,
		buckets: opts.Buckets,
	}
}

// Summary creates or retrieves a summary using the gRPC service
func (p *grpcProvider) Summary(name string, options ...Option) Summary {
	opts := &Options{}
	for _, opt := range options {
		opt(opts)
	}

	return &grpcSummary{
		client:    p.client,
		name:      name,
		tags:      append(p.tags, opts.Tags...),
		help:      opts.Help,
		quantiles: opts.Quantiles,
	}
}

// Timer creates or retrieves a timer using the gRPC service
func (p *grpcProvider) Timer(name string, options ...Option) Timer {
	opts := &Options{}
	for _, opt := range options {
		opt(opts)
	}

	return &grpcTimer{
		client: p.client,
		name:   name,
		tags:   append(p.tags, opts.Tags...),
		help:   opts.Help,
	}
}

// Registry returns a mock registry (gRPC providers don't have local registries)
func (p *grpcProvider) Registry() Registry {
	return &grpcRegistry{client: p.client}
}

// Handler returns a mock HTTP handler (gRPC providers don't serve HTTP directly)
func (p *grpcProvider) Handler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNotFound)
		fmt.Fprint(w, "gRPC provider does not serve HTTP metrics")
	})
}

// Start starts the provider (no-op for gRPC clients)
func (p *grpcProvider) Start(ctx context.Context) error {
	return nil
}

// Stop stops the provider by closing the gRPC connection
func (p *grpcProvider) Stop(ctx context.Context) error {
	if p.conn != nil {
		return p.conn.Close()
	}
	return nil
}

// WithTags returns a new provider with the given tags
func (p *grpcProvider) WithTags(tags ...Tag) Provider {
	p.mu.Lock()
	defer p.mu.Unlock()

	newProvider := &grpcProvider{
		client: p.client,
		conn:   p.conn,
		tags:   append(p.tags, tags...),
	}
	return newProvider
}
