// file: test/integration/framework/fixtures.go
// version: 1.1.0
// guid: d744dd39-a0f1-4eb9-8ec8-e59cb829fa1f

package framework

import "context"

// LoadFixtures prepares test data fixtures.
func LoadFixtures(te *TestEnvironment) error {
	if te.Redis == nil {
		return nil
	}
	return te.Redis.Set(context.Background(), "fixture", "value", 0).Err()
}

// LoadFixtures loads integration test fixtures (method version).
func (te *TestEnvironment) LoadFixtures() error {
	return LoadFixtures(te)
}
