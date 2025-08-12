package middleware

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/jdfalk/gcommon/pkg/metrics"
	"github.com/jdfalk/gcommon/pkg/metrics/mock"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock as testmock"
)

func TestHTTPMetricsMiddleware(t *testing.T) {
	// Create mock provider and metrics
	mockProvider := mock.NewMockProvider(t)
	mockCounter := mock.NewMockCounter(t)
	mockHistogram := mock.NewMockHistogram(t)

	// Setup expectations
	mockProvider.On("Counter", "http_requests_total", []metrics.Option(nil)).Return(mockCounter)
	mockProvider.On("Histogram", "http_request_duration_seconds", []metrics.Option(nil)).Return(mockHistogram)

	mockCounter.On("WithTags", testmock.MatchedBy(func(tags []metrics.Tag) bool {
		return len(tags) >= 2 // method and status code tags
	})).Return(mockCounter)
	mockCounter.On("Inc").Return()

	mockHistogram.On("WithTags", testmock.MatchedBy(func(tags []metrics.Tag) bool {
		return len(tags) >= 1 // method tag
	})).Return(mockHistogram)
	mockHistogram.On("Observe", testmock.AnythingOfType("float64")).Return()

	// Create middleware
	middleware := HTTPMetrics(HTTPMetricsOptions{Provider: mockProvider})

	// Create test handler
	handler := middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	}))

	// Create test request
	req := httptest.NewRequest("GET", "/test", nil)
	w := httptest.NewRecorder()

	// Execute request
	handler.ServeHTTP(w, req)

	// Verify response
	assert.Equal(t, http.StatusOK, w.Code)
	assert.Equal(t, "OK", w.Body.String())

	// Verify mock expectations
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockHistogram.AssertExpectations(t)
}

func TestHTTPMetricsMiddleware_ErrorStatus(t *testing.T) {
	// Create mock provider and metrics
	mockProvider := mock.NewMockProvider(t)
	mockCounter := mock.NewMockCounter(t)
	mockHistogram := mock.NewMockHistogram(t)

	// Setup expectations
	mockProvider.On("Counter", "http_requests_total", []metrics.Option(nil)).Return(mockCounter)
	mockProvider.On("Histogram", "http_request_duration_seconds", []metrics.Option(nil)).Return(mockHistogram)

	mockCounter.On("WithTags", testmock.MatchedBy(func(tags []metrics.Tag) bool {
		for _, tag := range tags {
			if tag.Key == "status" && tag.Value == "500" {
				return true
			}
		}
		return false
	})).Return(mockCounter)
	mockCounter.On("Inc").Return()

	mockHistogram.On("WithTags", testmock.MatchedBy(func(tags []metrics.Tag) bool {
		return len(tags) >= 1
	})).Return(mockHistogram)
	mockHistogram.On("Observe", testmock.AnythingOfType("float64")).Return()

	// Create middleware
	middleware := HTTPMetrics(HTTPMetricsOptions{Provider: mockProvider})

	// Create test handler that returns 500
	handler := middleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("Error"))
	}))

	// Create test request
	req := httptest.NewRequest("POST", "/error", nil)
	w := httptest.NewRecorder()

	// Execute request
	handler.ServeHTTP(w, req)

	// Verify response
	assert.Equal(t, http.StatusInternalServerError, w.Code)
	assert.Equal(t, "Error", w.Body.String())

	// Verify mock expectations
	mockProvider.AssertExpectations(t)
	mockCounter.AssertExpectations(t)
	mockHistogram.AssertExpectations(t)
}
