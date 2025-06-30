// file: pkg/metrics/grpc_service.go
// Package metrics provides gRPC service implementations for metrics collection and management.
package metrics

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/types/known/timestamppb"

	pb "github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// MetricsGRPCService implements the gRPC MetricsService interface.
type MetricsGRPCService struct {
	pb.UnimplementedMetricsServiceServer
	provider Provider
	registry map[string]Provider // provider registry for multi-provider support
}

// NewMetricsGRPCService creates a new MetricsGRPCService.
func NewMetricsGRPCService(provider Provider) *MetricsGRPCService {
	return &MetricsGRPCService{
		provider: provider,
		registry: make(map[string]Provider),
	}
}

// RecordMetric records a single metric data point.
func (s *MetricsGRPCService) RecordMetric(ctx context.Context, req *pb.RecordMetricRequest) (*pb.RecordMetricResponse, error) {
	if req == nil || req.Metric == nil {
		return nil, status.Error(codes.InvalidArgument, "metric data is required")
	}

	// Get the provider to use
	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	// Record the metric based on its type
	start := time.Now()
	err := s.recordMetricData(provider, req.Metric)
	if err != nil {
		return &pb.RecordMetricResponse{
			Success: false,
			Error: &pb.Error{
				Code:    "RECORDING_FAILED",
				Message: err.Error(),
			},
		}, nil
	}

	// Build response
	response := &pb.RecordMetricResponse{
		Success:     true,
		MetricId:    generateMetricID(req.Metric),
		RecordedAt:  timestamppb.New(start),
		ProviderId:  req.ProviderId,
		Validation: &pb.ValidationResult{
			Valid: true,
		},
		Stats: &pb.RecordingStats{
			ProcessingTimeMs: time.Since(start).Milliseconds(),
			Persisted:        true,
		},
	}

	return response, nil
}

