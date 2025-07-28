// file: pkg/health/checks/db_test.go
package checks

import (
	"context"
	_ "database/sql"
	"errors"
	"testing"
	"time"

	"github.com/DATA-DOG/go-sqlmock"
	"github.com/jdfalk/gcommon/pkg/health"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestNewDBCheck(t *testing.T) {
	// Create a mock database
	db, _, err := sqlmock.New()
	require.NoError(t, err)
	defer db.Close()

	// Test cases for constructor options
	tests := []struct {
		name     string
		query    string
		options  []DBCheckOption
		expected struct {
			name      string
			query     string
			timeout   time.Duration
			dbName    string
			checkType health.CheckType
			interval  time.Duration
			enabled   bool
		}
	}{
		{
			name:    "default configuration",
			query:   "",
			options: []DBCheckOption{},
			expected: struct {
				name      string
				query     string
				timeout   time.Duration
				dbName    string
				checkType health.CheckType
				interval  time.Duration
				enabled   bool
			}{
				name:      "db-check",
				query:     "SELECT 1",
				timeout:   5 * time.Second,
				dbName:    "",
				checkType: health.TypeReadiness,
				interval:  30 * time.Second,
				enabled:   true,
			},
		},
		{
			name:  "custom configuration",
			query: "SELECT now()",
			options: []DBCheckOption{
				WithDBName("test-db"),
				WithDBQueryTimeout(10 * time.Second),
				WithDBCheckInterval(1 * time.Minute),
				WithDBCheckType(health.TypeLiveness),
				WithDBCheckEnabled(false),
			},
			expected: struct {
				name      string
				query     string
				timeout   time.Duration
				dbName    string
				checkType health.CheckType
				interval  time.Duration
				enabled   bool
			}{
				name:      "db-check",
				query:     "SELECT now()",
				timeout:   10 * time.Second,
				dbName:    "test-db",
				checkType: health.TypeLiveness,
				interval:  1 * time.Minute,
				enabled:   false,
			},
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			check := NewDBCheck("db-check", db, tc.query, tc.options...)

			assert.Equal(t, tc.expected.name, check.Name())
			assert.Equal(t, tc.expected.query, check.query)
			assert.Equal(t, tc.expected.timeout, check.timeout)
			assert.Equal(t, tc.expected.dbName, check.dbName)
			assert.Equal(t, tc.expected.checkType, check.Type())
			assert.Equal(t, tc.expected.interval, check.Interval())
			assert.Equal(t, tc.expected.enabled, check.Enabled())
		})
	}
}

func TestDBCheck_Execute(t *testing.T) {
	// Test cases for execute method
	tests := []struct {
		name      string
		setupMock func(sqlmock.Sqlmock)
		expected  health.Status
		expectErr bool
		customCtx context.Context
	}{
		{
			name: "successful query",
			setupMock: func(mock sqlmock.Sqlmock) {
				rows := sqlmock.NewRows([]string{"value"}).AddRow(1)
				mock.ExpectQuery("SELECT 1").WillReturnRows(rows)
			},
			expected:  health.StatusUp,
			expectErr: false,
		},
		{
			name: "query error",
			setupMock: func(mock sqlmock.Sqlmock) {
				mock.ExpectQuery("SELECT 1").WillReturnError(errors.New("connection refused"))
			},
			expected:  health.StatusDown,
			expectErr: false,
		},
		{
			name: "no rows returned",
			setupMock: func(mock sqlmock.Sqlmock) {
				rows := sqlmock.NewRows([]string{"value"}) // No rows added
				mock.ExpectQuery("SELECT 1").WillReturnRows(rows)
			},
			expected:  health.StatusDown,
			expectErr: false,
		},
		{
			name: "rows error",
			setupMock: func(mock sqlmock.Sqlmock) {
				rows := sqlmock.NewRows([]string{"value"}).AddRow(1).RowError(0, errors.New("row error"))
				mock.ExpectQuery("SELECT 1").WillReturnRows(rows)
			},
			expected:  health.StatusDown,
			expectErr: false,
		},
		{
			name: "context timeout",
			setupMock: func(mock sqlmock.Sqlmock) {
				// This creates a query that will hang and trigger the context timeout
				mock.ExpectQuery("SELECT 1").WillDelayFor(100 * time.Millisecond).WillReturnRows(sqlmock.NewRows([]string{"value"}).AddRow(1))
			},
			expected:  health.StatusDown,
			expectErr: false,
			customCtx: func() context.Context {
				ctx, _ := context.WithTimeout(context.Background(), 10*time.Millisecond)
				return ctx
			}(),
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			// Create a mock database
			db, mock, err := sqlmock.New()
			require.NoError(t, err)
			defer db.Close()

			// Setup the mock expectations
			tc.setupMock(mock)

			// Create the check
			check := NewDBCheck("test-db-check", db, "SELECT 1")

			// Execute the check
			ctx := context.Background()
			if tc.customCtx != nil {
				ctx = tc.customCtx
			}

			result, err := check.Execute(ctx)

			// Validate the results
			if tc.expectErr {
				assert.Error(t, err)
			} else {
				assert.NoError(t, err)
				assert.Equal(t, tc.expected, result.Status())
				assert.NotZero(t, result.Duration())

				// Check details
				details := result.Details()
				assert.NotNil(t, details)
				assert.Equal(t, "SELECT 1", details["query"])
				assert.Contains(t, details, "queryTime")

				if result.Status() == health.StatusDown && result.Error() != nil {
					// If status is down, we should have an error message
					assert.NotEmpty(t, result.Error().Error())
				}
			}

			// Ensure all expectations were met
			assert.NoError(t, mock.ExpectationsWereMet())
		})
	}
}

func TestDBCheck_String(t *testing.T) {
	// Create a mock database
	db, _, err := sqlmock.New()
	require.NoError(t, err)
	defer db.Close()

	// Test check with no database name
	check1 := NewDBCheck("test-check", db, "SELECT 1")
	str1 := check1.String()
	assert.Contains(t, str1, "test-check")
	assert.Contains(t, str1, "SELECT 1")
	assert.Contains(t, str1, "unknown") // Default db name

	// Test check with custom database name
	check2 := NewDBCheck("test-check", db, "SELECT version()", WithDBName("postgres"))
	str2 := check2.String()
	assert.Contains(t, str2, "test-check")
	assert.Contains(t, str2, "SELECT version()")
	assert.Contains(t, str2, "postgres") // Custom db name
}
