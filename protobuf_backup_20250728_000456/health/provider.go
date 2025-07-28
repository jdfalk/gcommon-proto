// file: pkg/health/provider.go
package health

import (
	"context"
	"fmt"
	"net/http"
	"sync"
	"time"
)

// DefaultConfig returns the default configuration for a health provider.
func DefaultConfig() Config {
	return Config{
		Enabled:                 true,
		Endpoint:                "/health",
		LivenessPath:            "/live",
		ReadinessPath:           "/ready",
		DetailsPath:             "/details",
		EnableLivenessEndpoint:  true,
		EnableReadinessEndpoint: true,
		RequireAuthentication:   false,
		AuthHeader:              "",
		AuthFunc:                nil,
		DefaultTimeout:          5 * time.Second,
		CheckInterval:           30 * time.Second,
		LogStatusChanges:        false,
		MetricsEnabled:          false,
	}
}

// provider implements the Provider interface.
type provider struct {
	config    Config
	checks    map[string]Check
	results   map[string]Result
	listeners []Listener
	stopCh    chan struct{}
	mu        sync.RWMutex
}

// NewProvider creates a new health provider.
func NewProvider(config Config) (Provider, error) {
	if config.DefaultTimeout == 0 {
		config.DefaultTimeout = 5 * time.Second
	}
	if config.CheckInterval == 0 {
		config.CheckInterval = 30 * time.Second
	}

	return &provider{
		config:    config,
		checks:    make(map[string]Check),
		results:   make(map[string]Result),
		listeners: make([]Listener, 0),
	}, nil
}

// Register registers a health check.
func (p *provider) Register(name string, check Check, options ...CheckOption) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	if _, exists := p.checks[name]; exists {
		return fmt.Errorf("check already exists: %s", name)
	}

	// Apply options
	for _, opt := range options {
		if err := opt(check); err != nil {
			return err
		}
	}

	p.checks[name] = check
	return nil
}

// Unregister removes a health check.
func (p *provider) Unregister(name string) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	if _, exists := p.checks[name]; !exists {
		return fmt.Errorf("check not found: %s", name)
	}

	delete(p.checks, name)
	delete(p.results, name)
	return nil
}

// Get retrieves a health check.
func (p *provider) Get(name string) (Check, bool) {
	p.mu.RLock()
	defer p.mu.RUnlock()

	check, exists := p.checks[name]
	return check, exists
}

// CheckAll runs all health checks.
func (p *provider) CheckAll(ctx context.Context) (Result, error) {
	p.mu.RLock()
	checks := make([]Check, 0, len(p.checks))
	for _, check := range p.checks {
		if check.Enabled() {
			checks = append(checks, check)
		}
	}
	p.mu.RUnlock()

	results := make([]Result, 0, len(checks))
	for _, check := range checks {
		checkCtx, cancel := context.WithTimeout(ctx, check.Timeout())
		result, err := check.Execute(checkCtx)
		cancel()

		if err != nil {
			result = NewResult(StatusDown).
				WithCheck(check).
				WithError(err)
		}

		results = append(results, result)
		p.updateResult(check.Name(), result)
	}

	status := ComputeAggregateStatus(results)

	return NewResult(status).
		WithChildren(results).
		WithDetails(map[string]interface{}{
			"total":     len(checks),
			"up":        countStatus(results, StatusUp),
			"down":      countStatus(results, StatusDown),
			"degraded":  countStatus(results, StatusDegraded),
			"unknown":   countStatus(results, StatusUnknown),
			"timestamp": time.Now().Format(time.RFC3339),
		}), nil
}

// CheckLiveness runs liveness checks.
func (p *provider) CheckLiveness(ctx context.Context) (Result, error) {
	return p.checkByType(ctx, TypeLiveness)
}

// CheckReadiness runs readiness checks.
func (p *provider) CheckReadiness(ctx context.Context) (Result, error) {
	return p.checkByType(ctx, TypeReadiness)
}

