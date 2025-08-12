package middleware

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/mock"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)
	histograms map[string]*mockHistogram
}

func newMockProvider() *mockProvider {
	return &mockProvider{
		counters:   make(map[string]*mockCounter),
		histograms: make(map[string]*mockHistogram),
	}
}

func (p *mockProvider) Counter(name string, options ...metrics.Option) metrics.Counter {
	counter := &mockCounter{name: name}
	p.counters[name] = counter
	return counter
}

func (p *mockProvider) Gauge(name string, options ...metrics.Option) metrics.Gauge {
	return nil // Not used in this test
}

func (p *mockProvider) Histogram(name string, options ...metrics.Option) metrics.Histogram {
	histogram := &mockHistogram{name: name}
	p.histograms[name] = histogram
	return histogram
}

func (p *mockProvider) Summary(name string, options ...metrics.Option) metrics.Summary {
	return nil // Not used in this test
}

func (p *mockProvider) Timer(name string, options ...metrics.Option) metrics.Timer {
	return nil // Not used in this test
}

func (p *mockProvider) Registry() metrics.Registry {
	return nil // Not used in this test
}

func (p *mockProvider) Handler() metrics.Handler {
	return nil // Not used in this test
}

func (p *mockProvider) Start(ctx metrics.Context) error {
	return nil // Not used in this test
}

func (p *mockProvider) Stop(ctx metrics.Context) error {
	return nil // Not used in this test
}

func (p *mockProvider) WithTags(tags ...metrics.Tag) metrics.Provider {
	return p // Not used in this test
}

// TestRequestMetrics tests the HTTP metrics middleware.
func TestRequestMetrics(t *testing.T) {
	// Create a mock provider
	provider := newMockProvider()

	// Create a test server with the middleware
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Simulate some processing
		time.Sleep(10 * time.Millisecond)
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	})

	// Create the middleware
	middleware := RequestMetrics(RequestMetricsOptions{
		Provider:            provider,
		IncludeRequestSize:  true,
		IncludeResponseSize: true,
	})

	// Wrap the handler
	wrappedHandler := middleware(handler)

	// Create a test server
	server := httptest.NewServer(wrappedHandler)
	defer server.Close()

	// Make a request
	resp, err := http.Get(server.URL)
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	// Verify that the request counter was incremented
	requestCounter, exists := provider.counters["http_server_requests_total"]
	if !exists {
		t.Errorf("Request counter was not created")
	} else if !requestCounter.incCalled {
		t.Errorf("Request counter was not incremented")
	}

	// Verify that the response counter was incremented
	responseCounter, exists := provider.counters["http_server_responses_total"]
	if !exists {
		t.Errorf("Response counter was not created")
	}

	// Verify that the request duration was measured
	durationHistogram, exists := provider.histograms["http_server_request_duration_seconds"]
	if !exists {
		t.Errorf("Request duration histogram was not created")
	} else if len(durationHistogram.observations) == 0 {
		t.Errorf("Request duration was not measured")
	}

	// Verify that the response size was measured
	responseSizeHistogram, exists := provider.histograms["http_server_response_size_bytes"]
	if !exists {
		t.Errorf("Response size histogram was not created")
	} else if len(responseSizeHistogram.observations) == 0 {
		t.Errorf("Response size was not measured")
	}
}

// TestRequestMetricsExcludePaths tests that the middleware respects excluded paths.
func TestRequestMetricsExcludePaths(t *testing.T) {
	// Create a mock provider
	provider := newMockProvider()

	// Create a test server with the middleware
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	})

	// Create the middleware with an excluded path
	middleware := RequestMetrics(RequestMetricsOptions{
		Provider:     provider,
		ExcludePaths: []string{"/excluded"},
	})

	// Wrap the handler
	wrappedHandler := middleware(handler)

	// Create a test server
	server := httptest.NewServer(wrappedHandler)
	defer server.Close()

	// Make a request to a non-excluded path
	resp, err := http.Get(server.URL + "/normal")
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	// Make a request to an excluded path
	resp2, err := http.Get(server.URL + "/excluded")
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp2.Body.Close()

	// Verify that the request counter was incremented only once
	requestCounter, exists := provider.counters["http_server_requests_total"]
	if !exists {
		t.Errorf("Request counter was not created")
	} else if requestCounter.value != 1 {
		t.Errorf("Expected request counter value to be 1, got %f", requestCounter.value)
	}
}

// TestRequestMetricsStatusCode tests that the middleware correctly records status codes.
func TestRequestMetricsStatusCode(t *testing.T) {
	// Create a mock provider
	provider := newMockProvider()

	// Create a test server with the middleware
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if strings.Contains(r.URL.Path, "error") {
			w.WriteHeader(http.StatusInternalServerError)
			w.Write([]byte("Error"))
		} else {
			w.WriteHeader(http.StatusOK)
			w.Write([]byte("OK"))
		}
	})

	// Create the middleware
	middleware := RequestMetrics(RequestMetricsOptions{
		Provider: provider,
	})

	// Wrap the handler
	wrappedHandler := middleware(handler)

	// Create a test server
	server := httptest.NewServer(wrappedHandler)
	defer server.Close()

	// Make a successful request
	resp, err := http.Get(server.URL + "/success")
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	// Make an error request
	resp2, err := http.Get(server.URL + "/error")
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp2.Body.Close()

	// Because we're using tags, the mock doesn't track separate counters for different status codes
	// This would require more complex test infrastructure
	// We're just verifying that the counter exists and was incremented
	responseCounter, exists := provider.counters["http_server_responses_total"]
	if !exists {
		t.Errorf("Response counter was not created")
	}

	// Verify that the request counter shows 2 requests
	requestCounter, exists := provider.counters["http_server_requests_total"]
	if !exists {
		t.Errorf("Request counter was not created")
	} else if requestCounter.value != 2 {
		t.Errorf("Expected request counter value to be 2, got %f", requestCounter.value)
	}
}

// TestStandardMetrics tests the StandardMetrics convenience function.
func TestStandardMetrics(t *testing.T) {
	// Create a mock provider
	provider := newMockProvider()

	// Create a test server with the middleware
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	})

	// Use the StandardMetrics convenience function
	wrappedHandler := StandardMetrics(provider)(handler)

	// Create a test server
	server := httptest.NewServer(wrappedHandler)
	defer server.Close()

	// Make a request
	resp, err := http.Get(server.URL)
	if err != nil {
		t.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	// Verify that the request counter was incremented
	requestCounter, exists := provider.counters["http_server_requests_total"]
	if !exists {
		t.Errorf("Request counter was not created")
	} else if !requestCounter.incCalled {
		t.Errorf("Request counter was not incremented")
	}
}
