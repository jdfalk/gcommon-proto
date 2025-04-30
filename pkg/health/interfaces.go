// file: pkg/health/interfaces.go
package health

import (
	"context"
	"net/http"
	"time"
)

// Provider represents a health check provider.
type Provider interface {
	// Register registers a health check.
	Register(name string, check Check, options ...CheckOption) error

	// Unregister removes a health check.
	Unregister(name string) error

	// Get retrieves a health check.
	Get(name string) (Check, bool)

	// CheckAll runs all health checks.
	CheckAll(ctx context.Context) (Result, error)

	// CheckLiveness runs liveness checks.
	CheckLiveness(ctx context.Context) (Result, error)

	// CheckReadiness runs readiness checks.
	CheckReadiness(ctx context.Context) (Result, error)

	// Handler returns an HTTP handler for health checks.
	Handler() http.Handler

	// Start starts background health checking.
	Start(ctx context.Context) error

	// Stop stops background health checking.
	Stop(ctx context.Context) error

	// AddListener adds a listener for health status changes.
	AddListener(listener Listener) error

	// RemoveListener removes a listener.
	RemoveListener(listener Listener) error
}

// Check represents a health check.
type Check interface {
	// Execute runs the health check.
	Execute(ctx context.Context) (Result, error)

	// Name returns the check name.
	Name() string

	// Type returns the check type.
	Type() CheckType

	// Timeout returns the check timeout.
	Timeout() time.Duration

	// Interval returns the check interval.
	Interval() time.Duration

	// Enabled returns whether the check is enabled.
	Enabled() bool

	// SetEnabled sets whether the check is enabled.
	SetEnabled(enabled bool)
}

// Result represents a health check result.
type Result interface {
	// Status returns the health status.
	Status() Status

	// Details returns the health details.
	Details() map[string]interface{}

	// Error returns the health check error.
	Error() error

	// Timestamp returns the check timestamp.
	Timestamp() time.Time

	// Duration returns the check duration.
	Duration() time.Duration

	// Check returns the check that produced this result.
	Check() Check

	// Children returns child results.
	Children() []Result

	// WithError sets an error for the result.
	WithError(err error) Result

	// WithDetails adds details to the result.
	WithDetails(details map[string]interface{}) Result
}

// Status represents a health status.
type Status int

const (
	// StatusUp indicates the component is healthy.
	StatusUp Status = iota

	// StatusDown indicates the component is unhealthy.
	StatusDown

	// StatusDegraded indicates the component is partially healthy.
	StatusDegraded

	// StatusUnknown indicates the component health is unknown.
	StatusUnknown
)

// String returns the string representation of the health status.
func (s Status) String() string {
	switch s {
	case StatusUp:
		return "UP"
	case StatusDown:
		return "DOWN"
	case StatusDegraded:
		return "DEGRADED"
	case StatusUnknown:
		return "UNKNOWN"
	default:
		return "UNKNOWN"
	}
}

// CheckType represents a health check type.
type CheckType int

const (
	// TypeLiveness indicates a liveness check.
	TypeLiveness CheckType = iota

	// TypeReadiness indicates a readiness check.
	TypeReadiness

	// TypeComponent indicates a component check.
	TypeComponent

	// TypeDependency indicates a dependency check.
	TypeDependency
)

// String returns the string representation of the check type.
func (t CheckType) String() string {
	switch t {
	case TypeLiveness:
		return "LIVENESS"
	case TypeReadiness:
		return "READINESS"
	case TypeComponent:
		return "COMPONENT"
	case TypeDependency:
		return "DEPENDENCY"
	default:
		return "UNKNOWN"
	}
}

// Listener represents a health status change listener.
type Listener interface {
	// OnStatusChange is called when a health status changes.
	OnStatusChange(name string, previous, current Result)
}

// CheckOption represents an option for a health check.
type CheckOption func(Check) error

// RemediationFunc represents a function that can remediate a failed health check.
type RemediationFunc func(ctx context.Context, result Result) error

// Config represents the health configuration.
type Config struct {
	// Enabled specifies whether health checking is enabled.
	Enabled bool

	// Endpoint is the HTTP endpoint for health checks.
	Endpoint string

	// CheckInterval is the interval for background health checking.
	CheckInterval time.Duration

	// DefaultTimeout is the default timeout for health checks.
	DefaultTimeout time.Duration

	// EnableLivenessEndpoint enables the liveness endpoint.
	EnableLivenessEndpoint bool

	// EnableReadinessEndpoint enables the readiness endpoint.
	EnableReadinessEndpoint bool

	// LivenessPath is the path for liveness checks.
	LivenessPath string

	// ReadinessPath is the path for readiness checks.
	ReadinessPath string

	// MetricsEnabled enables health check metrics.
	MetricsEnabled bool

	// LogStatusChanges indicates whether to log status changes.
	LogStatusChanges bool

	// AutoRemediationEnabled enables automatic remediation.
	AutoRemediationEnabled bool

	// RequireAuthentication requires authentication for detailed health checks.
	RequireAuthentication bool
}

// DefaultConfig returns the default health configuration.
func DefaultConfig() Config {
	return Config{
		Enabled:               true,
		Endpoint:              "/health",
		CheckInterval:         30 * time.Second,
		DefaultTimeout:        5 * time.Second,
		EnableLivenessEndpoint: true,
		EnableReadinessEndpoint: true,
		LivenessPath:          "/live",
		ReadinessPath:         "/ready",
		MetricsEnabled:        true,
		LogStatusChanges:      true,
		AutoRemediationEnabled: false,
		RequireAuthentication: false,
	}
}

// CheckFunc is a function that implements the Check interface.
type CheckFunc func(ctx context.Context) (Result, error)

// Execute runs the health check function.
func (f CheckFunc) Execute(ctx context.Context) (Result, error) {
	return f(ctx)
}
