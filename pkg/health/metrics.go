// file: pkg/health/metrics.go
package health

import (
	"context"
	"sync"
	"time"
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
