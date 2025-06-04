// filepath: /Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg/metrics/prometheus/utils.go
package prometheus

import (
	"math"
	"strings"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
)

// Standard common buckets for histograms
var (
	// DefaultLatencyBuckets are optimized for API latency measurements (in seconds)
	DefaultLatencyBuckets = []float64{
		0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10,
	}

	// DefaultSizeBuckets are optimized for response size measurements (in bytes)
	DefaultSizeBuckets = []float64{
		10, 100, 1000, 10000, 100000, 1000000, 10000000,
	}

	// DefaultTimeBuckets are optimized for timing measurements (in seconds)
	DefaultTimeBuckets = []float64{
		0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10,
	}

	// DefaultQuantiles are the standard quantiles to track in summaries
	DefaultQuantiles = map[float64]float64{
		0.5:  0.05,  // 50th percentile with 5% error
		0.9:  0.01,  // 90th percentile with 1% error
		0.95: 0.005, // 95th percentile with 0.5% error
		0.99: 0.001, // 99th percentile with 0.1% error
	}
)

// combineTags merges global tags with metric-specific tags.
// When a tag with the same key exists in both lists, the one from metricTags takes precedence.
//
// Parameters:
//   - globalTags: Global tags to apply to all metrics in the registry
//   - metricTags: Metric-specific tags
//
// Returns:
//   - []metrics.Tag: The combined list of tags
func combineTags(globalTags, metricTags []metrics.Tag) []metrics.Tag {
	if len(globalTags) == 0 {
		return metricTags
	}

	if len(metricTags) == 0 {
		return globalTags
	}

	// Create a map of global tags for quick lookup
	globalTagMap := make(map[string]string, len(globalTags))
	for _, tag := range globalTags {
		globalTagMap[tag.Key] = tag.Value
	}

	// Start with all metric-specific tags
	result := make([]metrics.Tag, len(metricTags))
	copy(result, metricTags)

	// Add global tags that don't conflict with metric-specific tags
	metricTagMap := make(map[string]bool, len(metricTags))
	for _, tag := range metricTags {
		metricTagMap[tag.Key] = true
	}

	for _, tag := range globalTags {
		if !metricTagMap[tag.Key] {
			result = append(result, tag)
		}
	}

	return result
}

// getTagKeys extracts the keys from a list of tags.
//
// Parameters:
//   - tags: The tags to extract keys from
//
// Returns:
//   - []string: The extracted tag keys
func getTagKeys(tags []metrics.Tag) []string {
	keys := make([]string, len(tags))
	for i, tag := range tags {
		keys[i] = tag.Key
	}
	return keys
}

// getTagValues extracts values in the order specified by keys.
//
// Parameters:
//   - tags: The tags to extract values from
//   - keys: The order to extract values in
//
// Returns:
//   - []string: The extracted tag values in the order of keys
func getTagValues(tags []metrics.Tag, keys []string) []string {
	// Create a map for quick lookup
	tagMap := make(map[string]string, len(tags))
	for _, tag := range tags {
		tagMap[tag.Key] = tag.Value
	}

	values := make([]string, len(keys))
	for i, key := range keys {
		values[i] = tagMap[key]
	}

	return values
}

// parseOptions processes a list of options into a consolidated Options struct.
//
// Parameters:
//   - options: The options to parse
//
// Returns:
//   - metrics.Options: The parsed options
func parseOptions(options ...metrics.Option) metrics.Options {
	var opts metrics.Options
	for _, opt := range options {
		opt(&opts)
	}
	return opts
}

// CreateRequestCounter creates a standard HTTP request counter with common tags.
//
// Parameters:
//   - registry: The metrics registry to register with
//   - subsystem: Optional subsystem name (e.g., "http", "grpc")
//   - tags: Additional tags to include
//
// Returns:
//   - metrics.Counter: A counter for tracking request counts
func CreateRequestCounter(registry metrics.Registry, subsystem string, tags ...metrics.Tag) metrics.Counter {
	name := "requests_total"
	if subsystem != "" {
		name = subsystem + "_" + name
	}

	return registry.Counter(
		name,
		append(tags, []metrics.Tag{
			{Key: "status", Value: ""},
			{Key: "method", Value: ""},
			{Key: "path", Value: ""},
		}...),
		metrics.WithDescription("Total number of requests processed"),
	)
}

