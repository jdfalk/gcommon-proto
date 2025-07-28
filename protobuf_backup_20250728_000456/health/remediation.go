// file: pkg/health/remediation.go
package health

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// RemediationStrategy defines how remediation attempts should be executed.
type RemediationStrategy int

const (
	// RemediationStrategyNone indicates no remediation should be attempted.
	RemediationStrategyNone RemediationStrategy = iota

	// RemediationStrategySingle indicates a single remediation attempt should be made.
	RemediationStrategySingle

	// RemediationStrategyExponential indicates remediation should be attempted with exponential backoff.
	RemediationStrategyExponential

	// RemediationStrategyConstant indicates remediation should be attempted at a constant interval.
	RemediationStrategyConstant
)

// RemediationConfig defines the configuration for a remediation manager.
type RemediationConfig struct {
	// Strategy defines the remediation strategy.
	Strategy RemediationStrategy

	// MaxAttempts defines the maximum number of remediation attempts.
	MaxAttempts int

	// InitialDelay defines the initial delay between remediation attempts.
	// For exponential backoff, this is the starting delay.
	InitialDelay time.Duration

	// MaxDelay defines the maximum delay between remediation attempts.
	// Only applicable for exponential backoff.
	MaxDelay time.Duration

	// BackoffFactor defines the factor by which delays increase in exponential backoff.
	// Only applicable for exponential backoff.
	BackoffFactor float64

	// OnRemediationStart is a callback executed when remediation starts.
	OnRemediationStart func(name string, attempt int)

	// OnRemediationSuccess is a callback executed when remediation succeeds.
	OnRemediationSuccess func(name string, attempt int)

	// OnRemediationFailure is a callback executed when remediation fails.
	OnRemediationFailure func(name string, attempt int, err error)

	// OnRemediationExhausted is a callback executed when remediation attempts are exhausted.
	OnRemediationExhausted func(name string, attempts int)
}

// DefaultRemediationConfig returns the default remediation configuration.
func DefaultRemediationConfig() RemediationConfig {
	return RemediationConfig{
		Strategy:      RemediationStrategyExponential,
		MaxAttempts:   3,
		InitialDelay:  1 * time.Second,
		MaxDelay:      1 * time.Minute,
		BackoffFactor: 2.0,
		OnRemediationStart: func(name string, attempt int) {
			// Default behavior is to do nothing
		},
		OnRemediationSuccess: func(name string, attempt int) {
			// Default behavior is to do nothing
		},
		OnRemediationFailure: func(name string, attempt int, err error) {
			// Default behavior is to do nothing
		},
		OnRemediationExhausted: func(name string, attempts int) {
			// Default behavior is to do nothing
		},
	}
}

// RemediableCheck represents a health check that can be remediated.
type RemediableCheck interface {
	Check
	Remediate(ctx context.Context, result Result) error
}

// CheckIsRemediable returns whether a check is remediable.
func CheckIsRemediable(check Check) bool {
	_, ok := check.(RemediableCheck)
	return ok
}

// remediationManager manages remediation for health checks.
type remediationManager struct {
	config       RemediationConfig
	provider     Provider
	remediations map[string]*remediationState
	mu           sync.RWMutex
	stopCh       chan struct{}
	stoppedCh    chan struct{}
	hasStarted   bool
}

// remediationState tracks the state of remediation for a check.
type remediationState struct {
	check        RemediableCheck
	lastResult   Result
	attempts     int
	nextAttempt  time.Time
	exponential  bool
	currentDelay time.Duration
}

// NewRemediationManager creates a new remediation manager.
func NewRemediationManager(provider Provider, config RemediationConfig) *remediationManager {
	return &remediationManager{
		config:       config,
		provider:     provider,
		remediations: make(map[string]*remediationState),
		stopCh:       make(chan struct{}),
		stoppedCh:    make(chan struct{}),
	}
}

// Start starts the remediation manager.
func (m *remediationManager) Start(ctx context.Context) error {
	m.mu.Lock()
	if m.hasStarted {
		m.mu.Unlock()
		return fmt.Errorf("remediation manager already started")
	}
	m.hasStarted = true
	m.mu.Unlock()

	// Register as a health check listener
	if err := m.provider.AddListener(m); err != nil {
		return fmt.Errorf("failed to register remediation manager as listener: %w", err)
	}

	// Start the remediation loop
	go m.run(ctx)

	return nil
}