// RecordBatchMetrics records multiple metrics in batch.
func (s *MetricsGRPCService) RecordBatchMetrics(ctx context.Context, req *pb.RecordMetricsRequest) (*pb.RecordMetricsResponse, error) {
	if req == nil || len(req.Metrics) == 0 {
		return nil, status.Error(codes.InvalidArgument, "metrics data is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	start := time.Now()
	successCount := int32(0)
	failureCount := int32(0)
	results := make([]*pb.MetricResult, 0, len(req.Metrics))

	// Process each metric
	for i, metric := range req.Metrics {
		result := &pb.MetricResult{
			Index:      int32(i),
			RecordedAt: timestamppb.New(time.Now()),
		}

		err := s.recordMetricData(provider, metric)
		if err != nil {
			result.Success = false
			result.Error = &pb.Error{
				Code:    "RECORDING_FAILED",
				Message: err.Error(),
			}
			failureCount++
		} else {
			result.Success = true
			result.MetricId = generateMetricID(metric)
			successCount++
		}

		results = append(results, result)

		// Check if we should fail fast
		if req.FailOnError && !result.Success {
			break
		}
	}

	response := &pb.RecordMetricsResponse{
		Success:      failureCount == 0,
		SuccessCount: successCount,
		FailureCount: failureCount,
		TotalCount:   int32(len(req.Metrics)),
		Results:      results,
		CompletedAt:  timestamppb.New(time.Now()),
		ProviderId:   req.ProviderId,
		Stats: &pb.BatchStats{
			TotalProcessingTimeMs: time.Since(start).Milliseconds(),
			AvgProcessingTimeMs:   time.Since(start).Milliseconds() / int64(len(req.Metrics)),
		},
	}

	return response, nil
}

// GetMetrics retrieves metrics data with filtering and aggregation.
func (s *MetricsGRPCService) GetMetrics(ctx context.Context, req *pb.GetMetricsRequest) (*pb.GetMetricsResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "request is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	start := time.Now()

	// For now, return a basic response indicating the service is implemented
	// In a real implementation, this would query the actual metrics data
	response := &pb.GetMetricsResponse{
		Success:     true,
		Metrics:     []*pb.MetricData{}, // Would be populated with actual data
		GeneratedAt: timestamppb.New(start),
		ProviderId:  req.ProviderId,
		Stats: &pb.QueryStats{
			ExecutionTimeMs: time.Since(start).Milliseconds(),
		},
	}

	return response, nil
}

// StreamMetrics streams metrics data in real-time.
func (s *MetricsGRPCService) StreamMetrics(req *pb.StreamMetricsRequest, stream pb.MetricsService_StreamMetricsServer) error {
	if req == nil {
		return status.Error(codes.InvalidArgument, "request is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return status.Error(codes.NotFound, "provider not found")
	}

	// For now, return a basic implementation that sends a few test metrics
	// In a real implementation, this would stream actual metrics data
	ctx := stream.Context()
	
	for i := 0; i < 5; i++ {
		select {
		case <-ctx.Done():
			return ctx.Err()
		default:
			// Send a test metric
			metric := &pb.MetricData{
				Name:      fmt.Sprintf("test_metric_%d", i),
				Value:     float64(i),
				Timestamp: timestamppb.New(time.Now()),
				Labels:    map[string]string{"source": "stream"},
			}
			
			if err := stream.Send(metric); err != nil {
				return err
			}
			
			time.Sleep(time.Second) // Simulate real-time streaming
		}
	}

	return nil
}

// RegisterMetric registers a new metric definition.
func (s *MetricsGRPCService) RegisterMetric(ctx context.Context, req *pb.RegisterMetricRequest) (*pb.RegisterMetricResponse, error) {
	if req == nil || req.Definition == nil {
		return nil, status.Error(codes.InvalidArgument, "metric definition is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	start := time.Now()

	// Basic validation
	if req.Definition.Name == "" {
		return &pb.RegisterMetricResponse{
			Success: false,
			Error: &pb.Error{
				Code:    "INVALID_DEFINITION",
				Message: "metric name is required",
			},
		}, nil
	}

	// For now, just return success
	// In a real implementation, this would register the metric definition
	response := &pb.RegisterMetricResponse{
		Success:      true,
		MetricId:     generateMetricIDFromName(req.Definition.Name),
		MetricName:   req.Definition.Name,
		RegisteredAt: timestamppb.New(start),
		ProviderId:   req.ProviderId,
		Validation: &pb.RegistrationValidation{
			Valid: true,
		},
		Result: &pb.RegistrationResult{
			Action: pb.RegistrationAction_REGISTRATION_ACTION_CREATED,
		},
	}

	return response, nil
}

// UnregisterMetric unregisters an existing metric.
func (s *MetricsGRPCService) UnregisterMetric(ctx context.Context, req *pb.UnregisterMetricRequest) (*pb.UnregisterMetricResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "request is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	start := time.Now()

	// Get metric identifier
	var metricName string
	switch id := req.MetricIdentifier.(type) {
	case *pb.UnregisterMetricRequest_MetricName:
		metricName = id.MetricName
	case *pb.UnregisterMetricRequest_MetricId:
		metricName = id.MetricId // In real implementation, would lookup name by ID
	default:
		return nil, status.Error(codes.InvalidArgument, "metric identifier is required")
	}

	// For now, just return success
	response := &pb.UnregisterMetricResponse{
		Success:        true,
		MetricName:     metricName,
		UnregisteredAt: timestamppb.New(start),
		ProviderId:     req.ProviderId,
		Result: &pb.UnregistrationResult{
			DefinitionDeleted: true,
		},
	}

	return response, nil
}

// GetMetricMetadata gets metadata for a specific metric.
func (s *MetricsGRPCService) GetMetricMetadata(ctx context.Context, req *pb.GetMetricMetadataRequest) (*pb.GetMetricMetadataResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "request is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	// For now, return a basic response
	response := &pb.GetMetricMetadataResponse{
		Success: true,
		// Metadata would be populated in real implementation
	}

	return response, nil
}

// QueryMetrics queries metrics data using complex query expressions.
func (s *MetricsGRPCService) QueryMetrics(ctx context.Context, req *pb.QueryMetricsRequest) (*pb.QueryMetricsResponse, error) {
	if req == nil || req.Query == nil {
		return nil, status.Error(codes.InvalidArgument, "query is required")
	}

	start := time.Now()

	// For now, return a basic response
	response := &pb.QueryMetricsResponse{
		Success: true,
		Series:  []*pb.MetricSeries{}, // Would be populated with actual query results
		Statistics: &pb.QueryStatistics{
			ExecutionTime: timestamppb.New(time.Now()).AsDuration(),
			QueryTime:     timestamppb.New(start),
		},
	}

	return response, nil
}

// GetMetricsSummary gets summary statistics about metrics.
func (s *MetricsGRPCService) GetMetricsSummary(ctx context.Context, req *pb.GetMetricsSummaryRequest) (*pb.GetMetricsSummaryResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "request is required")
	}

	provider := s.getProvider(req.ProviderId)
	if provider == nil {
		return nil, status.Error(codes.NotFound, "provider not found")
	}

	start := time.Now()

	// For now, return a basic summary
	response := &pb.GetMetricsSummaryResponse{
		Success: true,
		Summary: &pb.MetricsSummary{
			TotalMetrics:    100, // Example data
			TotalDataPoints: 10000,
			TypeCounts: &pb.MetricTypeCounts{
				CounterCount:   25,
				GaugeCount:     30,
				HistogramCount: 20,
				SummaryCount:   15,
				TimerCount:     10,
			},
		},
		GeneratedAt: timestamppb.New(start),
	}

	return response, nil
}

// Helper methods

func (s *MetricsGRPCService) getProvider(providerID string) Provider {
	if providerID == "" {
		return s.provider // Use default provider
	}
	
	if provider, exists := s.registry[providerID]; exists {
		return provider
	}
	
	return s.provider // Fallback to default
}

func (s *MetricsGRPCService) recordMetricData(provider Provider, metric *pb.MetricData) error {
	if metric == nil {
		return fmt.Errorf("metric data is nil")
	}

	// Convert proto metric to internal metric based on type
	tags := make([]Tag, 0, len(metric.Labels))
	for key, value := range metric.Labels {
		tags = append(tags, Tag{Key: key, Value: value})
	}

	// Record based on metric type (this is a simplified example)
	switch metric.Type {
	case pb.MetricType_METRIC_TYPE_COUNTER:
		counter := provider.Counter(metric.Name, WithTags(tags...))
		counter.Add(metric.Value)
	case pb.MetricType_METRIC_TYPE_GAUGE:
		gauge := provider.Gauge(metric.Name, WithTags(tags...))
		gauge.Set(metric.Value)
	case pb.MetricType_METRIC_TYPE_HISTOGRAM:
		histogram := provider.Histogram(metric.Name, WithTags(tags...))
		histogram.Observe(metric.Value)
	default:
		return fmt.Errorf("unsupported metric type: %s", metric.Type)
	}

	return nil
}

func generateMetricID(metric *pb.MetricData) string {
	// In a real implementation, this would generate a proper unique ID
	return fmt.Sprintf("metric_%s_%d", metric.Name, time.Now().UnixNano())
}

func generateMetricIDFromName(name string) string {
	return fmt.Sprintf("metric_%s_%d", name, time.Now().UnixNano())
}

// Option helpers
func WithTags(tags ...Tag) Option {
	return func(o *Options) {
		o.Tags = append(o.Tags, tags...)
	}
}