// CreateResponseTimeHistogram creates a standard histogram for tracking response times.
//
// Parameters:
//   - registry: The metrics registry to register with
//   - subsystem: Optional subsystem name (e.g., "http", "grpc")
//   - buckets: Optional custom buckets (defaults to latency-optimized buckets)
//   - tags: Additional tags to include
//
// Returns:
//   - metrics.Histogram: A histogram for tracking response times
func CreateResponseTimeHistogram(registry metrics.Registry, subsystem string, buckets []float64, tags ...metrics.Tag) metrics.Histogram {
	name := "response_time_seconds"
	if subsystem != "" {
		name = subsystem + "_" + name
	}

	if buckets == nil {
		buckets = DefaultLatencyBuckets
	}

	return registry.Histogram(
		name,
		append(tags, []metrics.Tag{
			{Key: "status", Value: ""},
			{Key: "method", Value: ""},
			{Key: "path", Value: ""},
		}...),
		metrics.WithDescription("Response time in seconds"),
		metrics.WithBuckets(buckets),
	)
}

// CreateResponseSizeHistogram creates a standard histogram for tracking response sizes.
//
// Parameters:
//   - registry: The metrics registry to register with
//   - subsystem: Optional subsystem name (e.g., "http", "grpc")
//   - buckets: Optional custom buckets (defaults to size-optimized buckets)
//   - tags: Additional tags to include
//
// Returns:
//   - metrics.Histogram: A histogram for tracking response sizes
func CreateResponseSizeHistogram(registry metrics.Registry, subsystem string, buckets []float64, tags ...metrics.Tag) metrics.Histogram {
	name := "response_size_bytes"
	if subsystem != "" {
		name = subsystem + "_" + name
	}

	if buckets == nil {
		buckets = DefaultSizeBuckets
	}

	return registry.Histogram(
		name,
		append(tags, []metrics.Tag{
			{Key: "status", Value: ""},
			{Key: "method", Value: ""},
			{Key: "path", Value: ""},
		}...),
		metrics.WithDescription("Response size in bytes"),
		metrics.WithBuckets(buckets),
	)
}

// CreateInFlightGauge creates a standard gauge for tracking in-flight requests.
//
// Parameters:
//   - registry: The metrics registry to register with
//   - subsystem: Optional subsystem name (e.g., "http", "grpc")
//   - tags: Additional tags to include
//
// Returns:
//   - metrics.Gauge: A gauge for tracking in-flight requests
func CreateInFlightGauge(registry metrics.Registry, subsystem string, tags ...metrics.Tag) metrics.Gauge {
	name := "in_flight_requests"
	if subsystem != "" {
		name = subsystem + "_" + name
	}

	return registry.Gauge(
		name,
		tags,
		metrics.WithDescription("Current number of in-flight requests"),
	)
}

// StandardizeMetricName ensures a metric name conforms to Prometheus naming standards.
//
// Parameters:
//   - name: The metric name to standardize
//
// Returns:
//   - string: A standardized metric name
func StandardizeMetricName(name string) string {
	// Replace non-alphanumeric characters with underscores
	name = strings.Map(func(r rune) rune {
		if (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z') || (r >= '0' && r <= '9') {
			return r
		}
		return '_'
	}, name)

	// Ensure it starts with a letter
	if len(name) > 0 && !((name[0] >= 'a' && name[0] <= 'z') || (name[0] >= 'A' && name[0] <= 'Z')) {
		name = "m_" + name
	}

	return strings.ToLower(name)
}

// FormatBuckets creates exponentially increasing bucket values.
//
// Parameters:
//   - start: Starting bucket boundary
//   - factor: Multiplier between buckets
//   - count: Number of buckets to create
//
// Returns:
//   - []float64: A slice of exponentially increasing bucket boundaries
func FormatBuckets(start, factor float64, count int) []float64 {
	buckets := make([]float64, count)
	for i := 0; i < count; i++ {
		buckets[i] = start
		start *= factor
	}
	return buckets
}

