// file: pkg/metrics/memory/provider.go
// version: 1.1.0
// guid: 6e4e9a8b-4a8c-4f1c-8a3c-89bf7d4ae1c1

package memory

import (
	"context"
	"math"
	"net/http"
	"sort"
	"sync"
	"time"

	metrics "github.com/jdfalk/gcommon/pkg/metrics"
)

type provider struct {
	registry *registry
}

// NewProvider creates a new in-memory metrics provider.
func NewProvider(config metrics.Config) (metrics.Provider, error) {
	return &provider{registry: newRegistry()}, nil
}

// init registers the memory provider with the factory.
func init() {
	metrics.RegisterProvider("memory", NewProvider)
}

func (p *provider) Counter(name string, options ...metrics.Option) metrics.Counter {
	return p.registry.getOrCreateCounter(name)
}

func (p *provider) Gauge(name string, options ...metrics.Option) metrics.Gauge {
	return p.registry.getOrCreateGauge(name)
}

func (p *provider) Histogram(name string, options ...metrics.Option) metrics.Histogram {
	return p.registry.getOrCreateHistogram(name, nil)
}

func (p *provider) Summary(name string, options ...metrics.Option) metrics.Summary {
	return p.registry.getOrCreateSummary(name)
}

func (p *provider) Timer(name string, options ...metrics.Option) metrics.Timer {
	return p.registry.getOrCreateTimer(name)
}

func (p *provider) Registry() metrics.Registry                    { return p.registry }
func (p *provider) Handler() http.Handler                         { return nil }
func (p *provider) Start(ctx context.Context) error               { return nil }
func (p *provider) Stop(ctx context.Context) error                { return nil }
func (p *provider) WithTags(tags ...metrics.Tag) metrics.Provider { return p }

// counter implementation

type counter struct {
	mu    sync.Mutex
	value float64
}

func (c *counter) Inc() { c.Add(1) }
func (c *counter) Add(v float64) {
	c.mu.Lock()
	c.value += v
	c.mu.Unlock()
}
func (c *counter) WithTags(tags ...metrics.Tag) metrics.Counter { return c }
func (c *counter) Value() float64 {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.value
}

// gauge implementation

type gauge struct {
	mu    sync.Mutex
	value float64
}

func (g *gauge) Set(v float64) {
	g.mu.Lock()
	g.value = v
	g.mu.Unlock()
}
func (g *gauge) Inc() { g.Add(1) }
func (g *gauge) Dec() { g.Add(-1) }
func (g *gauge) Add(v float64) {
	g.mu.Lock()
	g.value += v
	g.mu.Unlock()
}
func (g *gauge) Sub(v float64)                              { g.Add(-v) }
func (g *gauge) WithTags(tags ...metrics.Tag) metrics.Gauge { return g }
func (g *gauge) Value() float64 {
	g.mu.Lock()
	defer g.mu.Unlock()
	return g.value
}

// histogram implementation

type histogram struct {
	mu      sync.Mutex
	buckets []float64
	counts  map[float64]int64
	sum     float64
}

func newHistogram(buckets []float64) *histogram {
	if len(buckets) == 0 {
		buckets = []float64{0.5, 1, 5, 10}
	}
	sort.Float64s(buckets)
	counts := make(map[float64]int64, len(buckets)+1)
	counts[math.Inf(1)] = 0
	return &histogram{buckets: buckets, counts: counts}
}

func (h *histogram) Observe(v float64) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.sum += v
	for _, b := range h.buckets {
		if v <= b {
			h.counts[b]++
			return
		}
	}
	h.counts[math.Inf(1)]++
}

func (h *histogram) WithTags(tags ...metrics.Tag) metrics.Histogram { return h }
func (h *histogram) Snapshot() metrics.HistogramSnapshot {
	h.mu.Lock()
	defer h.mu.Unlock()
	counts := make(map[float64]int64, len(h.counts))
	var total int64
	for b, c := range h.counts {
		counts[b] = c
		total += c
	}
	return &histogramSnapshot{count: total, sum: h.sum, buckets: counts, boundaries: append([]float64(nil), h.buckets...)}
}

type histogramSnapshot struct {
	count      int64
	sum        float64
	buckets    map[float64]int64
	boundaries []float64
}

func (s *histogramSnapshot) Count() int64 { return s.count }
func (s *histogramSnapshot) Sum() float64 { return s.sum }
func (s *histogramSnapshot) Quantile(q float64) float64 {
	if s.count == 0 {
		return 0
	}
	target := q * float64(s.count)
	var cum int64
	for _, b := range append(s.boundaries, math.Inf(1)) {
		cum += s.buckets[b]
		if float64(cum) >= target {
			return b
		}
	}
	return s.boundaries[len(s.boundaries)-1]
}
func (s *histogramSnapshot) Buckets() map[float64]int64 { return s.buckets }

