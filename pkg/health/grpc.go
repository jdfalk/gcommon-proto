// file: pkg/health/grpc.go
package health

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	proto "github.com/jdfalk/gcommon/pkg/health/proto"
)

// GRPCServer implements the gRPC health service.
// It serves as a bridge between the Provider interface and gRPC service definitions,
// allowing health checks to be exposed via gRPC.
type GRPCServer struct {
	proto.UnimplementedHealthServiceServer // Required for forward compatibility
	provider Provider
}

// NewGRPCServer creates a new gRPC health server using the given provider.
//
// Parameters:
//   - provider: The health check provider that contains all registered checks
//
// Returns:
//   - A GRPCServer instance that can be registered with a gRPC server
func NewGRPCServer(provider Provider) *GRPCServer {
	return &GRPCServer{provider: provider}
}

// Register registers the gRPC health service with a gRPC server.
//
// Parameters:
//   - server: The gRPC server to register with
func (s *GRPCServer) Register(server *grpc.Server) {
	proto.RegisterHealthServiceServer(server, s)
}

// Check performs a health check and returns a simple health status.
// This method implements the CheckRequest RPC defined in the health.proto file.
//
// Parameters:
//   - ctx: The request context which can carry deadlines, cancellation signals, etc.
//   - req: The CheckRequest message which may specify which type of check to perform
//
// Returns:
//   - A CheckResponse containing the overall health status
//   - An error if the check failed to execute
func (s *GRPCServer) Check(ctx context.Context, req *proto.HealthCheckRequest) (*proto.HealthCheckResponse, error) {
	var result Result
	var err error

	// Default to checking all health checks if no specific service is requested
	if req.Service == "" {
		result, err = s.provider.CheckAll(ctx)
	} else if req.Service == "liveness" {
		result, err = s.provider.CheckLiveness(ctx)
	} else if req.Service == "readiness" {
		result, err = s.provider.CheckReadiness(ctx)
	} else {
		// Look for a specific check by name
		check, exists := s.provider.Get(req.Service)
		if !exists || check == nil {
			return nil, status.Errorf(codes.NotFound, "check not found: %s", req.Service)
		}
		result, err = check.Execute(ctx)
	}

	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to perform health check: %v", err)
	}

	return &proto.HealthCheckResponse{
		Status:    toProtoServingStatus(result.Status()),
		Timestamp: time.Now().Format(time.RFC3339),
		Details:   convertDetailsToMap(result.Details()),
	}, nil
}

// CheckAll performs all health checks and returns detailed information.
// This method implements the CheckAll RPC defined in the health.proto file.
//
// Parameters:
//   - ctx: The request context which can carry deadlines, cancellation signals, etc.
//   - req: The CheckAllRequest message which specifies options for the checks
//
// Returns:
//   - A CheckAllResponse containing comprehensive health information
//   - An error if the checks failed to execute
func (s *GRPCServer) CheckAll(ctx context.Context, req *proto.HealthCheckAllRequest) (*proto.HealthCheckAllResponse, error) {
	var result Result
	var err error

	if len(req.Types) > 0 {
		// Filter checks by type - this would need custom implementation
		// For now, we'll just use the default check all behavior
		result, err = s.provider.CheckAll(ctx)
	} else {
		result, err = s.provider.CheckAll(ctx)
	}

	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to perform health checks: %v", err)
	}

	resp := &proto.HealthCheckAllResponse{
		Status:    toProtoServingStatus(result.Status()),
		Timestamp: time.Now().Format(time.RFC3339),
		Results:   make(map[string]*proto.HealthCheckResult),
	}

	// Add check details for all children if requested
	if req.IncludeDetails {
		for _, child := range result.Children() {
			if child.Check() != nil {
				checkInfo := resultToHealthCheckResult(child)
				resp.Results[child.Check().Name()] = checkInfo
			}
		}
	}

	return resp, nil
}

