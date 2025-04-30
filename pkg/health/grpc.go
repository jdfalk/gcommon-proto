// file: pkg/health/grpc.go
package health

import (
	"context"
	"fmt"
	"sync"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"github.com/jdfalk/gcommon/pkg/health/proto"
)

// GRPCServer implements the gRPC health service interface.
// It provides both standard gRPC health checking protocol and our custom extended protocol.
type GRPCServer struct {
	proto.UnimplementedHealthServiceServer
	provider Provider
	watches  map[string]map[proto.HealthService_WatchServer]chan proto.ServingStatus
	mu       sync.RWMutex
}

// NewGRPCServer creates a new gRPC health server.
func NewGRPCServer(provider Provider) *GRPCServer {
	return &GRPCServer{
		provider: provider,
		watches:  make(map[string]map[proto.HealthService_WatchServer]chan proto.ServingStatus),
	}
}

// Register registers this health server with a gRPC server.
func (s *GRPCServer) Register(server *grpc.Server) {
	proto.RegisterHealthServiceServer(server, s)

	// Also register as standard grpc_health_v1.Health server
	RegisterStandardGRPCHealthServer(server, s.provider)
}

// Check performs a health check and returns the status.
func (s *GRPCServer) Check(ctx context.Context, req *proto.HealthCheckRequest) (*proto.HealthCheckResponse, error) {
	serviceName := req.GetService()

	var result Result
	var err error

	if serviceName == "" {
		// If no service is specified, check overall health
		result, err = s.provider.CheckAll(ctx)
	} else {
		// Check specific service
		check, exists := s.provider.Get(serviceName)
		if !exists {
			return nil, status.Errorf(codes.NotFound, "service not found: %s", serviceName)
		}

		checkCtx, cancel := context.WithTimeout(ctx, check.Timeout())
		result, err = check.Execute(checkCtx)
		cancel()
	}

	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}

	return &proto.HealthCheckResponse{
		Status:    statusToProto(result.Status()),
		Timestamp: result.Timestamp().Format(time.RFC3339),
		Details:   convertDetailsToStringMap(result.Details()),
	}, nil
}

// Watch performs a streaming health check and reports status changes.
func (s *GRPCServer) Watch(req *proto.HealthCheckRequest, stream proto.HealthService_WatchServer) error {
	serviceName := req.GetService()
	if serviceName == "" {
		serviceName = "all"
	}

	// Create a channel for this watch
	statusCh := make(chan proto.ServingStatus, 1)

	// Register the watch
	s.mu.Lock()
	if _, exists := s.watches[serviceName]; !exists {
		s.watches[serviceName] = make(map[proto.HealthService_WatchServer]chan proto.ServingStatus)
	}
	s.watches[serviceName][stream] = statusCh
	s.mu.Unlock()

	// Add a listener to the provider to get status changes
	listener := &watchListener{
		serviceName: serviceName,
		server:      s,
	}
	s.provider.AddListener(listener)
	defer s.provider.RemoveListener(listener)

	// Perform an initial check
	var status proto.ServingStatus
	if serviceName == "all" {
		result, _ := s.provider.CheckAll(stream.Context())
		status = statusToProto(result.Status())
	} else {
		check, exists := s.provider.Get(serviceName)
		if !exists {
			status = proto.ServingStatus_UNKNOWN
		} else {
			result, _ := check.Execute(stream.Context())
			status = statusToProto(result.Status())
		}
	}

	// Send the initial status
	if err := stream.Send(&proto.HealthCheckResponse{
		Status:    status,
		Timestamp: time.Now().Format(time.RFC3339),
	}); err != nil {
		s.removeWatch(serviceName, stream)
		return err
	}

	// Wait for updates or context cancellation
	for {
		select {
		case <-stream.Context().Done():
			s.removeWatch(serviceName, stream)
			return stream.Context().Err()

		case status := <-statusCh:
			if err := stream.Send(&proto.HealthCheckResponse{
				Status:    status,
				Timestamp: time.Now().Format(time.RFC3339),
			}); err != nil {
				s.removeWatch(serviceName, stream)
				return err
			}
		}
	}
}

