// file: pkg/metrics/grpc_timer.go
// version: 1.0.0
// guid: f1g2h3i4-j5k6-7890-l1m2-n3o4p5q6r7s8

package metrics

import (
	"context"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// grpcTimer implements Timer interface using gRPC service
type grpcTimer struct {
	client proto.MetricsServiceClient
	name   string
	tags   []Tag
	help   string
}

// Record records a duration
func (t *grpcTimer) Record(duration time.Duration) {
	t.recordValue(duration.Seconds())
}

// Time times a function call
func (t *grpcTimer) Time(fn func()) {
	start := time.Now()
	fn()
	t.Record(time.Since(start))
}

// WithTags returns a new timer with the given tags
func (t *grpcTimer) WithTags(tags ...Tag) Timer {
	return &grpcTimer{
		client: t.client,
		name:   t.name,
		tags:   append(t.tags, tags...),
		help:   t.help,
	}
}

// Snapshot returns a snapshot of the timer (using histogram snapshot interface)
func (t *grpcTimer) Snapshot() HistogramSnapshot {
	return &grpcHistogramSnapshot{} // Empty snapshot for gRPC client
}

// NewStopwatch returns a new stopwatch
func (t *grpcTimer) NewStopwatch() Stopwatch {
	return &grpcStopwatch{
		timer: t,
		start: time.Now(),
	}
}

// grpcStopwatch implements Stopwatch interface
type grpcStopwatch struct {
	timer *grpcTimer
	start time.Time
}

// Stop stops the timer and records its duration
func (s *grpcStopwatch) Stop() {
	duration := time.Since(s.start)
	s.timer.Record(duration)
}

// Reset resets the timer
func (s *grpcStopwatch) Reset() {
	s.start = time.Now()
}

// recordValue sends the duration value to the gRPC service
func (t *grpcTimer) recordValue(seconds float64) {
	// Convert tags to protobuf format
	protoTags := make(map[string]string)
	for _, tag := range t.tags {
		protoTags[tag.Key] = tag.Value
	}

	// Create metric data
	metricData := &proto.MetricData{}
	metricData.SetName(t.name)
	metricData.SetType(proto.MetricType_METRIC_TYPE_TIMER)
	metricData.SetLabels(protoTags)

	// Create metric value
	metricValue := &proto.MetricValue{}
	metricValue.SetDoubleValue(seconds)
	metricData.SetValues([]*proto.MetricValue{metricValue})

	// Create request
	req := &proto.RecordMetricRequest{}
	req.SetMetric(metricData)

	// Fire and forget - we don't wait for response in performance-critical path
	go func() {
		_, _ = t.client.RecordMetric(context.Background(), req)
	}()
}