// summary implementation

type summary struct {
	mu           sync.Mutex
	observations []float64
	sum          float64
}

func newSummary() *summary { return &summary{} }

func (s *summary) Observe(v float64) {
	s.mu.Lock()
	s.observations = append(s.observations, v)
	s.sum += v
	s.mu.Unlock()
}

func (s *summary) WithTags(tags ...metrics.Tag) metrics.Summary { return s }
func (s *summary) Snapshot() metrics.SummarySnapshot {
	s.mu.Lock()
	defer s.mu.Unlock()
	obs := append([]float64(nil), s.observations...)
	sort.Float64s(obs)
	return &summarySnapshot{values: obs, sum: s.sum}
}

type summarySnapshot struct {
	values []float64
	sum    float64
}

func (s *summarySnapshot) Count() int64 { return int64(len(s.values)) }
func (s *summarySnapshot) Sum() float64 { return s.sum }
func (s *summarySnapshot) Quantile(q float64) float64 {
	n := len(s.values)
	if n == 0 {
		return 0
	}
	if q <= 0 {
		return s.values[0]
	}
	if q >= 1 {
		return s.values[n-1]
	}
	rank := q * float64(n-1)
	lower := int(math.Floor(rank))
	upper := int(math.Ceil(rank))
	if lower == upper {
		return s.values[lower]
	}
	frac := rank - float64(lower)
	return s.values[lower] + (s.values[upper]-s.values[lower])*frac
}
func (s *summarySnapshot) Quantiles() map[float64]float64 {
	qs := []float64{0.5, 0.9, 0.99}
	m := make(map[float64]float64, len(qs))
	for _, q := range qs {
		m[q] = s.Quantile(q)
	}
	return m
}

// timer implementation

type timer struct{ hist *histogram }

func newTimer() *timer { return &timer{hist: newHistogram(nil)} }

func (t *timer) Record(d time.Duration)                     { t.hist.Observe(d.Seconds()) }
func (t *timer) Time(f func())                              { start := time.Now(); f(); t.Record(time.Since(start)) }
func (t *timer) WithTags(tags ...metrics.Tag) metrics.Timer { return t }
func (t *timer) Snapshot() metrics.HistogramSnapshot        { return t.hist.Snapshot() }
func (t *timer) NewStopwatch() metrics.Stopwatch            { return &stopwatch{start: time.Now(), h: t.hist} }

type stopwatch struct {
	start time.Time
	h     *histogram
}

func (s *stopwatch) Stop()  { s.h.Observe(time.Since(s.start).Seconds()) }
func (s *stopwatch) Reset() { s.start = time.Now() }

// registry implementation

type registry struct {
	mu         sync.RWMutex
	counters   map[string]*counter
	gauges     map[string]*gauge
	histograms map[string]*histogram
	summaries  map[string]*summary
	timers     map[string]*timer
}

func newRegistry() *registry {
	return &registry{
		counters:   make(map[string]*counter),
		gauges:     make(map[string]*gauge),
		histograms: make(map[string]*histogram),
		summaries:  make(map[string]*summary),
		timers:     make(map[string]*timer),
	}
}

func (r *registry) getOrCreateCounter(name string) *counter {
	r.mu.Lock()
	defer r.mu.Unlock()
	c, ok := r.counters[name]
	if !ok {
		c = &counter{}
		r.counters[name] = c
	}
	return c
}

func (r *registry) getOrCreateGauge(name string) *gauge {
	r.mu.Lock()
	defer r.mu.Unlock()
	g, ok := r.gauges[name]
	if !ok {
		g = &gauge{}
		r.gauges[name] = g
	}
	return g
}

func (r *registry) getOrCreateHistogram(name string, buckets []float64) *histogram {
	r.mu.Lock()
	defer r.mu.Unlock()
	h, ok := r.histograms[name]
	if !ok {
		h = newHistogram(buckets)
		r.histograms[name] = h
	}
	return h
}

func (r *registry) getOrCreateSummary(name string) *summary {
	r.mu.Lock()
	defer r.mu.Unlock()
	s, ok := r.summaries[name]
	if !ok {
		s = newSummary()
		r.summaries[name] = s
	}
	return s
}

func (r *registry) getOrCreateTimer(name string) *timer {
	r.mu.Lock()
	defer r.mu.Unlock()
	t, ok := r.timers[name]
	if !ok {
		t = newTimer()
		r.timers[name] = t
	}
	return t
}