// checkByType runs checks of a specific type.
func (p *provider) checkByType(ctx context.Context, checkType CheckType) (Result, error) {
	p.mu.RLock()
	checks := make([]Check, 0)
	for _, check := range p.checks {
		if check.Enabled() && check.Type() == checkType {
			checks = append(checks, check)
		}
	}
	p.mu.RUnlock()

	results := make([]Result, 0, len(checks))
	for _, check := range checks {
		checkCtx, cancel := context.WithTimeout(ctx, check.Timeout())
		result, err := check.Execute(checkCtx)
		cancel()

		if err != nil {
			result = NewResult(StatusDown).
				WithCheck(check).
				WithError(err)
		}

		results = append(results, result)
		p.updateResult(check.Name(), result)
	}

	status := ComputeAggregateStatus(results)

	return NewResult(status).
		WithChildren(results).
		WithDetails(map[string]interface{}{
			"type":      checkType.String(),
			"total":     len(checks),
			"up":        countStatus(results, StatusUp),
			"down":      countStatus(results, StatusDown),
			"degraded":  countStatus(results, StatusDegraded),
			"unknown":   countStatus(results, StatusUnknown),
			"timestamp": time.Now().Format(time.RFC3339),
		}), nil
}

// Handler returns an HTTP handler for health checks.
func (p *provider) Handler() http.Handler {
	return newHealthHandler(p)
}

// Start starts background health checking.
func (p *provider) Start(ctx context.Context) error {
	if !p.config.Enabled {
		return nil
	}

	p.mu.Lock()
	if p.stopCh != nil {
		p.mu.Unlock()
		return fmt.Errorf("already started")
	}
	p.stopCh = make(chan struct{})
	p.mu.Unlock()

	go p.run(ctx)
	return nil
}

// Stop stops background health checking.
func (p *provider) Stop(ctx context.Context) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	if p.stopCh == nil {
		return nil
	}

	close(p.stopCh)
	p.stopCh = nil

	return nil
}

// AddListener adds a listener for health status changes.
func (p *provider) AddListener(listener Listener) error {
	if listener == nil {
		return fmt.Errorf("listener cannot be nil")
	}

	p.mu.Lock()
	defer p.mu.Unlock()

	p.listeners = append(p.listeners, listener)
	return nil
}

// RemoveListener removes a listener.
func (p *provider) RemoveListener(listener Listener) error {
	p.mu.Lock()
	defer p.mu.Unlock()

	for i, l := range p.listeners {
		if l == listener {
			p.listeners = append(p.listeners[:i], p.listeners[i+1:]...)
			return nil
		}
	}

	return fmt.Errorf("listener not found")
}

// run runs the background health checking loop.
func (p *provider) run(ctx context.Context) {
	ticker := time.NewTicker(p.config.CheckInterval)
	defer ticker.Stop()

	for {
		select {
		case <-p.stopCh:
			return
		case <-ctx.Done():
			return
		case <-ticker.C:
			_, _ = p.CheckAll(ctx)
		}
	}
}

// updateResult updates a check result and notifies listeners if the status changed.
func (p *provider) updateResult(name string, result Result) {
	p.mu.Lock()
	defer p.mu.Unlock()

	previous, exists := p.results[name]
	p.results[name] = result

	// If the status changed, notify listeners
	if exists && previous.Status() != result.Status() && len(p.listeners) > 0 {
		// Copy listeners to avoid holding the lock during callbacks
		listeners := make([]Listener, len(p.listeners))
		copy(listeners, p.listeners)

		// Release the lock before notifying listeners
		p.mu.Unlock()

		// Notify listeners
		for _, listener := range listeners {
			listener.OnStatusChange(name, previous, result)
		}

		// Re-acquire the lock
		p.mu.Lock()
	}
}

// countStatus counts the number of results with the given status.
func countStatus(results []Result, status Status) int {
	count := 0
	for _, r := range results {
		if r.Status() == status {
			count++
		}
	}
	return count
}
