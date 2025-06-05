// Package otel provides an OpenTelemetry implementation of the metrics provider.
package otel

import (
	"context"
	"net/http"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp"
	"go.opentelemetry.io/otel/metric"
	sdkmetric "go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/metric/metricdata"
	"go.opentelemetry.io/otel/sdk/resource"
	semconv "go.opentelemetry.io/otel/semconv/v1.17.0"
	"google.golang.org/grpc/credentials"
)

// provider implements the metrics.Provider interface for OpenTelemetry.
type provider struct {
	config        metrics.Config
	meter         metric.Meter
	meterProvider *sdkmetric.MeterProvider
	exporter      sdkmetric.Exporter
	registry      *registry
	globalTags    []metrics.Tag
	shutdown      func(context.Context) error
	shutdownMutex sync.Mutex
}

// registry implements the metrics.Registry interface for OpenTelemetry.
type registry struct {
	namespace    string
	subsystem    string
	defaultAttrs []attribute.KeyValue
	meter        metric.Meter
	mutex        sync.RWMutex
	metrics      map[string]interface{}
}

// OpenTelemetryConfig represents OpenTelemetry-specific configuration.
type OpenTelemetryConfig struct {
	// CollectorURL is the URL of the OpenTelemetry collector.
	CollectorURL string

	// ExportInterval is the interval for exporting metrics.
	ExportInterval time.Duration

	// ResourceAttributes are resource attributes to include with metrics.
	ResourceAttributes map[string]string

	// Headers are HTTP headers for the exporter.
	Headers map[string]string

	// Insecure specifies whether to use insecure connections.
	Insecure bool
}

// extractOTelConfig extracts OpenTelemetry configuration from ProviderConfig.
func extractOTelConfig(providerConfig map[string]interface{}) *OpenTelemetryConfig {
	config := &OpenTelemetryConfig{
		ExportInterval: 30 * time.Second, // Default
		Insecure:       false,            // Default
	}

	if providerConfig == nil {
		return config
	}

	if url, ok := providerConfig["collector_url"].(string); ok {
		config.CollectorURL = url
	}
	if url, ok := providerConfig["collectorURL"].(string); ok {
		config.CollectorURL = url
	}

	if interval, ok := providerConfig["export_interval"].(time.Duration); ok {
		config.ExportInterval = interval
	}
	if interval, ok := providerConfig["exportInterval"].(time.Duration); ok {
		config.ExportInterval = interval
	}

	if attrs, ok := providerConfig["resource_attributes"].(map[string]string); ok {
		config.ResourceAttributes = attrs
	}
	if attrs, ok := providerConfig["resourceAttributes"].(map[string]string); ok {
		config.ResourceAttributes = attrs
	}

	if headers, ok := providerConfig["headers"].(map[string]string); ok {
		config.Headers = headers
	}

	if insecure, ok := providerConfig["insecure"].(bool); ok {
		config.Insecure = insecure
	}

	return config
}

