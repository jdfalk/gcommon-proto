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
	"go.opentelemetry.io/otel/metric/global"
	sdkmetric "go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/resource"
	semconv "go.opentelemetry.io/otel/semconv/v1.17.0"
	"google.golang.org/grpc/credentials"
)

// provider implements the metrics.Provider interface for OpenTelemetry.
type provider struct {
	config         metrics.Config
	meter          metric.Meter
	meterProvider  *sdkmetric.MeterProvider
	exporter       sdkmetric.Exporter
	registry       *registry
	globalTags     []metrics.Tag
	shutdown       func(context.Context) error
	shutdownMutex  sync.Mutex
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

// NewProvider creates a new OpenTelemetry metrics provider.
func NewProvider(config metrics.Config) (metrics.Provider, error) {
	if config.OpenTelemetryConfig == nil {
		config.OpenTelemetryConfig = &metrics.OpenTelemetryConfig{}
	}

	// Create resource with attributes
	res := resource.NewWithAttributes(
		semconv.SchemaURL,
		semconv.ServiceNameKey.String(config.Namespace),
		semconv.ServiceVersionKey.String("1.0.0"), // This should be configurable
	)

	// Add resource attributes from config
	if config.OpenTelemetryConfig.ResourceAttributes != nil {
		attrs := make([]attribute.KeyValue, 0, len(config.OpenTelemetryConfig.ResourceAttributes))
		for k, v := range config.OpenTelemetryConfig.ResourceAttributes {
			attrs = append(attrs, attribute.String(k, v))
		}
		res = resource.NewWithAttributes(semconv.SchemaURL, attrs...)
	}

	// Setup exporter based on collector URL
	var exporter sdkmetric.Exporter
	var err error

	if config.OpenTelemetryConfig.CollectorURL != "" {
		// Determine if using HTTP or gRPC based on URL
		if useGRPC(config.OpenTelemetryConfig.CollectorURL) {
			opts := []otlpmetricgrpc.Option{
				otlpmetricgrpc.WithEndpoint(config.OpenTelemetryConfig.CollectorURL),
			}

			// Setup TLS if not insecure
			if !config.OpenTelemetryConfig.Insecure {
				opts = append(opts, otlpmetricgrpc.WithTLSCredentials(credentials.NewClientTLSFromCert(nil, "")))
			} else {
				opts = append(opts, otlpmetricgrpc.WithInsecure())
			}

			// Add headers if provided
			if len(config.OpenTelemetryConfig.Headers) > 0 {
				headers := make(map[string]string)
				for k, v := range config.OpenTelemetryConfig.Headers {
					headers[k] = v
				}
				opts = append(opts, otlpmetricgrpc.WithHeaders(headers))
			}

			exporter, err = otlpmetricgrpc.New(context.Background(), opts...)
		} else {
			// Using HTTP
			opts := []otlpmetrichttp.Option{
				otlpmetrichttp.WithEndpoint(config.OpenTelemetryConfig.CollectorURL),
			}

			// Setup TLS if not insecure
			if config.OpenTelemetryConfig.Insecure {
				opts = append(opts, otlpmetrichttp.WithInsecure())
			}

			// Add headers if provided
			if len(config.OpenTelemetryConfig.Headers) > 0 {
				headers := make(map[string]string)
				for k, v := range config.OpenTelemetryConfig.Headers {
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
	if config.OpenTelemetryConfig.ExportInterval > 0 {
		exportInterval = config.OpenTelemetryConfig.ExportInterval
	}

	meterProvider := sdkmetric.NewMeterProvider(
		sdkmetric.WithResource(res),
		sdkmetric.WithReader(sdkmetric.NewPeriodicReader(exporter, sdkmetric.WithInterval(exportInterval))),
	)

	// Set as global meter provider
	global.SetMeterProvider(meterProvider)

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

func (e *noopExporter) Temporality(k sdkmetric.InstrumentKind) sdkmetric.Temporality {
	return sdkmetric.CumulativeTemporality
}

func (e *noopExporter) AggregationSelector(sdkmetric.InstrumentKind) sdkmetric.Aggregation {
	return sdkmetric.DefaultAggregation
}

func (e *noopExporter) Export(context.Context, *sdkmetric.ResourceMetrics) error {
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
	return newHistogram(p.registry, name, p.globalTags, options...)
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
