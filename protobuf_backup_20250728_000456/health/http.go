// file: pkg/health/http.go
package health

import (
	"encoding/json"
	"net/http"
	"path"
)

// healthHandler implements the HTTP handler for health checks.
type healthHandler struct {
	provider Provider
	config   Config
}

// newHealthHandler creates a new health handler.
func newHealthHandler(provider Provider) *healthHandler {
	p, ok := provider.(*provider)
	if !ok {
		// If provider is not the internal provider, use default config
		return &healthHandler{
			provider: provider,
			config:   DefaultConfig(),
		}
	}
	return &healthHandler{
		provider: provider,
		config:   p.config,
	}
}

// ServeHTTP handles HTTP requests for health checks.
func (h *healthHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	// Get the path relative to the base endpoint
	p := path.Clean(r.URL.Path)
	basePath := path.Clean(h.config.Endpoint)
	relativePath := "/"

	// Handle root path
	if p != basePath {
		// Get the relative path
		relativePath = p[len(basePath):]
		if relativePath == "" {
			relativePath = "/"
		}
	}

	switch relativePath {
	case "/", "":
		h.handleAll(w, r)
	case h.config.LivenessPath:
		if h.config.EnableLivenessEndpoint {
			h.handleLiveness(w, r)
		} else {
			http.NotFound(w, r)
		}
	case h.config.ReadinessPath:
		if h.config.EnableReadinessEndpoint {
			h.handleReadiness(w, r)
		} else {
			http.NotFound(w, r)
		}
	case "/details":
		h.handleDetails(w, r)
	default:
		http.NotFound(w, r)
	}
}

// handleAll handles the root health endpoint.
func (h *healthHandler) handleAll(w http.ResponseWriter, r *http.Request) {
	result, err := h.provider.CheckAll(r.Context())
	if err != nil {
		h.handleError(w, err, http.StatusInternalServerError)
		return
	}

	h.writeResponse(w, result)
}

// handleLiveness handles the liveness endpoint.
func (h *healthHandler) handleLiveness(w http.ResponseWriter, r *http.Request) {
	result, err := h.provider.CheckLiveness(r.Context())
	if err != nil {
		h.handleError(w, err, http.StatusInternalServerError)
		return
	}

	h.writeResponse(w, result)
}

// handleReadiness handles the readiness endpoint.
func (h *healthHandler) handleReadiness(w http.ResponseWriter, r *http.Request) {
	result, err := h.provider.CheckReadiness(r.Context())
	if err != nil {
		h.handleError(w, err, http.StatusInternalServerError)
		return
	}

	h.writeResponse(w, result)
}

// handleDetails handles the detailed health endpoint.
func (h *healthHandler) handleDetails(w http.ResponseWriter, r *http.Request) {
	// Check authentication if required
	if h.config.RequireAuthentication {
		// In a real implementation, this would check for authentication
		// This is a placeholder
		auth := r.Header.Get("Authorization")
		if auth == "" {
			h.handleError(w,
				&httpError{"Authentication required", http.StatusUnauthorized},
				http.StatusUnauthorized)
			return
		}
	}

	result, err := h.provider.CheckAll(r.Context())
	if err != nil {
		h.handleError(w, err, http.StatusInternalServerError)
		return
	}

	h.writeDetailedResponse(w, result)
}

// handleError handles an error response.
func (h *healthHandler) handleError(w http.ResponseWriter, err error, status int) {
	// Check if it's an HTTP error
	if he, ok := err.(*httpError); ok {
		status = he.StatusCode
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(map[string]interface{}{
		"status": "ERROR",
		"error":  err.Error(),
	})
}

// writeResponse writes a health check result as a response.
func (h *healthHandler) writeResponse(w http.ResponseWriter, result Result) {
	status := http.StatusOK
	if result.Status() == StatusDown {
		status = http.StatusServiceUnavailable
	} else if result.Status() == StatusDegraded {
		status = http.StatusMultiStatus
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)

	resp := map[string]interface{}{
		"status": result.Status().String(),
	}

	// Add top-level details
	for k, v := range result.Details() {
		resp[k] = v
	}

	json.NewEncoder(w).Encode(resp)
}

// writeDetailedResponse writes a detailed health check result as a response.
func (h *healthHandler) writeDetailedResponse(w http.ResponseWriter, result Result) {
	status := http.StatusOK
	if result.Status() == StatusDown {
		status = http.StatusServiceUnavailable
	} else if result.Status() == StatusDegraded {
		status = http.StatusMultiStatus
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)

	// Build the detailed response
	json.NewEncoder(w).Encode(h.buildDetailedResponse(result))
}

// buildDetailedResponse builds a detailed response from a result.
func (h *healthHandler) buildDetailedResponse(result Result) map[string]interface{} {
	resp := map[string]interface{}{
		"status":    result.Status().String(),
		"timestamp": result.Timestamp().Format("2006-01-02T15:04:05Z07:00"),
	}

	// Add details
	for k, v := range result.Details() {
		resp[k] = v
	}

	// Add children if they exist
	if len(result.Children()) > 0 {
		children := make(map[string]interface{})
		for _, child := range result.Children() {
			check := child.Check()
			if check != nil {
				children[check.Name()] = h.buildChildResponse(child)
			}
		}
		resp["checks"] = children
	}

	// Add error if it exists
	if err := result.Error(); err != nil {
		resp["error"] = err.Error()
	}

	return resp
}

// buildChildResponse builds a response for a child result.
func (h *healthHandler) buildChildResponse(result Result) map[string]interface{} {
	resp := map[string]interface{}{
		"status":    result.Status().String(),
		"timestamp": result.Timestamp().Format("2006-01-02T15:04:05Z07:00"),
	}

	// Add duration
	if result.Duration() > 0 {
		resp["duration"] = result.Duration().String()
	}

	// Add details
	for k, v := range result.Details() {
		resp[k] = v
	}

	// Add error if it exists
	if err := result.Error(); err != nil {
		resp["error"] = err.Error()
	}

	// Add children if they exist
	if len(result.Children()) > 0 {
		children := make(map[string]interface{})
		for _, child := range result.Children() {
			check := child.Check()
			if check != nil {
				children[check.Name()] = h.buildChildResponse(child)
			}
		}
		resp["checks"] = children
	}

	return resp
}

// httpError represents an HTTP error.
type httpError struct {
	Message    string
	StatusCode int
}

// Error returns the error message.
func (e *httpError) Error() string {
	return e.Message
}
