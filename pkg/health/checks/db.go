// file: pkg/health/checks/db.go
package checks

import (
	"context"
	"database/sql"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// DBCheck is a health check that verifies database connectivity.
// It executes a query (typically "SELECT 1") to check if the database is responsive.
type DBCheck struct {
	*health.BaseCheck
	db        *sql.DB       // Database connection
	query     string        // Query to execute for health check
	timeout   time.Duration // Timeout for the database query
	threshold time.Duration // Threshold for slow query warning
}

// DBCheckOption represents an option for a database health check.
type DBCheckOption func(*DBCheck)

// NewDBCheck creates a new database health check.
// It verifies connectivity to the database by executing a simple query.
func NewDBCheck(db *sql.DB, options ...DBCheckOption) *DBCheck {
	c := &DBCheck{
		db:        db,
		query:     "SELECT 1",
		timeout:   5 * time.Second,
		threshold: 1 * time.Second,
	}

	// Initialize the base check
	c.BaseCheck = health.NewBaseCheck("database", health.TypeDependency, c.timeout, 60*time.Second)

	// Apply options
	for _, opt := range options {
		opt(c)
	}

	return c
}

// Execute runs the database health check by executing a query.
func (c *DBCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	if c.db == nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("database connection is nil")), nil
	}

	startTime := time.Now()
	details := map[string]interface{}{
		"query": c.query,
	}

	// Create a context with timeout
	queryCtx, cancel := context.WithTimeout(ctx, c.timeout)
	defer cancel()

	// Execute the query
	_, err := c.db.ExecContext(queryCtx, c.query)
	duration := time.Since(startTime)
	details["duration"] = duration.String()

	// Check for errors
	if err != nil {
		details["error"] = err.Error()
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("database query failed: %w", err)).
			WithDuration(duration).
			WithDetails(details), nil
	}

	// Check if query was slow (but still successful)
	result := health.NewResult(health.StatusUp).
		WithDuration(duration).
		WithDetails(details)

	if duration > c.threshold {
		details["warning"] = fmt.Sprintf("query took longer than threshold (%s)", c.threshold)
		return health.NewResult(health.StatusDegraded).
			WithDuration(duration).
			WithDetails(details), nil
	}

	return result, nil
}

// WithQuery sets the query to execute for the health check.
func WithQuery(query string) DBCheckOption {
	return func(c *DBCheck) {
		c.query = query
	}
}

// WithDBTimeout sets the timeout for the database query.
func WithDBTimeout(timeout time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		c.timeout = timeout
	}
}

// WithSlowThreshold sets the threshold for slow query warnings.
// If a query takes longer than this threshold but still succeeds,
// the check will return a degraded status.
func WithSlowThreshold(threshold time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		c.threshold = threshold
	}
}

// WithDBName sets the name for the database check.
// This helps identify which database is being checked when multiple
// database checks are used.
func WithDBName(name string) DBCheckOption {
	return func(c *DBCheck) {
		c.BaseCheck = health.NewBaseCheck("database-"+name, health.TypeDependency, c.timeout, 60*time.Second)
	}
}
