// filepath: /Users/jdfalk/repos/github.com/jdfalk/gcommon/examples/metrics/comprehensive.go
package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Example demonstrating comprehensive metrics usage
// This example showcases all metric types and their various features:
// - Counters for tracking counts of events
// - Gauges for tracking values that can go up and down
// - Histograms for tracking distributions of values
// - Summaries for tracking quantiles
// - Timers for tracking durations
// - Tags for dimensional metrics
// - Snapshots for point-in-time metrics state
func main() {
	// Create a new Prometheus metrics registry with global tags
	registry := prometheus.NewRegistry(
		metrics.WithTags(
			metrics.Tag{Key: "service", Value: "comprehensive-example"},
			metrics.Tag{Key: "environment", Value: "development"},
		),
	)

	// Set up HTTP server to expose metrics
	http.Handle("/metrics", promhttp.Handler())
	go func() {
		fmt.Println("Starting metrics server on :2112")
		fmt.Println("Visit http://localhost:2112/metrics to see the metrics")
		if err := http.ListenAndServe(":2112", nil); err != nil {
			fmt.Printf("Error starting metrics server: %v\n", err)
		}
	}()

	// COUNTER EXAMPLES
	//
	// Create a counter for tracking total requests
	requestCounter := registry.Counter(
		"example_requests_total",
		[]metrics.Tag{
			{Key: "endpoint", Value: ""},
			{Key: "method", Value: ""},
		},
		metrics.WithDescription("Total number of example requests"),
	)

	// Create counters with tags
	getCounter := requestCounter.WithTags(
		metrics.Tag{Key: "method", Value: "GET"},
		metrics.Tag{Key: "endpoint", Value: "/api"},
	)
	postCounter := requestCounter.WithTags(
		metrics.Tag{Key: "method", Value: "POST"},
		metrics.Tag{Key: "endpoint", Value: "/api"},
	)

	// GAUGE EXAMPLES
	//
	// Create a gauge for tracking current connections
	connectionsGauge := registry.Gauge(
		"example_active_connections",
		[]metrics.Tag{
			{Key: "pool", Value: ""},
		},
		metrics.WithDescription("Current number of active connections"),
	)

	// Create gauges with tags
	apiConnections := connectionsGauge.WithTags(metrics.Tag{Key: "pool", Value: "api"})
	dbConnections := connectionsGauge.WithTags(metrics.Tag{Key: "pool", Value: "database"})

	// HISTOGRAM EXAMPLES
	//
	// Create a histogram for tracking response sizes with custom buckets
	responseSizeHistogram := registry.Histogram(
		"example_response_size_bytes",
		[]metrics.Tag{
			{Key: "endpoint", Value: ""},
		},
		metrics.WithDescription("Size of HTTP responses in bytes"),
		metrics.WithBuckets([]float64{10, 100, 1000, 10000, 100000}),
	)

	// Create a histogram with tags
	apiResponseSizes := responseSizeHistogram.WithTags(metrics.Tag{Key: "endpoint", Value: "/api"})

	// SUMMARY EXAMPLES
	//
	// Create a summary for tracking response times with custom quantiles
	responseTimeSummary := registry.Summary(
		"example_response_time_seconds",
		[]metrics.Tag{
			{Key: "endpoint", Value: ""},
		},
		metrics.WithDescription("Response time in seconds"),
		metrics.WithQuantiles(map[float64]float64{
			0.5:  0.05,  // 50th percentile with 5% error
			0.9:  0.01,  // 90th percentile with 1% error
			0.99: 0.001, // 99th percentile with 0.1% error
		}),
	)

	// Create a summary with tags
	apiResponseTimes := responseTimeSummary.WithTags(metrics.Tag{Key: "endpoint", Value: "/api"})

	// TIMER EXAMPLES
	//
	// Create a timer for tracking function execution times
	functionTimer := registry.Timer(
		"example_function_duration_seconds",
		[]metrics.Tag{
			{Key: "function", Value: ""},
		},
		metrics.WithDescription("Duration of function execution"),
		// Custom buckets optimized for very fast operations
		metrics.WithBuckets([]float64{0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0}),
	)

	// Create timers with tags
	processTimer := functionTimer.WithTags(metrics.Tag{Key: "function", Value: "process"})
	validateTimer := functionTimer.WithTags(metrics.Tag{Key: "function", Value: "validate"})

	// Simulate application activity
	fmt.Println("Generating metrics data...")
	for i := 0; i < 100; i++ {
		// Update counters
		getCounter.Inc()
		if i%3 == 0 {
			postCounter.Inc()
		}

		// Update gauges
		apiConnections.Set(float64(rand.Intn(100)))
		dbConnections.Set(float64(rand.Intn(20)))

		// Update histograms
		apiResponseSizes.Observe(float64(rand.Intn(10000)))

		// Update summaries
		apiResponseTimes.Observe(rand.Float64() * 0.1) // 0-100ms

		// Use timer with function call
		processTimer.Time(func() {
			// Simulate work
			time.Sleep(time.Millisecond * time.Duration(rand.Intn(5)))
		})

		// Use timer with stopwatch
		sw := validateTimer.NewStopwatch()
		// Simulate validation work
		time.Sleep(time.Millisecond * time.Duration(rand.Intn(3)))
		sw.Stop()

		// Sleep to simulate request interval
		time.Sleep(time.Millisecond * 100)

		// Every 10 iterations, output some snapshot data
		if i%10 == 0 {
			fmt.Printf("\n--- Metrics Snapshot at iteration %d ---\n", i)

			// Counter snapshot
			fmt.Printf("GET requests: %.0f\n", getCounter.Value())
			fmt.Printf("POST requests: %.0f\n", postCounter.Value())

			// Gauge snapshot
			fmt.Printf("API connections: %.0f\n", apiConnections.Value())
			fmt.Printf("DB connections: %.0f\n", dbConnections.Value())

			// Histogram snapshot
			histSnapshot := apiResponseSizes.Snapshot()
			fmt.Printf("Response size histogram: count=%.0f sum=%.0f\n",
				histSnapshot.Count, histSnapshot.Sum)

			// Summary snapshot
			summarySnapshot := apiResponseTimes.Snapshot()
			fmt.Printf("Response time summary: count=%.0f sum=%.5f\n",
				summarySnapshot.Count, summarySnapshot.Sum)
			fmt.Printf("Response time p50=%.5fs p99=%.5fs\n",
				summarySnapshot.Quantiles[0.5], summarySnapshot.Quantiles[0.99])

			// Timer histogram snapshot
			timerSnapshot := processTimer.Snapshot()
			fmt.Printf("Process timer: count=%.0f sum=%.5fs\n",
				timerSnapshot.Count, timerSnapshot.Sum)

			fmt.Println("--------------------------------------")
		}
	}

	fmt.Println("\nExample complete! The metrics server is still running.")
	fmt.Println("Visit http://localhost:2112/metrics to see all the metrics.")
	fmt.Println("Press Ctrl+C to exit.")

	// Block forever (or until Ctrl+C)
	select {}
}
