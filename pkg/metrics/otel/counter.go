package otel

import (
	"context"
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/metric"
)

// counter implements the metrics.Counter interface for OpenTelemetry.
type counter struct {
	counter     metric.Int64Counter
	registry    *registry
	name        string
	description string
	attrs       []attribute.KeyValue
	mutex       sync.RWMutex
	value       int64 // For tracking current value
}

// newCounter creates a new OpenTelemetry counter.
func newCounter(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Counter {
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

	// Check if we already have this counter
	if existing, ok := registry.metrics[fullName]; ok {
		if c, ok := existing.(*counter); ok {
			return c
		}
	}

	// Create a new counter
	description := opts.Description
	if description == "" {
		description = "Counter " + fullName
	}

	otelCounter, err := registry.meter.Int64Counter(
		fullName,
		metric.WithDescription(description),
		metric.WithUnit(opts.Unit),
	)

	if err != nil {
		// In a production implementation, we would log this error
		// For now, create a noop counter
		return &counter{
			registry:    registry,
			name:        fullName,
			description: description,
			attrs:       attrs,
		}
	}

	c := &counter{
		counter:     otelCounter,
		registry:    registry,
		name:        fullName,
		description: description,
		attrs:       attrs,
	}

	// Store in registry
	registry.metrics[fullName] = c

	return c
}

// Inc increments the counter by 1.
func (c *counter) Inc() {
	c.Add(1)
}

// Add adds the given value to the counter.
func (c *counter) Add(value float64) {
	if c.counter == nil {
		return
	}

	c.mutex.Lock()
	defer c.mutex.Unlock()

	// OpenTelemetry counters only support int64 values
	intValue := int64(value)
	c.counter.Add(context.Background(), intValue, c.attrs...)
	c.value += intValue
}

// WithTags returns a new counter with the given tags.
func (c *counter) WithTags(tags ...metrics.Tag) metrics.Counter {
	if len(tags) == 0 {
		return c
	}

	c.mutex.RLock()
	defer c.mutex.RUnlock()

	// Combine existing attributes with new ones
	newAttrs := make([]attribute.KeyValue, len(c.attrs))
	copy(newAttrs, c.attrs)

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

	// Create a new counter with the updated attributes
	return &counter{
		counter:     c.counter,
		registry:    c.registry,
		name:        c.name,
		description: c.description,
		attrs:       finalAttrs,
	}
}

// Value returns the current value.
func (c *counter) Value() float64 {
	c.mutex.RLock()
	defer c.mutex.RUnlock()

	// Return the tracked value
	return float64(c.value)
}
