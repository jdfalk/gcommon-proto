// file: pkg/health/kubernetes.go
package health

import (
	"context"
	"net/http"
	"time"
)

// KubernetesProbeConfig defines configuration for Kubernetes health probes.
type KubernetesProbeConfig struct {
	// LivenessPath is the HTTP path for the liveness probe
	LivenessPath string

	// ReadinessPath is the HTTP path for the readiness probe
	ReadinessPath string

	// StartupPath is the HTTP path for the startup probe (Kubernetes 1.16+)
	StartupPath string

	// ProbeTimeout is the timeout for probe checks
	ProbeTimeout time.Duration

	// SuccessStatus is the HTTP status code for successful probes
	SuccessStatus int

	// FailureStatus is the HTTP status code for failed probes
	FailureStatus int
}

// DefaultKubernetesProbeConfig returns the default Kubernetes probe configuration.
func DefaultKubernetesProbeConfig() KubernetesProbeConfig {
	return KubernetesProbeConfig{
		LivenessPath:  "/healthz",
		ReadinessPath: "/readyz",
		StartupPath:   "/startupz",
		ProbeTimeout:  1 * time.Second,
		SuccessStatus: http.StatusOK,
		FailureStatus: http.StatusServiceUnavailable,
	}
}

// KubernetesProbeHandler creates HTTP handlers for Kubernetes health probes.
type KubernetesProbeHandler struct {
	provider Provider
	config   KubernetesProbeConfig
}

// NewKubernetesProbeHandler creates a new Kubernetes probe handler.
func NewKubernetesProbeHandler(provider Provider, config KubernetesProbeConfig) *KubernetesProbeHandler {
	return &KubernetesProbeHandler{
		provider: provider,
		config:   config,
	}
}

// RegisterWithMux registers the Kubernetes probe handlers with the provided HTTP mux.
func (h *KubernetesProbeHandler) RegisterWithMux(mux *http.ServeMux) {
	// Liveness probe
	mux.HandleFunc(h.config.LivenessPath, h.LivenessHandler)

	// Readiness probe
	mux.HandleFunc(h.config.ReadinessPath, h.ReadinessHandler)

	// Startup probe
	mux.HandleFunc(h.config.StartupPath, h.StartupHandler)
}

// LivenessHandler handles Kubernetes liveness probe requests.
func (h *KubernetesProbeHandler) LivenessHandler(w http.ResponseWriter, r *http.Request) {
	ctx, cancel := context.WithTimeout(r.Context(), h.config.ProbeTimeout)
	defer cancel()

	result, err := h.provider.CheckLiveness(ctx)
	h.handleProbeResult(w, result, err)
}

// ReadinessHandler handles Kubernetes readiness probe requests.
func (h *KubernetesProbeHandler) ReadinessHandler(w http.ResponseWriter, r *http.Request) {
	ctx, cancel := context.WithTimeout(r.Context(), h.config.ProbeTimeout)
	defer cancel()

	result, err := h.provider.CheckReadiness(ctx)
	h.handleProbeResult(w, result, err)
}

// StartupHandler handles Kubernetes startup probe requests.
// This is similar to readiness but specifically for initial startup.
func (h *KubernetesProbeHandler) StartupHandler(w http.ResponseWriter, r *http.Request) {
	ctx, cancel := context.WithTimeout(r.Context(), h.config.ProbeTimeout)
	defer cancel()

	// For startup, we use readiness checks as they're most appropriate
	result, err := h.provider.CheckReadiness(ctx)
	h.handleProbeResult(w, result, err)
}

// handleProbeResult processes the result of a health check for a Kubernetes probe.
func (h *KubernetesProbeHandler) handleProbeResult(w http.ResponseWriter, result Result, err error) {
	// Check for execution error
	if err != nil {
		http.Error(w, "Health check execution failed: "+err.Error(), h.config.FailureStatus)
		return
	}

	// Handle status
	if result.Status() == StatusUp {
		w.WriteHeader(h.config.SuccessStatus)
		w.Write([]byte("OK"))
	} else {
		statusCode := h.config.FailureStatus

		// Generate detailed message
		message := "Health check failed with status: " + result.Status().String()
		if result.Error() != nil {
			message += " - " + result.Error().Error()
		}

		http.Error(w, message, statusCode)
	}
}
