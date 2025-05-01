package prometheus

import (
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// gauge implements the metrics.Gauge interface for Prometheus.
type gauge struct {
	gauge       prometheus.Gauge
	vecGauge    *prometheus.GaugeVec
	labelNames  []string
	labelValues []string
	registry    *registry
	mutex       sync.RWMutex
}

// newGauge creates a new Prometheus gauge.
func newGauge(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Gauge {
	opts := parseOptions(options...)

	// Combine global tags with metric-specific tags
	allTags := append(globalTags, opts.Tags...)
	labelNames := getTagKeys(allTags)
	labelValues := make([]string, len(labelNames))

	for i, tag := range allTags {
		labelValues[i] = tag.Value
	}

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.GaugeOpts{
		Namespace: namespace,
		Subsystem: subsystem,
		Name:      name,
		Help:      opts.Description,
	}

	g := &gauge{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
	}

	registry.mutex.Lock()
	defer registry.mutex.Unlock()

	// If we have labels, create a vector gauge
	if len(labelNames) > 0 {
		vecGauge := prometheus.NewGaugeVec(promOpts, labelNames)
		if err := registry.registry.Register(vecGauge); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				vecGauge = are.ExistingCollector.(*prometheus.GaugeVec)
			}
			// Could log the error here if not already registered
		}
		g.vecGauge = vecGauge
		g.gauge = vecGauge.WithLabelValues(labelValues...)
	} else {
		// No labels, create a simple gauge
		gauge := prometheus.NewGauge(promOpts)
		if err := registry.registry.Register(gauge); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				gauge = are.ExistingCollector.(prometheus.Gauge)
			}
			// Could log the error here if not already registered
		}
		g.gauge = gauge
	}

	return g
}

// Set sets the gauge to the given value.
func (g *gauge) Set(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Set(value)
}

// Inc increments the gauge by 1.
func (g *gauge) Inc() {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Inc()
}

// Dec decrements the gauge by 1.
func (g *gauge) Dec() {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Dec()
}

// Add adds the given value to the gauge.
func (g *gauge) Add(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Add(value)
}

// Sub subtracts the given value from the gauge.
func (g *gauge) Sub(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Sub(value)
}

// WithTags returns a new gauge with the given tags.
func (g *gauge) WithTags(tags ...metrics.Tag) metrics.Gauge {
	if g.vecGauge == nil || len(tags) == 0 {
		return g
	}

	g.mutex.RLock()
	labelNames := g.labelNames
	g.mutex.RUnlock()

	// Create a map of current label values
	currentValues := make(map[string]string)
	for i, name := range labelNames {
		currentValues[name] = g.labelValues[i]
	}

	// Override with new tag values
	for _, tag := range tags {
		currentValues[tag.Key] = tag.Value
	}

	// Create new label values array in the correct order
	newValues := make([]string, len(labelNames))
	for i, name := range labelNames {
		newValues[i] = currentValues[name]
	}

	// Create a new gauge with the updated label values
	return &gauge{
		registry:    g.registry,
		vecGauge:    g.vecGauge,
		gauge:       g.vecGauge.WithLabelValues(newValues...),
		labelNames:  labelNames,
		labelValues: newValues,
	}
}

// Value returns the current gauge value.
func (g *gauge) Value() float64 {
	// Note: Prometheus doesn't provide direct access to the current value
	// This is a limitation, but we can use a metric collector with a callback function
	// for more accurate real-time access to gauge values.

	// For now, we return 0 as a default value
	return 0 // This is a placeholder and should be improved
}
