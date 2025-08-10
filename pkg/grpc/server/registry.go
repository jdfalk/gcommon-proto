// file: pkg/grpc/server/registry.go
// version: 1.1.0
// guid: 6d7d1e9f-4b71-4e3c-9a31-6c7bde9d2d92

// Package server provides unified gRPC service registration utilities.
package server

import (
	"context"
	"net"
	"sync"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	healthgrpc "github.com/jdfalk/gcommon/pkg/health"
	healthpb "github.com/jdfalk/gcommon/pkg/health/proto"
)

// ServiceRegistrar defines methods for registering gRPC services.
type ServiceRegistrar interface {
	RegisterService(desc *grpc.ServiceDesc, impl interface{})
	RegisterHealthService(provider healthgrpc.Provider)
	RegisterReflectionService()
	GetRegisteredServices() []string
}

// ServerStats contains simple runtime statistics for the server.
type ServerStats struct {
	mu       sync.RWMutex
	services []string
}

// add records a newly registered service.
func (s *ServerStats) add(name string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.services = append(s.services, name)
}

// Services returns a snapshot of registered service names.
func (s *ServerStats) Services() []string {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return append([]string(nil), s.services...)
}

// Registry implements ServiceRegistrar on top of a gRPC server.
type Registry struct {
	server *grpc.Server
	stats  *ServerStats
}

// NewRegistry creates a new Registry for the provided gRPC server.
func NewRegistry(s *grpc.Server) *Registry {
	return &Registry{
		server: s,
		stats:  &ServerStats{},
	}
}

// RegisterService registers a generic gRPC service.
func (r *Registry) RegisterService(desc *grpc.ServiceDesc, impl interface{}) {
	if desc == nil || impl == nil {
		return
	}
	r.server.RegisterService(desc, impl)
	r.stats.add(desc.ServiceName)
}

// RegisterHealthService registers the health service using the provided provider.
func (r *Registry) RegisterHealthService(provider healthgrpc.Provider) {
	if provider == nil {
		return
	}
	hs := healthgrpc.NewGRPCServer(provider)
	hs.Register(r.server)
	r.stats.add(healthpb.HealthService_ServiceDesc.ServiceName)
}

// RegisterReflectionService enables gRPC reflection on the server.
func (r *Registry) RegisterReflectionService() {
	reflection.Register(r.server)
	r.stats.add("grpc.reflection.v1alpha.ServerReflection")
}

// GetRegisteredServices returns all registered service names.
func (r *Registry) GetRegisteredServices() []string {
	return r.stats.Services()
}

// GRPCServer defines lifecycle methods for a gRPC server.
type GRPCServer interface {
	ServiceRegistrar
	Start(ctx context.Context) error
	Stop(ctx context.Context) error
	GetAddress() string
	GetStats() *ServerStats
}

// Server provides a minimal implementation of GRPCServer.
type Server struct {
	addr     string
	server   *grpc.Server
	registry *Registry
}

// NewServer creates a new gRPC server listening on the provided address.
func NewServer(addr string, opts ...grpc.ServerOption) *Server {
	s := grpc.NewServer(opts...)
	return &Server{
		addr:     addr,
		server:   s,
		registry: NewRegistry(s),
	}
}

// Start begins serving on the configured address.
func (s *Server) Start(ctx context.Context) error {
	lis, err := net.Listen("tcp", s.addr)
	if err != nil {
		return err
	}
	go func() {
		_ = s.server.Serve(lis)
	}()
	return nil
}

// Stop gracefully stops the gRPC server.
func (s *Server) Stop(ctx context.Context) error {
	stopped := make(chan struct{})
	go func() {
		s.server.GracefulStop()
		close(stopped)
	}()
	select {
	case <-ctx.Done():
		s.server.Stop()
		return ctx.Err()
	case <-stopped:
		return nil
	}
}

// RegisterService registers services using the provided registrar.
func (s *Server) RegisterService(desc *grpc.ServiceDesc, impl interface{}) {
	s.registry.RegisterService(desc, impl)
}

// RegisterHealthService registers the health service using the provided provider.
func (s *Server) RegisterHealthService(provider healthgrpc.Provider) {
	s.registry.RegisterHealthService(provider)
}

// RegisterReflectionService enables gRPC reflection on the server.
func (s *Server) RegisterReflectionService() {
	s.registry.RegisterReflectionService()
}

// GetRegisteredServices returns all registered service names.
func (s *Server) GetRegisteredServices() []string {
	return s.registry.GetRegisteredServices()
}

// GetAddress returns the server's listening address.
func (s *Server) GetAddress() string {
	return s.addr
}

// GetStats returns server statistics.
func (s *Server) GetStats() *ServerStats {
	return s.registry.stats
}

// Registrar exposes the internal registry.
func (s *Server) Registrar() *Registry {
	return s.registry
}
