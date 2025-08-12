// file: pkg/metrics/grpc_summary.go
// version: 1.0.0
// guid: e1f2g3h4-i5j6-7890-k1l2-m3n4o5p6q7r8

package metrics

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// grpcSummary implements Summary interface using gRPC service
type grpcSummary struct {
	client    proto.MetricsServiceClient
	name      string
	tags      []Tag
	help      string
	quantiles []float64
}

// Observe adds a single observation to the summary
func (s *grpcSummary) Observe(value float64) {
	// Convert tags to protobuf format
	protoTags := make(map[string]string)
	for _, tag := range s.tags {
		protoTags[tag.Key] = tag.Value
	}

	// Create metric data
	metricData := &proto.MetricData{}
	metricData.SetName(s.name)
	metricData.SetType(proto.MetricType_METRIC_TYPE_SUMMARY)
	metricData.SetLabels(protoTags)

	// Create metric value (using double value for simplicity)
	metricValue := &proto.MetricValue{}
	metricValue.SetDoubleValue(value)
	metricData.SetValues([]*proto.MetricValue{metricValue})

	// Create request
	req := &proto.RecordMetricRequest{}
	req.SetMetric(metricData)

	// Fire and forget - we don't wait for response in performance-critical path
	go func() {
		_, _ = s.client.RecordMetric(context.Background(), req)
	}()
}

// WithTags returns a new summary with the given tags
func (s *grpcSummary) WithTags(tags ...Tag) Summary {
	return &grpcSummary{
		client:    s.client,
		name:      s.name,
		tags:      append(s.tags, tags...),
		help:      s.help,
		quantiles: s.quantiles,
	}
}

// Snapshot returns a snapshot of the summary
func (s *grpcSummary) Snapshot() SummarySnapshot {
	return &grpcSummarySnapshot{
		summary: s,
	}
}

// grpcSummarySnapshot implements SummarySnapshot
type grpcSummarySnapshot struct {
	summary *grpcSummary
}

// Count returns the number of observations (not implemented for gRPC client)
func (s *grpcSummarySnapshot) Count() int64 {
	return 0
}

// Sum returns the sum of all observations (not implemented for gRPC client)
func (s *grpcSummarySnapshot) Sum() float64 {
	return 0
}

// Quantile returns the value at the given quantile (not implemented for gRPC client)
func (s *grpcSummarySnapshot) Quantile(q float64) float64 {
	return 0
}

// Quantiles returns all quantiles (not implemented for gRPC client)
func (s *grpcSummarySnapshot) Quantiles() map[float64]float64 {
	return make(map[float64]float64)
}