// Stop stops the remediation manager.
func (m *remediationManager) Stop(ctx context.Context) error {
	m.mu.Lock()
	if !m.hasStarted {
		m.mu.Unlock()
		return nil
	}
	m.hasStarted = false
	close(m.stopCh)
	m.mu.Unlock()

	// Unregister as a health check listener
	if err := m.provider.RemoveListener(m); err != nil {
		return fmt.Errorf("failed to unregister remediation manager as listener: %w", err)
	}

	// Wait for the remediation loop to stop
	select {
	case <-m.stoppedCh:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

// OnStatusChange is called when a health check status changes.
func (m *remediationManager) OnStatusChange(name string, previous, current Result) {
	// Only act on status changes to DOWN
	if current.Status() != StatusDown {
		// If the check was previously in remediation and now it's recovered,
		// remove it from the remediation map
		m.mu.Lock()
		delete(m.remediations, name)
		m.mu.Unlock()
		return
	}

	// Skip if remediation is disabled
	if m.config.Strategy == RemediationStrategyNone {
		return
	}

	// Get the check
	check, exists := m.provider.Get(name)
	if !exists {
		return
	}

	// Check if the check is remediable
	remediableCheck, ok := check.(RemediableCheck)
	if !ok {
		return
	}

	// Add to the remediation map
	m.mu.Lock()
	defer m.mu.Unlock()

	// Skip if already being remediated
	if _, exists := m.remediations[name]; exists {
		return
	}

	m.remediations[name] = &remediationState{
		check:        remediableCheck,
		lastResult:   current,
		attempts:     0,
		nextAttempt:  time.Now().Add(m.config.InitialDelay),
		exponential:  m.config.Strategy == RemediationStrategyExponential,
		currentDelay: m.config.InitialDelay,
	}
}

// run is the main remediation loop.
func (m *remediationManager) run(ctx context.Context) {
	ticker := time.NewTicker(1 * time.Second)
	defer func() {
		ticker.Stop()
		close(m.stoppedCh)
	}()

	for {
		select {
		case <-m.stopCh:
			return
		case <-ctx.Done():
			return
		case <-ticker.C:
			m.processRemediations(ctx)
		}
	}
}

// processRemediations processes pending remediations.
func (m *remediationManager) processRemediations(ctx context.Context) {
	now := time.Now()
	toRemediate := make([]*remediationState, 0)

	// First, collect checks that need remediation
	m.mu.Lock()
	for name, state := range m.remediations {
		if now.After(state.nextAttempt) && state.attempts < m.config.MaxAttempts {
			toRemediate = append(toRemediate, state)
			state.attempts++

			// Calculate next attempt time based on strategy
			if state.exponential {
				factor := float64(state.attempts) * m.config.BackoffFactor
				nextDelay := time.Duration(float64(m.config.InitialDelay) * factor)
				if nextDelay > m.config.MaxDelay {
					nextDelay = m.config.MaxDelay
				}
				state.currentDelay = nextDelay
			}
			state.nextAttempt = now.Add(state.currentDelay)
		} else if state.attempts >= m.config.MaxAttempts {
			// Remediation attempts exhausted
			if m.config.OnRemediationExhausted != nil {
				m.config.OnRemediationExhausted(name, state.attempts)
			}
			delete(m.remediations, name)
		}
	}
	m.mu.Unlock()

	// Then, attempt remediation for each check
	for _, state := range toRemediate {
		checkName := state.check.Name()

		// Notify remediation start
		if m.config.OnRemediationStart != nil {
			m.config.OnRemediationStart(checkName, state.attempts)
		}

		// Attempt remediation
		err := state.check.Remediate(ctx, state.lastResult)

		// Handle result
		m.mu.Lock()
		if err != nil {
			// Remediation failed
			if m.config.OnRemediationFailure != nil {
				m.config.OnRemediationFailure(checkName, state.attempts, err)
			}
		} else {
			// Remediation succeeded
			if m.config.OnRemediationSuccess != nil {
				m.config.OnRemediationSuccess(checkName, state.attempts)
			}

			// Re-run check to verify remediation worked
			checkCtx, cancel := context.WithTimeout(ctx, state.check.Timeout())
			newResult, checkErr := state.check.Execute(checkCtx)
			cancel()

			if checkErr == nil && newResult.Status() != StatusDown {
				// Remediation was successful
				delete(m.remediations, checkName)
			} else {
				// Remediation didn't fix the issue, update last result
				state.lastResult = newResult
			}
		}
		m.mu.Unlock()
	}
}

// GetRemediationStatus returns the current remediation status for a check.
func (m *remediationManager) GetRemediationStatus(name string) (bool, int, time.Time) {
	m.mu.RLock()
	defer m.mu.RUnlock()

	state, exists := m.remediations[name]
	if !exists {
		return false, 0, time.Time{}
	}

	return true, state.attempts, state.nextAttempt
}

// GetAllRemediationStatuses returns the current remediation statuses for all checks.
func (m *remediationManager) GetAllRemediationStatuses() map[string]struct {
	Attempts    int
	NextAttempt time.Time
} {
	m.mu.RLock()
	defer m.mu.RUnlock()

	result := make(map[string]struct {
		Attempts    int
		NextAttempt time.Time
	})

	for name, state := range m.remediations {
		result[name] = struct {
			Attempts    int
			NextAttempt time.Time
		}{
			Attempts:    state.attempts,
			NextAttempt: state.nextAttempt,
		}
	}

	return result
}
