// file: pkg/health/metrics_prometheus.go
package health

import (
	"fmt"
	"time"

	"github.com/prometheus/client_golang/prometheus"
)

// PrometheusMetricsProvider implements the MetricsProvider interface for Prometheus.
type PrometheusMetricsProvider struct {
	*BaseMetricsProvider
	registry           prometheus.Registerer
	namespace          string
	checkStatusGauge   *prometheus.GaugeVec
	checkDurationHist  *prometheus.HistogramVec
	checkErrorCounter  *prometheus.CounterVec
	remediationCounter *prometheus.CounterVec
}

// NewPrometheusMetricsProvider creates a new Prometheus metrics provider.
func NewPrometheusMetricsProvider(registry prometheus.Registerer, namespace string) *PrometheusMetricsProvider {
	if namespace == "" {
		namespace = "health"
	}

	provider := &PrometheusMetricsProvider{
		BaseMetricsProvider: NewBaseMetricsProvider(),
		registry:            registry,
		namespace:           namespace,
	}

	// Initialize metrics
	provider.initMetrics()

	return provider
}

// initMetrics initializes Prometheus metrics.
func (p *PrometheusMetricsProvider) initMetrics() {
	// Check status gauge
	p.checkStatusGauge = prometheus.NewGaugeVec(
		prometheus.GaugeOpts{
			Namespace: p.namespace,
			Name:      "check_status",
			Help:      "Health check status (0=DOWN, 1=DEGRADED, 2=UP, 3=UNKNOWN).",
		},
		[]string{"name", "type"},
	)

	// Check duration histogram
	p.checkDurationHist = prometheus.NewHistogramVec(
		prometheus.HistogramOpts{
			Namespace: p.namespace,
			Name:      "check_duration_seconds",
			Help:      "Health check duration in seconds.",
			Buckets:   prometheus.DefBuckets,
		},
		[]string{"name", "type"},
	)

	// Check error counter
	p.checkErrorCounter = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Namespace: p.namespace,
			Name:      "check_errors_total",
			Help:      "Total number of health check errors.",
		},
		[]string{"name", "type"},
	)

	// Remediation counter
	p.remediationCounter = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Namespace: p.namespace,
			Name:      "remediation_attempts_total",
			Help:      "Total number of remediation attempts.",
		},
		[]string{"name", "success"},
	)

	// Register metrics with Prometheus
	p.registry.MustRegister(
		p.checkStatusGauge,
		p.checkDurationHist,
		p.checkErrorCounter,
		p.remediationCounter,
	)
}

// ReportCheckStatus reports a check status.
func (p *PrometheusMetricsProvider) ReportCheckStatus(name string, checkType CheckType, status Status, duration time.Duration) {
	// Forward to base implementation
	p.BaseMetricsProvider.ReportCheckStatus(name, checkType, status, duration)

	// Convert status to numeric value
	var statusValue float64
	switch status {
	case StatusUp:
		statusValue = 2
	case StatusDown:
		statusValue = 0
	case StatusDegraded:
		statusValue = 1
	default:
		statusValue = 3 // Unknown
	}

	// Update Prometheus metrics
	p.checkStatusGauge.WithLabelValues(name, checkType.String()).Set(statusValue)
	p.checkDurationHist.WithLabelValues(name, checkType.String()).Observe(duration.Seconds())
}

// ReportCheckError reports a check error.
func (p *PrometheusMetricsProvider) ReportCheckError(name string, checkType CheckType, err error) {
	// Forward to base implementation
	p.BaseMetricsProvider.ReportCheckError(name, checkType, err)

	// Update Prometheus metrics
	p.checkErrorCounter.WithLabelValues(name, checkType.String()).Inc()
}

// ReportRemediationAttempt reports a remediation attempt.
func (p *PrometheusMetricsProvider) ReportRemediationAttempt(name string, attempt int, success bool) {
	// Forward to base implementation
	p.BaseMetricsProvider.ReportRemediationAttempt(name, attempt, success)

	// Update Prometheus metrics
	successLabel := fmt.Sprintf("%t", success)
	p.remediationCounter.WithLabelValues(name, successLabel).Inc()
}

// ReportAggregateStatus reports an aggregate check status.
// This implementation uses the base implementation without additional Prometheus metrics.
func (p *PrometheusMetricsProvider) ReportAggregateStatus(checkType CheckType, status Status, counts map[Status]int) {
	// Forward to base implementation
	p.BaseMetricsProvider.ReportAggregateStatus(checkType, status, counts)

	// Do not add Prometheus metrics for aggregate status
	// as this would cause duplication with individual check metrics
}
