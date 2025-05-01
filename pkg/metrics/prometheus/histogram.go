package prometheus

import (
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// histogram implements the metrics.Histogram interface for Prometheus.
type histogram struct {
	histogram   prometheus.Observer
	vecHistogram *prometheus.HistogramVec
	labelNames   []string
	labelValues  []string
	registry     *registry
	mutex        sync.RWMutex
	buckets      []float64
}

// histogramSnapshot implements the metrics.HistogramSnapshot interface.
type histogramSnapshot struct {
	count   int64
	sum     float64
	buckets map[float64]int64
}

// newHistogram creates a new Prometheus histogram.
func newHistogram(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Histogram {
	opts := parseOptions(options...)

	// Use provided buckets or default ones
	buckets := opts.Buckets
	if len(buckets) == 0 {
		buckets = prometheus.DefBuckets
	}

	// Combine global tags with metric-specific tags
	allTags := append(globalTags, opts.Tags...)
	labelNames := getTagKeys(allTags)
	labelValues := make([]string, len(labelNames))

	for i, tag := range allTags {
		labelValues[i] = tag.Value
	}

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.HistogramOpts{
		Namespace: namespace,
		Subsystem: subsystem,
		Name:      name,
		Help:      opts.Description,
		Buckets:   buckets,
	}

	h := &histogram{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
		buckets:     buckets,
	}

	registry.mutex.Lock()
	defer registry.mutex.Unlock()

	// If we have labels, create a vector histogram
	if len(labelNames) > 0 {
		vecHistogram := prometheus.NewHistogramVec(promOpts, labelNames)
		if err := registry.registry.Register(vecHistogram); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				vecHistogram = are.ExistingCollector.(*prometheus.HistogramVec)
			}
			// Could log the error here if not already registered
		}
		h.vecHistogram = vecHistogram
		h.histogram = vecHistogram.WithLabelValues(labelValues...)
	} else {
		// No labels, create a simple histogram
		histogram := prometheus.NewHistogram(promOpts)
		if err := registry.registry.Register(histogram); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				histogram = are.ExistingCollector.(prometheus.Histogram)
			}
			// Could log the error here if not already registered
		}
		h.histogram = histogram
	}

	return h
}

// Observe records a value.
func (h *histogram) Observe(value float64) {
	h.mutex.Lock()
	defer h.mutex.Unlock()

	h.histogram.Observe(value)
}

// WithTags returns a new histogram with the given tags.
func (h *histogram) WithTags(tags ...metrics.Tag) metrics.Histogram {
	if h.vecHistogram == nil || len(tags) == 0 {
		return h
	}

	h.mutex.RLock()
	labelNames := h.labelNames
	buckets := h.buckets
	h.mutex.RUnlock()

	// Create a map of current label values
	currentValues := make(map[string]string)
	for i, name := range labelNames {
		currentValues[name] = h.labelValues[i]
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

	// Create a new histogram with the updated label values
	return &histogram{
		registry:     h.registry,
		vecHistogram: h.vecHistogram,
		histogram:    h.vecHistogram.WithLabelValues(newValues...),
		labelNames:   labelNames,
		labelValues:  newValues,
		buckets:      buckets,
	}
}

// Snapshot returns the current snapshot.
func (h *histogram) Snapshot() metrics.HistogramSnapshot {
	// Note: Prometheus doesn't provide direct access to histogram state,
	// so we return a minimal snapshot with default values.
	// This is a limitation of the Prometheus client library.

	// In a production implementation, we would use Prometheus's exposition
	// format to extract the current values, but this is complex and beyond
	// the scope of this example.

	emptyBuckets := make(map[float64]int64)
	for _, bucket := range h.buckets {
		emptyBuckets[bucket] = 0
	}

	return &histogramSnapshot{
		count:   0,
		sum:     0,
		buckets: emptyBuckets,
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
	// Approximating quantiles from histogram buckets is not
	// straightforward and would require interpolation.
	// For a proper implementation, we would need to use a Summary
	// instead of a Histogram.
	return 0
}

// Buckets returns the bucket counts.
func (s *histogramSnapshot) Buckets() map[float64]int64 {
	return s.buckets
}
