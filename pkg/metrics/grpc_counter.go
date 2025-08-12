// file: pkg/metrics/grpc_counter.go
// version: 1.0.0
// guid: b1c2d3e4-f5g6-7890-h1i2-j3k4l5m6n7o8

package metrics

import (
	"context"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// grpcCounter implements Counter interface using gRPC service
type grpcCounter struct {
	client proto.MetricsServiceClient
	name   string
	tags   []Tag
	help   string
	value  int64
}

// Inc increments the counter by 1
func (c *grpcCounter) Inc() {
	c.Add(1)
}

// Add adds the given value to the counter
func (c *grpcCounter) Add(value float64) {
	atomic.AddInt64(&c.value, int64(value))

	// Convert tags to protobuf format
	protoTags := make(map[string]string)
	for _, tag := range c.tags {
		protoTags[tag.Key] = tag.Value
	}

	// Create metric data
	metricData := &proto.MetricData{}
	metricData.SetName(c.name)
	metricData.SetType(proto.MetricType_METRIC_TYPE_COUNTER)
	metricData.SetLabels(protoTags)

	// Create metric value
	metricValue := &proto.MetricValue{}
	metricValue.SetDoubleValue(value)
	metricData.SetValues([]*proto.MetricValue{metricValue})

	// Create request
	req := &proto.RecordMetricRequest{}
	req.SetMetric(metricData)

	// Fire and forget - we don't wait for response in performance-critical path
	go func() {
		_, _ = c.client.RecordMetric(context.Background(), req)
	}()
}

// WithTags returns a new counter with the given tags
func (c *grpcCounter) WithTags(tags ...Tag) Counter {
	return &grpcCounter{
		client: c.client,
		name:   c.name,
		tags:   append(c.tags, tags...),
		help:   c.help,
		value:  atomic.LoadInt64(&c.value),
	}
}

// Value returns the current local value of the counter
func (c *grpcCounter) Value() float64 {
	return float64(atomic.LoadInt64(&c.value))
}
