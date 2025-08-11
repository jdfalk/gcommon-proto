// file: monitoring/exporters/prometheus_test.go
// version: 1.1.0
// guid: 9d1c5e23-42b1-4e6c-a3a4-1e5b2d4f6e7a

package exporters

import (
	"context"
	"fmt"
	"io"
	"net"
	"net/http"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/monitoring/collectors"
	"strings"
)

// TestPrometheusExporter serves metrics and verifies they are accessible.
func TestPrometheusExporter(t *testing.T) {
	mc, err := collectors.NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	counter := mc.RegisterCounter("requests_total", "requests")
	counter.Add(context.Background(), 1)

	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatalf("listen: %v", err)
	}
	addr := ln.Addr().String()
	ln.Close()

	exp := NewPrometheusExporter(mc.Registry(), addr, "/metrics")
	exp.Start()
	defer exp.Shutdown()

	// Wait for server to start.
	time.Sleep(50 * time.Millisecond)
	resp, err := http.Get(fmt.Sprintf("http://%s/metrics", addr))
	if err != nil {
		t.Fatalf("http get: %v", err)
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	if !strings.Contains(string(body), "requests_total") {
		t.Fatalf("metrics output missing counter")
	}
}

// TestPrometheusExporterShutdown verifies shutdown succeeds even if started on ephemeral port.
func TestPrometheusExporterShutdown(t *testing.T) {
	mc, err := collectors.NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	exp := NewPrometheusExporter(mc.Registry(), "127.0.0.1:0", "/metrics")
	exp.Start()
	if err := exp.Shutdown(); err != nil {
		t.Fatalf("Shutdown: %v", err)
	}
}