func (r *registry) getOrCreate(name string, typ metrics.MetricType, options ...metrics.Option) interface{} {
	switch typ {
	case metrics.TypeCounter:
		return r.getOrCreateCounter(name)
	case metrics.TypeGauge:
		return r.getOrCreateGauge(name)
	case metrics.TypeHistogram:
		return r.getOrCreateHistogram(name, nil)
	case metrics.TypeSummary:
		return r.getOrCreateSummary(name)
	case metrics.TypeTimer:
		return r.getOrCreateTimer(name)
	default:
		return nil
	}
}

func (r *registry) Get(name string, typ metrics.MetricType) (interface{}, bool) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	switch typ {
	case metrics.TypeCounter:
		v, ok := r.counters[name]
		return v, ok
	case metrics.TypeGauge:
		v, ok := r.gauges[name]
		return v, ok
	case metrics.TypeHistogram:
		v, ok := r.histograms[name]
		return v, ok
	case metrics.TypeSummary:
		v, ok := r.summaries[name]
		return v, ok
	case metrics.TypeTimer:
		v, ok := r.timers[name]
		return v, ok
	default:
		return nil, false
	}
}

func (r *registry) GetOrCreate(name string, typ metrics.MetricType, options ...metrics.Option) interface{} {
	return r.getOrCreate(name, typ, options...)
}

func (r *registry) Register(name string, metric interface{}, options ...metrics.Option) error {
	r.mu.Lock()
	defer r.mu.Unlock()
	switch m := metric.(type) {
	case *counter:
		r.counters[name] = m
	case *gauge:
		r.gauges[name] = m
	case *histogram:
		r.histograms[name] = m
	case *summary:
		r.summaries[name] = m
	case *timer:
		r.timers[name] = m
	}
	return nil
}

func (r *registry) Unregister(name string) bool {
	r.mu.Lock()
	defer r.mu.Unlock()
	deleted := false
	if _, ok := r.counters[name]; ok {
		delete(r.counters, name)
		deleted = true
	}
	if _, ok := r.gauges[name]; ok {
		delete(r.gauges, name)
		deleted = true
	}
	if _, ok := r.histograms[name]; ok {
		delete(r.histograms, name)
		deleted = true
	}
	if _, ok := r.summaries[name]; ok {
		delete(r.summaries, name)
		deleted = true
	}
	if _, ok := r.timers[name]; ok {
		delete(r.timers, name)
		deleted = true
	}
	return deleted
}

func (r *registry) Visit(visitor metrics.MetricVisitor) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	for name, c := range r.counters {
		visitor(name, metrics.TypeCounter, c)
	}
	for name, g := range r.gauges {
		visitor(name, metrics.TypeGauge, g)
	}
	for name, h := range r.histograms {
		visitor(name, metrics.TypeHistogram, h)
	}
	for name, s := range r.summaries {
		visitor(name, metrics.TypeSummary, s)
	}
	for name, t := range r.timers {
		visitor(name, metrics.TypeTimer, t)
	}
}

func (r *registry) WithTags(tags ...metrics.Tag) metrics.Registry { return r }

func (r *registry) Snapshot() metrics.Snapshot {
	r.mu.RLock()
	defer r.mu.RUnlock()
	counters := make(map[string]float64, len(r.counters))
	for k, c := range r.counters {
		counters[k] = c.Value()
	}
	gauges := make(map[string]float64, len(r.gauges))
	for k, g := range r.gauges {
		gauges[k] = g.Value()
	}
	histSnaps := make(map[string]metrics.HistogramSnapshot, len(r.histograms))
	for k, h := range r.histograms {
		histSnaps[k] = h.Snapshot()
	}
	sumSnaps := make(map[string]metrics.SummarySnapshot, len(r.summaries))
	for k, s := range r.summaries {
		sumSnaps[k] = s.Snapshot()
	}
	return &snapshot{counters: counters, gauges: gauges, histograms: histSnaps, summaries: sumSnaps}
}

type snapshot struct {
	counters   map[string]float64
	gauges     map[string]float64
	histograms map[string]metrics.HistogramSnapshot
	summaries  map[string]metrics.SummarySnapshot
}

func (s *snapshot) Counters() map[string]float64                     { return s.counters }
func (s *snapshot) Gauges() map[string]float64                       { return s.gauges }
func (s *snapshot) Histograms() map[string]metrics.HistogramSnapshot { return s.histograms }
func (s *snapshot) Summaries() map[string]metrics.SummarySnapshot    { return s.summaries }

// ensure sort import used
var _ = sort.Float64s