// Watch establishes a stream to monitor health status changes.
// This method implements the Watch streaming RPC defined in the health.proto file.
//
// Parameters:
//   - req: The WatchRequest message which specifies what type of health changes to monitor
//   - stream: The server stream for sending health updates
//
// Returns:
//   - An error if the watch operation failed
func (s *GRPCServer) Watch(req *proto.HealthCheckRequest, stream grpc.ServerStreamingServer[proto.HealthCheckResponse]) error {
	ctx := stream.Context()

	// Create a channel to receive health status updates
	updateCh := make(chan Result, 10)
	doneCh := make(chan struct{})

	// Create a listener that will forward health status changes to our channel
	listener := &watchListener{
		updateCh:  updateCh,
		service:   req.Service,
	}

	// Add the listener to the provider
	if err := s.provider.AddListener(listener); err != nil {
		return status.Errorf(codes.Internal, "failed to register health listener: %v", err)
	}

	// Make sure to remove the listener when done
	defer func() {
		s.provider.RemoveListener(listener)
		close(doneCh)
	}()

	// Perform an initial check and send it
	var result Result
	var err error

	if req.Service == "" {
		result, err = s.provider.CheckAll(ctx)
	} else if req.Service == "liveness" {
		result, err = s.provider.CheckLiveness(ctx)
	} else if req.Service == "readiness" {
		result, err = s.provider.CheckReadiness(ctx)
	} else {
		// Look for a specific check by name
		check, exists := s.provider.Get(req.Service)
		if !exists || check == nil {
			return status.Errorf(codes.NotFound, "check not found: %s", req.Service)
		}
		result, err = check.Execute(ctx)
	}

	if err != nil {
		return status.Errorf(codes.Internal, "failed to perform initial health check: %v", err)
	}

	// Send the initial status
	if err := stream.Send(&proto.HealthCheckResponse{
		Status:    toProtoServingStatus(result.Status()),
		Timestamp: time.Now().Format(time.RFC3339),
		Details:   convertDetailsToMap(result.Details()),
	}); err != nil {
		return status.Errorf(codes.Internal, "failed to send initial health status: %v", err)
	}

	// Process status updates
	for {
		select {
		case result := <-updateCh:
			// Send the updated status
			if err := stream.Send(&proto.HealthCheckResponse{
				Status:    toProtoServingStatus(result.Status()),
				Timestamp: time.Now().Format(time.RFC3339),
				Details:   convertDetailsToMap(result.Details()),
			}); err != nil {
				return status.Errorf(codes.Internal, "failed to send health status update: %v", err)
			}
		case <-ctx.Done():
			// Client disconnected or context was cancelled
			return status.FromContextError(ctx.Err()).Err()
		}
	}
}

// watchListener implements the Listener interface for streaming health updates.
type watchListener struct {
	updateCh  chan Result
	service   string
	lastSent  time.Time
}

// OnStatusChange processes health status changes and sends them to the update channel.
// Implements the Listener interface.
//
// Parameters:
//   - name: The name of the check that changed status
//   - previous: The previous result of the check
//   - current: The current result of the check
func (l *watchListener) OnStatusChange(name string, previous, current Result) {
	// Rate limit updates to at most one per second
	if time.Since(l.lastSent) < time.Second {
		return
	}

	// Only send updates for the checks we're watching
	if l.service != "" && l.service != name && l.service != "all" {
		// Get the check to determine its type
		check := current.Check()
		if check == nil {
			return
		}

		// Filter by service name
		if (l.service == "liveness" && check.Type() != TypeLiveness) ||
			(l.service == "readiness" && check.Type() != TypeReadiness) {
			return
		}
	}

	// Send the update if the channel isn't full (non-blocking)
	select {
	case l.updateCh <- current:
		l.lastSent = time.Now()
	default:
		// Channel is full, skip this update
	}
}

// toProtoServingStatus converts a health.Status to a proto.ServingStatus.
//
// Parameters:
//   - status: The internal health status to convert
//
// Returns:
//   - The corresponding protobuf status enum value
func toProtoServingStatus(status Status) proto.ServingStatus {
	switch status {
	case StatusUp:
		return proto.ServingStatus_SERVING
	case StatusDown:
		return proto.ServingStatus_NOT_SERVING
	case StatusDegraded:
		return proto.ServingStatus_SERVING_DEGRADED
	default:
		return proto.ServingStatus_UNKNOWN
	}
}

// convertDetailsToMap converts the details map to a map of strings.
//
// Parameters:
//   - details: The details map from the result
//
// Returns:
//   - A map of string values
func convertDetailsToMap(details map[string]interface{}) map[string]string {
	if details == nil {
		return nil
	}

	result := make(map[string]string)
	for k, v := range details {
		if v != nil {
			result[k] = fmt.Sprintf("%v", v)
		}
	}
	return result
}

// resultToHealthCheckResult converts a health.Result to a proto.HealthCheckResult.
//
// Parameters:
//   - result: The health check result to convert
//
// Returns:
//   - A HealthCheckResult protobuf message containing details from the result
func resultToHealthCheckResult(result Result) *proto.HealthCheckResult {
	checkType := proto.CheckType_TYPE_UNSPECIFIED
	if result.Check() != nil {
		switch result.Check().Type() {
		case TypeLiveness:
			checkType = proto.CheckType_LIVENESS
		case TypeReadiness:
			checkType = proto.CheckType_READINESS
		case TypeComponent:
			checkType = proto.CheckType_COMPONENT
		case TypeDependency:
			checkType = proto.CheckType_DEPENDENCY
		}
	}

	info := &proto.HealthCheckResult{
		Status:    toProtoServingStatus(result.Status()),
		Type:      checkType,
		Timestamp: time.Now().Format(time.RFC3339),
		Details:   convertDetailsToMap(result.Details()),
		Children:  make(map[string]*proto.HealthCheckResult),
	}

	// Add error if present
	if err := result.Error(); err != nil {
		info.Error = err.Error()
	}

	// Add duration if available
	duration := result.Duration()
	if duration > 0 {
		info.DurationMs = int64(duration / time.Millisecond)
	}

	// Process children recursively
	for _, child := range result.Children() {
		if child.Check() != nil {
			childResult := resultToHealthCheckResult(child)
			info.Children[child.Check().Name()] = childResult
		}
	}

	return info
}
