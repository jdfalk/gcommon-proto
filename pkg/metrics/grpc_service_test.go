// file: pkg/metrics/grpc_service_test.go
package metrics

import (
	"context"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
	pb "github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// MockProvider implements the Provider interface for testing
type MockProvider struct {
	mock.Mock
}

func (m *MockProvider) Counter(name string, options ...Option) Counter {
	args := m.Called(name, options)
	return args.Get(0).(Counter)
}

func (m *MockProvider) Gauge(name string, options ...Option) Gauge {
	args := m.Called(name, options)
	return args.Get(0).(Gauge)
}

func (m *MockProvider) Histogram(name string, options ...Option) Histogram {
	args := m.Called(name, options)
	return args.Get(0).(Histogram)
}

func (m *MockProvider) Summary(name string, options ...Option) Summary {
	args := m.Called(name, options)
	return args.Get(0).(Summary)
}

func (m *MockProvider) Timer(name string, options ...Option) Timer {
	args := m.Called(name, options)
	return args.Get(0).(Timer)
}

func (m *MockProvider) Registry() Registry {
	args := m.Called()
	return args.Get(0).(Registry)
}

func (m *MockProvider) Handler() http.Handler {
	args := m.Called()
	return args.Get(0).(http.Handler)
}

func (m *MockProvider) Start(ctx context.Context) error {
	args := m.Called(ctx)
	return args.Error(0)
}

func (m *MockProvider) Stop(ctx context.Context) error {
	args := m.Called(ctx)
	return args.Error(0)
}

func (m *MockProvider) WithTags(tags ...Tag) Provider {
	args := m.Called(tags)
	return args.Get(0).(Provider)
}

// MockCounter implements the Counter interface for testing
type MockCounter struct {
	mock.Mock
}

func (m *MockCounter) Inc() {
	m.Called()
}

func (m *MockCounter) Add(value float64) {
	m.Called(value)
}

func (m *MockCounter) WithTags(tags ...Tag) Counter {
	args := m.Called(tags)
	return args.Get(0).(Counter)
}

func (m *MockCounter) Value() float64 {
	args := m.Called()
	return args.Get(0).(float64)
}

// MockGauge implements the Gauge interface for testing
type MockGauge struct {
	mock.Mock
}

func (m *MockGauge) Set(value float64) {
	m.Called(value)
}

func (m *MockGauge) Inc() {
	m.Called()
}

func (m *MockGauge) Dec() {
	m.Called()
}

func (m *MockGauge) Add(value float64) {
	m.Called(value)
}

func (m *MockGauge) Sub(value float64) {
	m.Called(value)
}

func (m *MockGauge) WithTags(tags ...Tag) Gauge {
	args := m.Called(tags)
	return args.Get(0).(Gauge)
}

func (m *MockGauge) Value() float64 {
	args := m.Called()
	return args.Get(0).(float64)
}

// MockHistogram implements the Histogram interface for testing
type MockHistogram struct {
	mock.Mock
}

func (m *MockHistogram) Observe(value float64) {
	m.Called(value)
}

func (m *MockHistogram) WithTags(tags ...Tag) Histogram {
	args := m.Called(tags)
	return args.Get(0).(Histogram)
}

func (m *MockHistogram) Snapshot() HistogramSnapshot {
	args := m.Called()
	return args.Get(0).(HistogramSnapshot)
}

func TestMetricsGRPCService_RecordMetric(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	mockCounter := &MockCounter{}
	service := NewMetricsGRPCService(mockProvider)

	// Mock expectations
	mockProvider.On("Counter", "test_counter", mock.Anything).Return(mockCounter)
	mockCounter.On("Add", 1.0).Return()

	// Test data
	req := &pb.RecordMetricRequest{
		Metric: &pb.MetricData{
			Name:  "test_counter",
			Type:  pb.MetricType_METRIC_TYPE_COUNTER,
			Value: 1.0,
			Labels: map[string]string{
				"env": "test",
			},
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.RecordMetric(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.NotEmpty(t, resp.MetricId)
	assert.NotNil(t, resp.RecordedAt)
	assert.True(t, resp.Validation.Valid)

	// Verify mocks
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
}

func TestMetricsGRPCService_RecordMetric_InvalidRequest(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	service := NewMetricsGRPCService(mockProvider)

	// Test with nil request
	ctx := context.Background()
	resp, err := service.RecordMetric(ctx, nil)

	// Assert
	assert.Error(t, err)
	assert.Nil(t, resp)
}

func TestMetricsGRPCService_RecordBatchMetrics(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	mockCounter := &MockCounter{}
	mockGauge := &MockGauge{}
	service := NewMetricsGRPCService(mockProvider)

	// Mock expectations
	mockProvider.On("Counter", "counter1", mock.Anything).Return(mockCounter)
	mockProvider.On("Gauge", "gauge1", mock.Anything).Return(mockGauge)
	mockCounter.On("Add", 1.0).Return()
	mockGauge.On("Set", 42.0).Return()

	// Test data
	req := &pb.RecordMetricsRequest{
		Metrics: []*pb.MetricData{
			{
				Name:  "counter1",
				Type:  pb.MetricType_METRIC_TYPE_COUNTER,
				Value: 1.0,
			},
			{
				Name:  "gauge1",
				Type:  pb.MetricType_METRIC_TYPE_GAUGE,
				Value: 42.0,
			},
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.RecordBatchMetrics(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.Equal(t, int32(2), resp.SuccessCount)
	assert.Equal(t, int32(0), resp.FailureCount)
	assert.Equal(t, int32(2), resp.TotalCount)
	assert.Len(t, resp.Results, 2)

	// Verify all results are successful
	for _, result := range resp.Results {
		assert.True(t, result.Success)
		assert.NotEmpty(t, result.MetricId)
	}

	// Verify mocks
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockGauge.AssertExpectations(t)
}

func TestMetricsGRPCService_GetMetrics(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	service := NewMetricsGRPCService(mockProvider)

	// Test data
	req := &pb.GetMetricsRequest{
		Filter: &pb.MetricFilter{
			Names: []string{"test_metric"},
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.GetMetrics(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.NotNil(t, resp.GeneratedAt)
	assert.NotNil(t, resp.Stats)
}

func TestMetricsGRPCService_GetMetricsSummary(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	service := NewMetricsGRPCService(mockProvider)

	// Test data
	req := &pb.GetMetricsSummaryRequest{
		Options: &pb.SummaryOptions{
			IncludeCounts:      true,
			IncludePerformance: true,
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.GetMetricsSummary(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.NotNil(t, resp.Summary)
	assert.NotNil(t, resp.Summary.TypeCounts)
	assert.Greater(t, resp.Summary.TotalMetrics, int64(0))
}

func TestMetricsGRPCService_RegisterMetric(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	service := NewMetricsGRPCService(mockProvider)

	// Test data
	req := &pb.RegisterMetricRequest{
		Definition: &pb.MetricDefinition{
			Name:        "test_metric",
			Type:        pb.MetricType_METRIC_TYPE_COUNTER,
			Description: "A test metric",
			Unit:        "requests",
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.RegisterMetric(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.Equal(t, "test_metric", resp.MetricName)
	assert.NotEmpty(t, resp.MetricId)
	assert.NotNil(t, resp.RegisteredAt)
	assert.True(t, resp.Validation.Valid)
	assert.Equal(t, pb.RegistrationAction_REGISTRATION_ACTION_CREATED, resp.Result.Action)
}

func TestMetricsGRPCService_UnregisterMetric(t *testing.T) {
	// Setup
	mockProvider := &MockProvider{}
	service := NewMetricsGRPCService(mockProvider)

	// Test data
	req := &pb.UnregisterMetricRequest{
		MetricIdentifier: &pb.UnregisterMetricRequest_MetricName{
			MetricName: "test_metric",
		},
	}

	// Execute
	ctx := context.Background()
	resp, err := service.UnregisterMetric(ctx, req)

	// Assert
	assert.NoError(t, err)
	assert.NotNil(t, resp)
	assert.True(t, resp.Success)
	assert.Equal(t, "test_metric", resp.MetricName)
	assert.NotNil(t, resp.UnregisteredAt)
	assert.True(t, resp.Result.DefinitionDeleted)
}

func TestGenerateMetricID(t *testing.T) {
	metric := &pb.MetricData{
		Name: "test_metric",
	}

	id := generateMetricID(metric)
	assert.NotEmpty(t, id)
	assert.Contains(t, id, "test_metric")
}

func TestGenerateMetricIDFromName(t *testing.T) {
	name := "test_metric"
	id := generateMetricIDFromName(name)
	assert.NotEmpty(t, id)
	assert.Contains(t, id, name)
}