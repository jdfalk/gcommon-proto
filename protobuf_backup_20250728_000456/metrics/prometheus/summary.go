package prometheus

import (
	"math"
	"sync"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// summary implements the metrics.Summary interface for Prometheus.
// It provides a way to track streaming φ-quantiles (e.g., 0.5 for median,
// 0.99 for 99th percentile) of a distribution of observations.
type summary struct {
	summary     prometheus.Observer
	vecSummary  *prometheus.SummaryVec
	labelNames  []string
	labelValues []string
	registry    *registry
	mutex       sync.RWMutex
	objectives  map[float64]float64

	// Track metrics for snapshot capability
	count        atomic.Int64
	sum          uint64   // Use uint64 for atomic operations with float64 conversion
	quantileVals sync.Map // map[float64]*quantileEstimator
}

// summarySnapshot implements the metrics.SummarySnapshot interface.
// It provides a point-in-time view of summary measurements.
type summarySnapshot struct {
	count     int64
	sum       float64
	quantiles map[float64]float64
}

// quantileEstimator is a simple implementation of a quantile estimator.
// In a production system, you might use a more sophisticated algorithm.
type quantileEstimator struct {
	mutex       sync.RWMutex
	values      []float64
	maxSize     int
	quantile    float64
	cachedValue uint64 // Use uint64 for atomic operations with float64 conversion
}

// newSummary creates a new Prometheus summary.
//
// Parameters:
//   - registry: The Prometheus registry to register the summary with
//   - name: The name of the summary metric
//   - globalTags: Global tags to apply to all metrics in the registry
//   - options: Optional configurations for the summary
//
// Returns:
//   - metrics.Summary: A new summary instance with the specified configuration
func newSummary(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Summary {
	opts := parseOptions(options...)

	// Use provided objectives or default ones
	objectives := opts.Objectives
	if objectives == nil {
		objectives = map[float64]float64{
			0.5:  0.05,  // 50th percentile with 5% error
			0.9:  0.01,  // 90th percentile with 1% error
			0.95: 0.005, // 95th percentile with 0.5% error
			0.99: 0.001, // 99th percentile with 0.1% error
		}
	}

	// Combine global tags with metric-specific tags
	allTags := combineTags(globalTags, opts.Tags)
	labelNames := getTagKeys(allTags)
	labelValues := getTagValues(allTags, labelNames)

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.SummaryOpts{
		Namespace:   namespace,
		Subsystem:   subsystem,
		Name:        name,
		Help:        opts.Description,
		Objectives:  objectives,
		MaxAge:      opts.MaxAge,
		AgeBuckets:  uint32(opts.AgeBuckets),
		BufCap:      uint32(opts.BufCap),
		ConstLabels: opts.ConstLabels,
	}

	s := &summary{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
		objectives:  objectives,
	}

	// Initialize quantile estimators for each objective
	for q := range objectives {
		s.quantileVals.Store(q, &quantileEstimator{
			maxSize:  1000, // Configurable buffer size
			quantile: q,
			values:   make([]float64, 0, 1000),
		})
	}

	registry.mutex.Lock()
	defer registry.mutex.Unlock()

	// If we have labels, create a vector summary
	if len(labelNames) > 0 {
		vecSummary := prometheus.NewSummaryVec(promOpts, labelNames)
		if err := registry.registry.Register(vecSummary); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				vecSummary = are.ExistingCollector.(*prometheus.SummaryVec)
			}
			// Could log the error here if not already registered
		}
		s.vecSummary = vecSummary
		s.summary = vecSummary.WithLabelValues(labelValues...)
	} else {
		// No labels, create a simple summary
		summary := prometheus.NewSummary(promOpts)
		if err := registry.registry.Register(summary); err != nil {
			if are, ok := err.(prometheus.AlreadyRegisteredError); ok {
				summary = are.ExistingCollector.(prometheus.Summary)
			}
			// Could log the error here if not already registered
		}
		s.summary = summary
	}

	// Register the metric with our registry for tracking
	registry.Register(name, s, options...)

	return s
}

// Observe records a value in the summary.
//
// Parameters:
//   - value: The value to observe
func (s *summary) Observe(value float64) {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	// Update Prometheus summary
	s.summary.Observe(value)

	// Update our tracking for snapshot capability
	s.count.Add(1)
	// Atomic add for float64 sum
	for {
		current := atomic.LoadUint64(&s.sum)
		currentFloat := math.Float64frombits(current)
		newFloat := currentFloat + value
		newBits := math.Float64bits(newFloat)
		if atomic.CompareAndSwapUint64(&s.sum, current, newBits) {
			break
		}
	}

	// Update all quantile estimators
	s.quantileVals.Range(func(key, val interface{}) bool {
		if estimator, ok := val.(*quantileEstimator); ok {
			estimator.observe(value)
		}
		return true
	})
}

