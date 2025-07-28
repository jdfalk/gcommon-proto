package otel

import (
	"context"
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/metric"
)

// histogram implements the metrics.Histogram interface for OpenTelemetry.
type histogram struct {
	histogram   metric.Float64Histogram
	registry    *registry
	name        string
	description string
	attrs       []attribute.KeyValue
	mutex       sync.RWMutex
	buckets     []float64
	count       int64
	sum         float64
	values      []float64 // Store recent values for snapshot
	maxValues   int       // Maximum number of values to store
}

// histogramSnapshot implements the metrics.HistogramSnapshot interface.
type histogramSnapshot struct {
	count   int64
	sum     float64
	buckets map[float64]int64
	values  []float64
}

// newHistogram creates a new OpenTelemetry histogram.
func newHistogram(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Histogram {
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

	// Check if we already have this histogram
	if existing, ok := registry.metrics[fullName]; ok {
		if h, ok := existing.(*histogram); ok {
			return h
		}
	}

	// Create a new histogram
	description := opts.Description
	if description == "" {
		description = "Histogram " + fullName
	}

	// Use provided buckets or default ones
	buckets := opts.Buckets
	if len(buckets) == 0 {
		// Default buckets similar to Prometheus defaults
		buckets = []float64{0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10}
	}

	// Create histogram options
	histogramOpts := []metric.Float64HistogramOption{
		metric.WithDescription(description),
		metric.WithUnit(opts.Unit),
	}

	// Explicit buckets are not supported in OTel API directly
	// The SDK's View API can be used for this, but we're not using it here

	otelHistogram, err := registry.meter.Float64Histogram(
		fullName,
		histogramOpts...,
	)

	h := &histogram{
		registry:    registry,
		name:        fullName,
		description: description,
		attrs:       attrs,
		buckets:     buckets,
		maxValues:   1000, // Store last 1000 values for snapshot
	}

	if err == nil {
		h.histogram = otelHistogram
	}

	// Store in registry
	registry.metrics[fullName] = h

	return h
}

// Observe records a value.
func (h *histogram) Observe(value float64) {
	h.mutex.Lock()
	defer h.mutex.Unlock()

	// Record to OTel histogram if available
	if h.histogram != nil {
		h.histogram.Record(context.Background(), value, h.attrs...)
	}

	// Update our tracking for snapshots
	h.count++
	h.sum += value

	// Store value for snapshot (with limit)
	if len(h.values) < h.maxValues {
		h.values = append(h.values, value)
	} else if len(h.values) > 0 {
		// Replace a random value (simple approach)
		// In a production implementation, we might use a circular buffer
		h.values[h.count%int64(h.maxValues)] = value
	}
}

// WithTags returns a new histogram with the given tags.
func (h *histogram) WithTags(tags ...metrics.Tag) metrics.Histogram {
	if len(tags) == 0 {
		return h
	}

	h.mutex.RLock()
	defer h.mutex.RUnlock()

	// Combine existing attributes with new ones
	newAttrs := make([]attribute.KeyValue, len(h.attrs))
	copy(newAttrs, h.attrs)

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

	// Create a new histogram with the updated attributes
	newHist := &histogram{
		histogram:   h.histogram,
		registry:    h.registry,
		name:        h.name,
		description: h.description,
		attrs:       finalAttrs,
		buckets:     h.buckets,
		maxValues:   h.maxValues,
	}

	return newHist
}

// Snapshot returns the current snapshot.
func (h *histogram) Snapshot() metrics.HistogramSnapshot {
	h.mutex.RLock()
	defer h.mutex.RUnlock()

	// Create a copy of values for the snapshot
	valuesCopy := make([]float64, len(h.values))
	copy(valuesCopy, h.values)

	// Create bucket counts (approximate since OTel doesn't expose this)
	bucketCounts := make(map[float64]int64, len(h.buckets))
	for _, bucket := range h.buckets {
		bucketCounts[bucket] = 0
	}

	// Count values in each bucket
	for _, v := range valuesCopy {
		for _, bucket := range h.buckets {
			if v <= bucket {
				bucketCounts[bucket]++
			}
		}
	}

	return &histogramSnapshot{
		count:   h.count,
		sum:     h.sum,
		buckets: bucketCounts,
		values:  valuesCopy,
	}
}

// Count returns the count of values.
func (s *histogramSnapshot) Count() int64 {
	return s.count
}

// Sum returns the sum of values.
func (s *histogramSnapshot) Sum() float64 {
	return s.sum
}

// Quantile returns the value at the given quantile (0-1).
func (s *histogramSnapshot) Quantile(q float64) float64 {
	if len(s.values) == 0 {
		return 0
	}

	// Simple quantile estimation from stored values
	// In a production implementation, we might use a more sophisticated algorithm

	// Sort values (this is inefficient for large datasets)
	values := make([]float64, len(s.values))
	copy(values, s.values)

	// For simplicity, use a bubble sort
	// In production code, we would use a more efficient sort
	for i := 0; i < len(values); i++ {
		for j := i + 1; j < len(values); j++ {
			if values[i] > values[j] {
				values[i], values[j] = values[j], values[i]
			}
		}
	}

	// Get the index corresponding to the quantile
	idx := int(float64(len(values)-1) * q)
	if idx < 0 {
		idx = 0
	}
	if idx >= len(values) {
		idx = len(values) - 1
	}

	return values[idx]
}

// Buckets returns the bucket counts.
func (s *histogramSnapshot) Buckets() map[float64]int64 {
	return s.buckets
}
