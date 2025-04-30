// file: pkg/health/result.go
package health

import (
	"time"
)

// healthResult implements the Result interface.
type healthResult struct {
	status    Status
	details   map[string]interface{}
	err       error
	timestamp time.Time
	duration  time.Duration
	check     Check
	children  []Result
}

// NewResult creates a new health check result with the given status.
func NewResult(status Status) Result {
	return &healthResult{
		status:    status,
		details:   make(map[string]interface{}),
		timestamp: time.Now(),
	}
}

// Status returns the health status.
func (r *healthResult) Status() Status {
	return r.status
}

// Details returns the health details.
func (r *healthResult) Details() map[string]interface{} {
	return r.details
}

// Error returns the health check error.
func (r *healthResult) Error() error {
	return r.err
}

// Timestamp returns the check timestamp.
func (r *healthResult) Timestamp() time.Time {
	return r.timestamp
}

// Duration returns the check duration.
func (r *healthResult) Duration() time.Duration {
	return r.duration
}

// Check returns the check that produced this result.
func (r *healthResult) Check() Check {
	return r.check
}

// Children returns child results.
func (r *healthResult) Children() []Result {
	return r.children
}

// WithError sets an error for the result.
func (r *healthResult) WithError(err error) Result {
	r.err = err
	return r
}

// WithDetails adds details to the result.
func (r *healthResult) WithDetails(details map[string]interface{}) Result {
	for k, v := range details {
		r.details[k] = v
	}
	return r
}

// WithCheck sets the check that produced this result.
func (r *healthResult) WithCheck(check Check) Result {
	r.check = check
	return r
}

// WithDuration sets the check duration.
func (r *healthResult) WithDuration(duration time.Duration) Result {
	r.duration = duration
	return r
}

// WithChildren sets child results.
func (r *healthResult) WithChildren(children []Result) Result {
	r.children = children
	return r
}

// AddChild adds a child result.
func (r *healthResult) AddChild(child Result) Result {
	r.children = append(r.children, child)
	return r
}

// ComputeAggregateStatus computes the aggregate status from child results.
// The aggregation logic is:
// - If any child is DOWN, the aggregate is DOWN
// - If any child is DEGRADED, the aggregate is DEGRADED
// - If any child is UNKNOWN (and none are DOWN or DEGRADED), the aggregate is UNKNOWN
// - Otherwise, the aggregate is UP
func ComputeAggregateStatus(results []Result) Status {
	if len(results) == 0 {
		return StatusUnknown
	}

	hasUnknown := false
	for _, r := range results {
		switch r.Status() {
		case StatusDown:
			return StatusDown
		case StatusDegraded:
			return StatusDegraded
		case StatusUnknown:
			hasUnknown = true
		}
	}

	if hasUnknown {
		return StatusUnknown
	}
	return StatusUp
}
