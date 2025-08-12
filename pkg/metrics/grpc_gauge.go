// file: pkg/metrics/grpc_gauge.go
// version: 1.0.0
// guid: c1d2e3f4-g5h6-7890-i1j2-k3l4m5n6o7p8

package metrics

import (
	"context"
	"sync/atomic"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// grpcGauge implements Gauge interface using gRPC service
type grpcGauge struct {
	client proto.MetricsServiceClient
	name   string
	tags   []Tag
	help   string
	value  int64 // Using int64 for atomic operations, convert to float64 when needed
}

// Set sets the gauge to the given value
func (g *grpcGauge) Set(value float64) {
	atomic.StoreInt64(&g.value, int64(value*1000)) // Store as millis for precision
	g.recordValue(value)
}

// Inc increments the gauge by 1
func (g *grpcGauge) Inc() {
	g.Add(1)
}

// Dec decrements the gauge by 1
func (g *grpcGauge) Dec() {
	g.Sub(1)
}

// Add adds the given value to the gauge
func (g *grpcGauge) Add(value float64) {
	newVal := float64(atomic.AddInt64(&g.value, int64(value*1000))) / 1000
	g.recordValue(newVal)
}

// Sub subtracts the given value from the gauge
func (g *grpcGauge) Sub(value float64) {
	newVal := float64(atomic.AddInt64(&g.value, int64(-value*1000))) / 1000
	g.recordValue(newVal)
}

// WithTags returns a new gauge with the given tags
func (g *grpcGauge) WithTags(tags ...Tag) Gauge {
	return &grpcGauge{
		client: g.client,
		name:   g.name,
		tags:   append(g.tags, tags...),
		help:   g.help,
		value:  atomic.LoadInt64(&g.value),
	}
}

// Value returns the current value of the gauge
func (g *grpcGauge) Value() float64 {
	return float64(atomic.LoadInt64(&g.value)) / 1000
}

// recordValue sends the value to the gRPC service
func (g *grpcGauge) recordValue(value float64) {
	// Convert tags to protobuf format
	protoTags := make(map[string]string)
	for _, tag := range g.tags {
		protoTags[tag.Key] = tag.Value
	}

	// Create metric data
	metricData := &proto.MetricData{}
	metricData.SetName(g.name)
	metricData.SetType(proto.MetricType_METRIC_TYPE_GAUGE)
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
		_, _ = g.client.RecordMetric(context.Background(), req)
	}()
}