// NewProvider creates a new OpenTelemetry metrics provider.
func NewProvider(config metrics.Config) (metrics.Provider, error) {
	// Extract OpenTelemetry config from ProviderConfig
	otelConfig := extractOTelConfig(config.ProviderConfig)

	// Create resource with attributes
	res := resource.NewWithAttributes(
		semconv.SchemaURL,
		semconv.ServiceNameKey.String(config.Namespace),
		semconv.ServiceVersionKey.String("1.0.0"), // This should be configurable
	)

	// Add resource attributes from config
	if otelConfig.ResourceAttributes != nil {
		attrs := make([]attribute.KeyValue, 0, len(otelConfig.ResourceAttributes))
		for k, v := range otelConfig.ResourceAttributes {
			attrs = append(attrs, attribute.String(k, v))
		}
		res = resource.NewWithAttributes(semconv.SchemaURL, attrs...)
	}

	// Setup exporter based on collector URL
	var exporter sdkmetric.Exporter
	var err error

	if otelConfig.CollectorURL != "" {
		// Determine if using HTTP or gRPC based on URL
		if useGRPC(otelConfig.CollectorURL) {
			opts := []otlpmetricgrpc.Option{
				otlpmetricgrpc.WithEndpoint(otelConfig.CollectorURL),
			}

			// Setup TLS if not insecure
			if !otelConfig.Insecure {
				opts = append(opts, otlpmetricgrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, "")))
			} else {
				opts = append(opts, otlpmetricgrpc.WithInsecure())
			}

			// Add headers if provided
			if len(otelConfig.Headers) > 0 {
				headers := make(map[string]string)
				for k, v := range otelConfig.Headers {
					headers[k] = v
				}
				opts = append(opts, otlpmetricgrpc.WithHeaders(headers))
			}

			exporter, err = otlpmetricgrpc.New(context.Background(), opts...)
		} else {
			// Using HTTP
			opts := []otlpmetrichttp.Option{
				otlpmetrichttp.WithEndpoint(otelConfig.CollectorURL),
			}

			// Setup TLS if not insecure
			if otelConfig.Insecure {
				opts = append(opts, otlpmetrichttp.WithInsecure())
			}

			// Add headers if provided
			if len(otelConfig.Headers) > 0 {
				headers := make(map[string]string)
				for k, v := range otelConfig.Headers {
					headers[k] = v
				}
				opts = append(opts, otlpmetrichttp.WithHeaders(headers))
			}

			exporter, err = otlpmetrichttp.New(context.Background(), opts...)
		}

		if err != nil {
			return nil, err
		}
	} else {
		// Default to a noop exporter if no collector URL is provided
		exporter = &noopExporter{}
	}

	// Set up the meter provider
	exportInterval := time.Second * 30 // Default
	if otelConfig.ExportInterval > 0 {
		exportInterval = otelConfig.ExportInterval
	}

	meterProvider := sdkmetric.NewMeterProvider(
		sdkmetric.WithResource(res),
		sdkmetric.WithReader(sdkmetric.NewPeriodicReader(exporter, sdkmetric.WithInterval(exportInterval))),
	)

	// Create a meter
	meterName := config.Namespace
	if config.Subsystem != "" {
		meterName = config.Namespace + "." + config.Subsystem
	}
	meter := meterProvider.Meter(meterName)

	// Create default attributes from global tags
	defaultAttrs := make([]attribute.KeyValue, 0, len(config.Tags))
	for _, tag := range config.Tags {
		defaultAttrs = append(defaultAttrs, attribute.String(tag.Key, tag.Value))
	}

	// Create the registry
	reg := &registry{
		namespace:    config.Namespace,
		subsystem:    config.Subsystem,
		defaultAttrs: defaultAttrs,
		meter:        meter,
		metrics:      make(map[string]interface{}),
	}

	// Create the provider
	p := &provider{
		config:        config,
		meterProvider: meterProvider,
		exporter:      exporter,
		meter:         meter,
		registry:      reg,
		globalTags:    config.Tags,
		shutdown: func(ctx context.Context) error {
			return meterProvider.Shutdown(ctx)
		},
	}

	return p, nil
}

// useGRPC determines if the collector URL should use gRPC based on its prefix
func useGRPC(url string) bool {
	// Simple heuristic: if it ends with ":grpc", use gRPC
	return len(url) >= 5 && url[len(url)-5:] == ":grpc"
}

// noopExporter is a no-op exporter that does nothing
type noopExporter struct{}

func (e *noopExporter) Temporality(k sdkmetric.InstrumentKind) metricdata.Temporality {
	return metricdata.CumulativeTemporality
}

func (e *noopExporter) Aggregation(k sdkmetric.InstrumentKind) sdkmetric.Aggregation {
	return sdkmetric.DefaultAggregationSelector(k)
}

func (e *noopExporter) Export(context.Context, *metricdata.ResourceMetrics) error {
	return nil
}

