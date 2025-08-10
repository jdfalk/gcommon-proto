// file: test/integration/framework/cleanup.go
// version: 1.1.0
// guid: b0125097-d6f3-46cb-8904-87f60b5b56b3

package framework

import (
	"context"
	"os"
)

// Cleanup releases resources used by the test environment.
func (te *TestEnvironment) Cleanup() error {
	if te == nil {
		return nil
	}
	if te.Database != nil {
		_ = te.Database.Close()
	}
	if te.Redis != nil {
		_ = te.Redis.Close()
	}
	if te.redisServer != nil {
		te.redisServer.Close()
	}
	if te.Metrics != nil {
		_ = te.Metrics.Stop(context.Background())
	}
	if te.TempDir != "" {
		_ = os.RemoveAll(te.TempDir)
	}
	return nil
}
