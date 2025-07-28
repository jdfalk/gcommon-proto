package otel

import (
	"context"
	"sync"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/metric"
)

// gauge implements the metrics.Gauge interface for OpenTelemetry.
type gauge struct {
	gauge       metric.Int64ObservableGauge
	asyncGauge  metric.Registration
	registry    *registry
	name        string
	description string
	attrs       []attribute.KeyValue
	mutex       sync.RWMutex
	value       int64 // Atomic for current value
}

// newGauge creates a new OpenTelemetry gauge.
func newGauge(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Gauge {
	opts := parseOptions(options...)

	// Combine global tags with metric-specific tags
	allTags := append(globalTags, opts.Tags...)
	attrs := convertToAttributes(allTags)

	// Create a more descriptive name if namespace/subsystem are provided
	fullName := name
	if registry.namespace != "" {
		if registry.subsystem != "" {
			fullName = registry.namespace + "." + registry.subsystem + "." + name
		} else {
			fullName = registry.namespace + "." + name
		}
	}

	registry.mutex.Lock()
	defer registry.mutex.Unlock()

	// Check if we already have this gauge
	if existing, ok := registry.metrics[fullName]; ok {
		if g, ok := existing.(*gauge); ok {
			return g
		}
	}

	// Create a new gauge
	description := opts.Description
	if description == "" {
		description = "Gauge " + fullName
	}

	g := &gauge{
		registry:    registry,
		name:        fullName,
		description: description,
		attrs:       attrs,
	}

	// Create an observable gauge that returns the current value
	otelGauge, err := registry.meter.Int64ObservableGauge(
		fullName,
		metric.WithDescription(description),
		metric.WithUnit(opts.Unit),
	)

	if err != nil {
		// In a production implementation, we would log this error
		// For now, just return the gauge without registration
		registry.metrics[fullName] = g
		return g
	}

	// Register the gauge observation callback
	callback := func(ctx context.Context, result metric.Int64Observer) error {
		result.Observe(atomic.LoadInt64(&g.value), g.attrs...)
		return nil
	}

	asyncGauge, err := registry.meter.RegisterCallback(callback, otelGauge)
	if err != nil {
		// In a production implementation, we would log this error
		registry.metrics[fullName] = g
		return g
	}

	g.gauge = otelGauge
	g.asyncGauge = asyncGauge

	// Store in registry
	registry.metrics[fullName] = g

	return g
}

// Set sets the gauge to the given value.
func (g *gauge) Set(value float64) {
	atomic.StoreInt64(&g.value, int64(value))
}

// Inc increments the gauge by 1.
func (g *gauge) Inc() {
	atomic.AddInt64(&g.value, 1)
}

// Dec decrements the gauge by 1.
func (g *gauge) Dec() {
	atomic.AddInt64(&g.value, -1)
}

// Add adds the given value to the gauge.
func (g *gauge) Add(value float64) {
	atomic.AddInt64(&g.value, int64(value))
}

// Sub subtracts the given value from the gauge.
func (g *gauge) Sub(value float64) {
	atomic.AddInt64(&g.value, -int64(value))
}

// WithTags returns a new gauge with the given tags.
func (g *gauge) WithTags(tags ...metrics.Tag) metrics.Gauge {
	if len(tags) == 0 {
		return g
	}

	g.mutex.RLock()
	originalAttrs := g.attrs
	registry := g.registry
	name := g.name
	description := g.description
	g.mutex.RUnlock()

	// Combine existing attributes with new ones
	newAttrs := make([]attribute.KeyValue, len(originalAttrs))
	copy(newAttrs, originalAttrs)

	// Convert and add new tags as attributes
	tagAttrs := convertToAttributes(tags)

	// Create a map to handle overrides
	attrMap := make(map[string]string)
	for _, attr := range newAttrs {
		attrMap[string(attr.Key)] = attr.Value.AsString()
	}

	for _, attr := range tagAttrs {
		attrMap[string(attr.Key)] = attr.Value.AsString()
	}

	// Convert back to attributes
	finalAttrs := make([]attribute.KeyValue, 0, len(attrMap))
	for k, v := range attrMap {
		finalAttrs = append(finalAttrs, attribute.String(k, v))
	}

	// Create a new gauge for the specific tag combination
	// For OpenTelemetry, we need a new instance as the attributes are part of the observation
	newGauge := &gauge{
		registry:    registry,
		name:        name,
		description: description,
		attrs:       finalAttrs,
	}

	// Create a new observable gauge with the specific attributes
	otelGauge, err := registry.meter.Int64ObservableGauge(
		name+".with_tags", // Unique name to avoid conflicts
		metric.WithDescription(description),
	)

	if err != nil {
		return newGauge
	}

	// Register callback for the new gauge
	callback := func(ctx context.Context, result metric.Int64Observer) error {
		result.Observe(atomic.LoadInt64(&newGauge.value), finalAttrs...)
		return nil
	}

	asyncGauge, err := registry.meter.RegisterCallback(callback, otelGauge)
	if err != nil {
		return newGauge
	}

	newGauge.gauge = otelGauge
	newGauge.asyncGauge = asyncGauge

	return newGauge
}

// Value returns the current value.
func (g *gauge) Value() float64 {
	return float64(atomic.LoadInt64(&g.value))
}