func (e *noopExporter) ForceFlush(context.Context) error {
	return nil
}

func (e *noopExporter) Shutdown(context.Context) error {
	return nil
}

// Counter creates or gets a counter.
func (p *provider) Counter(name string, options ...metrics.Option) metrics.Counter {
	return newCounter(p.registry, name, p.globalTags, options...)
}

// Gauge creates or gets a gauge.
func (p *provider) Gauge(name string, options ...metrics.Option) metrics.Gauge {
	return newGauge(p.registry, name, p.globalTags, options...)
}

// Histogram creates or gets a histogram.
func (p *provider) Histogram(name string, options ...metrics.Option) metrics.Histogram {
	return newHistogram(p.registry, name, p.globalTags, options...)
}

// Summary creates or gets a summary.
func (p *provider) Summary(name string, options ...metrics.Option) metrics.Summary {
	// OpenTelemetry doesn't directly support summaries, so we map it to a histogram
	return newSummaryWrapper(p.registry, name, p.globalTags, options...)
}

// Timer creates or gets a timer.
func (p *provider) Timer(name string, options ...metrics.Option) metrics.Timer {
	return newTimer(p.registry, name, p.globalTags, options...)
}

// Registry returns the metrics registry.
func (p *provider) Registry() metrics.Registry {
	return p.registry
}

// Handler returns an HTTP handler for metrics exposition.
func (p *provider) Handler() http.Handler {
	// OpenTelemetry doesn't provide a direct HTTP handler for metrics
	// We return a simple handler that indicates metrics are collected via OpenTelemetry
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain")
		w.Write([]byte("OpenTelemetry metrics are being collected and exported to configured collector.\n"))
	})
}

// Start initializes the metrics provider.
func (p *provider) Start(ctx context.Context) error {
	// Nothing special needed for starting OpenTelemetry metrics
	return nil
}

// Stop stops the metrics provider.
func (p *provider) Stop(ctx context.Context) error {
	p.shutdownMutex.Lock()
	defer p.shutdownMutex.Unlock()

	if p.shutdown != nil {
		return p.shutdown(ctx)
	}
	return nil
}

// WithTags returns a new provider with the given tags.
func (p *provider) WithTags(tags ...metrics.Tag) metrics.Provider {
	// Convert GCommon tags to OpenTelemetry attributes
	newTags := append(p.globalTags, tags...)

	// Create a new provider with the combined tags
	newProvider := &provider{
		config:        p.config,
		meterProvider: p.meterProvider,
		exporter:      p.exporter,
		meter:         p.meter,
		registry:      p.registry,
		globalTags:    newTags,
		shutdown:      p.shutdown,
	}

	return newProvider
}

// convertToAttributes converts GCommon tags to OpenTelemetry attributes.
func convertToAttributes(tags []metrics.Tag) []attribute.KeyValue {
	attrs := make([]attribute.KeyValue, 0, len(tags))
	for _, tag := range tags {
		attrs = append(attrs, attribute.String(tag.Key, tag.Value))
	}
	return attrs
}

// parseOptions parses metric options.
func parseOptions(options ...metrics.Option) metrics.Options {
	opts := metrics.Options{}
	for _, option := range options {
		option(&opts)
	}
	return opts
}

// init registers the OpenTelemetry provider with the metrics package.
func init() {
	metrics.RegisterProvider("opentelemetry", NewProvider)
	metrics.RegisterProvider("otel", NewProvider) // Convenience alias
}

