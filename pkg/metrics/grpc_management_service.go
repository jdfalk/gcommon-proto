// file: pkg/metrics/grpc_management_service.go
// Package metrics provides gRPC management service implementations for metrics provider administration.
package metrics

import (
	"context"
	"fmt"
	"sync"
	"time"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/types/known/timestamppb"

	pb "github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// MetricsManagementGRPCService implements the gRPC MetricsManagementService interface.
type MetricsManagementGRPCService struct {
	pb.UnimplementedMetricsManagementServiceServer
	providers map[string]*ProviderInfo
	mutex     sync.RWMutex
	factory   ProviderFactory
}

// ProviderInfo contains information about a managed provider.
type ProviderInfo struct {
	ID          string
	Name        string
	Type        string
	Provider    Provider
	Config      *pb.ProviderConfig
	Status      *pb.ProviderStatus
	CreatedAt   time.Time
	UpdatedAt   time.Time
	Tags        map[string]string
	Description string
}

// ProviderFactory interface for creating providers.
type ProviderFactory interface {
	CreateProvider(config *pb.ProviderConfig) (Provider, error)
	ValidateConfig(config *pb.ProviderConfig) error
}

// NewMetricsManagementGRPCService creates a new MetricsManagementGRPCService.
func NewMetricsManagementGRPCService(factory ProviderFactory) *MetricsManagementGRPCService {
	return &MetricsManagementGRPCService{
		providers: make(map[string]*ProviderInfo),
		factory:   factory,
	}
}

// CreateMetricsProvider creates a new metrics provider.
func (s *MetricsManagementGRPCService) CreateMetricsProvider(ctx context.Context, req *pb.CreateProviderRequest) (*pb.CreateProviderResponse, error) {
	if req == nil || req.Config == nil {
		return nil, status.Error(codes.InvalidArgument, "provider configuration is required")
	}

	s.mutex.Lock()
	defer s.mutex.Unlock()

	start := time.Now()

	// Check if provider already exists
	if _, exists := s.providers[req.Config.ProviderId]; exists {
		return &pb.CreateProviderResponse{
			Success: false,
			Error: &pb.Error{
				Code:    "PROVIDER_EXISTS",
				Message: fmt.Sprintf("provider with ID '%s' already exists", req.Config.ProviderId),
			},
		}, nil
	}

	// Validate configuration
	validation := &pb.ValidationResult{Valid: true}
	if req.ValidateConfig && s.factory != nil {
		if err := s.factory.ValidateConfig(req.Config); err != nil {
			validation.Valid = false
			validation.Errors = []string{err.Error()}
		}
	}

	// If dry run, return validation results only
	if req.DryRun {
		return &pb.CreateProviderResponse{
			Success:    validation.Valid,
			ProviderId: req.Config.ProviderId,
			CreatedAt:  timestamppb.New(start),
			Validation: validation,
		}, nil
	}

	// If validation failed, return error
	if !validation.Valid {
		return &pb.CreateProviderResponse{
			Success:    false,
			ProviderId: req.Config.ProviderId,
			Validation: validation,
			Error: &pb.Error{
				Code:    "VALIDATION_FAILED",
				Message: "provider configuration validation failed",
			},
		}, nil
	}

	// Create the provider
	var provider Provider
	var err error
	if s.factory != nil {
		provider, err = s.factory.CreateProvider(req.Config)
		if err != nil {
			return &pb.CreateProviderResponse{
				Success: false,
				Error: &pb.Error{
					Code:    "CREATION_FAILED",
					Message: err.Error(),
				},
			}, nil
		}
	}

	// Create provider info
	providerInfo := &ProviderInfo{
		ID:          req.Config.ProviderId,
		Name:        req.Config.Name,
		Type:        req.Config.Type.String(),
		Provider:    provider,
		Config:      req.Config,
		CreatedAt:   start,
		UpdatedAt:   start,
		Tags:        req.Config.Tags,
		Description: req.Config.Description,
		Status: &pb.ProviderStatus{
			State:       pb.ProviderState_PROVIDER_STATE_CREATING.String(),
			Message:     "Provider created successfully",
			Health:      "healthy",
			LastUpdated: timestamppb.New(start),
		},
	}

	// Start provider if auto-start is enabled
	if req.AutoStart && provider != nil {
		if err := provider.Start(ctx); err != nil {
			providerInfo.Status.State = pb.ProviderState_PROVIDER_STATE_ERROR.String()
			providerInfo.Status.Message = fmt.Sprintf("Failed to start provider: %v", err)
			providerInfo.Status.Health = "unhealthy"
		} else {
			providerInfo.Status.State = pb.ProviderState_PROVIDER_STATE_RUNNING.String()
			providerInfo.Status.Message = "Provider running"
		}
	}

	// Store provider info
	s.providers[req.Config.ProviderId] = providerInfo

	// Build response
	response := &pb.CreateProviderResponse{
		Success:    true,
		ProviderId: req.Config.ProviderId,
		CreatedAt:  timestamppb.New(start),
		Status:     providerInfo.Status,
		Validation: validation,
		AppliedConfig: &pb.AppliedConfig{
			ConfigSummary: fmt.Sprintf("Provider %s of type %s created", req.Config.Name, req.Config.Type),
		},
		Endpoints: &pb.ProviderEndpoints{
			ServiceEndpoint: fmt.Sprintf("http://localhost:8080/providers/%s", req.Config.ProviderId),
			HealthEndpoint:  fmt.Sprintf("http://localhost:8080/providers/%s/health", req.Config.ProviderId),
		},
	}

	return response, nil
}

// UpdateMetricsProvider updates an existing metrics provider configuration.
func (s *MetricsManagementGRPCService) UpdateMetricsProvider(ctx context.Context, req *pb.UpdateProviderRequest) (*pb.UpdateProviderResponse, error) {
	if req == nil || req.ProviderId == "" {
		return nil, status.Error(codes.InvalidArgument, "provider ID is required")
	}

	s.mutex.Lock()
	defer s.mutex.Unlock()

	start := time.Now()

	// Find existing provider
	providerInfo, exists := s.providers[req.ProviderId]
	if !exists {
		return nil, status.Error(codes.NotFound, fmt.Sprintf("provider '%s' not found", req.ProviderId))
	}

	// Validate update configuration
	validation := &pb.ValidationResult{Valid: true}
	if req.Options != nil && req.Options.ValidateConfig {
		// In a real implementation, validate the configuration updates
		validation.Valid = true
	}

	// If dry run, return what would be changed
	if req.Options != nil && req.Options.DryRun {
		return &pb.UpdateProviderResponse{
			Success:    validation.Valid,
			ProviderId: req.ProviderId,
			UpdatedAt:  timestamppb.New(start),
			Validation: validation,
			UpdateResult: &pb.UpdateResult{
				Action: pb.UpdateAction_UPDATE_ACTION_UPDATED,
				ConfigChanges: []*pb.ConfigChange{
					{
						ChangeType:  pb.ChangeType_CHANGE_TYPE_UPDATED,
						SettingPath: "example.setting",
						OldValue:    "old_value",
						NewValue:    "new_value",
						Description: "Example configuration change",
					},
				},
			},
		}, nil
	}

	// Apply updates to provider info
	if req.ConfigUpdate != nil {
		if req.ConfigUpdate.Name != "" {
			providerInfo.Name = req.ConfigUpdate.Name
		}
		if req.ConfigUpdate.Description != "" {
			providerInfo.Description = req.ConfigUpdate.Description
		}
	}

	providerInfo.UpdatedAt = start
	providerInfo.Status.LastUpdated = timestamppb.New(start)
	providerInfo.Status.Message = "Provider updated successfully"

	// Build response
	response := &pb.UpdateProviderResponse{
		Success:    true,
		ProviderId: req.ProviderId,
		UpdatedAt:  timestamppb.New(start),
		Status:     providerInfo.Status,
		Validation: validation,
		UpdateResult: &pb.UpdateResult{
			Action:        pb.UpdateAction_UPDATE_ACTION_UPDATED,
			UpdatedSettings: []string{"name", "description"},
			UpdateDuration: time.Since(start).String(),
		},
	}

	return response, nil
}

// DeleteMetricsProvider deletes a metrics provider and optionally its data.
func (s *MetricsManagementGRPCService) DeleteMetricsProvider(ctx context.Context, req *pb.DeleteProviderRequest) (*pb.DeleteProviderResponse, error) {
	if req == nil || req.ProviderId == "" {
		return nil, status.Error(codes.InvalidArgument, "provider ID is required")
	}

	s.mutex.Lock()
	defer s.mutex.Unlock()

	start := time.Now()

	// Find existing provider
	providerInfo, exists := s.providers[req.ProviderId]
	if !exists {
		return nil, status.Error(codes.NotFound, fmt.Sprintf("provider '%s' not found", req.ProviderId))
	}

	// If dry run, return what would be deleted
	if req.Options != nil && req.Options.DryRun {
		return &pb.DeleteProviderResponse{
			Success:    true,
			ProviderId: req.ProviderId,
			DeletedAt:  timestamppb.New(start),
			DeletionResult: &pb.DeletionResult{
				DryRunResult: &pb.DryRunResult{
					WouldDeleteMetrics: 100, // Example data
					WouldDeletePoints:  10000,
					EstimatedDeletionTime: "30s",
				},
			},
		}, nil
	}

	// Stop provider if it's running
	if providerInfo.Provider != nil {
		if err := providerInfo.Provider.Stop(ctx); err != nil {
			return &pb.DeleteProviderResponse{
				Success: false,
				Error: &pb.Error{
					Code:    "STOP_FAILED",
					Message: fmt.Sprintf("failed to stop provider: %v", err),
				},
			}, nil
		}
	}

	// Remove from registry
	delete(s.providers, req.ProviderId)

	// Build response
	response := &pb.DeleteProviderResponse{
		Success:    true,
		ProviderId: req.ProviderId,
		DeletedAt:  timestamppb.New(start),
		DeletionResult: &pb.DeletionResult{
			ProviderDeleted:       true,
			MetricsDeleted:        100,  // Example data
			DataPointsDeleted:     10000,
			CleanupStrategyUsed:   "immediate",
			DeletionDuration:      time.Since(start).String(),
		},
	}

	return response, nil
}

// ListMetricsProviders lists all configured metrics providers.
func (s *MetricsManagementGRPCService) ListMetricsProviders(ctx context.Context, req *pb.ListProvidersRequest) (*pb.ListProvidersResponse, error) {
	s.mutex.RLock()
	defer s.mutex.RUnlock()

	start := time.Now()

	// Apply filters and collect providers
	var providers []*pb.ProviderInfo
	for _, info := range s.providers {
		// Apply filters if specified
		if req.Filter != nil {
			if !s.matchesFilter(info, req.Filter) {
				continue
			}
		}

		pbInfo := &pb.ProviderInfo{
			ProviderId:  info.ID,
			Name:        info.Name,
			Type:        info.Type,
			Status:      info.Status,
			CreatedAt:   timestamppb.New(info.CreatedAt),
			UpdatedAt:   timestamppb.New(info.UpdatedAt),
			Tags:        info.Tags,
			Description: info.Description,
		}

		// Add optional details if requested
		if req.IncludeConfig {
			pbInfo.Config = &pb.ProviderConfigSummary{
				SecurityEnabled: true, // Example data
				ResourceLimits: &pb.ResourceLimitsSummary{
					MemoryLimitBytes: 1024 * 1024 * 1024, // 1GB
					CpuLimitPercent:  50.0,
				},
			}
		}

		if req.IncludeStats {
			pbInfo.Stats = &pb.ProviderStats{
				MetricsCount:       100,
				DataPointsCount:    10000,
				OperationsPerSecond: 50.5,
				ErrorRate:          0.01,
			}
		}

		providers = append(providers, pbInfo)
	}

	// Apply pagination
	totalCount := int64(len(providers))
	pageSize := int32(10) // Default page size
	if req.Pagination != nil && req.Pagination.PageSize > 0 {
		pageSize = req.Pagination.PageSize
	}

	// For simplicity, return all providers (pagination would be implemented in production)
	response := &pb.ListProvidersResponse{
		Success:   true,
		Providers: providers,
		Pagination: &pb.PaginationInfo{
			PageSize:    pageSize,
			TotalCount:  totalCount,
			HasMore:     false,
		},
		Summary: &pb.ProviderSummary{
			TotalProviders: int32(len(s.providers)),
			ProvidersByState: map[string]int32{
				"running": int32(len(s.providers)),
			},
			ProvidersByType: s.getProvidersByType(),
			TotalMetrics:    1000, // Example aggregate
		},
		GeneratedAt: timestamppb.New(start),
	}

	return response, nil
}

// GetProviderStats gets statistics and status for a specific provider.
func (s *MetricsManagementGRPCService) GetProviderStats(ctx context.Context, req *pb.GetProviderStatsRequest) (*pb.GetProviderStatsResponse, error) {
	if req == nil || req.ProviderId == "" {
		return nil, status.Error(codes.InvalidArgument, "provider ID is required")
	}

	s.mutex.RLock()
	defer s.mutex.RUnlock()

	start := time.Now()

	// Find provider
	providerInfo, exists := s.providers[req.ProviderId]
	if !exists {
		return nil, status.Error(codes.NotFound, fmt.Sprintf("provider '%s' not found", req.ProviderId))
	}

	// Build comprehensive statistics
	statistics := &pb.ProviderStatistics{
		ProviderInfo: &pb.ProviderInfo{
			ProviderId: providerInfo.ID,
			Name:       providerInfo.Name,
			Type:       providerInfo.Type,
			Status:     providerInfo.Status.State,
			Health:     providerInfo.Status.Health,
			Uptime:     time.Since(providerInfo.CreatedAt).String(),
			CreatedAt:  timestamppb.New(providerInfo.CreatedAt),
			LastUpdated: timestamppb.New(providerInfo.UpdatedAt),
		},
		Performance: &pb.PerformanceStats{
			CurrentOpsPerSecond: 50.5,
			AvgOpsPerSecond:     45.2,
			PeakOpsPerSecond:    100.0,
			AvgLatencyMs:        25.5,
			P95LatencyMs:        50.0,
			P99LatencyMs:        100.0,
		},
		ResourceUsage: &pb.ResourceUsageStats{
			Memory: &pb.MemoryUsage{
				UsedBytes:     512 * 1024 * 1024, // 512MB
				LimitBytes:    1024 * 1024 * 1024, // 1GB
				UsagePercent:  50.0,
			},
			Cpu: &pb.CPUUsage{
				CurrentPercent: 25.5,
				AvgPercent:     20.0,
				PeakPercent:    75.0,
			},
		},
		Errors: &pb.ErrorStats{
			TotalErrors:       10,
			CurrentErrorRate:  0.1,
			AvgErrorRate:      0.05,
			ErrorRatePercent:  0.2,
		},
		DataVolume: &pb.DataVolumeStats{
			TotalBytes:                    10 * 1024 * 1024, // 10MB
			TotalMetrics:                  100,
			TotalDataPoints:               10000,
			IngestionRateBytesPerSecond:   1024,
			IngestionRatePointsPerSecond:  10,
			CompressionRatio:              0.7,
		},
	}

	response := &pb.GetProviderStatsResponse{
		Success:     true,
		ProviderId:  req.ProviderId,
		Statistics:  statistics,
		GeneratedAt: timestamppb.New(start),
	}

	return response, nil
}

// Helper methods

func (s *MetricsManagementGRPCService) matchesFilter(info *ProviderInfo, filter *pb.ProviderFilter) bool {
	// Apply type filter
	if len(filter.ProviderTypes) > 0 {
		found := false
		for _, filterType := range filter.ProviderTypes {
			if info.Type == filterType {
				found = true
				break
			}
		}
		if !found {
			return false
		}
	}

	// Apply state filter
	if len(filter.States) > 0 {
		found := false
		for _, filterState := range filter.States {
			if info.Status.State == filterState {
				found = true
				break
			}
		}
		if !found {
			return false
		}
	}

	// Apply tag filter
	if len(filter.Tags) > 0 {
		for key, value := range filter.Tags {
			if info.Tags[key] != value {
				return false
			}
		}
	}

	return true
}

func (s *MetricsManagementGRPCService) getProvidersByType() map[string]int32 {
	typeCount := make(map[string]int32)
	for _, info := range s.providers {
		typeCount[info.Type]++
	}
	return typeCount
}

// RegisterProvider registers a provider in the service registry.
func (s *MetricsManagementGRPCService) RegisterProvider(providerID string, provider Provider) {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	if info, exists := s.providers[providerID]; exists {
		info.Provider = provider
	}
}

// GetProvider returns a provider by ID.
func (s *MetricsManagementGRPCService) GetProvider(providerID string) Provider {
	s.mutex.RLock()
	defer s.mutex.RUnlock()

	if info, exists := s.providers[providerID]; exists {
		return info.Provider
	}
	return nil
}