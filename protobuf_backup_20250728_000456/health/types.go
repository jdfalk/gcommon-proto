// file: pkg/health/types.go
package health

import (
	"fmt"
	"time"

	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
)

// Type aliases for protobuf enums to maintain Go API compatibility
type (
	// Status represents the health status using protobuf enum
	Status = healthpb.ServingStatus

	// CheckType represents the type of health check using protobuf enum
	CheckType = healthpb.CheckType
)

// Status constants using protobuf values
const (
	StatusUnknown  = healthpb.ServingStatus_UNKNOWN
	StatusUp       = healthpb.ServingStatus_SERVING
	StatusDown     = healthpb.ServingStatus_NOT_SERVING
	StatusDegraded = healthpb.ServingStatus_SERVING_DEGRADED
)

// CheckType constants using protobuf values
const (
	TypeUnspecified = healthpb.CheckType_TYPE_UNSPECIFIED
	TypeLiveness    = healthpb.CheckType_LIVENESS
	TypeReadiness   = healthpb.CheckType_READINESS
	TypeStartup     = healthpb.CheckType_STARTUP
	TypeComponent   = healthpb.CheckType_COMPONENT
	TypeDependency  = healthpb.CheckType_DEPENDENCY
)

// HealthConfig represents health configuration using protobuf message
type HealthConfig = *healthpb.HealthConfig

// RemediationDetails represents remediation details using protobuf message
type RemediationDetails = *healthpb.RemediationDetails

// NewHealthConfig creates a new health configuration with default values
func NewHealthConfig() HealthConfig {
	return &healthpb.HealthConfig{
		Enabled:                 true,
		Endpoint:                "/health",
		LivenessPath:            "/live",
		ReadinessPath:           "/ready",
		DetailsPath:             "/details",
		EnableLivenessEndpoint:  true,
		EnableReadinessEndpoint: true,
		RequireAuthentication:   false,
		DefaultTimeoutMs:        5000,  // 5 seconds
		CheckIntervalMs:         30000, // 30 seconds
		LogStatusChanges:        false,
		MetricsEnabled:          false,
	}
}

// DefaultHealthConfig returns the default health configuration
func DefaultHealthConfig() HealthConfig {
	return NewHealthConfig()
}

// Helper functions for HealthConfig

// GetDefaultTimeoutFromConfig returns the default timeout as a time.Duration
func GetDefaultTimeoutFromConfig(c HealthConfig) time.Duration {
	return time.Duration(c.DefaultTimeoutMs) * time.Millisecond
}

// GetCheckIntervalFromConfig returns the check interval as a time.Duration
func GetCheckIntervalFromConfig(c HealthConfig) time.Duration {
	return time.Duration(c.CheckIntervalMs) * time.Millisecond
}

// SetDefaultTimeoutInConfig sets the default timeout for health checks
func SetDefaultTimeoutInConfig(c HealthConfig, d time.Duration) {
	c.DefaultTimeoutMs = int64(d.Milliseconds())
}

// SetCheckIntervalInConfig sets the check interval for background checks
func SetCheckIntervalInConfig(c HealthConfig, d time.Duration) {
	c.CheckIntervalMs = int64(d.Milliseconds())
}

// Helper functions for RemediationDetails

// NewRemediationDetails creates a new remediation details instance
func NewRemediationDetails(checkName string, attempt int32, success bool) RemediationDetails {
	return &healthpb.RemediationDetails{
		CheckName:    checkName,
		AttemptCount: attempt,
		Success:      success,
		Timestamp:    time.Now().Format(time.RFC3339),
		Error:        "",
	}
}

// SetRemediationError sets the remediation error
func SetRemediationError(r RemediationDetails, err error) {
	if err != nil {
		r.Error = err.Error()
		r.Success = false
	}
}

// resultImpl implements the Result interface using protobuf as the underlying data structure
type resultImpl struct {
	pb       *healthpb.HealthCheckResult
	err      error
	check    Check
	children []Result
}

// NewResultFromProtobuf creates a new Result implementation backed by protobuf
func NewResultFromProtobuf(status Status) Result {
	return &resultImpl{
		pb: &healthpb.HealthCheckResult{
			Status:    status,
			Timestamp: time.Now().Format(time.RFC3339),
			Details:   make(map[string]string),
		},
		children: make([]Result, 0),
	}
}

// Status returns the health status
func (r *resultImpl) Status() Status {
	return r.pb.Status
}

// Error returns any error encountered during the check execution
func (r *resultImpl) Error() error {
	return r.err
}

// Check returns the Check that produced this result
func (r *resultImpl) Check() Check {
	return r.check
}

// Timestamp returns when the check was executed
func (r *resultImpl) Timestamp() time.Time {
	if t, err := time.Parse(time.RFC3339, r.pb.Timestamp); err == nil {
		return t
	}
	return time.Time{}
}

// Duration returns how long the check took to execute
func (r *resultImpl) Duration() time.Duration {
	return time.Duration(r.pb.DurationMs) * time.Millisecond
}

// Children returns any child results
func (r *resultImpl) Children() []Result {
	return r.children
}

// Details returns additional check-specific information
func (r *resultImpl) Details() map[string]interface{} {
	details := make(map[string]interface{})
	for k, v := range r.pb.Details {
		details[k] = v
	}
	return details
}

// WithError adds an error to this Result
func (r *resultImpl) WithError(err error) Result {
	r.err = err
	if err != nil {
		r.pb.Error = err.Error()
	}
	return r
}

// WithCheck associates this Result with the Check that produced it
func (r *resultImpl) WithCheck(check Check) Result {
	r.check = check
	return r
}

// WithDetails adds additional information to this Result
func (r *resultImpl) WithDetails(details map[string]interface{}) Result {
	if r.pb.Details == nil {
		r.pb.Details = make(map[string]string)
	}
	for k, v := range details {
		r.pb.Details[k] = fmt.Sprintf("%v", v)
	}
	return r
}

// WithDuration sets how long the check took to execute
func (r *resultImpl) WithDuration(duration time.Duration) Result {
	r.pb.DurationMs = int64(duration.Milliseconds())
	return r
}

// WithChildren adds child results to this Result
func (r *resultImpl) WithChildren(children []Result) Result {
	r.children = children
	return r
}

// AddChild adds a single child Result
func (r *resultImpl) AddChild(child Result) Result {
	r.children = append(r.children, child)
	return r
}

// WithStatus sets the status for this Result
func (r *resultImpl) WithStatus(status Status) Result {
	r.pb.Status = status
	return r
}

// GetProtobuf returns the underlying protobuf message for serialization
func (r *resultImpl) GetProtobuf() *healthpb.HealthCheckResult {
	return r.pb
}
