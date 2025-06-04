package prometheus

import (
	"sync"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// histogram implements the metrics.Histogram interface for Prometheus.
// It provides a way to track distributions of measurements, such as
// request durations or response sizes, with predefined bucket boundaries.
type histogram struct {
	histogram    prometheus.Observer
	vecHistogram *prometheus.HistogramVec
	labelNames   []string
	labelValues  []string
	registry     *registry
	mutex        sync.RWMutex
	buckets      []float64

	// Track metrics for snapshot capability
	count      atomic.Int64
	sum        atomic.Float64
	bucketVals map[float64]*atomic.Int64
}

// histogramSnapshot implements the metrics.HistogramSnapshot interface.
// It provides a point-in-time view of histogram measurements.
type histogramSnapshot struct {
	count   int64
	sum     float64
	buckets map[float64]int64
}

// newHistogram creates a new Prometheus histogram.
//
// Parameters:
//   - registry: The Prometheus registry to register the histogram with
//   - name: The name of the histogram metric
//   - globalTags: Global tags to apply to all metrics in the registry
//   - options: Optional configurations for the histogram
//
// Returns:
//   - metrics.Histogram: A new histogram instance with the specified configuration
func newHistogram(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Histogram {
	opts := parseOptions(options...)

	// Use provided buckets or default ones
	buckets := opts.Buckets
	if len(buckets) == 0 {
		buckets = prometheus.DefBuckets
	}

	// Create bucket tracking map
	bucketVals := make(map[float64]*atomic.Int64, len(buckets))
	for _, b := range buckets {
		bucketVals[b] = &atomic.Int64{}
	}

	// Combine global tags with metric-specific tags
	allTags := combineTags(globalTags, opts.Tags)
	labelNames := getTagKeys(allTags)
	labelValues := getTagValues(allTags, labelNames)

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.HistogramOpts{
		Namespace:   namespace,
		Subsystem:   subsystem,
		Name:        name,
		Help:        opts.Description,
		Buckets:     buckets,
		ConstLabels: opts.ConstLabels,
	}

	h := &histogram{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
		buckets:     buckets,
		bucketVals:  bucketVals,
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

	// Register the metric with our registry for tracking
	registry.Register(name, h, options...)

	return h
}

// Observe records a single observation in the histogram.
//
// Parameters:
//   - value: The value to observe
func (h *histogram) Observe(value float64) {
	h.mutex.Lock()
	defer h.mutex.Unlock()

	// Update Prometheus histogram
	h.histogram.Observe(value)

	// Track value for our snapshot capability
	h.count.Add(1)
	h.sum.Add(value)

	// Update appropriate buckets
	for bucket := range h.bucketVals {
		if value <= bucket {
			h.bucketVals[bucket].Add(1)
		}
	}
}

// WithTags returns a new histogram with the given tags.
// This allows for dimensional metrics where the same histogram can be tracked
// across different dimensions (e.g., status code, endpoint, method).
//
// Parameters:
//   - tags: The tags to apply to the histogram
//
// Returns:
//   - metrics.Histogram: A new histogram instance with the combined tags
func (h *histogram) WithTags(tags ...metrics.Tag) metrics.Histogram {
	if h.vecHistogram == nil || len(tags) == 0 {
		return h
	}

	h.mutex.RLock()
	labelNames := h.labelNames
	labelValues := h.labelValues
	buckets := h.buckets
	h.mutex.RUnlock()

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

	// Create bucket tracking map for the new instance
	bucketVals := make(map[float64]*atomic.Int64, len(buckets))
	for _, b := range buckets {
		bucketVals[b] = &atomic.Int64{}
	}

	// Create a new histogram with the updated label values
	return &histogram{
		registry:     h.registry,
		vecHistogram: h.vecHistogram,
		histogram:    h.vecHistogram.WithLabelValues(newValues...),
		labelNames:   labelNames,
		labelValues:  newValues,
		buckets:      buckets,
		bucketVals:   bucketVals,
	}
}

// Snapshot returns the current state of the histogram.
// This provides a point-in-time view of all measurements recorded in the histogram.
//
// Returns:
//   - metrics.HistogramSnapshot: A snapshot of the histogram's current state
func (h *histogram) Snapshot() metrics.HistogramSnapshot {
	h.mutex.RLock()
	defer h.mutex.RUnlock()

	// Create a copy of the current bucket counts
	buckets := make(map[float64]int64, len(h.bucketVals))
	for bucket, count := range h.bucketVals {
		buckets[bucket] = count.Load()
	}

	return &histogramSnapshot{
		count:   h.count.Load(),
		sum:     h.sum.Load(),
		buckets: buckets,
	}
}

// Count returns the number of observations in the histogram snapshot.
//
// Returns:
//   - int64: The count of observations
func (s *histogramSnapshot) Count() int64 {
	return s.count
}

// Sum returns the sum of all observations in the histogram snapshot.
//
// Returns:
//   - float64: The sum of all observed values
func (s *histogramSnapshot) Sum() float64 {
	return s.sum
}

// Quantile returns an approximation of the value at the given quantile (0-1).
// Note that histograms can only provide approximate quantiles based on bucket boundaries.
//
// Parameters:
//   - q: The quantile to calculate (0.0 to 1.0)
//
// Returns:
//   - float64: The approximate value at the given quantile
func (s *histogramSnapshot) Quantile(q float64) float64 {
	if q < 0 || q > 1 {
		return 0
	}

	if s.count == 0 {
		return 0
	}

	// Sort buckets for linear interpolation
	var bucketBoundaries []float64
	for b := range s.buckets {
		bucketBoundaries = append(bucketBoundaries, b)
	}

	// Simple implementation - in a real system, we'd use proper quantile estimation
	// This is only a rough approximation based on histogram buckets
	target := int64(float64(s.count) * q)
	running := int64(0)

	// Simple sorting for the boundaries
	for i := 0; i < len(bucketBoundaries)-1; i++ {
		for j := i + 1; j < len(bucketBoundaries); j++ {
			if bucketBoundaries[i] > bucketBoundaries[j] {
				bucketBoundaries[i], bucketBoundaries[j] = bucketBoundaries[j], bucketBoundaries[i]
			}
		}
	}

	// Linear search - in a production system we'd use binary search
	for i, boundary := range bucketBoundaries {
		count := s.buckets[boundary]
		nextRunning := running + count

		if nextRunning >= target {
			if i == 0 {
				return boundary / 2 // Rough approximation for first bucket
			}

			// Linear interpolation between this boundary and previous
			prev := bucketBoundaries[i-1]
			ratio := float64(target-running) / float64(count)
			return prev + (boundary-prev)*ratio
		}

		running = nextRunning
	}

	// If we get here, return the highest bucket boundary
	if len(bucketBoundaries) > 0 {
		return bucketBoundaries[len(bucketBoundaries)-1]
	}

	return 0
}

// Buckets returns the bucket counts for all defined bucket boundaries.
//
// Returns:
//   - map[float64]int64: A map of bucket upper bounds to counts
func (s *histogramSnapshot) Buckets() map[float64]int64 {
	return s.buckets
}
