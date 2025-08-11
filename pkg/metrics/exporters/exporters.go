// file: pkg/metrics/exporters/exporters.go
// version: 1.0.1
// guid: 0a1b2c3d-4e5f-6789-abcd-0123456789ab

// Package exporters contains helper types for metrics exporters.
package exporters

import (
	"context"
	"errors"
	"sync"

	metrics "github.com/jdfalk/gcommon/pkg/metrics"
)

// ErrExporterNotConfigured is returned when an exporter is not properly configured.
var ErrExporterNotConfigured = errors.New("exporter not configured")

// Exporter defines the behaviour for metrics exporters.
//
// Exporters are responsible for exposing metrics collected by a provider to
// external systems. Each exporter implementation should manage its own
// lifecycle and ensure thread-safety. The interface intentionally mirrors the
// Provider interface to keep the integration straightforward.
type Exporter interface {
	// Start launches the exporter. Implementations should spawn any required
	// goroutines and begin serving metrics to the target system.
	Start(ctx context.Context) error

	// Stop gracefully stops the exporter. Implementations should release all
	// resources and ensure that any pending metrics are flushed before
	// returning.
	Stop(ctx context.Context) error

	// WithProvider attaches a metrics provider to the exporter.
	WithProvider(provider metrics.Provider) Exporter
}

// BaseExporter provides a minimal implementation of the Exporter interface that
// can be embedded by other exporters. It handles provider assignment and offers
// basic lifecycle management utilities. The implementation is intentionally
// simple and primarily serves as a convenience for skeleton implementations.
type BaseExporter struct {
	mu       sync.RWMutex
	provider metrics.Provider
	started  bool
}

// WithProvider attaches a metrics provider to the exporter.
func (b *BaseExporter) WithProvider(provider metrics.Provider) Exporter {
	b.mu.Lock()
	defer b.mu.Unlock()
	b.provider = provider
	return b
}

// Provider returns the currently configured metrics provider.
// It is safe for concurrent use.
func (b *BaseExporter) Provider() metrics.Provider {
	b.mu.RLock()
	defer b.mu.RUnlock()
	return b.provider
}

// MarkStarted marks the exporter as started.
// It does not perform any operations beyond updating internal state.
func (b *BaseExporter) MarkStarted() {
	b.mu.Lock()
	b.started = true
	b.mu.Unlock()
}

// MarkStopped marks the exporter as stopped.
func (b *BaseExporter) MarkStopped() {
	b.mu.Lock()
	b.started = false
	b.mu.Unlock()
}

// IsStarted reports whether the exporter has been started.
func (b *BaseExporter) IsStarted() bool {
	b.mu.RLock()
	defer b.mu.RUnlock()
	return b.started
}

// Start implements Exporter and performs no operation.
// Concrete exporters should override this method.
func (b *BaseExporter) Start(ctx context.Context) error { return nil }

// Stop implements Exporter and performs no operation.
// Concrete exporters should override this method.
func (b *BaseExporter) Stop(ctx context.Context) error { return nil }

// ensure interface implementation
var _ Exporter = (*BaseExporter)(nil)

//
// NOTE: This file only provides scaffolding for exporter implementations. The
// concrete exporters within this package are intentionally minimal and include
// extensive TODO comments describing required behaviour. Future contributors
// should replace these placeholders with production-ready logic that integrates
// with the metrics providers defined in the root metrics package.
//
// The intention of these skeletons is to provide a clear starting point while
// emphasising that significant work remains. The repeated TODO comments found
// throughout the exporter implementations are deliberate and are intended to
// draw attention to the incomplete nature of this code.
//
// Additional helper types or shared utilities for exporters should be added to
// this file as needed. For now the focus is on establishing a consistent API
// surface and providing room for future development.
// TODO: revisit exporter interface for streaming support
