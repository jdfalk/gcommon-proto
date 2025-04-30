// file: pkg/health/checks/remediable_http.go
package checks

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"strings"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// RemediableHTTPCheck is an HTTP health check that can automatically remediate common failures.
type RemediableHTTPCheck struct {
	*HTTPCheck
	maxRetries       int           // Maximum number of retries during remediation
	retryDelay       time.Duration // Delay between retries
	allowedStatusCodes []int       // Status codes that are considered successful (in addition to expectedStatus)
	alternateURLs    []string      // Alternate URLs to try if primary fails
	customHeaders    map[string]string // Custom headers to send during remediation
	onBeforeRemediate func(ctx context.Context, result health.Result) // Called before remediation
	onAfterRemediate  func(ctx context.Context, result health.Result, err error) // Called after remediation
}

// RemediableHTTPCheckOption represents an option for a remediable HTTP check.
type RemediableHTTPCheckOption func(*RemediableHTTPCheck)

// NewRemediableHTTPCheck creates a new remediable HTTP check.
func NewRemediableHTTPCheck(url string, options ...interface{}) *RemediableHTTPCheck {
	// Process standard HTTP check options
	var httpOptions []HTTPCheckOption
	var remediableOptions []RemediableHTTPCheckOption

	for _, opt := range options {
		switch o := opt.(type) {
		case HTTPCheckOption:
			httpOptions = append(httpOptions, o)
		case RemediableHTTPCheckOption:
			remediableOptions = append(remediableOptions, o)
		}
	}

	c := &RemediableHTTPCheck{
		HTTPCheck:    NewHTTPCheck(url, httpOptions...),
		maxRetries:   3,
		retryDelay:   500 * time.Millisecond,
		customHeaders: make(map[string]string),
	}

	// Apply remediable options
	for _, opt := range remediableOptions {
		opt(c)
	}

	return c
}

// Remediate attempts to remediate a failed HTTP check.
func (c *RemediableHTTPCheck) Remediate(ctx context.Context, result health.Result) error {
	// Call the before remediation callback if set
	if c.onBeforeRemediate != nil {
		c.onBeforeRemediate(ctx, result)
	}

	var lastErr error
	var success bool

	// First remediation strategy: retry the original URL with increasing timeouts
	for i := 0; i < c.maxRetries; i++ {
		// Delay between retries, except for the first one
		if i > 0 {
			select {
			case <-time.After(c.retryDelay):
				// Continue with retry
			case <-ctx.Done():
				lastErr = ctx.Err()
				goto done
			}
		}

		// Try with a longer timeout
		client := &http.Client{
			Timeout: c.timeout * time.Duration(i+2),
		}

		// Create the request with the original URL
		req, err := http.NewRequestWithContext(ctx, c.method, c.url, nil)
		if err != nil {
			lastErr = fmt.Errorf("failed to create request: %w", err)
			continue
		}

		// Add all headers
		for k, v := range c.headers {
			req.Header.Set(k, v)
		}
		for k, v := range c.customHeaders {
			req.Header.Set(k, v)
		}

		// Execute the request
		resp, err := client.Do(req)
		if err != nil {
			lastErr = fmt.Errorf("request failed: %w", err)
			continue
		}

		// Check the status code
		if resp.StatusCode == c.expectedStatus || containsInt(c.allowedStatusCodes, resp.StatusCode) {
			// Request was successful
			resp.Body.Close()
			success = true
			break
		}

		// Read response body for error details
		body, _ := io.ReadAll(resp.Body)
		resp.Body.Close()
		lastErr = fmt.Errorf("unexpected status code: %d, body: %s", resp.StatusCode, truncateString(string(body), 100))
	}

	// If first strategy failed and we have alternate URLs, try them
	if !success && len(c.alternateURLs) > 0 {
		for _, url := range c.alternateURLs {
			req, err := http.NewRequestWithContext(ctx, c.method, url, nil)
			if err != nil {
				lastErr = fmt.Errorf("failed to create request for alternate URL: %w", err)
				continue
			}

			// Add all headers
			for k, v := range c.headers {
				req.Header.Set(k, v)
			}
			for k, v := range c.customHeaders {
				req.Header.Set(k, v)
			}

			// Execute the request
			client := &http.Client{
				Timeout: c.timeout * 2,
			}
			resp, err := client.Do(req)
			if err != nil {
				lastErr = fmt.Errorf("request to alternate URL failed: %w", err)
				continue
			}

			// Check the status code
			if resp.StatusCode == c.expectedStatus || containsInt(c.allowedStatusCodes, resp.StatusCode) {
				// Alternate URL was successful
				resp.Body.Close()

				// Switch to this URL for future checks
				c.url = url
				success = true
				break
			}

			// Read response body for error details
			body, _ := io.ReadAll(resp.Body)
			resp.Body.Close()
			lastErr = fmt.Errorf("unexpected status code from alternate URL: %d, body: %s", resp.StatusCode, truncateString(string(body), 100))
		}
	}

done:
	// Call the after remediation callback if set
	if c.onAfterRemediate != nil {
		c.onAfterRemediate(ctx, result, lastErr)
	}

	if success {
		return nil
	}
	return lastErr
}

// WithMaxRetries sets the maximum number of retries for remediation.
func WithMaxRetries(count int) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		if count > 0 {
			c.maxRetries = count
		}
	}
}

// WithRetryDelay sets the delay between retries for remediation.
func WithRetryDelay(delay time.Duration) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		if delay > 0 {
			c.retryDelay = delay
		}
	}
}

// WithAllowedStatusCodes sets additional status codes that are considered successful.
func WithAllowedStatusCodes(codes ...int) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		c.allowedStatusCodes = codes
	}
}

// WithAlternateURLs sets alternate URLs to try if the primary URL fails.
func WithAlternateURLs(urls ...string) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		c.alternateURLs = urls
	}
}

// WithRemediationHeaders sets custom headers to send during remediation.
func WithRemediationHeaders(headers map[string]string) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		for k, v := range headers {
			c.customHeaders[k] = v
		}
	}
}

// WithBeforeRemediateCallback sets a callback function to be executed before remediation.
func WithBeforeRemediateCallback(fn func(ctx context.Context, result health.Result)) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		c.onBeforeRemediate = fn
	}
}

// WithAfterRemediateCallback sets a callback function to be executed after remediation.
func WithAfterRemediateCallback(fn func(ctx context.Context, result health.Result, err error)) RemediableHTTPCheckOption {
	return func(c *RemediableHTTPCheck) {
		c.onAfterRemediate = fn
	}
}

// Helper functions

// containsInt checks if a slice contains a specific integer.
func containsInt(slice []int, value int) bool {
	for _, v := range slice {
		if v == value {
			return true
		}
	}
	return false
}

// truncateString truncates a string to the given maximum length.
func truncateString(s string, maxLength int) string {
	if len(s) <= maxLength {
		return s
	}
	return s[:maxLength] + "..."
}
