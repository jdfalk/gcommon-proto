// Package prometheus provides a Prometheus implementation of the metrics provider.
package prometheus

import (
	"context"
	"errors"
	"net/http"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/collectors"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/prometheus/client_golang/prometheus/push"
)

// ErrInvalidMetricType is returned when an invalid metric type is provided
var ErrInvalidMetricType = errors.New("invalid metric type")

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

// NewProvider creates a new Prometheus metrics provider.
func NewProvider(config metrics.Config) (metrics.Provider, error) {
	if config.PrometheusConfig == nil {
		config.PrometheusConfig = &metrics.PrometheusConfig{}
	}

	// Create a new registry
	reg := newRegistry(config.Namespace, config.Subsystem, config.Tags)

	// Add default collectors if enabled
	if config.EnableRuntimeMetrics ||
		(config.PrometheusConfig != nil && config.PrometheusConfig.EnableGoCollector) {
		reg.registry.MustRegister(collectors.NewGoCollector())
	}

	if config.PrometheusConfig != nil && config.PrometheusConfig.EnableProcessCollector {
		reg.registry.MustRegister(collectors.NewProcessCollector(collectors.ProcessCollectorOpts{}))
	}

	// Create the provider
	p := &provider{
		config:     config,
		registry:   reg,
		globalTags: config.Tags,
	}

	// Configure push gateway if enabled
	if config.PrometheusConfig != nil && config.PrometheusConfig.PushGateway != nil {
		pusher := push.New(
			config.PrometheusConfig.PushGateway.URL,
			config.PrometheusConfig.PushJobName,
		).Gatherer(reg.registry)

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

// init registers the prometheus provider with the metrics package.
func init() {
	metrics.RegisterProvider("prometheus", NewProvider)
}