// Get retrieves a metric by name and type.
func (r *registry) Get(name string, typ metrics.MetricType) (interface{}, bool) {
	r.mutex.RLock()
	defer r.mutex.RUnlock()

	// Create a more descriptive name if namespace/subsystem are provided
	fullName := name
	if r.namespace != "" {
		if r.subsystem != "" {
			fullName = r.namespace + "." + r.subsystem + "." + name
		} else {
			fullName = r.namespace + "." + name
		}
	}

	metric, exists := r.metrics[fullName]
	if !exists {
		return nil, false
	}

	// Check if the metric type matches what's expected
	switch typ {
	case metrics.TypeCounter:
		if _, ok := metric.(*counter); ok {
			return metric, true
		}
	case metrics.TypeGauge:
		if _, ok := metric.(*gauge); ok {
			return metric, true
		}
	case metrics.TypeHistogram:
		if _, ok := metric.(*histogram); ok {
			return metric, true
		}
	case metrics.TypeSummary:
		if _, ok := metric.(*summaryWrapper); ok {
			return metric, true
		}
	case metrics.TypeTimer:
		if _, ok := metric.(*timer); ok {
			return metric, true
		}
	}

	return nil, false
}

// GetOrCreate retrieves a metric or creates it if it doesn't exist.
func (r *registry) GetOrCreate(name string, typ metrics.MetricType, options ...metrics.Option) interface{} {
	// First try to get the existing metric
	if metric, exists := r.Get(name, typ); exists {
		return metric
	}

	// Create a new metric based on type
	switch typ {
	case metrics.TypeCounter:
		return newCounter(r, name, nil, options...)
	case metrics.TypeGauge:
		return newGauge(r, name, nil, options...)
	case metrics.TypeHistogram:
		return newHistogram(r, name, nil, options...)
	case metrics.TypeSummary:
		return newSummaryWrapper(r, name, nil, options...)
	case metrics.TypeTimer:
		return newTimer(r, name, nil, options...)
	default:
		return nil
	}
}

// Register registers a metric.
func (r *registry) Register(name string, metric interface{}, options ...metrics.Option) error {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	// Create a more descriptive name if namespace/subsystem are provided
	fullName := name
	if r.namespace != "" {
		if r.subsystem != "" {
			fullName = r.namespace + "." + r.subsystem + "." + name
		} else {
			fullName = r.namespace + "." + name
		}
	}

	// Store the metric
	r.metrics[fullName] = metric
	return nil
}

// Unregister removes a metric from the registry.
func (r *registry) Unregister(name string) bool {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	// Create a more descriptive name if namespace/subsystem are provided
	fullName := name
	if r.namespace != "" {
		if r.subsystem != "" {
			fullName = r.namespace + "." + r.subsystem + "." + name
		} else {
			fullName = r.namespace + "." + name
		}
	}

	if _, exists := r.metrics[fullName]; exists {
		delete(r.metrics, fullName)
		return true
	}
	return false
}

// Visit visits all metrics in the registry.
func (r *registry) Visit(visitor metrics.MetricVisitor) {
	r.mutex.RLock()
	defer r.mutex.RUnlock()

	for name, metric := range r.metrics {
		var typ metrics.MetricType
		switch metric.(type) {
		case *counter:
			typ = metrics.TypeCounter
		case *gauge:
			typ = metrics.TypeGauge
		case *histogram:
			typ = metrics.TypeHistogram
		case *summaryWrapper:
			typ = metrics.TypeSummary
		case *timer:
			typ = metrics.TypeTimer
		default:
			continue // Skip unknown types
		}
		visitor(name, typ, metric)
	}
}

// WithTags returns a new registry with the given tags.
func (r *registry) WithTags(tags ...metrics.Tag) metrics.Registry {
	// Convert tags to attributes and combine with existing
	newAttrs := make([]attribute.KeyValue, len(r.defaultAttrs)+len(tags))
	copy(newAttrs, r.defaultAttrs)

	for i, tag := range tags {
		newAttrs[len(r.defaultAttrs)+i] = attribute.String(tag.Key, tag.Value)
	}

	return &registry{
		namespace:    r.namespace,
		subsystem:    r.subsystem,
		defaultAttrs: newAttrs,
		meter:        r.meter,
		metrics:      make(map[string]interface{}),
	}
}

