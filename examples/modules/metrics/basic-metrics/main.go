// file: examples/modules/metrics/basic-metrics/main.go
// version: 1.1.0
// guid: 085a36c1-0992-4b71-be20-339d80353c42

package main

import (
        "context"
        "fmt"
        "time"

        "github.com/jdfalk/gcommon/pkg/metrics"
        prom "github.com/jdfalk/gcommon/pkg/metrics/prometheus"
)

// metricsApp holds the provider and example metrics used in this demo.
type metricsApp struct {
        provider metrics.Provider
        counter  metrics.Counter
        gauge    metrics.Gauge
}

// setup initializes the Prometheus provider and creates two basic metrics.
func setup(ctx context.Context) (*metricsApp, error) {
        provider, err := prom.NewProvider(metrics.Config{})
        if err != nil {
                return nil, err
        }
        if err := provider.Start(ctx); err != nil {
                return nil, err
        }
        return &metricsApp{
                provider: provider,
                counter:  provider.Counter("requests_total"),
                gauge:    provider.Gauge("temperature_celsius"),
        }, nil
}

// run increments the counter and sets a gauge value, then prints the values.
func run(ctx context.Context, app *metricsApp) error {
        app.counter.Inc()
        app.gauge.Set(21.5)
        fmt.Printf("counter=%v gauge=%v\n", app.counter.Value(), app.gauge.Value())
        return nil
}

func main() {
        ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
        defer cancel()
        app, err := setup(ctx)
        if err != nil {
                panic(err)
        }
        if err := run(ctx, app); err != nil {
                panic(err)
        }
}
