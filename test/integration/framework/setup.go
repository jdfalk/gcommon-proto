// file: test/integration/framework/setup.go
// version: 1.1.0
// guid: a140e477-5008-4669-8525-e1d830ad6a76

package framework

import (
	"context"
	"database/sql"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/DATA-DOG/go-sqlmock"
	"github.com/alicebob/miniredis/v2"
	"github.com/go-redis/redis/v8"
	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/metrics"
)

// TestEnvironment contains resources for integration tests.
type TestEnvironment struct {
	Config      *config.Config
	Database    *sql.DB
	Redis       *redis.Client
	Logger      *log.Logger
	Metrics     metrics.Provider
	TempDir     string
	redisServer *miniredis.Miniredis
}

// SetupTestEnvironment configures a basic test environment.
func SetupTestEnvironment() (*TestEnvironment, error) {
	tempDir, err := os.MkdirTemp("", "gcommon-test-")
	if err != nil {
		return nil, fmt.Errorf("create temp dir: %w", err)
	}

	db, _, err := sqlmock.New()
	if err != nil {
		os.RemoveAll(tempDir)
		return nil, fmt.Errorf("create mock database: %w", err)
	}

	mr, err := miniredis.Run()
	if err != nil {
		db.Close()
		os.RemoveAll(tempDir)
		return nil, fmt.Errorf("start miniredis: %w", err)
	}

	rdb := redis.NewClient(&redis.Options{Addr: mr.Addr()})

	logger := log.New(io.Discard, "", log.LstdFlags)

	metricsProvider, err := metrics.NewProvider(metrics.Config{})
	if err != nil {
		db.Close()
		rdb.Close()
		mr.Close()
		os.RemoveAll(tempDir)
		return nil, fmt.Errorf("create metrics provider: %w", err)
	}

	env := &TestEnvironment{
		Config:      &config.Config{},
		Database:    db,
		Redis:       rdb,
		Logger:      logger,
		Metrics:     metricsProvider,
		TempDir:     tempDir,
		redisServer: mr,
	}

	_ = env.Metrics.Start(context.Background())

	return env, nil
}
