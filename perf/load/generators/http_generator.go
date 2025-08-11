// file: perf/load/generators/http_generator.go
// version: 0.1.0
// guid: bbb4c2ba-c06f-4cd3-a6de-99b915ee61a0

package generators

import (
	"context"
	"net/http"

	"github.com/jdfalk/gcommon/perf/framework"
)

// HTTPGenerator produces HTTP requests for load testing. The implementation is
// currently a stub and should be extended to support complex request patterns.
type HTTPGenerator struct {
	// Client is the HTTP client used to send requests.
	Client *http.Client
	// metrics is a channel of generated performance metrics.
	metrics chan framework.PerformanceMetrics
	// TODO: Add fields for request templates, headers, and body data.
}

// NewHTTPGenerator creates a generator with a default HTTP client.
func NewHTTPGenerator() *HTTPGenerator {
	return &HTTPGenerator{Client: &http.Client{}, metrics: make(chan framework.PerformanceMetrics, 1)}
}

// Start begins generating load. This placeholder sends a single metric.
func (g *HTTPGenerator) Start(ctx context.Context, conc int) error {
	// TODO: Implement real load generation respecting concurrency.
	go func() {
		g.metrics <- framework.NewPerformanceMetrics()
	}()
	return nil
}

// Stop stops the generator. This placeholder closes the metrics channel.
func (g *HTTPGenerator) Stop() {
	close(g.metrics)
}

// Metrics returns the channel of performance metrics.
func (g *HTTPGenerator) Metrics() <-chan framework.PerformanceMetrics {
	return g.metrics
}

// Generate issues a single HTTP request. This placeholder does not send actual
// requests and should be replaced with full functionality.
func (g *HTTPGenerator) Generate(req *http.Request) (*http.Response, error) {
	// TODO: Implement HTTP request generation and sending.
	_ = req
	return &http.Response{StatusCode: http.StatusOK}, nil
}

// TODO: Support rate limiting and concurrency controls.
// TODO: Add helpers for generating requests from scenario definitions.
