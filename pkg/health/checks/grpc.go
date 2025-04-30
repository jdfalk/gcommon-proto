// file: pkg/health/checks/grpc.go
package checks

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/connectivity"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/health/grpc_health_v1"

	"github.com/jdfalk/gcommon/pkg/health"
)

// GRPCCheck is a health check that verifies the health of a gRPC service.
// It uses the standard gRPC health checking protocol defined in
// https://github.com/grpc/grpc/blob/master/doc/health-checking.md
type GRPCCheck struct {
	*health.BaseCheck
	target          string           // Address of the gRPC server (host:port)
	serviceName     string           // Optional name of the service to check
	conn            *grpc.ClientConn // Connection to the gRPC server
	timeout         time.Duration    // Timeout for the health check
	dialOptions     []grpc.DialOption // Options for establishing the connection
	healthClient    grpc_health_v1.HealthClient
	useStandardProto bool // Whether to use the standard gRPC health protocol
}

// GRPCCheckOption represents an option for a gRPC health check.
type GRPCCheckOption func(*GRPCCheck)

// NewGRPCCheck creates a new gRPC dependency health check.
// By default, it uses the standard gRPC health checking protocol.
// The target parameter should be in the format "host:port".
func NewGRPCCheck(target string, options ...GRPCCheckOption) *GRPCCheck {
	c := &GRPCCheck{
		target:          target,
		timeout:         5 * time.Second,
		useStandardProto: true,
		dialOptions:     []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())},
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("grpc-"+target, health.TypeDependency, c.timeout, 60*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the gRPC health check.
func (c *GRPCCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()
	details := map[string]interface{}{
		"target": c.target,
	}

	if c.serviceName != "" {
		details["service"] = c.serviceName
	}

	// Initialize the connection if it doesn't exist
	if err := c.initConnection(ctx); err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("connection failed: %w", err)).
			WithDuration(time.Since(startTime)).
			WithDetails(details), nil
	}

	// Check the connection state
	state := c.conn.GetState()
	if state != connectivity.Ready && state != connectivity.Idle {
		details["state"] = state.String()
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("connection state: %s", state.String())).
			WithDuration(time.Since(startTime)).
			WithDetails(details), nil
	}

	// If using standard health protocol, perform a health check
	if c.useStandardProto {
		checkCtx, cancel := context.WithTimeout(ctx, c.timeout)
		defer cancel()

		resp, err := c.healthClient.Check(checkCtx, &grpc_health_v1.HealthCheckRequest{
			Service: c.serviceName,
		})

		if err != nil {
			details["error"] = err.Error()
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("health check failed: %w", err)).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}

		details["status"] = resp.Status.String()

		switch resp.Status {
		case grpc_health_v1.HealthCheckResponse_SERVING:
			return health.NewResult(health.StatusUp).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		case grpc_health_v1.HealthCheckResponse_NOT_SERVING:
			return health.NewResult(health.StatusDown).
				WithError(fmt.Errorf("service not serving")).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		default:
			return health.NewResult(health.StatusUnknown).
				WithError(fmt.Errorf("unknown service status: %s", resp.Status.String())).
				WithDuration(time.Since(startTime)).
				WithDetails(details), nil
		}
	}

	// If we're not using the standard health protocol, just having a valid connection is enough
	return health.NewResult(health.StatusUp).
		WithDuration(time.Since(startTime)).
		WithDetails(details), nil
}

// initConnection initializes the gRPC connection and health client if not already done.
func (c *GRPCCheck) initConnection(ctx context.Context) error {
	var err error

	if c.conn == nil {
		dialCtx, cancel := context.WithTimeout(ctx, c.timeout)
		defer cancel()

		c.conn, err = grpc.DialContext(dialCtx, c.target, c.dialOptions...)
		if err != nil {
			return err
		}

		if c.useStandardProto {
			c.healthClient = grpc_health_v1.NewHealthClient(c.conn)
		}
	}

	return nil
}

// Close closes the gRPC connection.
func (c *GRPCCheck) Close() error {
	if c.conn != nil {
		err := c.conn.Close()
		c.conn = nil
		c.healthClient = nil
		return err
	}
	return nil
}

// WithService sets the service name to check.
func WithService(service string) GRPCCheckOption {
	return func(c *GRPCCheck) {
		c.serviceName = service
	}
}

// WithGRPCTimeout sets the timeout for the gRPC health check.
func WithGRPCTimeout(timeout time.Duration) GRPCCheckOption {
	return func(c *GRPCCheck) {
		c.timeout = timeout
	}
}

// WithDialOptions adds gRPC dial options to use when establishing the connection.
func WithDialOptions(options ...grpc.DialOption) GRPCCheckOption {
	return func(c *GRPCCheck) {
		c.dialOptions = append(c.dialOptions, options...)
	}
}

// WithTLS configures the check to use TLS.
func WithTLS() GRPCCheckOption {
	return func(c *GRPCCheck) {
		// Replace the insecure credentials with system certificates
		for i, opt := range c.dialOptions {
			if _, ok := opt.(grpc.TransportCredentialsOption); ok {
				c.dialOptions = append(c.dialOptions[:i], c.dialOptions[i+1:]...)
				break
			}
		}
		// Add TLS credentials
		c.dialOptions = append(c.dialOptions, grpc.WithTransportCredentials(
			// Use system certificates
			grpc.WithSystemCertPool(),
		))
	}
}

// WithoutHealthProto disables the use of the standard gRPC health checking protocol.
// In this mode, the check will only verify that a connection can be established.
func WithoutHealthProto() GRPCCheckOption {
	return func(c *GRPCCheck) {
		c.useStandardProto = false
	}
}
