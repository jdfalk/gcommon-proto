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
// It performs a simple query (e.g., "SELECT 1") to verify that
// the database is responsive and the connection is valid.
type DBCheck struct {
	// Embed the BaseCheck to inherit its functionality
	health.BaseCheck

	// The database connection to check
	db *sql.DB

	// The query to execute as the health check
	query string

	// Timeout for query execution
	timeout time.Duration

	// Optional name of the database for reporting
	dbName string
}

// DBCheckOption is a functional option type for configuring DBCheck.
type DBCheckOption func(*DBCheck)

// WithDBName sets a descriptive name for the database.
func WithDBName(name string) DBCheckOption {
	return func(c *DBCheck) {
		c.dbName = name
	}
}

// WithDBQueryTimeout sets the query timeout.
func WithDBQueryTimeout(timeout time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		c.timeout = timeout
	}
}

// WithDBCheckInterval sets the check interval.
func WithDBCheckInterval(interval time.Duration) DBCheckOption {
	return func(c *DBCheck) {
		c.SetInterval(interval)
	}
}

// WithDBCheckType sets the check type.
func WithDBCheckType(checkType health.CheckType) DBCheckOption {
	return func(c *DBCheck) {
		c.SetType(checkType)
	}
}

// WithDBCheckEnabled sets whether the check is initially enabled.
func WithDBCheckEnabled(enabled bool) DBCheckOption {
	return func(c *DBCheck) {
		c.SetEnabled(enabled)
	}
}

// NewDBCheck creates a new DBCheck to monitor the health of a database connection.
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
	if query == "" {
		query = "SELECT 1"
	}

	check := &DBCheck{
		db:      db,
		query:   query,
		timeout: 5 * time.Second,
	}

	// Initialize the BaseCheck
	check.BaseCheck = health.NewBaseCheck(name)

	// Default configuration
	check.SetType(health.TypeReadiness)  // Database checks are typically used for dependency readiness
	check.SetInterval(30 * time.Second)  // Default 30 second interval
	check.SetEnabled(true)               // Enabled by default

	// Apply the options
	for _, option := range options {
		option(check)
	}

	return check
}

// Execute performs the database health check by executing the configured query.
//
// The check performs these steps:
// 1. Create a context with the configured timeout
// 2. Attempt to execute the query against the database
// 3. Return appropriate health result based on query success/failure
//
// Parameters:
//   - ctx: Context that can be used to cancel the check
//
// Returns:
//   - A Result indicating the health status
//   - An error if the check execution itself failed (not the same as an unhealthy database)
func (c *DBCheck) Execute(ctx context.Context) (health.Result, error) {
	startTime := time.Now()

	// Prepare details map with available information
	details := map[string]interface{}{
		"query": c.query,
	}

	if c.dbName != "" {
		details["database"] = c.dbName
	}

	// Create a timeout context if not already set
	execCtx := ctx
	if _, hasDeadline := ctx.Deadline(); !hasDeadline {
		var cancel context.CancelFunc
		execCtx, cancel = context.WithTimeout(ctx, c.timeout)
		defer cancel()
	}

	// Execute the query
	start := time.Now()
	rows, err := c.db.QueryContext(execCtx, c.query)
	queryTime := time.Since(start)

	// Add query execution time to details
	details["queryTime"] = queryTime.String()

	if err != nil {
		// Query failed
		return health.NewResult(health.StatusDown).
			WithError(err).
			WithDetails(details).
			WithDuration(time.Since(startTime)), nil
	}

	// Make sure to close the rows
	defer rows.Close()

	// Check for errors during row iteration
	if rows.Next() {
		// Successfully got a row, which means the database is responsive
		if err := rows.Err(); err != nil {
			return health.NewResult(health.StatusDown).
				WithError(err).
				WithDetails(details).
				WithDuration(time.Since(startTime)), nil
		}
	} else {
		// No rows returned - this might be OK for some queries, but for "SELECT 1" it's unusual
		return health.NewResult(health.StatusDown).
			WithError(fmt.Errorf("no rows returned from query")).
			WithDetails(details).
			WithDuration(time.Since(startTime)), nil
	}

	// Database is healthy
	return health.NewResult(health.StatusUp).
		WithDetails(details).
		WithDuration(time.Since(startTime)), nil
}

// String returns a string representation of the DB check.
//
// Returns:
//   - A string describing this check for logging and debugging
func (c *DBCheck) String() string {
	dbDesc := "unknown"
	if c.dbName != "" {
		dbDesc = c.dbName
	}

	return fmt.Sprintf("DBCheck{name=%s, database=%s, query=%q, timeout=%s, type=%s, enabled=%t}",
		c.Name(), dbDesc, c.query, c.timeout, c.Type(), c.Enabled())
}
