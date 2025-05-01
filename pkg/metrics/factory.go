// Package metrics provides a unified interface for metrics collection.
package metrics

import (
	"fmt"
	"sync"
)

// providerRegistry is a registry of provider constructors.
var providerRegistry = struct {
	sync.RWMutex
	constructors map[string]ProviderConstructor
}{
	constructors: make(map[string]ProviderConstructor),
}

// ProviderConstructor is a function that creates a provider from a config.
type ProviderConstructor func(config Config) (Provider, error)

// RegisterProvider registers a provider constructor.
func RegisterProvider(name string, constructor ProviderConstructor) {
	providerRegistry.Lock()
	defer providerRegistry.Unlock()
	providerRegistry.constructors[name] = constructor
}

// NewProvider creates a new provider from the given config.
func NewProvider(config Config) (Provider, error) {
	if !config.Enabled {
		return newNoopProvider(), nil
	}

	providerRegistry.RLock()
	constructor, ok := providerRegistry.constructors[config.Provider]
	providerRegistry.RUnlock()

	if !ok {
		return nil, fmt.Errorf("unknown metrics provider: %s", config.Provider)
	}

	return constructor(config)
}

// DefaultBuckets are the default buckets for histograms.
var DefaultBuckets = []float64{.005, .01, .025, .05, .075, .1, .25, .5, .75, 1, 2.5, 5, 7.5, 10}

// DefaultQuantiles are the default quantiles for summaries.
var DefaultQuantiles = []float64{0.5, 0.9, 0.95, 0.99}

// WithNamespace sets the metrics namespace.
func WithNamespace(namespace string) Option {
	return func(o *Options) {
		if o.Namespace == "" {
			o.Namespace = namespace
		}
	}
}

// WithSubsystem sets the metrics subsystem.
func WithSubsystem(subsystem string) Option {
	return func(o *Options) {
		if o.Subsystem == "" {
			o.Subsystem = subsystem
		}
	}
}

// TagsToMap converts a slice of tags to a map.
func TagsToMap(tags []Tag) map[string]string {
	m := make(map[string]string, len(tags))
	for _, tag := range tags {
		m[tag.Key] = tag.Value
	}
	return m
}

// MapToTags converts a map to a slice of tags.
func MapToTags(m map[string]string) []Tag {
	tags := make([]Tag, 0, len(m))
	for k, v := range m {
		tags = append(tags, Tag{Key: k, Value: v})
	}
	return tags
}

// MergeTags merges two slices of tags, with tags2 taking precedence.
func MergeTags(tags1, tags2 []Tag) []Tag {
	merged := make([]Tag, len(tags1))
	copy(merged, tags1)

	// Convert to map for easy lookup
	m := TagsToMap(merged)

	// Add tags from tags2, overriding duplicates
	for _, tag := range tags2 {
		m[tag.Key] = tag.Value
	}

	// Convert back to slice
	result := make([]Tag, 0, len(m))
	for k, v := range m {
		result = append(result, Tag{Key: k, Value: v})
	}

	return result
}

// ApplyOptions applies options to the given Options.
func ApplyOptions(options ...Option) *Options {
	opts := &Options{
		Buckets:   DefaultBuckets,
		Quantiles: DefaultQuantiles,
	}
	for _, option := range options {
		option(opts)
	}
	return opts
}

// noopProvider is a provider that does nothing.
type noopProvider struct{}

func newNoopProvider() Provider {
	return &noopProvider{}
}

func (p *noopProvider) Counter(name string, options ...Option) Counter {
	return &noopCounter{}
}

func (p *noopProvider) Gauge(name string, options ...Option) Gauge {
	return &noopGauge{}
}

func (p *noopProvider) Histogram(name string, options ...Option) Histogram {
	return &noopHistogram{}
}

func (p *noopProvider) Summary(name string, options ...Option) Summary {
	return &noopSummary{}
}

func (p *noopProvider) Timer(name string, options ...Option) Timer {
	return &noopTimer{}
}

func (p *noopProvider) Registry() Registry {
	return &noopRegistry{}
}

func (p *noopProvider) Handler() Handler {
	return http.HandlerFunc(func(w ResponseWriter, r *Request) {
		w.WriteHeader(StatusOK)
	})
}

func (p *noopProvider) Start(ctx Context) error {
	return nil
}

func (p *noopProvider) Stop(ctx Context) error {
	return nil
}

func (p *noopProvider) WithTags(tags ...Tag) Provider {
	return p
}

