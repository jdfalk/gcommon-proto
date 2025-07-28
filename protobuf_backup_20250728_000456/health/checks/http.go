// file: pkg/health/checks/http.go
package checks

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// HTTPCheck is a health check that makes an HTTP request to a dependency.
type HTTPCheck struct {
	*health.BaseCheck
	url            string
	method         string
	timeout        time.Duration
	client         *http.Client
	expectedStatus int
	headers        map[string]string
}

// HTTPCheckOption represents an option for an HTTP check.
type HTTPCheckOption func(*HTTPCheck)

// NewHTTPCheck creates a new HTTP dependency check.
func NewHTTPCheck(url string, options ...HTTPCheckOption) *HTTPCheck {
	c := &HTTPCheck{
		url:            url,
		method:         http.MethodGet,
		expectedStatus: http.StatusOK,
		timeout:        5 * time.Second,
		headers:        make(map[string]string),
	}

	// Create a default client
	c.client = &http.Client{
		Timeout: c.timeout,
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("http-"+url, health.TypeDependency, c.timeout, 60*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the HTTP health check.
func (c *HTTPCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Create the request
	req, err := http.NewRequestWithContext(ctx, c.method, c.url, nil)
	if err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("failed to create request: %w", err)).
			WithDuration(time.Since(startTime)), nil
	}

	// Add headers
	for k, v := range c.headers {
		req.Header.Set(k, v)
	}

	// Execute the request
	resp, err := c.client.Do(req)
	if err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("request failed: %w", err)).
			WithDuration(time.Since(startTime)), nil
	}
	defer resp.Body.Close()

	// Read and discard the response body to properly handle connection reuse
	_, _ = io.Copy(io.Discard, resp.Body)

	// Check the status code
	if resp.StatusCode != c.expectedStatus {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("unexpected status code: %d, expected: %d", resp.StatusCode, c.expectedStatus)).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"url":            c.url,
				"statusCode":     resp.StatusCode,
				"expectedStatus": c.expectedStatus,
			}), nil
	}

	duration := time.Since(startTime)
	return health.NewResult(health.StatusUp).
		WithDuration(duration).
		WithDetails(map[string]interface{}{
			"url":        c.url,
			"statusCode": resp.StatusCode,
			"duration":   duration.String(),
		}), nil
}

// WithMethod sets the HTTP method for the check.
func WithMethod(method string) HTTPCheckOption {
	return func(c *HTTPCheck) {
		c.method = method
	}
}

// WithTimeout sets the timeout for the check.
func WithTimeout(timeout time.Duration) HTTPCheckOption {
	return func(c *HTTPCheck) {
		c.timeout = timeout
		c.client.Timeout = timeout
	}
}

// WithExpectedStatus sets the expected status code for the check.
func WithExpectedStatus(statusCode int) HTTPCheckOption {
	return func(c *HTTPCheck) {
		c.expectedStatus = statusCode
	}
}

// WithHeader adds a header to the HTTP request.
func WithHeader(key, value string) HTTPCheckOption {
	return func(c *HTTPCheck) {
		c.headers[key] = value
	}
}

// WithClient sets the HTTP client for the check.
func WithClient(client *http.Client) HTTPCheckOption {
	return func(c *HTTPCheck) {
		c.client = client
	}
}
