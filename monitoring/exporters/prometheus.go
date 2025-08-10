// file: monitoring/exporters/prometheus.go
// version: 1.1.0
// guid: 0f1a2b3c-4d5e-6789-0abc-def123456789

package exporters

import (
	"net/http"
	"sync"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// PrometheusExporter exposes metrics collected by a MetricsCollector via an HTTP
// endpoint compatible with Prometheus scraping.
type PrometheusExporter struct {
	registry *prometheus.Registry
	server   *http.Server
	mu       sync.Mutex
}

// NewPrometheusExporter creates an exporter serving metrics on the given address
// and path. The registry must be the same used by MetricsCollector.
func NewPrometheusExporter(reg *prometheus.Registry, addr, path string) *PrometheusExporter {
	mux := http.NewServeMux()
	mux.Handle(path, promhttp.HandlerFor(reg, promhttp.HandlerOpts{}))
	return &PrometheusExporter{registry: reg, server: &http.Server{Addr: addr, Handler: mux}}
}

// Start begins serving the metrics endpoint in a new goroutine.
func (e *PrometheusExporter) Start() {
	e.mu.Lock()
	defer e.mu.Unlock()
	if e.server == nil {
		return
	}
	go e.server.ListenAndServe()
}

// Shutdown gracefully stops the HTTP server.
func (e *PrometheusExporter) Shutdown() error {
	e.mu.Lock()
	defer e.mu.Unlock()
	if e.server == nil {
		return nil
	}
	err := e.server.Close()
	e.server = nil
	return err
}