// noopCounter is a counter that does nothing.
type noopCounter struct{}

func (c *noopCounter) Inc() {}

func (c *noopCounter) Add(value float64) {}

func (c *noopCounter) WithTags(tags ...Tag) Counter {
	return c
}

func (c *noopCounter) Value() float64 {
	return 0
}

// noopGauge is a gauge that does nothing.
type noopGauge struct{}

func (g *noopGauge) Set(value float64) {}

func (g *noopGauge) Inc() {}

func (g *noopGauge) Dec() {}

func (g *noopGauge) Add(value float64) {}

func (g *noopGauge) Sub(value float64) {}

func (g *noopGauge) WithTags(tags ...Tag) Gauge {
	return g
}

func (g *noopGauge) Value() float64 {
	return 0
}

// noopHistogram is a histogram that does nothing.
type noopHistogram struct{}

func (h *noopHistogram) Observe(value float64) {}

func (h *noopHistogram) WithTags(tags ...Tag) Histogram {
	return h
}

func (h *noopHistogram) Snapshot() HistogramSnapshot {
	return &noopHistogramSnapshot{}
}

// noopHistogramSnapshot is a histogram snapshot that does nothing.
type noopHistogramSnapshot struct{}

func (s *noopHistogramSnapshot) Count() int64 {
	return 0
}

func (s *noopHistogramSnapshot) Sum() float64 {
	return 0
}

func (s *noopHistogramSnapshot) Quantile(q float64) float64 {
	return 0
}

func (s *noopHistogramSnapshot) Buckets() map[float64]int64 {
	return nil
}

// noopSummary is a summary that does nothing.
type noopSummary struct{}

func (s *noopSummary) Observe(value float64) {}

func (s *noopSummary) WithTags(tags ...Tag) Summary {
	return s
}

func (s *noopSummary) Snapshot() SummarySnapshot {
	return &noopSummarySnapshot{}
}

// noopSummarySnapshot is a summary snapshot that does nothing.
type noopSummarySnapshot struct{}

func (s *noopSummarySnapshot) Count() int64 {
	return 0
}

func (s *noopSummarySnapshot) Sum() float64 {
	return 0
}

func (s *noopSummarySnapshot) Quantile(q float64) float64 {
	return 0
}

func (s *noopSummarySnapshot) Quantiles() map[float64]float64 {
	return nil
}

// noopTimer is a timer that does nothing.
type noopTimer struct{}

func (t *noopTimer) Record(duration Duration) {}

func (t *noopTimer) Time(f func()) {
	f()
}

func (t *noopTimer) WithTags(tags ...Tag) Timer {
	return t
}

func (t *noopTimer) Snapshot() HistogramSnapshot {
	return &noopHistogramSnapshot{}
}

func (t *noopTimer) NewStopwatch() Stopwatch {
	return &noopStopwatch{}
}

// noopStopwatch is a stopwatch that does nothing.
type noopStopwatch struct{}

func (s *noopStopwatch) Stop() {}

func (s *noopStopwatch) Reset() {}

// noopRegistry is a registry that does nothing.
type noopRegistry struct{}

func (r *noopRegistry) Get(name string, typ MetricType) (interface{}, bool) {
	return nil, false
}

func (r *noopRegistry) GetOrCreate(name string, typ MetricType, options ...Option) interface{} {
	switch typ {
	case TypeCounter:
		return &noopCounter{}
	case TypeGauge:
		return &noopGauge{}
	case TypeHistogram:
		return &noopHistogram{}
	case TypeSummary:
		return &noopSummary{}
	case TypeTimer:
		return &noopTimer{}
	default:
		return nil
	}
}

func (r *noopRegistry) Register(name string, metric interface{}, options ...Option) error {
	return nil
}

func (r *noopRegistry) Unregister(name string) bool {
	return false
}

func (r *noopRegistry) Visit(visitor MetricVisitor) {}

func (r *noopRegistry) WithTags(tags ...Tag) Registry {
	return r
}

func (r *noopRegistry) Snapshot() Snapshot {
	return &noopSnapshot{}
}

// noopSnapshot is a snapshot that does nothing.
type noopSnapshot struct{}

func (s *noopSnapshot) Counters() map[string]float64 {
	return nil
}

func (s *noopSnapshot) Gauges() map[string]float64 {
	return nil
}

func (s *noopSnapshot) Histograms() map[string]HistogramSnapshot {
	return nil
}

func (s *noopSnapshot) Summaries() map[string]SummarySnapshot {
	return nil
}
