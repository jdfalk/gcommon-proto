// file: pkg/metrics/grpc_registry.go
// version: 1.0.0
// guid: 2e8f7a6b-3c4d-5e9f-1a2b-3c4d5e6f7a8b

package metrics

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/metrics/proto"
)

// grpcRegistry implements Registry interface using gRPC calls
type grpcRegistry struct {
	client   proto.MetricsServiceClient
	tags     map[string]string
	provider *grpcProvider
	metrics  map[string]interface{} // Cache for created metrics
}

// newGrpcRegistry creates a new gRPC-based registry
func newGrpcRegistry(client proto.MetricsServiceClient, provider *grpcProvider) *grpcRegistry {
	return &grpcRegistry{
		client:   client,
		tags:     make(map[string]string),
		provider: provider,
		metrics:  make(map[string]interface{}),
	}
}

// Counter creates or returns a counter metric
func (r *grpcRegistry) Counter(name string) Counter {
	return newGrpcCounter(r.client, name, r.tags)
}

// Gauge creates or returns a gauge metric
func (r *grpcRegistry) Gauge(name string) Gauge {
	return newGrpcGauge(r.client, name, r.tags)
}

// Histogram creates or returns a histogram metric
func (r *grpcRegistry) Histogram(name string) Histogram {
	return newGrpcHistogram(r.client, name, r.tags)
}

// Summary creates or returns a summary metric
func (r *grpcRegistry) Summary(name string) Summary {
	return newGrpcSummary(r.client, name, r.tags)
}

// Timer creates or returns a timer metric
func (r *grpcRegistry) Timer(name string) Timer {
	return newGrpcTimer(r.client, name, r.tags)
}

// Get retrieves a metric by name and type
func (r *grpcRegistry) Get(name string, typ MetricType) (interface{}, bool) {
	key := fmt.Sprintf("%s:%d", name, typ)
	metric, exists := r.metrics[key]
	return metric, exists
}

// GetOrCreate creates or returns a metric of the specified type
func (r *grpcRegistry) GetOrCreate(name string, typ MetricType, options ...Option) interface{} {
	key := fmt.Sprintf("%s:%d", name, typ)
	if metric, exists := r.metrics[key]; exists {
		return metric
	}

	var metric interface{}
	switch typ {
	case TypeCounter:
		metric = r.Counter(name)
	case TypeGauge:
		metric = r.Gauge(name)
	case TypeHistogram:
		metric = r.Histogram(name)
	case TypeSummary:
		metric = r.Summary(name)
	case TypeTimer:
		metric = r.Timer(name)
	default:
		return nil
	}

	r.metrics[key] = metric
	return metric
}

// Visit calls the visitor function for each metric
func (r *grpcRegistry) Visit(visitor MetricVisitor) {
	for key, metric := range r.metrics {
		// Parse metric name and type from key
		// Key format: "name:type"
		for i := len(key) - 1; i >= 0; i-- {
			if key[i] == ':' {
				name := key[:i]
				typStr := key[i+1:]

				var typ MetricType
				switch typStr {
				case "0":
					typ = TypeCounter
				case "1":
					typ = TypeGauge
				case "2":
					typ = TypeHistogram
				case "3":
					typ = TypeSummary
				case "4":
					typ = TypeTimer
				default:
					continue
				}

				visitor(name, typ, metric)
				break
			}
		}
	}
}

// WithTags returns a new registry with additional tags
func (r *grpcRegistry) WithTags(tags ...Tag) Registry {
	newTags := make(map[string]string)
	for k, v := range r.tags {
		newTags[k] = v
	}
	for _, tag := range tags {
		newTags[tag.Key] = tag.Value
	}

	return &grpcRegistry{
		client:   r.client,
		tags:     newTags,
		provider: r.provider,
		metrics:  make(map[string]interface{}),
	}
}

// Snapshot returns a snapshot of all metrics
func (r *grpcRegistry) Snapshot() Snapshot {
	return &grpcSnapshot{
		registry: r,
	}
}

// Register registers a metric with the registry
func (r *grpcRegistry) Register(name string, metric interface{}, options ...Option) error {
	// Determine metric type
	var typ MetricType
	switch metric.(type) {
	case Counter, *grpcCounter:
		typ = TypeCounter
	case Gauge, *grpcGauge:
		typ = TypeGauge
	case Histogram, *grpcHistogram:
		typ = TypeHistogram
	case Summary, *grpcSummary:
		typ = TypeSummary
	case Timer, *grpcTimer:
		typ = TypeTimer
	default:
		return ErrInvalidMetricType
	}

	key := fmt.Sprintf("%s:%d", name, typ)
	r.metrics[key] = metric
	return nil
}

// Unregister removes a metric from the registry
func (r *grpcRegistry) Unregister(name string) bool {
	// Find and remove any metric with this name
	for key := range r.metrics {
		if r.extractNameFromKey(key) == name {
			delete(r.metrics, key)
			return true
		}
	}
	return false
}

// extractNameFromKey extracts the metric name from the registry key
func (r *grpcRegistry) extractNameFromKey(key string) string {
	for i := len(key) - 1; i >= 0; i-- {
		if key[i] == ':' {
			return key[:i]
		}
	}
	return key
}

// newGrpcCounter creates a new gRPC counter
func newGrpcCounter(client proto.MetricsServiceClient, name string, tags map[string]string) *grpcCounter {
	counter := &grpcCounter{
		client: client,
		name:   name,
		tags:   tagsFromMap(tags),
	}
	return counter
}

// newGrpcGauge creates a new gRPC gauge
func newGrpcGauge(client proto.MetricsServiceClient, name string, tags map[string]string) *grpcGauge {
	gauge := &grpcGauge{
		client: client,
		name:   name,
		tags:   tagsFromMap(tags),
	}
	return gauge
}

// newGrpcHistogram creates a new gRPC histogram
func newGrpcHistogram(client proto.MetricsServiceClient, name string, tags map[string]string) *grpcHistogram {
	histogram := &grpcHistogram{
		client: client,
		name:   name,
		tags:   tagsFromMap(tags),
	}
	return histogram
}

// newGrpcSummary creates a new gRPC summary
func newGrpcSummary(client proto.MetricsServiceClient, name string, tags map[string]string) *grpcSummary {
	summary := &grpcSummary{
		client: client,
		name:   name,
		tags:   tagsFromMap(tags),
	}
	return summary
}

// newGrpcTimer creates a new gRPC timer
func newGrpcTimer(client proto.MetricsServiceClient, name string, tags map[string]string) *grpcTimer {
	timer := &grpcTimer{
		client: client,
		name:   name,
		tags:   tagsFromMap(tags),
	}
	return timer
}

// tagsFromMap converts map[string]string to []Tag
func tagsFromMap(m map[string]string) []Tag {
	tags := make([]Tag, 0, len(m))
	for k, v := range m {
		tags = append(tags, Tag{Key: k, Value: v})
	}
	return tags
}
