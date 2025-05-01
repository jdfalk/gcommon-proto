// Package prometheus provides a Prometheus implementation of the metrics provider.
package prometheus

import (
	"context"
	"net/http"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/collectors"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/prometheus/client_golang/prometheus/push"
)

// provider implements the metrics.Provider interface for Prometheus.
type provider struct {
	config         metrics.Config
	registry       *registry
	globalTags     []metrics.Tag
	pusher         *push.Pusher
	pushTicker     *time.Ticker
	pushCancelFunc context.CancelFunc
	pushMutex      sync.Mutex
}

// registry implements the metrics.Registry interface for Prometheus.
type registry struct {
	registry      *prometheus.Registry
	namespace     string
	subsystem     string
	defaultLabels prometheus.Labels
	mutex         sync.RWMutex
}

// NewProvider creates a new Prometheus metrics provider.
func NewProvider(config metrics.Config) (metrics.Provider, error) {
	if config.PrometheusConfig == nil {
		config.PrometheusConfig = &metrics.PrometheusConfig{}
	}

	// Create a new registry
	reg := prometheus.NewRegistry()

	// Add default collectors if enabled
	if config.EnableRuntimeMetrics ||
		(config.PrometheusConfig != nil && config.PrometheusConfig.EnableGoCollector) {
		reg.MustRegister(collectors.NewGoCollector())
	}

	if config.PrometheusConfig != nil && config.PrometheusConfig.EnableProcessCollector {
		reg.MustRegister(collectors.NewProcessCollector(collectors.ProcessCollectorOpts{}))
	}

	// Create default labels from global tags
	defaultLabels := make(prometheus.Labels)
	for _, tag := range config.Tags {
		defaultLabels[tag.Key] = tag.Value
	}

	// Create the registry wrapper
	r := &registry{
		registry:      reg,
		namespace:     config.Namespace,
		subsystem:     config.Subsystem,
		defaultLabels: defaultLabels,
	}

	// Create the provider
	p := &provider{
		config:     config,
		registry:   r,
		globalTags: config.Tags,
	}

	// Configure push gateway if enabled
	if config.PrometheusConfig != nil && config.PrometheusConfig.PushGateway != "" {
		pusher := push.New(
			config.PrometheusConfig.PushGateway,
			config.PrometheusConfig.PushJobName,
		).Gatherer(reg)

		p.pusher = pusher
	}

	return p, nil
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
	return newSummary(p.registry, name, p.globalTags, options...)
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
	return promhttp.HandlerFor(p.registry.registry, promhttp.HandlerOpts{})
}

// Start initializes the metrics provider.
func (p *provider) Start(ctx context.Context) error {
	// If the push gateway is configured, start pushing metrics
	if p.pusher != nil && p.config.PrometheusConfig != nil &&
		p.config.PrometheusConfig.PushInterval > 0 {

		p.pushMutex.Lock()
		defer p.pushMutex.Unlock()

		if p.pushTicker != nil {
			return nil
		}

		pushCtx, cancel := context.WithCancel(ctx)
		p.pushCancelFunc = cancel
		p.pushTicker = time.NewTicker(p.config.PrometheusConfig.PushInterval)

		go func() {
			for {
				select {
				case <-p.pushTicker.C:
					if err := p.pusher.Push(); err != nil {
						// Log error here if logger is available
					}
				case <-pushCtx.Done():
					return
				}
			}
		}()
	}

	return nil
}

// Stop stops the metrics provider.
func (p *provider) Stop(ctx context.Context) error {
	p.pushMutex.Lock()
	defer p.pushMutex.Unlock()

	if p.pushTicker != nil {
		p.pushTicker.Stop()
		p.pushTicker = nil
	}

	if p.pushCancelFunc != nil {
		p.pushCancelFunc()
		p.pushCancelFunc = nil
	}

	return nil
}

// WithTags returns a new provider with the given tags.
func (p *provider) WithTags(tags ...metrics.Tag) metrics.Provider {
	newProvider := &provider{
		config:     p.config,
		registry:   p.registry,
		globalTags: append(p.globalTags, tags...),
		pusher:     p.pusher,
	}
	return newProvider
}

// getNames formats a metric name according to Prometheus naming conventions.
func (r *registry) getNames(name string) (string, string) {
	return r.namespace, r.subsystem
}

// getTags converts metrics.Tag to Prometheus labels.
func getTags(tags []metrics.Tag) prometheus.Labels {
	labels := make(prometheus.Labels)
	for _, tag := range tags {
		labels[tag.Key] = tag.Value
	}
	return labels
}

// combineLabels combines default labels with custom labels.
func combineLabels(defaultLabels, customLabels prometheus.Labels) prometheus.Labels {
	result := make(prometheus.Labels)

	// Copy default labels
	for k, v := range defaultLabels {
		result[k] = v
	}

	// Add/override with custom labels
	for k, v := range customLabels {
		result[k] = v
	}

	return result
}

// parseOptions parses metric options.
func parseOptions(options ...metrics.Option) metrics.Options {
	opts := metrics.Options{}
	for _, option := range options {
		option(&opts)
	}
	return opts
}

// getTagKeys extracts tag keys from tags.
func getTagKeys(tags []metrics.Tag) []string {
	keys := make([]string, len(tags))
	for i, tag := range tags {
		keys[i] = tag.Key
	}
	return keys
}

// init registers the prometheus provider with the metrics package.
func init() {
	metrics.RegisterProvider("prometheus", NewProvider)
}
