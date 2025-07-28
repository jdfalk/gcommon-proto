// Package middleware provides HTTP middleware for metrics collection.
package middleware

import (
	"fmt"
	"net/http"
	"strconv"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
)

// RequestMetricsOptions configures the RequestMetrics middleware.
type RequestMetricsOptions struct {
	// Provider is the metrics provider.
	Provider metrics.Provider

	// Buckets are the duration histogram buckets.
	Buckets []float64

	// SizeBuckets are the size histogram buckets.
	SizeBuckets []float64

	// ExcludePaths are paths to exclude from metrics collection.
	ExcludePaths []string

	// IncludeRequestSize controls whether to track request size.
	IncludeRequestSize bool

	// IncludeResponseSize controls whether to track response size.
	IncludeResponseSize bool

	// AdditionalTags are additional tags to add to all metrics.
	AdditionalTags []metrics.Tag

	// RequestPrefix is the prefix for request metrics.
	// Default: "http_server_requests".
	RequestPrefix string

	// ResponsePrefix is the prefix for response metrics.
	// Default: "http_server_responses".
	ResponsePrefix string

	// DurationName is the name of the duration histogram.
	// Default: "http_server_request_duration_seconds".
	DurationName string

	// RequestSizeName is the name of the request size histogram.
	// Default: "http_server_request_size_bytes".
	RequestSizeName string

	// ResponseSizeName is the name of the response size histogram.
	// Default: "http_server_response_size_bytes".
	ResponseSizeName string
}

// metricResponseWriter is a custom ResponseWriter that tracks metrics.
type metricResponseWriter struct {
	http.ResponseWriter
	statusCode int
	size       int
}

// WriteHeader captures the status code.
func (w *metricResponseWriter) WriteHeader(statusCode int) {
	w.statusCode = statusCode
	w.ResponseWriter.WriteHeader(statusCode)
}

// Write captures the response size.
func (w *metricResponseWriter) Write(b []byte) (int, error) {
	size, err := w.ResponseWriter.Write(b)
	w.size += size
	return size, err
}

// StatusCode returns the status code.
func (w *metricResponseWriter) StatusCode() int {
	if w.statusCode == 0 {
		return http.StatusOK
	}
	return w.statusCode
}

// Size returns the response size.
func (w *metricResponseWriter) Size() int {
	return w.size
}

