package prometheus

import (
	"sync"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
)

// metricInfo stores metadata about a registered metric.
type metricInfo struct {
	name        string
	metricType  metrics.MetricType
	metric      interface{}
	description string
	labels      []metrics.Tag
}

// registry implements the metrics.Registry interface for Prometheus.
// It provides methods for registering, retrieving, and managing metrics.
type registry struct {
	registry      *prometheus.Registry
	namespace     string
	subsystem     string
	defaultLabels prometheus.Labels
	mutex         sync.RWMutex

	// Track metrics for snapshot and enumeration
	metrics     map[string]metricInfo
	metricMutex sync.RWMutex
}

// Get gets a metric by name and type.
//
// Parameters:
//   - name: The name of the metric to retrieve
//   - typ: The type of metric to retrieve
//
// Returns:
//   - interface{}: The metric or nil if not found
//   - bool: True if the metric was found, false otherwise
func (r *registry) Get(name string, typ metrics.MetricType) (interface{}, bool) {
	r.metricMutex.RLock()
	defer r.metricMutex.RUnlock()

	fullName := r.getFullName(name)
	info, exists := r.metrics[fullName]
	if !exists || info.metricType != typ {
		return nil, false
	}

	return info.metric, true
}

// GetOrCreate gets or creates a metric.
//
// Parameters:
//   - name: The name of the metric to retrieve or create
//   - typ: The type of metric to retrieve or create
//   - options: Optional configurations for creating the metric
//
// Returns:
//   - interface{}: The retrieved or created metric
func (r *registry) GetOrCreate(name string, typ metrics.MetricType, options ...metrics.Option) interface{} {
	// Check if the metric already exists
	if metric, exists := r.Get(name, typ); exists {
		return metric
	}

	// Create a new metric based on the type
	// This is handled at the provider level for actual metric creation
	return nil
}

// Register registers a metric.
//
// Parameters:
//   - name: The name of the metric to register
//   - metric: The metric to register
//   - options: Optional configurations for the metric
//
// Returns:
//   - error: Any error that occurred during registration
func (r *registry) Register(name string, metric interface{}, options ...metrics.Option) error {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	opts := parseOptions(options...)
	var metricType metrics.MetricType

	// Determine the metric type
	switch metric.(type) {
	case metrics.Counter, *counter:
		metricType = metrics.TypeCounter
	case metrics.Gauge, *gauge:
		metricType = metrics.TypeGauge
	case metrics.Histogram, *histogram:
		metricType = metrics.TypeHistogram
	case metrics.Summary, *summary:
		metricType = metrics.TypeSummary
	case metrics.Timer, *timer:
		metricType = metrics.TypeTimer
	default:
		// For raw Prometheus collectors
		if collector, ok := metric.(prometheus.Collector); ok {
			err := r.registry.Register(collector)
			if err != nil && isAlreadyRegisteredError(err) {
				// Not really an error, metric already exists
				return nil
			}
			return err
		}
		// Unknown metric type
		return metrics.ErrInvalidMetricType
	}

	// Store the metric info for later retrieval
	r.metricMutex.Lock()
	defer r.metricMutex.Unlock()

	if r.metrics == nil {
		r.metrics = make(map[string]metricInfo)
	}

	fullName := r.getFullName(name)
	r.metrics[fullName] = metricInfo{
		name:        name,
		metricType:  metricType,
		metric:      metric,
		description: opts.Help,
		labels:      opts.Tags,
	}

	return nil
}

// Unregister removes a metric from the registry.
//
// Parameters:
//   - name: The name of the metric to unregister
//
// Returns:
//   - bool: True if the metric was unregistered, false otherwise
func (r *registry) Unregister(name string) bool {
	r.metricMutex.Lock()
	defer r.metricMutex.Unlock()

	fullName := r.getFullName(name)
	info, exists := r.metrics[fullName]
	if !exists {
		return false
	}

	// Remove from local tracking
	delete(r.metrics, fullName)

	// Try to unregister from Prometheus if it's a collector
	if collector, ok := info.metric.(prometheus.Collector); ok {
		return r.registry.Unregister(collector)
	}

	return true
}

// Visit visits all metrics in the registry.
//
// Parameters:
//   - visitor: The function to call for each metric
func (r *registry) Visit(visitor metrics.MetricVisitor) {
	r.metricMutex.RLock()
	defer r.metricMutex.RUnlock()

	for name, info := range r.metrics {
		visitor(name, info.metricType, info.metric)
	}
}

// WithTags returns a new registry with the given tags.
//
// Parameters:
//   - tags: The tags to add to the registry
//
// Returns:
//   - metrics.Registry: A new registry with the combined tags
func (r *registry) WithTags(tags ...metrics.Tag) metrics.Registry {
	r.mutex.RLock()
	defer r.mutex.RUnlock()

	// Create a new registry with combined tags
	newLabels := make(prometheus.Labels)
	for k, v := range r.defaultLabels {
		newLabels[k] = v
	}

	for _, tag := range tags {
		newLabels[tag.Key] = tag.Value
	}

	return &registry{
		registry:      r.registry,
		namespace:     r.namespace,
		subsystem:     r.subsystem,
		defaultLabels: newLabels,
		metrics:       r.metrics,
	}
}

