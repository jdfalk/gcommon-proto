package prometheus

import (
	"sync"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// counter implements the metrics.Counter interface for Prometheus.
// It provides a way to track monotonically increasing values, such as
// request counts, completed tasks, or error occurrences.
type counter struct {
	counter     prometheus.Counter
	vecCounter  *prometheus.CounterVec
	labelNames  []string
	labelValues []string
	registry    *registry
	mutex       sync.RWMutex

	// Track value internally for efficient retrieval
	value atomic.Float64
}

// newCounter creates a new Prometheus counter.
//
// Parameters:
//   - registry: The Prometheus registry to register the counter with
//   - name: The name of the counter metric
//   - globalTags: Global tags to apply to all metrics in the registry
//   - options: Optional configurations for the counter
//
// Returns:
//   - metrics.Counter: A new counter instance with the specified configuration
func newCounter(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Counter {
	opts := parseOptions(options...)

	// Combine global tags with metric-specific tags
	allTags := combineTags(globalTags, opts.Tags)
	labelNames := getTagKeys(allTags)
	labelValues := getTagValues(allTags, labelNames)

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.CounterOpts{
		Namespace:   namespace,
		Subsystem:   subsystem,
		Name:        name,
		Help:        opts.Description,
		ConstLabels: opts.ConstLabels,
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

	// Register the metric with our registry for tracking
	registry.Register(name, c, options...)

	return c
}

// Inc increments the counter by 1.
// This is a convenient method for incrementing the counter by a single unit.
func (c *counter) Inc() {
	// Atomic update for thread safety without locking
	c.counter.Inc()
	c.value.Add(1)
}

// Add adds the given value to the counter.
//
// Parameters:
//   - value: The value to add to the counter (must be non-negative)
func (c *counter) Add(value float64) {
	// Counter values must be non-negative in Prometheus
	if value < 0 {
		return
	}

	c.counter.Add(value)
	c.value.Add(value)
}

// WithTags returns a new counter with the given tags.
// This allows for dimensional metrics where the same counter can be tracked
// across different dimensions (e.g., status code, endpoint, method).
//
// Parameters:
//   - tags: The tags to apply to the counter
//
// Returns:
//   - metrics.Counter: A new counter instance with the combined tags
func (c *counter) WithTags(tags ...metrics.Tag) metrics.Counter {
	if c.vecCounter == nil || len(tags) == 0 {
		return c
	}

	c.mutex.RLock()
	labelNames := c.labelNames
	labelValues := c.labelValues
	c.mutex.RUnlock()

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
//
// Returns:
//   - float64: The current value of the counter
func (c *counter) Value() float64 {
	// Use atomic read for thread safety without locking
	return c.value.Load()
}