// TimeBuckets generates histogram buckets appropriate for measuring
// durations in seconds. The buckets are exponentially distributed and
// cover the range from min to max.
//
// Parameters:
// - min: The minimum duration to measure (in seconds)
// - max: The maximum duration to measure (in seconds)
// - factor: The exponential factor between buckets (usually 2-10)
//
// Returns:
// - []float64: A slice of bucket boundaries in seconds
func TimeBuckets(min, max float64, factor float64) []float64 {
	if min <= 0 {
		min = 0.001 // 1ms minimum
	}
	if max <= min {
		max = min * 1000 // Default to 1000x the minimum
	}
	if factor <= 1 {
		factor = 2 // Default to doubling
	}

	count := int(math.Ceil(math.Log(max/min) / math.Log(factor)))
	buckets := make([]float64, count+1)
	for i := 0; i <= count; i++ {
		buckets[i] = min * math.Pow(factor, float64(i))
	}

	return buckets
}

// LatencyBuckets returns histogram buckets suitable for measuring request latencies
// with a good distribution across orders of magnitude from milliseconds to seconds.
//
// Returns:
// - []float64: Standard latency buckets (in seconds)
func LatencyBuckets() []float64 {
	return []float64{
		0.005, // 5ms
		0.01,  // 10ms
		0.025, // 25ms
		0.05,  // 50ms
		0.1,   // 100ms
		0.25,  // 250ms
		0.5,   // 500ms
		1.0,   // 1s
		2.5,   // 2.5s
		5.0,   // 5s
		10.0,  // 10s
	}
}

// SizeBuckets returns histogram buckets suitable for measuring sizes
// (like request or response sizes) with a good distribution across
// orders of magnitude from bytes to megabytes.
//
// Returns:
// - []float64: Standard size buckets (in bytes)
func SizeBuckets() []float64 {
	return []float64{
		10,       // 10 B
		100,      // 100 B
		1000,     // 1 KB
		10000,    // 10 KB
		100000,   // 100 KB
		1000000,  // 1 MB
		10000000, // 10 MB
	}
}

// CleanMetricName sanitizes a metric name according to Prometheus naming conventions.
// It replaces any characters that are not alphanumeric or underscores with underscores
// and ensures the name starts with a letter.
//
// Parameters:
// - name: The raw metric name to clean
//
// Returns:
// - string: A sanitized metric name
func CleanMetricName(name string) string {
	// Prometheus metric names must match [a-zA-Z_:][a-zA-Z0-9_:]*
	var result strings.Builder

	// Ensure the name starts with a letter if it doesn't already
	if len(name) > 0 && !((name[0] >= 'a' && name[0] <= 'z') ||
		(name[0] >= 'A' && name[0] <= 'Z') ||
		name[0] == '_' || name[0] == ':') {
		result.WriteString("metric_")
	}

	for i, char := range name {
		if (char >= 'a' && char <= 'z') ||
			(char >= 'A' && char <= 'Z') ||
			(char >= '0' && char <= '9' && i > 0) ||
			char == '_' || char == ':' {
			result.WriteRune(char)
		} else {
			result.WriteRune('_')
		}
	}

	return result.String()
}

// CleanLabelName sanitizes a label name according to Prometheus naming conventions.
// It replaces any characters that are not alphanumeric or underscores with underscores.
//
// Parameters:
// - name: The raw label name to clean
//
// Returns:
// - string: A sanitized label name
func CleanLabelName(name string) string {
	// Prometheus label names must match [a-zA-Z_][a-zA-Z0-9_]*
	var result strings.Builder

	// Ensure the name starts with a letter if it doesn't already
	if len(name) > 0 && !((name[0] >= 'a' && name[0] <= 'z') ||
		(name[0] >= 'A' && name[0] <= 'Z') ||
		name[0] == '_') {
		result.WriteString("label_")
	}

	for i, char := range name {
		if (char >= 'a' && char <= 'z') ||
			(char >= 'A' && char <= 'Z') ||
			(char >= '0' && char <= '9' && i > 0) ||
			char == '_' {
			result.WriteRune(char)
		} else {
			result.WriteRune('_')
		}
	}

	return result.String()
}