// RequestMetrics returns a middleware that collects HTTP request metrics.
//
// The following metrics are collected:
//
//   - Counter: <RequestPrefix>_total - number of HTTP requests
//   - Counter: <ResponsePrefix>_total - number of HTTP responses by status code
//   - Histogram: <DurationName> - request duration in seconds
//   - Histogram: <RequestSizeName> - request size in bytes (optional)
//   - Histogram: <ResponseSizeName> - response size in bytes (optional)
//
// The following tags are added to all metrics:
//
//   - method: the HTTP method
//   - path: the HTTP path
//   - status: the HTTP status code (responses only)
//
// Request paths can be excluded from metrics collection with ExcludePaths.
func RequestMetrics(opts RequestMetricsOptions) func(http.Handler) http.Handler {
	// Set defaults
	if opts.RequestPrefix == "" {
		opts.RequestPrefix = "http_server_requests"
	}
	if opts.ResponsePrefix == "" {
		opts.ResponsePrefix = "http_server_responses"
	}
	if opts.DurationName == "" {
		opts.DurationName = "http_server_request_duration_seconds"
	}
	if opts.RequestSizeName == "" {
		opts.RequestSizeName = "http_server_request_size_bytes"
	}
	if opts.ResponseSizeName == "" {
		opts.ResponseSizeName = "http_server_response_size_bytes"
	}
	if opts.Buckets == nil {
		opts.Buckets = []float64{.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10}
	}
	if opts.SizeBuckets == nil {
		opts.SizeBuckets = []float64{100, 1000, 10000, 100000, 1000000}
	}

	// Create metrics
	requestsCounter := opts.Provider.Counter(
		fmt.Sprintf("%s_total", opts.RequestPrefix),
		metrics.WithDescription("Total number of HTTP requests"),
	)

	responsesCounter := opts.Provider.Counter(
		fmt.Sprintf("%s_total", opts.ResponsePrefix),
		metrics.WithDescription("Total number of HTTP responses by status code"),
	)

	durationHistogram := opts.Provider.Histogram(
		opts.DurationName,
		metrics.WithDescription("HTTP request duration in seconds"),
		metrics.WithBuckets(opts.Buckets),
	)

	var requestSizeHistogram, responseSizeHistogram metrics.Histogram
	if opts.IncludeRequestSize {
		requestSizeHistogram = opts.Provider.Histogram(
			opts.RequestSizeName,
			metrics.WithDescription("HTTP request size in bytes"),
			metrics.WithBuckets(opts.SizeBuckets),
		)
	}

	if opts.IncludeResponseSize {
		responseSizeHistogram = opts.Provider.Histogram(
			opts.ResponseSizeName,
			metrics.WithDescription("HTTP response size in bytes"),
			metrics.WithBuckets(opts.SizeBuckets),
		)
	}

	// Build excluded paths map for efficient lookup
	excludedPaths := make(map[string]bool, len(opts.ExcludePaths))
	for _, path := range opts.ExcludePaths {
		excludedPaths[path] = true
	}

	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			// Skip excluded paths
			if excludedPaths[r.URL.Path] {
				next.ServeHTTP(w, r)
				return
			}

			// Start the timer
			start := time.Now()

			// Wrap the response writer
			metricsWriter := &metricResponseWriter{
				ResponseWriter: w,
				statusCode:     0,
			}

			// Track request metrics
			requestsCounter.WithTags(
				append(opts.AdditionalTags, []metrics.Tag{
					{Key: "method", Value: r.Method},
					{Key: "path", Value: r.URL.Path},
				}...)...,
			).Inc()

			// Track request size
			if opts.IncludeRequestSize && r.ContentLength > 0 {
				requestSizeHistogram.WithTags(
					append(opts.AdditionalTags, []metrics.Tag{
						{Key: "method", Value: r.Method},
						{Key: "path", Value: r.URL.Path},
					}...)...,
				).Observe(float64(r.ContentLength))
			}

			// Call the next handler
			next.ServeHTTP(metricsWriter, r)

			// Get the status code
			status := metricsWriter.StatusCode()
			statusClass := strconv.Itoa(status / 100)
			statusStr := strconv.Itoa(status)

			// Track the response metrics
			responsesCounter.WithTags(
				append(opts.AdditionalTags, []metrics.Tag{
					{Key: "method", Value: r.Method},
					{Key: "path", Value: r.URL.Path},
					{Key: "status", Value: statusStr},
					{Key: "status_class", Value: fmt.Sprintf("%sxx", statusClass)},
				}...)...,
			).Inc()

			// Calculate duration
			duration := time.Since(start).Seconds()

			// Track duration
			durationHistogram.WithTags(
				append(opts.AdditionalTags, []metrics.Tag{
					{Key: "method", Value: r.Method},
					{Key: "path", Value: r.URL.Path},
					{Key: "status", Value: statusStr},
					{Key: "status_class", Value: fmt.Sprintf("%sxx", statusClass)},
				}...)...,
			).Observe(duration)

			// Track response size
			if opts.IncludeResponseSize {
				responseSizeHistogram.WithTags(
					append(opts.AdditionalTags, []metrics.Tag{
						{Key: "method", Value: r.Method},
						{Key: "path", Value: r.URL.Path},
						{Key: "status", Value: statusStr},
						{Key: "status_class", Value: fmt.Sprintf("%sxx", statusClass)},
					}...)...,
				).Observe(float64(metricsWriter.Size()))
			}
		})
	}
}

// StandardMetrics returns a middleware with standard configuration.
//
// This is a convenience function that calls RequestMetrics with a standard configuration.
// It includes request and response metrics, but not size metrics.
func StandardMetrics(provider metrics.Provider) func(http.Handler) http.Handler {
	return RequestMetrics(RequestMetricsOptions{
		Provider: provider,
	})
}

// RecordingResponseWriter is a ResponseWriter that records the status code and size.
type RecordingResponseWriter interface {
	http.ResponseWriter
	StatusCode() int
	Size() int
}

// MakeRecordingResponseWriter wraps a ResponseWriter to record metrics.
func MakeRecordingResponseWriter(w http.ResponseWriter) RecordingResponseWriter {
	return &metricResponseWriter{
		ResponseWriter: w,
		statusCode:     0,
	}
}
