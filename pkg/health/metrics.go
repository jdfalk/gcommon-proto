// file: pkg/health/metrics.go
package health

import (
	"context"
	"sync"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
)

// MetricsProvider defines the interface for reporting health check metrics.
type MetricsProvider interface {
	// ReportCheckStatus reports a check status.
	ReportCheckStatus(name string, checkType CheckType, status Status, duration time.Duration)

	// ReportCheckError reports a check error.
	ReportCheckError(name string, checkType CheckType, err error)

	// ReportAggregateStatus reports an aggregate check status.
	ReportAggregateStatus(checkType CheckType, status Status, counts map[Status]int)

	// ReportRemediationAttempt reports a remediation attempt.
	ReportRemediationAttempt(name string, attempt int, success bool)
}

// MetricsConfig defines the configuration for health check metrics.
type MetricsConfig struct {
	// Prefix is the prefix for all health check metrics
	Prefix string

	// EnableStatusMetrics enables metrics for health check statuses
	EnableStatusMetrics bool

	// EnableDurationMetrics enables metrics for health check durations
	EnableDurationMetrics bool

	// EnableCountMetrics enables metrics for health check execution counts
	EnableCountMetrics bool

	// DurationBuckets defines the histogram buckets for duration metrics
	DurationBuckets []float64

	// CollectInterval is the interval at which metrics are collected
	CollectInterval time.Duration

	// LabelFilter is a function that can filter or modify metric labels
	LabelFilter func(name string, checkType CheckType, status Status) []metrics.Tag
}

// DefaultMetricsConfig returns the default metrics configuration.
func DefaultMetricsConfig() MetricsConfig {
	return MetricsConfig{
		Prefix:                "health",
		EnableStatusMetrics:   true,
		EnableDurationMetrics: true,
		EnableCountMetrics:    true,
		DurationBuckets:       []float64{0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0},
		CollectInterval:       30 * time.Second,
		LabelFilter: func(name string, checkType CheckType, status Status) []metrics.Tag {
			return []metrics.Tag{
				{Key: "check", Value: name},
				{Key: "type", Value: checkType.String()},
				{Key: "status", Value: status.String()},
			}
		},
	}
}

// MetricsCollector collects metrics for health checks.
type MetricsCollector struct {
	provider        Provider
	metricsProvider metrics.Provider
	config          MetricsConfig

	// Metrics
	statusGauge       metrics.Gauge
	executionCounter  metrics.Counter
	durationHistogram metrics.Histogram
	failureCounter    metrics.Counter
	successCounter    metrics.Counter

	stopCh    chan struct{}
	stoppedCh chan struct{}
}

// NewMetricsCollector creates a new metrics collector for health checks.
func NewMetricsCollector(provider Provider, metricsProvider metrics.Provider, config MetricsConfig) *MetricsCollector {
	prefix := config.Prefix

	collector := &MetricsCollector{
		provider:        provider,
		metricsProvider: metricsProvider,
		config:          config,
		stopCh:          make(chan struct{}),
		stoppedCh:       make(chan struct{}),
	}

	// Create metrics
	if config.EnableStatusMetrics {
		collector.statusGauge = metricsProvider.Gauge(
			prefix+".status",
			metrics.WithDescription("Health check status (0=down, 1=degraded, 2=up, 3=unknown)"),
		)
	}

	if config.EnableCountMetrics {
		collector.executionCounter = metricsProvider.Counter(
			prefix+".executions_total",
			metrics.WithDescription("Total number of health check executions"),
		)

		collector.successCounter = metricsProvider.Counter(
			prefix+".success_total",
			metrics.WithDescription("Total number of successful health check executions"),
		)

		collector.failureCounter = metricsProvider.Counter(
			prefix+".failure_total",
			metrics.WithDescription("Total number of failed health check executions"),
		)
	}

	if config.EnableDurationMetrics {
		collector.durationHistogram = metricsProvider.Histogram(
			prefix+".duration_seconds",
			metrics.WithDescription("Duration of health check executions in seconds"),
			metrics.WithBuckets(config.DurationBuckets),
		)
	}

	return collector
}