// DurationToSeconds converts a Go duration to seconds as a float64,
// which is the standard unit for time in Prometheus.
//
// Parameters:
// - d: The duration to convert
//
// Returns:
// - float64: The duration in seconds
func DurationToSeconds(d time.Duration) float64 {
	return float64(d) / float64(time.Second)
}

// CreateHTTPServerMetrics creates a standard set of metrics for monitoring HTTP servers.
// This is a convenience function to ensure consistent naming and structure across HTTP metrics.
//
// Parameters:
// - registry: The metrics registry to register the metrics with
// - serviceName: The name of the service (used as a prefix for metric names)
// - defaultLabels: Default labels to apply to all metrics
//
// Returns:
// - A struct containing all the created metrics
func CreateHTTPServerMetrics(registry metrics.Registry, serviceName string, defaultLabels []metrics.Tag) *HTTPServerMetrics {
	prefix := serviceName
	if prefix != "" {
		prefix = prefix + "_"
	}

	// Default tags for HTTP metrics
	labelNames := []metrics.Tag{
		{Key: "method", Value: ""},
		{Key: "path", Value: ""},
		{Key: "status", Value: ""},
	}

	// Combine default labels with HTTP-specific labels
	for _, label := range defaultLabels {
		labelNames = append(labelNames, label)
	}

	return &HTTPServerMetrics{
		RequestsTotal: registry.Counter(
			prefix+"http_requests_total",
			labelNames,
			metrics.WithDescription("Total number of HTTP requests"),
		),

		RequestDurationSeconds: registry.Histogram(
			prefix+"http_request_duration_seconds",
			labelNames,
			metrics.WithDescription("HTTP request duration in seconds"),
			metrics.WithBuckets(LatencyBuckets()),
		),

		ResponseSizeBytes: registry.Histogram(
			prefix+"http_response_size_bytes",
			labelNames,
			metrics.WithDescription("HTTP response size in bytes"),
			metrics.WithBuckets(SizeBuckets()),
		),

		RequestSizeBytes: registry.Histogram(
			prefix+"http_request_size_bytes",
			labelNames,
			metrics.WithDescription("HTTP request size in bytes"),
			metrics.WithBuckets(SizeBuckets()),
		),

		InFlightRequests: registry.Gauge(
			prefix+"http_in_flight_requests",
			[]metrics.Tag{},
			metrics.WithDescription("Current number of in-flight HTTP requests"),
		),
	}
}

// HTTPServerMetrics contains a standard set of metrics for an HTTP server
type HTTPServerMetrics struct {
	// RequestsTotal counts total HTTP requests
	RequestsTotal metrics.Counter

	// RequestDurationSeconds measures request durations
	RequestDurationSeconds metrics.Histogram

	// ResponseSizeBytes measures response sizes
	ResponseSizeBytes metrics.Histogram

	// RequestSizeBytes measures request sizes
	RequestSizeBytes metrics.Histogram

	// InFlightRequests tracks currently active requests
	InFlightRequests metrics.Gauge
}

// CreateDatabaseMetrics creates a standard set of metrics for monitoring database operations.
// This ensures consistent naming and structure across database metrics.
//
// Parameters:
// - registry: The metrics registry to register the metrics with
// - serviceName: The name of the service (used as a prefix for metric names)
// - defaultLabels: Default labels to apply to all metrics
//
// Returns:
// - A struct containing all the created metrics
func CreateDatabaseMetrics(registry metrics.Registry, serviceName string, defaultLabels []metrics.Tag) *DatabaseMetrics {
	prefix := serviceName
	if prefix != "" {
		prefix = prefix + "_"
	}

	// Default tags for database metrics
	labelNames := []metrics.Tag{
		{Key: "operation", Value: ""},
		{Key: "database", Value: ""},
		{Key: "table", Value: ""},
	}

	// Combine default labels with database-specific labels
	for _, label := range defaultLabels {
		labelNames = append(labelNames, label)
	}

	return &DatabaseMetrics{
		OperationsTotal: registry.Counter(
			prefix+"db_operations_total",
			labelNames,
			metrics.WithDescription("Total number of database operations"),
		),

		OperationErrors: registry.Counter(
			prefix+"db_operation_errors_total",
			labelNames,
			metrics.WithDescription("Total number of database operation errors"),
		),

		OperationDurationSeconds: registry.Histogram(
			prefix+"db_operation_duration_seconds",
			labelNames,
			metrics.WithDescription("Database operation duration in seconds"),
			metrics.WithBuckets(LatencyBuckets()),
		),

		ConnectionsOpen: registry.Gauge(
			prefix+"db_connections_open",
			[]metrics.Tag{{Key: "database", Value: ""}},
			metrics.WithDescription("Number of open database connections"),
		),

		ConnectionsMax: registry.Gauge(
			prefix+"db_connections_max",
			[]metrics.Tag{{Key: "database", Value: ""}},
			metrics.WithDescription("Maximum number of open database connections"),
		),
	}
}

