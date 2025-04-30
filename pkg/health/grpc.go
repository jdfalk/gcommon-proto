// file: pkg/health/grpc.go
package health

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/types/known/timestamppb"

	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
)

// GRPCServer implements the gRPC health service.
// It serves as a bridge between the Provider interface and gRPC service definitions,
// allowing health checks to be exposed via gRPC.
type GRPCServer struct {
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
	healthpb.RegisterHealthServiceServer(server, s)
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
func (s *GRPCServer) Check(ctx context.Context, req *healthpb.CheckRequest) (*healthpb.CheckResponse, error) {
	var result Result
	var err error

	switch req.Type {
	case healthpb.CheckType_LIVENESS:
		result, err = s.provider.CheckLiveness(ctx)
	case healthpb.CheckType_READINESS:
		result, err = s.provider.CheckReadiness(ctx)
	default:
		result, err = s.provider.CheckAll(ctx)
	}

	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to perform health check: %v", err)
	}

	return &healthpb.CheckResponse{
		Status:    toProtoStatus(result.Status()),
		Timestamp: timestamppb.New(result.Timestamp()),
	}, nil
}

// CheckDetailed performs a health check and returns detailed information.
// This method implements the CheckDetailedRequest RPC defined in the health.proto file.
//
// Parameters:
//   - ctx: The request context which can carry deadlines, cancellation signals, etc.
//   - req: The CheckDetailedRequest message which may specify which type of check to perform
//
// Returns:
//   - A CheckDetailedResponse containing comprehensive health information
//   - An error if the check failed to execute
func (s *GRPCServer) CheckDetailed(ctx context.Context, req *healthpb.CheckDetailedRequest) (*healthpb.CheckDetailedResponse, error) {
	var result Result
	var err error

	switch req.Type {
	case healthpb.CheckType_LIVENESS:
		result, err = s.provider.CheckLiveness(ctx)
	case healthpb.CheckType_READINESS:
		result, err = s.provider.CheckReadiness(ctx)
	default:
		result, err = s.provider.CheckAll(ctx)
	}

	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to perform health check: %v", err)
	}

	resp := &healthpb.CheckDetailedResponse{
		Status:     toProtoStatus(result.Status()),
		Timestamp:  timestamppb.New(result.Timestamp()),
		StatusInfo: resultToStatusInfo(result),
		Checks:     make(map[string]*healthpb.CheckInfo),
	}

	// Add check details for all children
	for _, child := range result.Children() {
		if child.Check() != nil {
			checkInfo := resultToCheckInfo(child)
			resp.Checks[child.Check().Name()] = checkInfo
		}
	}

	return resp, nil
}

// Watch establishes a stream to monitor health status changes.
// This method implements the WatchRequest streaming RPC defined in the health.proto file.
//
// Parameters:
//   - req: The WatchRequest message which specifies what type of health changes to monitor
//   - stream: The server stream for sending health updates
//
// Returns:
//   - An error if the watch operation failed
func (s *GRPCServer) Watch(req *healthpb.WatchRequest, stream healthpb.HealthService_WatchServer) error {
	ctx := stream.Context()

	// Create a channel to receive health status updates
	updateCh := make(chan Result, 10)
	doneCh := make(chan struct{})

	// Create a listener that will forward health status changes to our channel
	listener := &watchListener{
		updateCh:  updateCh,
		watchType: req.Type,
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

	switch req.Type {
	case healthpb.CheckType_LIVENESS:
		result, err = s.provider.CheckLiveness(ctx)
	case healthpb.CheckType_READINESS:
		result, err = s.provider.CheckReadiness(ctx)
	default:
		result, err = s.provider.CheckAll(ctx)
	}

	if err != nil {
		return status.Errorf(codes.Internal, "failed to perform initial health check: %v", err)
	}

	// Send the initial status
	if err := stream.Send(&healthpb.WatchResponse{
		Status:    toProtoStatus(result.Status()),
		Timestamp: timestamppb.New(result.Timestamp()),
	}); err != nil {
		return status.Errorf(codes.Internal, "failed to send initial health status: %v", err)
	}

	// Process status updates
	for {
		select {
		case result := <-updateCh:
			// Send the updated status
			if err := stream.Send(&healthpb.WatchResponse{
				Status:    toProtoStatus(result.Status()),
				Timestamp: timestamppb.New(result.Timestamp()),
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
	watchType healthpb.CheckType
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

	// Only send updates for the types we're watching
	// For ALL type, we send all updates
	if l.watchType != healthpb.CheckType_ALL {
		// Get the check to determine its type
		check := current.Check()
		if check == nil {
			return
		}

		// Filter by check type
		checkType := check.Type()
		if (l.watchType == healthpb.CheckType_LIVENESS && checkType != TypeLiveness) ||
			(l.watchType == healthpb.CheckType_READINESS && checkType != TypeReadiness) {
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

// toProtoStatus converts a health.Status to a healthpb.Status.
//
// Parameters:
//   - status: The internal health status to convert
//
// Returns:
//   - The corresponding protobuf status enum value
func toProtoStatus(status Status) healthpb.Status {
	switch status {
	case StatusUp:
		return healthpb.Status_UP
	case StatusDown:
		return healthpb.Status_DOWN
	case StatusDegraded:
		return healthpb.Status_DEGRADED
	default:
		return healthpb.Status_UNKNOWN
	}
}

// resultToStatusInfo converts a health.Result to a healthpb.StatusInfo.
//
// Parameters:
//   - result: The health check result to convert
//
// Returns:
//   - A StatusInfo protobuf message containing details from the result
func resultToStatusInfo(result Result) *healthpb.StatusInfo {
	info := &healthpb.StatusInfo{
		Message: result.Status().String(),
	}

	if err := result.Error(); err != nil {
		info.Error = err.Error()
	}

	return info
}

// resultToCheckInfo converts a health.Result to a healthpb.CheckInfo.
//
// Parameters:
//   - result: The health check result to convert
//
// Returns:
//   - A CheckInfo protobuf message containing details from the result
func resultToCheckInfo(result Result) *healthpb.CheckInfo {
	info := &healthpb.CheckInfo{
		Status:    toProtoStatus(result.Status()),
		Timestamp: timestamppb.New(result.Timestamp()),
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

	// Add details if available
	details := result.Details()
	if len(details) > 0 {
		info.Details = make(map[string]string)
		for k, v := range details {
			// Convert each detail value to a string
			if v != nil {
				info.Details[k] = fmt.Sprintf("%v", v)
			}
		}
	}

	return info
}
