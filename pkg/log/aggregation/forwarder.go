// file: pkg/log/aggregation/forwarder.go
// version: 1.0.0
// guid: c2d3e4f5-a6b7-48c9-0d1e-2345678901de

package aggregation

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/log"
)

// Forwarder forwards log entries to multiple providers.
type Forwarder struct {
	providers []log.Provider
}

// NewForwarder creates a Forwarder with the given providers.
func NewForwarder(providers ...log.Provider) *Forwarder {
	return &Forwarder{providers: providers}
}

// Forward sends the entry to all providers.
func (f *Forwarder) Forward(ctx context.Context, entry log.LogEntry) {
	for _, p := range f.providers {
		p.InfoContext(ctx, entry.Message, toFields(entry.Fields)...)
	}
}

// toFields converts a map into slice of fields.
func toFields(m map[string]interface{}) []log.Field {
	fields := make([]log.Field, 0, len(m))
	for k, v := range m {
		fields = append(fields, log.Field{Key: k, Value: v})
	}
	return fields
}
