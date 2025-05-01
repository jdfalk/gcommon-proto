package prometheus

import (
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// counter implements the metrics.Counter interface for Prometheus.
type counter struct {
	counter     prometheus.Counter
	vecCounter  *prometheus.CounterVec
	labelNames  []string
	labelValues []string
	registry    *registry
	mutex       sync.RWMutex
	value       float64 // For tracking current value when using vector
}

// newCounter creates a new Prometheus counter.
func newCounter(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Counter {
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
	promOpts := prometheus.CounterOpts{
		Namespace: namespace,
		Subsystem: subsystem,
		Name:      name,
		Help:      opts.Description,
	}

	c := &counter{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
	}

	registry.mutex.Lock()
	defer registry.mutex.Unlock()

	// If we have labels, create a vector counter
	if len(labelNames) > 0 {
		vecCounter := prometheus.NewCounterVec(promOpts, labelNames)
		if err := registry.registry.Register(vecCounter); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				vecCounter = are.ExistingCollector.(*prometheus.CounterVec)
			}
			// Could log the error here if not already registered
		}
		c.vecCounter = vecCounter
		c.counter = vecCounter.WithLabelValues(labelValues...)
	} else {
		// No labels, create a simple counter
		counter := prometheus.NewCounter(promOpts)
		if err := registry.registry.Register(counter); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				counter = are.ExistingCollector.(prometheus.Counter)
			}
			// Could log the error here if not already registered
		}
		c.counter = counter
	}

	return c
}

// Inc increments the counter by 1.
func (c *counter) Inc() {
	c.mutex.Lock()
	defer c.mutex.Unlock()

	c.counter.Inc()
	c.value++
}

// Add adds the given value to the counter.
func (c *counter) Add(value float64) {
	c.mutex.Lock()
	defer c.mutex.Unlock()

	c.counter.Add(value)
	c.value += value
}

// WithTags returns a new counter with the given tags.
func (c *counter) WithTags(tags ...metrics.Tag) metrics.Counter {
	if c.vecCounter == nil || len(tags) == 0 {
		return c
	}

	c.mutex.RLock()
	labelNames := c.labelNames
	c.mutex.RUnlock()

	// Create a map of current label values
	currentValues := make(map[string]string)
	for i, name := range labelNames {
		currentValues[name] = c.labelValues[i]
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

	// Create a new counter with the updated label values
	return &counter{
		registry:    c.registry,
		vecCounter:  c.vecCounter,
		counter:     c.vecCounter.WithLabelValues(newValues...),
		labelNames:  labelNames,
		labelValues: newValues,
	}
}

// Value returns the current counter value.
func (c *counter) Value() float64 {
	c.mutex.RLock()
	defer c.mutex.RUnlock()

	// For a standard Counter, we only have access to the observed value
	// that we've been tracking ourselves.
	return c.value
}
