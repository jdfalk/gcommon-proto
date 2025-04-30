// file: pkg/health/grpc_standard.go
package health

import (
	"context"
	"sync"

	"google.golang.org/grpc"
	"google.golang.org/grpc/health/grpc_health_v1"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/codes"
)

// StandardGRPCHealthServer implements the standard gRPC health checking protocol.
// It adapts our Provider interface to the official gRPC health checking protocol.
// This allows gRPC clients to check the health of our services using the widely
// adopted standard protocol.
type StandardGRPCHealthServer struct {
	grpc_health_v1.UnimplementedHealthServer
	provider Provider
	watches  map[string]map[grpc_health_v1.Health_WatchServer]chan grpc_health_v1.HealthCheckResponse_ServingStatus
	mu       sync.RWMutex
}

// RegisterStandardGRPCHealthServer registers a standard gRPC health server with the provided gRPC server.
func RegisterStandardGRPCHealthServer(server *grpc.Server, provider Provider) {
	healthServer := NewStandardGRPCHealthServer(provider)
	grpc_health_v1.RegisterHealthServer(server, healthServer)
}

// NewStandardGRPCHealthServer creates a new standard gRPC health server.
func NewStandardGRPCHealthServer(provider Provider) *StandardGRPCHealthServer {
	return &StandardGRPCHealthServer{
		provider: provider,
		watches:  make(map[string]map[grpc_health_v1.Health_WatchServer]chan grpc_health_v1.HealthCheckResponse_ServingStatus),
	}
}

// Check performs a health check and returns the status.
// This implements the standard gRPC health check protocol.
func (s *StandardGRPCHealthServer) Check(ctx context.Context, req *grpc_health_v1.HealthCheckRequest) (*grpc_health_v1.HealthCheckResponse, error) {
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

	return &grpc_health_v1.HealthCheckResponse{
		Status: statusToStandardProto(result.Status()),
	}, nil
}

// Watch performs a streaming health check and reports status changes.
// This implements the standard gRPC health check protocol.
func (s *StandardGRPCHealthServer) Watch(req *grpc_health_v1.HealthCheckRequest, stream grpc_health_v1.Health_WatchServer) error {
	serviceName := req.GetService()
	if serviceName == "" {
		serviceName = "all"
	}

	// Create a channel for this watch
	statusCh := make(chan grpc_health_v1.HealthCheckResponse_ServingStatus, 1)

	// Register the watch
	s.mu.Lock()
	if _, exists := s.watches[serviceName]; !exists {
		s.watches[serviceName] = make(map[grpc_health_v1.Health_WatchServer]chan grpc_health_v1.HealthCheckResponse_ServingStatus)
	}
	s.watches[serviceName][stream] = statusCh
	s.mu.Unlock()

	// Add a listener to the provider to get status changes
	listener := &standardWatchListener{
		serviceName: serviceName,
		server:      s,
	}
	s.provider.AddListener(listener)
	defer s.provider.RemoveListener(listener)

	// Perform an initial check
	var status grpc_health_v1.HealthCheckResponse_ServingStatus
	if serviceName == "all" {
		result, _ := s.provider.CheckAll(stream.Context())
		status = statusToStandardProto(result.Status())
	} else {
		check, exists := s.provider.Get(serviceName)
		if !exists {
			status = grpc_health_v1.HealthCheckResponse_UNKNOWN
		} else {
			result, _ := check.Execute(stream.Context())
			status = statusToStandardProto(result.Status())
		}
	}

	// Send the initial status
	if err := stream.Send(&grpc_health_v1.HealthCheckResponse{
		Status: status,
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
			if err := stream.Send(&grpc_health_v1.HealthCheckResponse{
				Status: status,
			}); err != nil {
				s.removeWatch(serviceName, stream)
				return err
			}
		}
	}
}

// removeWatch removes a watch stream.
func (s *StandardGRPCHealthServer) removeWatch(serviceName string, stream grpc_health_v1.Health_WatchServer) {
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
func (s *StandardGRPCHealthServer) notifyWatchers(serviceName string, status grpc_health_v1.HealthCheckResponse_ServingStatus) {
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

// standardWatchListener implements the Listener interface to notify standard gRPC watchers.
type standardWatchListener struct {
	serviceName string
	server      *StandardGRPCHealthServer
}

// OnStatusChange is called when a health status changes.
func (l *standardWatchListener) OnStatusChange(name string, previous, current Result) {
	// If we're watching a specific service and it's not this one, skip
	if l.serviceName != "all" && l.serviceName != name {
		return
	}

	// Notify watchers of the status change
	l.server.notifyWatchers(name, statusToStandardProto(current.Status()))
}

// statusToStandardProto converts our health status to the standard gRPC health proto status.
func statusToStandardProto(status Status) grpc_health_v1.HealthCheckResponse_ServingStatus {
	switch status {
	case StatusUp:
		return grpc_health_v1.HealthCheckResponse_SERVING
	case StatusDown:
		return grpc_health_v1.HealthCheckResponse_NOT_SERVING
	default:
		// The standard protocol doesn't have a DEGRADED status,
		// so we map both DEGRADED and UNKNOWN to UNKNOWN
		return grpc_health_v1.HealthCheckResponse_UNKNOWN
	}
}

// standardProtoToStatus converts the standard gRPC health proto status to our health status.
func standardProtoToStatus(status grpc_health_v1.HealthCheckResponse_ServingStatus) Status {
	switch status {
	case grpc_health_v1.HealthCheckResponse_SERVING:
		return StatusUp
	case grpc_health_v1.HealthCheckResponse_NOT_SERVING:
		return StatusDown
	default:
		return StatusUnknown
	}
}