// DatabaseMetrics contains a standard set of metrics for database operations
type DatabaseMetrics struct {
	// OperationsTotal counts total database operations
	OperationsTotal metrics.Counter

	// OperationErrors counts total database operation errors
	OperationErrors metrics.Counter

	// OperationDurationSeconds measures operation durations
	OperationDurationSeconds metrics.Histogram

	// ConnectionsOpen tracks currently open connections
	ConnectionsOpen metrics.Gauge

	// ConnectionsMax tracks the maximum number of connections
	ConnectionsMax metrics.Gauge
}

// CreateCacheMetrics creates a standard set of metrics for monitoring cache operations.
// This ensures consistent naming and structure across cache metrics.
//
// Parameters:
// - registry: The metrics registry to register the metrics with
// - serviceName: The name of the service (used as a prefix for metric names)
// - defaultLabels: Default labels to apply to all metrics
//
// Returns:
// - A struct containing all the created metrics
func CreateCacheMetrics(registry metrics.Registry, serviceName string, defaultLabels []metrics.Tag) *CacheMetrics {
	prefix := serviceName
	if prefix != "" {
		prefix = prefix + "_"
	}

	// Default tags for cache metrics
	labelNames := []metrics.Tag{
		{Key: "operation", Value: ""},
		{Key: "cache", Value: ""},
	}

	// Combine default labels with cache-specific labels
	for _, label := range defaultLabels {
		labelNames = append(labelNames, label)
	}

	return &CacheMetrics{
		OperationsTotal: registry.Counter(
			prefix+"cache_operations_total",
			labelNames,
			metrics.WithDescription("Total number of cache operations"),
		),

		Hits: registry.Counter(
			prefix+"cache_hits_total",
			labelNames,
			metrics.WithDescription("Total number of cache hits"),
		),

		Misses: registry.Counter(
			prefix+"cache_misses_total",
			labelNames,
			metrics.WithDescription("Total number of cache misses"),
		),

		OperationDurationSeconds: registry.Histogram(
			prefix+"cache_operation_duration_seconds",
			labelNames,
			metrics.WithDescription("Cache operation duration in seconds"),
			metrics.WithBuckets([]float64{0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5}),
		),

		Size: registry.Gauge(
			prefix+"cache_size",
			[]metrics.Tag{{Key: "cache", Value: ""}},
			metrics.WithDescription("Current number of items in cache"),
		),

		MemoryUsageBytes: registry.Gauge(
			prefix+"cache_memory_usage_bytes",
			[]metrics.Tag{{Key: "cache", Value: ""}},
			metrics.WithDescription("Current memory usage of cache in bytes"),
		),
	}
}

// CacheMetrics contains a standard set of metrics for cache operations
type CacheMetrics struct {
	// OperationsTotal counts total cache operations
	OperationsTotal metrics.Counter

	// Hits counts cache hits
	Hits metrics.Counter

	// Misses counts cache misses
	Misses metrics.Counter

	// OperationDurationSeconds measures operation durations
	OperationDurationSeconds metrics.Histogram

	// Size tracks the current number of items in the cache
	Size metrics.Gauge

	// MemoryUsageBytes tracks the memory usage of the cache
	MemoryUsageBytes metrics.Gauge
}