// CheckAll executes all health checks and returns detailed results.
func (s *GRPCServer) CheckAll(ctx context.Context, req *proto.HealthCheckAllRequest) (*proto.HealthCheckAllResponse, error) {
	// Execute all checks
	result, err := s.provider.CheckAll(ctx)
	if err != nil {
		return nil, status.Error(codes.Internal, err.Error())
	}

	// Convert the result to protobuf format
	response := &proto.HealthCheckAllResponse{
		Status:    statusToProto(result.Status()),
		Timestamp: result.Timestamp().Format(time.RFC3339),
		Results:   make(map[string]*proto.HealthCheckResult),
	}

	// Add child results if details are requested
	if req.GetIncludeDetails() {
		for _, child := range result.Children() {
			check := child.Check()
			if check != nil {
				response.Results[check.Name()] = resultToProto(child)
			}
		}
	}

	return response, nil
}

// removeWatch removes a watch stream.
func (s *GRPCServer) removeWatch(serviceName string, stream proto.HealthService_WatchServer) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if watches, exists := s.watches[serviceName]; exists {
		delete(watches, stream)
		if len(watches) == 0 {
			delete(s.watches, serviceName)
		}
	}
}

// notifyWatchers notifies all watchers of a status change.
func (s *GRPCServer) notifyWatchers(serviceName string, status proto.ServingStatus) {
	s.mu.RLock()
	defer s.mu.RUnlock()

	// Notify watchers for this specific service
	if watches, exists := s.watches[serviceName]; exists {
		for _, ch := range watches {
			select {
			case ch <- status:
			default:
				// Channel is full, skip
			}
		}
	}

	// Notify watchers for all services
	if watches, exists := s.watches["all"]; exists {
		for _, ch := range watches {
			select {
			case ch <- status:
			default:
				// Channel is full, skip
			}
		}
	}
}

// watchListener implements the Listener interface to notify gRPC watchers.
type watchListener struct {
	serviceName string
	server      *GRPCServer
}

// OnStatusChange is called when a health status changes.
func (l *watchListener) OnStatusChange(name string, previous, current Result) {
	// If we're watching a specific service and it's not this one, skip
	if l.serviceName != "all" && l.serviceName != name {
		return
	}

	// Notify watchers of the status change
	l.server.notifyWatchers(name, statusToProto(current.Status()))
}

// statusToProto converts a health status to a protobuf serving status.
func statusToProto(status Status) proto.ServingStatus {
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

// protoToStatus converts a protobuf serving status to a health status.
func protoToStatus(status proto.ServingStatus) Status {
	switch status {
	case proto.ServingStatus_SERVING:
		return StatusUp
	case proto.ServingStatus_NOT_SERVING:
		return StatusDown
	case proto.ServingStatus_SERVING_DEGRADED:
		return StatusDegraded
	default:
		return StatusUnknown
	}
}

// resultToProto converts a health check result to a protobuf health check result.
func resultToProto(result Result) *proto.HealthCheckResult {
	protoResult := &proto.HealthCheckResult{
		Status:     statusToProto(result.Status()),
		Timestamp:  result.Timestamp().Format(time.RFC3339),
		DurationMs: result.Duration().Milliseconds(),
		Details:    convertDetailsToStringMap(result.Details()),
		Children:   make(map[string]*proto.HealthCheckResult),
	}

	// Add error if it exists
	if err := result.Error(); err != nil {
		protoResult.Error = err.Error()
	}

	// Set check type if available
	if check := result.Check(); check != nil {
		protoResult.Type = checkTypeToProto(check.Type())
	}

	// Add children if they exist
	for _, child := range result.Children() {
		check := child.Check()
		if check != nil {
			protoResult.Children[check.Name()] = resultToProto(child)
		}
	}

	return protoResult
}

// checkTypeToProto converts a check type to a protobuf check type.
func checkTypeToProto(checkType CheckType) proto.CheckType {
	switch checkType {
	case TypeLiveness:
		return proto.CheckType_LIVENESS
	case TypeReadiness:
		return proto.CheckType_READINESS
	case TypeComponent:
		return proto.CheckType_COMPONENT
	case TypeDependency:
		return proto.CheckType_DEPENDENCY
	default:
		return proto.CheckType_TYPE_UNSPECIFIED
	}
}

// convertDetailsToStringMap converts a map[string]interface{} to map[string]string.
func convertDetailsToStringMap(details map[string]interface{}) map[string]string {
	result := make(map[string]string, len(details))
	for k, v := range details {
		result[k] = fmt.Sprintf("%v", v)
	}
	return result
}