// Snapshot returns a snapshot of all metrics in the registry.
func (r *registry) Snapshot() metrics.Snapshot {
	r.mutex.RLock()
	defer r.mutex.RUnlock()

	counters := make(map[string]float64)
	gauges := make(map[string]float64)
	histograms := make(map[string]metrics.HistogramSnapshot)
	summaries := make(map[string]metrics.SummarySnapshot)

	for name, metric := range r.metrics {
		switch m := metric.(type) {
		case *counter:
			counters[name] = m.Value()
		case *gauge:
			gauges[name] = m.Value()
		case *histogram:
			histograms[name] = m.Snapshot()
		case *summaryWrapper:
			summaries[name] = m.Snapshot()
		case *timer:
			histograms[name] = m.Snapshot()
		}
	}

	return &snapshot{
		counters:   counters,
		gauges:     gauges,
		histograms: histograms,
		summaries:  summaries,
	}
}

// snapshot implements the metrics.Snapshot interface.
type snapshot struct {
	counters   map[string]float64
	gauges     map[string]float64
	histograms map[string]metrics.HistogramSnapshot
	summaries  map[string]metrics.SummarySnapshot
}

// Counters returns the counter snapshots.
func (s *snapshot) Counters() map[string]float64 {
	return s.counters
}

// Gauges returns the gauge snapshots.
func (s *snapshot) Gauges() map[string]float64 {
	return s.gauges
}

// Histograms returns the histogram snapshots.
func (s *snapshot) Histograms() map[string]metrics.HistogramSnapshot {
	return s.histograms
}

// Summaries returns the summary snapshots.
func (s *snapshot) Summaries() map[string]metrics.SummarySnapshot {
	return s.summaries
}

// summaryWrapper wraps a histogram to provide Summary interface.
// OpenTelemetry doesn't have native summary support, so we use a histogram.
type summaryWrapper struct {
	histogram metrics.Histogram
}

// newSummaryWrapper creates a new summary wrapper around a histogram.
func newSummaryWrapper(registry *registry, name string, globalTags []metrics.Tag, options ...metrics.Option) metrics.Summary {
	// Create a histogram under the hood
	hist := newHistogram(registry, name, globalTags, options...)

	return &summaryWrapper{
		histogram: hist,
	}
}

// Observe records a value (delegates to histogram).
func (s *summaryWrapper) Observe(value float64) {
	s.histogram.Observe(value)
}

// WithTags returns a new summary with the given tags.
func (s *summaryWrapper) WithTags(tags ...metrics.Tag) metrics.Summary {
	newHist := s.histogram.WithTags(tags...)
	return &summaryWrapper{histogram: newHist}
}

// Snapshot returns the current snapshot as a SummarySnapshot.
func (s *summaryWrapper) Snapshot() metrics.SummarySnapshot {
	// Get the histogram snapshot and convert it to a summary snapshot
	histSnapshot := s.histogram.Snapshot()
	return &summarySnapshot{
		count: histSnapshot.Count(),
		sum:   histSnapshot.Sum(),
		// For simplicity, we'll provide some basic quantiles based on histogram data
		quantiles: map[float64]float64{
			0.5:  0.0, // TODO: Calculate from histogram buckets
			0.9:  0.0,
			0.95: 0.0,
			0.99: 0.0,
		},
	}
}

// summarySnapshot implements the metrics.SummarySnapshot interface.
type summarySnapshot struct {
	count     int64
	sum       float64
	quantiles map[float64]float64
}

// Count returns the count of values.
func (s *summarySnapshot) Count() int64 {
	return s.count
}

// Sum returns the sum of values.
func (s *summarySnapshot) Sum() float64 {
	return s.sum
}

// Quantile returns the value at the given quantile.
func (s *summarySnapshot) Quantile(q float64) float64 {
	if val, exists := s.quantiles[q]; exists {
		return val
	}
	return 0.0
}

// Quantiles returns all quantiles.
func (s *summarySnapshot) Quantiles() map[float64]float64 {
	return s.quantiles
}
