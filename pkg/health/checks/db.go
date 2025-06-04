// file: pkg/health/checks/db.go
package checks

import (
	"context"
	"database/sql"
	"fmt"
	"time"

	"github.com/jdfalk/gcommon/pkg/health"
)

// DBCheck monitors the health of a database connection.
// It executes a query against the database to determine connectivity
// and response time.
type DBCheck struct {
	baseCheck *health.BaseCheck
	db        *sql.DB
	query     string
	timeout   time.Duration
	dbName    string
}

// DBCheckOption is a functional option type for configuring a DBCheck.
type DBCheckOption func(*DBCheck)

// WithDBName sets a custom database name for the check.
func WithDBName(name string) DBCheckOption {
	return func(c *DBCheck) {
		c.dbName = name
	}
}

// WithDBQueryTimeout sets the query timeout.
func WithDBQueryTimeout(timeout time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		if timeout > 0 {
			c.timeout = timeout
		}
	}
}

// WithDBCheckInterval sets the check interval.
func WithDBCheckInterval(interval time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		if interval > 0 {
			c.baseCheck.SetInterval(interval)
		}
	}
}

// WithDBCheckType sets the check type.
func WithDBCheckType(checkType health.CheckType) DBCheckOption {
	return func(c *DBCheck) {
		c.baseCheck.SetType(checkType)
	}
}

// WithDBCheckEnabled sets whether the check is initially enabled.
func WithDBCheckEnabled(enabled bool) DBCheckOption {
	return func(c *DBCheck) {
		c.baseCheck.SetEnabled(enabled)
	}
}

// NewDBCheck creates a new database health check.
//
// Parameters:
//   - name: Unique name for this check
//   - db: The database connection to check
//   - query: The query to execute (defaults to "SELECT 1" if empty)
//   - options: Optional functional options for additional configuration
//
// Returns:
//   - A configured DBCheck instance
func NewDBCheck(name string, db *sql.DB, query string, options ...DBCheckOption) *DBCheck {
	// Use a default query if none provided
	if query == "" {
		query = "SELECT 1"
	}

	check := &DBCheck{
		db:      db,
		query:   query,
		timeout: 5 * time.Second,
		dbName:  "",
	}

	// Initialize the base check
	check.baseCheck = health.NewBaseCheck(name, health.TypeReadiness, check.timeout, 30*time.Second)

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Name returns the check name.
func (c *DBCheck) Name() string {
	return c.baseCheck.Name()
}

// Type returns the check type.
func (c *DBCheck) Type() health.CheckType {
	return c.baseCheck.Type()
}

// Timeout returns the check timeout.
func (c *DBCheck) Timeout() time.Duration {
	return c.timeout
}

// Interval returns the check interval.
func (c *DBCheck) Interval() time.Duration {
	return c.baseCheck.Interval()
}

// Enabled returns whether the check is enabled.
func (c *DBCheck) Enabled() bool {
	return c.baseCheck.Enabled()
}

// SetEnabled enables or disables the check.
func (c *DBCheck) SetEnabled(enabled bool) {
	c.baseCheck.SetEnabled(enabled)
}

// Execute performs the database health check by running the configured query.
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy target)
func (c *DBCheck) Execute(ctx context.Context) (health.Result, error) {
	if !c.Enabled() {
		return health.NewResult(health.StatusUnknown).
			WithError(fmt.Errorf("check disabled")), nil
	}

	startTime := time.Now()

	// Create a context with timeout
	execCtx, cancel := context.WithTimeout(ctx, c.timeout)
	defer cancel()

	// Execute the query
	rows, err := c.db.QueryContext(execCtx, c.query)
	if err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("database query failed: %w", err)).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"database": c.dbName,
				"query":    c.query,
			}), nil
	}
	defer rows.Close()

	// Check if there are any rows
	if !rows.Next() {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("database query returned no rows")).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"database": c.dbName,
				"query":    c.query,
			}), nil
	}

	// Check for errors during iteration
	if err := rows.Err(); err != nil {
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("error during database query: %w", err)).
			WithDuration(time.Since(startTime)).
			WithDetails(map[string]interface{}{
				"database": c.dbName,
				"query":    c.query,
			}), nil
	}

	// Database is healthy
	return health.NewResult(health.StatusUp).
		WithDuration(time.Since(startTime)).
		WithDetails(map[string]interface{}{
			"database": c.dbName,
			"query":    c.query,
		}), nil
}

// String returns a string representation of the DB check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *DBCheck) String() string {
	dbName := c.dbName
	if dbName == "" {
		dbName = "unknown"
	}
	return fmt.Sprintf("DBCheck{name=%s, database=%s, query=%s, timeout=%s}",
		c.Name(), dbName, c.query, c.timeout)
}