// WithTags returns a new summary with the given tags.
// This allows for dimensional metrics where the same summary can be tracked
// across different dimensions (e.g., status code, endpoint, method).
//
// Parameters:
//   - tags: The tags to apply to the summary
//
// Returns:
//   - metrics.Summary: A new summary instance with the combined tags
func (s *summary) WithTags(tags ...metrics.Tag) metrics.Summary {
	if s.vecSummary == nil || len(tags) == 0 {
		return s
	}

	s.mutex.RLock()
	labelNames := s.labelNames
	labelValues := s.labelValues
	objectives := s.objectives
	s.mutex.RUnlock()

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

	// Create a new summary with the updated label values
	newSummary := &summary{
		registry:    s.registry,
		vecSummary:  s.vecSummary,
		summary:     s.vecSummary.WithLabelValues(newValues...),
		labelNames:  labelNames,
		labelValues: newValues,
		objectives:  objectives,
	}

	// Initialize quantile estimators for the new summary
	for q := range objectives {
		newSummary.quantileVals.Store(q, &quantileEstimator{
			maxSize:  1000, // Configurable buffer size
			quantile: q,
			values:   make([]float64, 0, 1000),
		})
	}

	return newSummary
}

// Snapshot returns the current state of the summary.
// This provides a point-in-time view of all measurements recorded in the summary.
//
// Returns:
//   - metrics.SummarySnapshot: A snapshot of the summary's current state
func (s *summary) Snapshot() metrics.SummarySnapshot {
	// Get current count and sum
	count := s.count.Load()
	sum := math.Float64frombits(atomic.LoadUint64(&s.sum))

	// Get current quantile estimates
	quantiles := make(map[float64]float64, len(s.objectives))

	s.quantileVals.Range(func(key, val interface{}) bool {
		q, ok1 := key.(float64)
		estimator, ok2 := val.(*quantileEstimator)

		if ok1 && ok2 {
			quantiles[q] = estimator.estimate()
		}
		return true
	})

	return &summarySnapshot{
		count:     count,
		sum:       sum,
		quantiles: quantiles,
	}
}

// Count returns the number of observations in the summary snapshot.
//
// Returns:
//   - int64: The count of observations
func (s *summarySnapshot) Count() int64 {
	return s.count
}

// Sum returns the sum of all observations in the summary snapshot.
//
// Returns:
//   - float64: The sum of all observed values
func (s *summarySnapshot) Sum() float64 {
	return s.sum
}

// Quantile returns the value at the specified quantile.
//
// Parameters:
//   - q: The quantile to retrieve (0.0 to 1.0)
//
// Returns:
//   - float64: The value at the given quantile, or 0 if not available
func (s *summarySnapshot) Quantile(q float64) float64 {
	if value, ok := s.quantiles[q]; ok {
		return value
	}
	return 0
}

// Quantiles returns all tracked quantiles and their values.
//
// Returns:
//   - map[float64]float64: A map of quantiles to their values
func (s *summarySnapshot) Quantiles() map[float64]float64 {
	return s.quantiles
}

// observe adds a value to the quantile estimator.
//
// Parameters:
//   - value: The value to observe
func (q *quantileEstimator) observe(value float64) {
	q.mutex.Lock()
	defer q.mutex.Unlock()

	// Add the value
	q.values = append(q.values, value)

	// If we've exceeded maxSize, recalculate the estimate and reset
	if len(q.values) >= q.maxSize {
		atomic.StoreUint64(&q.cachedValue, math.Float64bits(q.calculateQuantile()))
		// Keep most recent values to maintain some history
		if len(q.values) > 100 {
			q.values = q.values[len(q.values)-100:]
		}
	}
}

// estimate returns the current quantile estimate.
//
// Returns:
//   - float64: The estimated value at the configured quantile
func (q *quantileEstimator) estimate() float64 {
	q.mutex.RLock()
	defer q.mutex.RUnlock()

	// If we have a cached value and it's meaningful, return it
	if len(q.values) >= q.maxSize/2 {
		return math.Float64frombits(atomic.LoadUint64(&q.cachedValue))
	}

	// Otherwise calculate it now
	if len(q.values) == 0 {
		return 0
	}

	return q.calculateQuantile()
}

// calculateQuantile performs the actual quantile calculation.
//
// Returns:
//   - float64: The calculated quantile value
func (q *quantileEstimator) calculateQuantile() float64 {
	if len(q.values) == 0 {
		return 0
	}

	// Copy values to avoid modifying the original
	valuesCopy := make([]float64, len(q.values))
	copy(valuesCopy, q.values)

	// Sort values (simple algorithm - in production, we'd use a more
	// efficient algorithm like t-digest or HDR histogram)
	for i := 0; i < len(valuesCopy)-1; i++ {
		for j := i + 1; j < len(valuesCopy); j++ {
			if valuesCopy[i] > valuesCopy[j] {
				valuesCopy[i], valuesCopy[j] = valuesCopy[j], valuesCopy[i]
			}
		}
	}

	// Calculate the index of the quantile
	idx := int(float64(len(valuesCopy)) * q.quantile)

	// Handle edge cases
	if idx <= 0 {
		return valuesCopy[0]
	}
	if idx >= len(valuesCopy) {
		return valuesCopy[len(valuesCopy)-1]
	}

	// Linear interpolation between the two nearest points
	return valuesCopy[idx]
}
