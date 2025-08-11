// file: examples/production/monitoring/main.go
// version: 1.1.0
// guid: 0042c09e-b61b-4268-838f-2d7af81706ea

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/monitoring/collectors"
	"github.com/jdfalk/gcommon/monitoring/exporters"
)

// setup configures metrics, logging, and tracing collectors along with a
// Prometheus exporter. The exporter serves metrics on :9090/metrics. A simple
// log subscriber prints log entries to standard output.
func setup(ctx context.Context) (*collectors.MetricsCollector, *collectors.LogsCollector, *collectors.TracesCollector, *exporters.PrometheusExporter, error) {
	mc, err := collectors.NewMetricsCollector()
	if err != nil {
		return nil, nil, nil, nil, err
	}
	mc.StartRuntimeMetrics(ctx, time.Second)

	promExp := exporters.NewPrometheusExporter(mc.Registry(), ":9090", "/metrics")
	promExp.Start()

	lc := collectors.NewLogsCollector(100)
	lc.Start(ctx)
	sub := lc.Subscribe(100)
	go func() {
		for entry := range sub {
			fmt.Printf("%s [%s] %s\n", entry.Timestamp.Format(time.RFC3339), entry.Level, entry.Message)
		}
	}()

	tc, err := collectors.NewTracesCollector("example-service", "http://localhost:14268/api/traces")
	if err != nil {
		return nil, nil, nil, nil, err
	}

	return mc, lc, tc, promExp, nil
}

// run demonstrates basic usage of the collectors by recording a metric, a log
// entry, and a trace span.
func run(ctx context.Context, mc *collectors.MetricsCollector, lc *collectors.LogsCollector, tc *collectors.TracesCollector) error {
	counter := mc.RegisterCounter("example_requests_total", "number of example requests")
	ctx, span := tc.StartSpan(ctx, "run")
	defer tc.EndSpan(span, nil)

	lc.Emit(collectors.LevelInfo, "starting work", nil)
	counter.Add(ctx, 1)
	lc.Emit(collectors.LevelInfo, "work complete", nil)
	return nil
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	mc, lc, tc, exp, err := setup(ctx)
	if err != nil {
		panic(err)
	}
	defer exp.Shutdown()
	defer tc.Shutdown(context.Background())

	if err := run(ctx, mc, lc, tc); err != nil {
		panic(err)
	}

	// Allow some time for asynchronous operations to complete before exit.
	time.Sleep(100 * time.Millisecond)
}
