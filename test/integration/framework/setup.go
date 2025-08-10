// file: test/integration/framework/setup.go
// version: 0.1.0
// guid: 6379a7e2-f5f5-4047-8127-aa3f6a7e3ed3

package framework

import (
	"database/sql"
	"fmt"
	"os"

	"github.com/go-redis/redis/v8"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/log"
	"github.com/jdfalk/gcommon/pkg/metrics"
)

// TestEnvironment holds shared resources for integration tests.
type TestEnvironment struct {
	Config   *config.Config
	Database *sql.DB
	Redis    *redis.Client
	Logger   log.Logger
	Metrics  metrics.Provider
	TempDir  string
}

// SetupTestEnvironment creates a basic integration testing environment.
func SetupTestEnvironment() (*TestEnvironment, error) {
	dir, err := os.MkdirTemp("", "gcommon-test-")
	if err != nil {
		return nil, fmt.Errorf("create temp dir: %w", err)
	}

	logger, err := log.NewProvider(log.Config{})
	if err != nil {
		os.RemoveAll(dir)
		return nil, fmt.Errorf("create logger: %w", err)
	}

	metricsProvider, err := metrics.NewProvider(metrics.Config{})
	if err != nil {
		os.RemoveAll(dir)
		return nil, fmt.Errorf("create metrics provider: %w", err)
	}

	return &TestEnvironment{
		Config:  &config.Config{},
		Logger:  logger,
		Metrics: metricsProvider,
		TempDir: dir,
	}, nil
}