// Snapshot returns a snapshot of all metrics in the registry.
//
// Returns:
//   - metrics.Snapshot: A snapshot of all metrics
func (r *registry) Snapshot() metrics.Snapshot {
	r.metricMutex.RLock()
	defer r.metricMutex.RUnlock()

	// Create counters map
	counters := make(map[string]float64)
	gauges := make(map[string]float64)
	histograms := make(map[string]metrics.HistogramSnapshot)
	summaries := make(map[string]metrics.SummarySnapshot)

	// Collect all metrics by type
	for name, info := range r.metrics {
		switch info.metricType {
		case metrics.TypeCounter:
			if counter, ok := info.metric.(metrics.Counter); ok {
				counters[name] = counter.Value()
			}
		case metrics.TypeGauge:
			if gauge, ok := info.metric.(metrics.Gauge); ok {
				gauges[name] = gauge.Value()
			}
		case metrics.TypeHistogram:
			if histogram, ok := info.metric.(metrics.Histogram); ok {
				histograms[name] = histogram.Snapshot()
			}
		case metrics.TypeSummary:
			if summary, ok := info.metric.(metrics.Summary); ok {
				summaries[name] = summary.Snapshot()
			}
		case metrics.TypeTimer:
			if timer, ok := info.metric.(metrics.Timer); ok {
				histograms[name] = timer.Snapshot()
			}
		}
	}

	return &snapshot{
		counters:   counters,
		gauges:     gauges,
		histograms: histograms,
		summaries:  summaries,
	}
}

// getFullName generates a full metric name including namespace and subsystem.
//
// Parameters:
//   - name: The base name of the metric
//
// Returns:
//   - string: The full metric name
func (r *registry) getFullName(name string) string {
	namespace, subsystem := r.getNames(name)
	if namespace == "" && subsystem == "" {
		return name
	}
	if namespace != "" && subsystem == "" {
		return namespace + "_" + name
	}
	if namespace == "" && subsystem != "" {
		return subsystem + "_" + name
	}
	return namespace + "_" + subsystem + "_" + name
}

// getNames returns the namespace and subsystem for a metric.
//
// Parameters:
//   - name: The base name of the metric
//
// Returns:
//   - string: The namespace
//   - string: The subsystem
func (r *registry) getNames(name string) (string, string) {
	// Simply return the registry's namespace and subsystem
	// This is used for generating fully qualified metric names
	return r.namespace, r.subsystem
}

// snapshot implements the metrics.Snapshot interface.
// It provides a point-in-time view of all metrics in the registry.
type snapshot struct {
	counters   map[string]float64
	gauges     map[string]float64
	histograms map[string]metrics.HistogramSnapshot
	summaries  map[string]metrics.SummarySnapshot
}

// Counters returns the counter snapshots.
//
// Returns:
//   - map[string]float64: A map of counter names to values
func (s *snapshot) Counters() map[string]float64 {
	return s.counters
}

// Gauges returns the gauge snapshots.
//
// Returns:
//   - map[string]float64: A map of gauge names to values
func (s *snapshot) Gauges() map[string]float64 {
	return s.gauges
}

// Histograms returns the histogram snapshots.
//
// Returns:
//   - map[string]metrics.HistogramSnapshot: A map of histogram names to snapshots
func (s *snapshot) Histograms() map[string]metrics.HistogramSnapshot {
	return s.histograms
}

// Summaries returns the summary snapshots.
//
// Returns:
//   - map[string]metrics.SummarySnapshot: A map of summary names to snapshots
func (s *snapshot) Summaries() map[string]metrics.SummarySnapshot {
	return s.summaries
}

// isAlreadyRegisteredError checks if an error is a Prometheus AlreadyRegisteredError.
//
// Parameters:
//   - err: The error to check
//
// Returns:
//   - bool: True if the error is an AlreadyRegisteredError, false otherwise
func isAlreadyRegisteredError(err error) bool {
	_, ok := err.(prometheus.AlreadyRegisteredError)
	return ok
}

// newRegistry creates a new Prometheus registry.
//
// Parameters:
//   - namespace: The namespace to use for all metrics in this registry
//   - subsystem: The subsystem to use for all metrics in this registry
//   - defaultTags: The default tags to apply to all metrics
//
// Returns:
//   - *registry: A new registry instance with the specified configuration
func newRegistry(namespace, subsystem string, defaultTags []metrics.Tag) *registry {
	// Create labels from tags
	labels := make(prometheus.Labels)
	for _, tag := range defaultTags {
		labels[tag.Key] = tag.Value
	}

	// Create the registry
	return &registry{
		registry:      prometheus.NewRegistry(),
		namespace:     namespace,
		subsystem:     subsystem,
		defaultLabels: labels,
		metrics:       make(map[string]metricInfo),
	}
}
