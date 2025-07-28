package prometheus

import (
	"math"
	"sync"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// gauge implements the metrics.Gauge interface for Prometheus.
// It provides a way to track a value that can arbitrarily go up and down,
// such as temperatures, memory usage, or the number of active connections.
type gauge struct {
	gauge       prometheus.Gauge
	vecGauge    *prometheus.GaugeVec
	labelNames  []string
	labelValues []string
	registry    *registry
	mutex       sync.RWMutex
	// cachedValue stores the last set value for Value() calls using uint64 for atomic operations
	cachedValue uint64
}

// newGauge creates a new Prometheus gauge.
//
// Parameters:
//   - registry: The Prometheus registry to register the gauge with
//   - name: The name of the gauge metric
//   - globalTags: Global tags to apply to all metrics in the registry
//   - options: Optional configurations for the gauge
//
// Returns:
//   - metrics.Gauge: A new gauge instance
func newGauge(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Gauge {
	opts := parseOptions(options...)

	// Combine global tags with metric-specific tags
	allTags := combineTags(globalTags, opts.Tags)
	labelNames := getTagKeys(allTags)
	labelValues := getTagValues(allTags, labelNames)

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.GaugeOpts{
		Namespace:   namespace,
		Subsystem:   subsystem,
		Name:        name,
		Help:        opts.Description,
		ConstLabels: opts.ConstLabels,
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
//
// Parameters:
//   - value: The value to set the gauge to
func (g *gauge) Set(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Set(value)
	atomic.StoreUint64(&g.cachedValue, math.Float64bits(value))
}

// Inc increments the gauge by 1.
func (g *gauge) Inc() {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Inc()
	for {
		current := atomic.LoadUint64(&g.cachedValue)
		currentFloat := math.Float64frombits(current)
		newFloat := currentFloat + 1
		newBits := math.Float64bits(newFloat)
		if atomic.CompareAndSwapUint64(&g.cachedValue, current, newBits) {
			break
		}
	}
}

// Dec decrements the gauge by 1.
func (g *gauge) Dec() {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Dec()
	for {
		current := atomic.LoadUint64(&g.cachedValue)
		currentFloat := math.Float64frombits(current)
		newFloat := currentFloat - 1
		newBits := math.Float64bits(newFloat)
		if atomic.CompareAndSwapUint64(&g.cachedValue, current, newBits) {
			break
		}
	}
}

// Add adds the given value to the gauge.
//
// Parameters:
//   - value: The value to add to the gauge
func (g *gauge) Add(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Add(value)
	for {
		current := atomic.LoadUint64(&g.cachedValue)
		currentFloat := math.Float64frombits(current)
		newFloat := currentFloat + value
		newBits := math.Float64bits(newFloat)
		if atomic.CompareAndSwapUint64(&g.cachedValue, current, newBits) {
			break
		}
	}
}

// Sub subtracts the given value from the gauge.
//
// Parameters:
//   - value: The value to subtract from the gauge
func (g *gauge) Sub(value float64) {
	g.mutex.Lock()
	defer g.mutex.Unlock()

	g.gauge.Sub(value)
	for {
		current := atomic.LoadUint64(&g.cachedValue)
		currentFloat := math.Float64frombits(current)
		newFloat := currentFloat - value
		newBits := math.Float64bits(newFloat)
		if atomic.CompareAndSwapUint64(&g.cachedValue, current, newBits) {
			break
		}
	}
}

// WithTags returns a new gauge with the given tags.
// This allows for dimensional metrics where the same gauge can be tracked
// across different dimensions (e.g., host, service, status).
//
// Parameters:
//   - tags: The tags to apply to the gauge
//
// Returns:
//   - metrics.Gauge: A new gauge instance with the combined tags
func (g *gauge) WithTags(tags ...metrics.Tag) metrics.Gauge {
	if g.vecGauge == nil || len(tags) == 0 {
		return g
	}

	g.mutex.RLock()
	labelNames := g.labelNames
	labelValues := g.labelValues
	currentValue := math.Float64frombits(atomic.LoadUint64(&g.cachedValue))
	g.mutex.RUnlock()

	// Create a map of current label values
	currentValues := make(map[string]string, len(labelNames))
	for i, name := range labelNames {
		currentValues[name] = labelValues[i]
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
	newGauge := &gauge{
		registry:    g.registry,
		vecGauge:    g.vecGauge,
		gauge:       g.vecGauge.WithLabelValues(newValues...),
		labelNames:  labelNames,
		labelValues: newValues,
	}

	// Set the cached value to maintain the value across gauge instances
	atomic.StoreUint64(&newGauge.cachedValue, math.Float64bits(currentValue))

	return newGauge
}

// Value returns the current gauge value.
//
// Returns:
//   - float64: The current value of the gauge
func (g *gauge) Value() float64 {
	bits := atomic.LoadUint64(&g.cachedValue)
	return math.Float64frombits(bits)
}

// Snapshot returns a snapshot of the gauge's current value.
//
// Returns:
//   - float64: The current value of the gauge
func (g *gauge) Snapshot() float64 {
	return g.Value()
}
