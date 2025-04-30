// file: pkg/health/check.go
package health

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// baseCheck provides a base implementation of Check.
type baseCheck struct {
	name      string
	checkType CheckType
	timeout   time.Duration
	interval  time.Duration
	enabled   bool
	mu        sync.RWMutex
}

// newBaseCheck creates a new base check.
func newBaseCheck(name string, checkType CheckType, timeout, interval time.Duration) *baseCheck {
	return &baseCheck{
		name:      name,
		checkType: checkType,
		timeout:   timeout,
		interval:  interval,
		enabled:   true,
	}
}

// Name returns the check name.
func (c *baseCheck) Name() string {
	return c.name
}

// Type returns the check type.
func (c *baseCheck) Type() CheckType {
	return c.checkType
}

// Timeout returns the check timeout.
func (c *baseCheck) Timeout() time.Duration {
	return c.timeout
}

// Interval returns the check interval.
func (c *baseCheck) Interval() time.Duration {
	return c.interval
}

// Enabled returns whether the check is enabled.
func (c *baseCheck) Enabled() bool {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.enabled
}

// SetEnabled sets whether the check is enabled.
func (c *baseCheck) SetEnabled(enabled bool) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.enabled = enabled
}

// Execute runs the health check (to be implemented by specific checks).
func (c *baseCheck) Execute(ctx context.Context) (Result, error) {
	return NewResult(StatusUnknown), fmt.Errorf("execute not implemented")
}

// WithType sets the check type.
func WithType(checkType CheckType) CheckOption {
	return func(c Check) error {
		if bc, ok := c.(*baseCheck); ok {
			bc.checkType = checkType
		}
		return nil
	}
}

// WithTimeout sets the check timeout.
func WithTimeout(timeout time.Duration) CheckOption {
	return func(c Check) error {
		if bc, ok := c.(*baseCheck); ok {
			bc.timeout = timeout
		}
		return nil
	}
}

// WithInterval sets the check interval.
func WithInterval(interval time.Duration) CheckOption {
	return func(c Check) error {
		if bc, ok := c.(*baseCheck); ok {
			bc.interval = interval
		}
		return nil
	}
}

// WithEnabled sets whether the check is enabled.
func WithEnabled(enabled bool) CheckOption {
	return func(c Check) error {
		c.SetEnabled(enabled)
		return nil
	}
}

// compositeCheck is a check that composes multiple child checks.
type compositeCheck struct {
	*baseCheck
	checks []Check
	mu     sync.RWMutex
}

// NewCompositeCheck creates a new composite check.
func NewCompositeCheck(name string, options ...CheckOption) *compositeCheck {
	c := &compositeCheck{
		baseCheck: newBaseCheck(name, TypeComponent, 30*time.Second, 60*time.Second),
		checks:    []Check{},
	}

	for _, opt := range options {
		_ = opt(c)
	}

	return c
}

// Execute runs the composite health check.
func (c *compositeCheck) Execute(ctx context.Context) (Result, error) {
	c.mu.RLock()
	checks := make([]Check, len(c.checks))
	copy(checks, c.checks)
	c.mu.RUnlock()

	if !c.Enabled() {
		return NewResult(StatusUnknown).
			WithCheck(c).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()
	results := make([]Result, 0, len(checks))

	for _, check := range checks {
		if !check.Enabled() {
			continue
		}

		checkCtx, cancel := context.WithTimeout(ctx, check.Timeout())
		result, err := check.Execute(checkCtx)
		cancel()

		if err != nil {
			result = NewResult(StatusDown).
				WithCheck(check).
				WithError(err)
		}

		results = append(results, result)
	}

	status := ComputeAggregateStatus(results)
	duration := time.Since(startTime)

	return NewResult(status).
		WithCheck(c).
		WithChildren(results).
		WithDuration(duration).
		WithDetails(map[string]interface{}{
			"checkCount": len(checks),
			"results":    len(results),
		}), nil
}

// AddChecks adds child checks to the composite check.
func (c *compositeCheck) AddChecks(checks ...Check) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.checks = append(c.checks, checks...)
}

// RemoveCheck removes a child check from the composite check.
func (c *compositeCheck) RemoveCheck(name string) bool {
	c.mu.Lock()
	defer c.mu.Unlock()

	for i, check := range c.checks {
		if check.Name() == name {
			c.checks = append(c.checks[:i], c.checks[i+1:]...)
			return true
		}
	}

	return false
}

// Checks returns the child checks.
func (c *compositeCheck) Checks() []Check {
	c.mu.RLock()
	defer c.mu.RUnlock()

	checks := make([]Check, len(c.checks))
	copy(checks, c.checks)

	return checks
}

// simpleCheck implements a simple check with a check function.
type simpleCheck struct {
	*baseCheck
	checkFunc CheckFunc
	remediationFunc RemediationFunc
}

// NewSimpleCheck creates a new simple check.
func NewSimpleCheck(name string, fn CheckFunc, options ...CheckOption) *simpleCheck {
	c := &simpleCheck{
		baseCheck: newBaseCheck(name, TypeComponent, 5*time.Second, 60*time.Second),
		checkFunc: fn,
	}

	for _, opt := range options {
		_ = opt(c)
	}

	return c
}

// Execute runs the simple health check.
func (c *simpleCheck) Execute(ctx context.Context) (Result, error) {
	if !c.Enabled() {
		return NewResult(StatusUnknown).
			WithCheck(c).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()
	result, err := c.checkFunc(ctx)
	duration := time.Since(startTime)

	// If there's an error and no result, create a result
	if err != nil && result == nil {
		result = NewResult(StatusDown).WithError(err)
	}

	// If there's a result, add the check and duration
	if result != nil {
		result = result.WithCheck(c).WithDuration(duration)
	} else {
		result = NewResult(StatusUnknown).
			WithCheck(c).
			WithDuration(duration).
			WithError(fmt.Errorf("check returned nil result"))
	}

	return result, nil
}

// WithRemediation sets the remediation function for the check.
func WithRemediation(fn RemediationFunc) CheckOption {
	return func(c Check) error {
		if sc, ok := c.(*simpleCheck); ok {
			sc.remediationFunc = fn
		}
		return nil
	}
}

// Remediate attempts to remediate a failed check.
func (c *simpleCheck) Remediate(ctx context.Context, result Result) error {
	if c.remediationFunc != nil {
		return c.remediationFunc(ctx, result)
	}
	return fmt.Errorf("no remediation function defined")
}
