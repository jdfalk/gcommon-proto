// file: pkg/health/interfaces.go
package health

import (
	"context"
	"net/http"
	"time"
)

// Check defines the interface for health checks.
// A Check represents a specific health verification that can be executed to determine
// the health status of a component, dependency, or the overall system.
type Check interface {
	// Name returns the check's name, which should be unique within a Provider.
	Name() string

	// Type returns the check's type, which categorizes its purpose.
	Type() CheckType

	// Timeout returns the maximum duration the check should run before timing out.
	Timeout() time.Duration

	// Interval returns the recommended interval between check executions.
	Interval() time.Duration

	// Enabled returns whether the check is currently enabled.
	Enabled() bool

	// SetEnabled enables or disables the check.
	SetEnabled(enabled bool)

	// Execute runs the health check and returns the result.
	// The provided context should be respected for cancellation and timeouts.
	// Returns a Result containing the health status and an error if the check execution failed.
	Execute(ctx context.Context) (Result, error)
}

// Remediator defines the interface for checks that support automatic remediation.
// A Remediator can attempt to fix issues detected during a health check execution.
type Remediator interface {
	// Remediate attempts to fix issues detected by the check.
	// The provided Result contains information about the failure that may be useful for remediation.
	// Returns an error if remediation fails or is not possible.
	Remediate(ctx context.Context, result Result) error
}

// CheckFunc is a function that performs a health check.
// The function should return a Result containing the health status and an error if the check execution failed.
type CheckFunc func(ctx context.Context) (Result, error)

// RemediationFunc is a function that performs remediation for a failed health check.
// The function should attempt to fix the issues described in the Result and return an error if remediation fails.
type RemediationFunc func(ctx context.Context, result Result) error

// CheckOption is a function that configures a Check.
// This is used with the functional options pattern to provide flexible configuration of checks.
type CheckOption func(Check) error

// Result defines the interface for health check results.
// A Result represents the outcome of executing a health check and contains status information,
// details, and metadata about the check execution.
type Result interface {
	// Status returns the health status determined by the check.
	Status() Status

	// Error returns any error encountered during the check execution.
	// A nil error does not necessarily mean the check passed; check Status() for the actual health status.
	Error() error

	// Check returns a reference to the Check that produced this result, if available.
	Check() Check

	// Timestamp returns when the check was executed.
	Timestamp() time.Time

	// Duration returns how long the check took to execute.
	Duration() time.Duration

	// Children returns any child results if this Result is composite.
	Children() []Result

	// Details returns additional check-specific information.
	// The contents are arbitrary and determined by each check implementation.
	Details() map[string]interface{}

	// WithError adds an error to this Result and returns the updated Result.
	WithError(err error) Result

	// WithCheck associates this Result with the Check that produced it and returns the updated Result.
	WithCheck(check Check) Result

	// WithDetails adds additional information to this Result and returns the updated Result.
	WithDetails(details map[string]interface{}) Result

	// WithDuration sets how long the check took to execute and returns the updated Result.
	WithDuration(duration time.Duration) Result

	// WithChildren adds child results to this Result and returns the updated Result.
	WithChildren(children []Result) Result

	// AddChild adds a single child Result and returns the updated Result.
	AddChild(child Result) Result

	// WithStatus sets the status for this Result and returns the updated Result.
	WithStatus(status Status) Result
}

// Provider defines the interface for a health check provider.
// A Provider manages a collection of health checks and provides methods to execute them
// and access their results. It serves as the central component of the health checking system.
type Provider interface {
	// Register adds a new check to the provider.
	// The name must be unique within this provider.
	// Returns an error if a check with the same name already exists.
	Register(name string, check Check, options ...CheckOption) error

	// Unregister removes a check from the provider.
	// Returns an error if the check does not exist.
	Unregister(name string) error

	// Get returns a check by name.
	// Returns the check and true if found, or nil and false if not found.
	Get(name string) (Check, bool)

	// CheckAll executes all registered checks and returns an aggregated result.
	// The result's Status is the worst status among all executed checks.
	CheckAll(ctx context.Context) (Result, error)

	// CheckLiveness executes all checks of type TypeLiveness and returns an aggregated result.
	// This is typically used by liveness probes in orchestration systems.
	CheckLiveness(ctx context.Context) (Result, error)

	// CheckReadiness executes all checks of type TypeReadiness and returns an aggregated result.
	// This is typically used by readiness probes in orchestration systems.
	CheckReadiness(ctx context.Context) (Result, error)

	// Handler returns an HTTP handler that exposes health check endpoints.
	// The handler provides endpoints for checking overall health, liveness, readiness, and detailed status.
	Handler() http.Handler

	// Start begins periodic background health checking.
	// Each check is executed at its recommended interval.
	// The provided context controls the overall lifecycle of background checking.
	Start(ctx context.Context) error

	// Stop terminates background health checking.
	// Any in-progress checks will be allowed to complete.
	Stop(ctx context.Context) error

	// AddListener registers a listener to be notified of health status changes.
	// Returns an error if the listener could not be added.
	AddListener(listener Listener) error

	// RemoveListener unregisters a previously added listener.
	// Returns an error if the listener was not found.
	RemoveListener(listener Listener) error
}

// Listener defines the interface for objects that receive health status change notifications.
// Listeners are notified when a check's status changes, allowing for custom handling of health events.
type Listener interface {
	// OnStatusChange is called when a check's status changes.
	// The name parameter identifies which check changed status.
	// The previous and current parameters provide the old and new results.
	OnStatusChange(name string, previous, current Result)
}

// Config defines the configuration options for a health check provider.
type Config struct {
	// Enabled indicates whether the health check system is active (default: true)
	Enabled bool

	// Base path for health endpoints (default: "/")
	Endpoint string

	// Path relative to Endpoint for liveness endpoint (default: "/live")
	LivenessPath string

	// Path relative to Endpoint for readiness endpoint (default: "/ready")
	ReadinessPath string

	// Path relative to Endpoint for detailed health info (default: "/details")
	DetailsPath string

	// Enable the liveness endpoint (default: false)
	EnableLivenessEndpoint bool

	// Enable the readiness endpoint (default: false)
	EnableReadinessEndpoint bool

	// Require authentication for detailed health info (default: false)
	RequireAuthentication bool

	// Authentication header value to check if RequireAuthentication is true (default: "")
	AuthHeader string

	// AuthFunc is called to authenticate requests if RequireAuthentication is true
	// If nil, simple header comparison with AuthHeader is used
	AuthFunc func(r *http.Request) bool

	// DefaultTimeout is the default timeout for health checks that don't specify one (default: 5s)
	DefaultTimeout time.Duration

	// Interval for background health checks (default: 30s)
	CheckInterval time.Duration

	// Log status changes to health checks (default: false)
	LogStatusChanges bool

	// Enable Prometheus metrics for health checks (default: false)
	MetricsEnabled bool
}
