// file: monitoring/integration_test.go
// version: 1.0.0
// guid: ab1c2d3e-4f5a-678b-9c0d-1e2f3a4b5c6d

package monitoring_test

import (
	"context"
	"fmt"
	"net"
	"net/http"
	"testing"
	"time"

	"github.com/jdfalk/gcommon/monitoring/alerts"
	"github.com/jdfalk/gcommon/monitoring/collectors"
	"github.com/jdfalk/gcommon/monitoring/exporters"
)

// TestFullMonitoringFlow simulates an end-to-end monitoring scenario using collectors, exporters, and alerts.
func TestFullMonitoringFlow(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Metrics collector and exporter
	mc, err := collectors.NewMetricsCollector()
	if err != nil {
		t.Fatalf("NewMetricsCollector: %v", err)
	}
	mc.StartRuntimeMetrics(ctx, time.Millisecond)
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatalf("listen: %v", err)
	}
	addr := ln.Addr().String()
	ln.Close()
	promExp := exporters.NewPrometheusExporter(mc.Registry(), addr, "/metrics")
	promExp.Start()
	defer promExp.Shutdown()

	// Log collector
	lc := collectors.NewLogsCollector(10)
	lc.Start(ctx)
	logSub := lc.Subscribe(1)
	lc.Emit(collectors.LevelInfo, "boot", nil)

	// Trace collector
	tc, err := collectors.NewTracesCollector("svc", "http://localhost:14268/api/traces")
	if err != nil {
		t.Fatalf("NewTracesCollector: %v", err)
	}
	defer tc.Shutdown(context.Background())
	tCtx, span := tc.StartSpan(ctx, "op")
	time.Sleep(1 * time.Millisecond)
	tc.EndSpan(span, nil)
	if tCtx == nil {
		t.Fatalf("expected context from span")
	}

	// Alerts
	sla := alerts.NewSLAAlert(time.Minute, 100)
	errA := alerts.NewErrorAlert(time.Minute, 0)
	perf := alerts.NewPerformanceAlert(time.Minute, 0)
	sla.Record(time.Now(), false)
	errA.Record(time.Now())
	perf.Record(1 * time.Millisecond)
	slaCh := make(chan float64, 1)
	errCh := make(chan float64, 1)
	perfCh := make(chan time.Duration, 1)
	go sla.Monitor(ctx, 10*time.Millisecond, func(f float64) { slaCh <- f })
	go errA.Monitor(ctx, 10*time.Millisecond, func(f float64) { errCh <- f })
	go perf.Monitor(ctx, 10*time.Millisecond, func(d time.Duration) { perfCh <- d })

	// Validate log received
	select {
	case entry := <-logSub:
		if entry.Message != "boot" {
			t.Fatalf("unexpected log: %+v", entry)
		}
	case <-time.After(time.Second):
		t.Fatalf("missing log entry")
	}

	// Validate metrics endpoint
	time.Sleep(50 * time.Millisecond)
	resp, err := http.Get(fmt.Sprintf("http://%s/metrics", addr))
	if err != nil || resp.StatusCode != http.StatusOK {
		t.Fatalf("metrics endpoint: %v %v", resp.StatusCode, err)
	}
	resp.Body.Close()

	// Ensure alerts fired
	timeout := time.After(time.Second)
	for i := 0; i < 3; i++ {
		select {
		case <-slaCh:
		case <-errCh:
		case <-perfCh:
		case <-timeout:
			t.Fatalf("missing alert")
		}
	}
}