// Start starts the metrics collector.
func (c *MetricsCollector) Start(ctx context.Context) error {
	// Register as a health check listener to collect metrics on status changes
	if err := c.provider.AddListener(c); err != nil {
		return err
	}

	// Start periodic metrics collection if an interval is set
	if c.config.CollectInterval > 0 {
		go c.run(ctx)
	}

	return nil
}

// Stop stops the metrics collector.
func (c *MetricsCollector) Stop(ctx context.Context) error {
	close(c.stopCh)

	// Unregister as a health check listener
	if err := c.provider.RemoveListener(c); err != nil {
		return err
	}

	// Wait for collection to stop or context to be done
	select {
	case <-c.stoppedCh:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

// OnStatusChange implements the Listener interface for health status changes.
func (c *MetricsCollector) OnStatusChange(name string, previous, current Result) {
	if c.config.EnableStatusMetrics {
		// Update status metric
		check := current.Check()
		if check != nil {
			labels := c.config.LabelFilter(name, check.Type(), current.Status())
			gauge := c.statusGauge.WithTags(labels...)
			gauge.Set(float64(current.Status()))
		}
	}

	if c.config.EnableCountMetrics {
		// Update execution counters
		check := current.Check()
		if check != nil {
			labels := c.config.LabelFilter(name, check.Type(), current.Status())

			// Update execution counter
			c.executionCounter.WithTags(labels...).Inc()

			// Update success/failure counters
			if current.Status() == StatusUp {
				c.successCounter.WithTags(labels...).Inc()
			} else {
				c.failureCounter.WithTags(labels...).Inc()
			}
		}
	}

	if c.config.EnableDurationMetrics && current.Duration() > 0 {
		// Update duration histogram
		check := current.Check()
		if check != nil {
			labels := c.config.LabelFilter(name, check.Type(), current.Status())
			hist := c.durationHistogram.WithTags(labels...)
			hist.Observe(current.Duration().Seconds())
		}
	}
}

// run is the main loop for periodic metrics collection.
func (c *MetricsCollector) run(ctx context.Context) {
	ticker := time.NewTicker(c.config.CollectInterval)
	defer func() {
		ticker.Stop()
		close(c.stoppedCh)
	}()

	for {
		select {
		case <-c.stopCh:
			return
		case <-ctx.Done():
			return
		case <-ticker.C:
			c.collectMetrics(ctx)
		}
	}
}

// collectMetrics collects metrics for all health checks.
func (c *MetricsCollector) collectMetrics(ctx context.Context) {
	// Run all checks
	result, err := c.provider.CheckAll(ctx)
	if err != nil {
		// Could log an error here
		return
	}

	// Overall status
	if c.config.EnableStatusMetrics {
		c.statusGauge.WithTags(metrics.Tag{Key: "check", Value: "overall"}).Set(float64(result.Status()))
	}

	// Additional metrics could be collected here, such as:
	// - Count of checks by status
	// - Aggregate counts and averages

	// Process results for each child check
	// Note: the listener will also get these individually, this is for cases where
	// the collector was started after some checks have already been executed
	for _, child := range result.Children() {
		check := child.Check()
		if check != nil {
			// Update metrics for this specific check (similar to OnStatusChange)
			name := check.Name()
			labels := c.config.LabelFilter(name, check.Type(), child.Status())

			if c.config.EnableStatusMetrics {
				c.statusGauge.WithTags(labels...).Set(float64(child.Status()))
			}

			if c.config.EnableDurationMetrics && child.Duration() > 0 {
				c.durationHistogram.WithTags(labels...).Observe(child.Duration().Seconds())
			}
		}
	}
}

// metricsListener implements the Listener interface for metrics reporting.
type metricsListener struct {
	provider MetricsProvider
}

// OnStatusChange is called when a health status changes.
func (l *metricsListener) OnStatusChange(name string, previous, current Result) {
	// Skip if there is no meaningful change
	if previous != nil && previous.Status() == current.Status() {
		return
	}

	// Get the check type
	var checkType CheckType = TypeComponent // Default
	if check := current.Check(); check != nil {
		checkType = check.Type()
	}

	// Report status
	l.provider.ReportCheckStatus(name, checkType, current.Status(), current.Duration())

	// Report error if present
	if err := current.Error(); err != nil {
		l.provider.ReportCheckError(name, checkType, err)
	}
}

// BaseMetricsProvider provides a base implementation of MetricsProvider.
type BaseMetricsProvider struct {
	statusCounts     map[CheckType]map[Status]int
	totalChecks      map[CheckType]int
	remediations     map[string]int
	remediationStats map[string]struct {
		Attempts int
		Success  int
		Failures int
	}
	mu sync.RWMutex
}

// NewBaseMetricsProvider creates a new base metrics provider.
func NewBaseMetricsProvider() *BaseMetricsProvider {
	return &BaseMetricsProvider{
		statusCounts: make(map[CheckType]map[Status]int),
		totalChecks:  make(map[CheckType]int),
		remediations: make(map[string]int),
		remediationStats: make(map[string]struct {
			Attempts int
			Success  int
			Failures int
		}),
	}
}

// ReportCheckStatus reports a check status.
func (p *BaseMetricsProvider) ReportCheckStatus(name string, checkType CheckType, status Status, duration time.Duration) {
	p.mu.Lock()
	defer p.mu.Unlock()

	// Initialize status counters if needed
	if _, exists := p.statusCounts[checkType]; !exists {
		p.statusCounts[checkType] = make(map[Status]int)
	}

	// Update status counts
	p.statusCounts[checkType][status]++
	p.totalChecks[checkType]++
}

// ReportCheckError reports a check error.
func (p *BaseMetricsProvider) ReportCheckError(name string, checkType CheckType, err error) {
	// Base implementation does nothing with errors
}

// ReportAggregateStatus reports an aggregate check status.
func (p *BaseMetricsProvider) ReportAggregateStatus(checkType CheckType, status Status, counts map[Status]int) {
	p.mu.Lock()
	defer p.mu.Unlock()

	// Update status counts
	if _, exists := p.statusCounts[checkType]; !exists {
		p.statusCounts[checkType] = make(map[Status]int)
	}

	for s, count := range counts {
		p.statusCounts[checkType][s] = count
	}
}

// ReportRemediationAttempt reports a remediation attempt.
func (p *BaseMetricsProvider) ReportRemediationAttempt(name string, attempt int, success bool) {
	p.mu.Lock()
	defer p.mu.Unlock()

	// Update remediation attempts
	p.remediations[name]++

	// Update remediation stats
	stats, exists := p.remediationStats[name]
	if !exists {
		stats = struct {
			Attempts int
			Success  int
			Failures int
		}{0, 0, 0}
	}

	stats.Attempts++
	if success {
		stats.Success++
	} else {
		stats.Failures++
	}

	p.remediationStats[name] = stats
}

// GetStatusCounts returns the status counts for a check type.
func (p *BaseMetricsProvider) GetStatusCounts(checkType CheckType) map[Status]int {
	p.mu.RLock()
	defer p.mu.RUnlock()

	counts, exists := p.statusCounts[checkType]
	if !exists {
		return make(map[Status]int)
	}

	// Create a copy to avoid concurrent map access
	result := make(map[Status]int, len(counts))
	for k, v := range counts {
		result[k] = v
	}

	return result
}

// GetTotalChecks returns the total number of checks for a check type.
func (p *BaseMetricsProvider) GetTotalChecks(checkType CheckType) int {
	p.mu.RLock()
	defer p.mu.RUnlock()
	return p.totalChecks[checkType]
}

// GetRemediationStats returns remediation statistics.
func (p *BaseMetricsProvider) GetRemediationStats() map[string]struct {
	Attempts int
	Success  int
	Failures int
} {
	p.mu.RLock()
	defer p.mu.RUnlock()

	// Create a copy to avoid concurrent map access
	result := make(map[string]struct {
		Attempts int
		Success  int
		Failures int
	}, len(p.remediationStats))

	for k, v := range p.remediationStats {
		result[k] = v
	}

	return result
}

// EnableMetricsReporting enables metrics reporting for a health provider.
func EnableMetricsReporting(healthProvider Provider, metricsProvider MetricsProvider) error {
	listener := &metricsListener{
		provider: metricsProvider,
	}
	return healthProvider.AddListener(listener)
}

// DisableMetricsReporting disables metrics reporting for a health provider.
func DisableMetricsReporting(healthProvider Provider, metricsProvider MetricsProvider) error {
	// Since we can't directly identify the metrics listener, we'll need to use a custom approach
	// This might require modifying the health provider implementation to support this
	return nil
}
