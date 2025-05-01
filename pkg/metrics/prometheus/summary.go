package prometheus

import (
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// summary implements the metrics.Summary interface for Prometheus.
type summary struct {
	summary       prometheus.Observer
	vecSummary    *prometheus.SummaryVec
	labelNames    []string
	labelValues   []string
	registry      *registry
	mutex         sync.RWMutex
	objectives    map[float64]float64
}

// summarySnapshot implements the metrics.SummarySnapshot interface.
type summarySnapshot struct {
	count      int64
	sum        float64
	quantiles  map[float64]float64
}

// newSummary creates a new Prometheus summary.
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
	allTags := append(globalTags, opts.Tags...)
	labelNames := getTagKeys(allTags)
	labelValues := make([]string, len(labelNames))

	for i, tag := range allTags {
		labelValues[i] = tag.Value
	}

	// Create metric options
	namespace, subsystem := registry.getNames(name)
	promOpts := prometheus.SummaryOpts{
		Namespace:  namespace,
		Subsystem:  subsystem,
		Name:       name,
		Help:       opts.Description,
		Objectives: objectives,
		MaxAge:     opts.MaxAge,
		AgeBuckets: opts.AgeBuckets,
		BufCap:     opts.BufCap,
	}

	s := &summary{
		registry:    registry,
		labelNames:  labelNames,
		labelValues: labelValues,
		objectives:  objectives,
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

	return s
}

// Observe records a value.
func (s *summary) Observe(value float64) {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	s.summary.Observe(value)
}

// WithTags returns a new summary with the given tags.
func (s *summary) WithTags(tags ...metrics.Tag) metrics.Summary {
	if s.vecSummary == nil || len(tags) == 0 {
		return s
	}

	s.mutex.RLock()
	labelNames := s.labelNames
	objectives := s.objectives
	s.mutex.RUnlock()

	// Create a map of current label values
	currentValues := make(map[string]string)
	for i, name := range labelNames {
		currentValues[name] = s.labelValues[i]
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
	return &summary{
		registry:    s.registry,
		vecSummary:  s.vecSummary,
		summary:     s.vecSummary.WithLabelValues(newValues...),
		labelNames:  labelNames,
		labelValues: newValues,
		objectives:  objectives,
	}
}

// Snapshot returns the current snapshot.
func (s *summary) Snapshot() metrics.SummarySnapshot {
	// Note: Similar to histograms, Prometheus doesn't provide direct access to summary state,
	// so we return a minimal snapshot with default values.
	// This is a limitation of the Prometheus client library.

	// In a production implementation, we would use Prometheus's exposition
	// format to extract the current values.

	emptyQuantiles := make(map[float64]float64)
	for q := range s.objectives {
		emptyQuantiles[q] = 0
	}

	return &summarySnapshot{
		count:     0,
		sum:       0,
		quantiles: emptyQuantiles,
	}
}

// Count returns the count of values.
func (s *summarySnapshot) Count() int64 {
	return s.count
}

// Sum returns the sum of values.
func (s *summarySnapshot) Sum() float64 {
	return s.sum
}

// Quantile returns the value at the given quantile (0-1).
func (s *summarySnapshot) Quantile(q float64) float64 {
	if value, ok := s.quantiles[q]; ok {
		return value
	}
	return 0
}

// Quantiles returns the configured quantiles.
func (s *summarySnapshot) Quantiles() map[float64]float64 {
	return s.quantiles
}
