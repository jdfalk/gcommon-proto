// file: test/integration/framework/cleanup.go
// version: 0.1.0
// guid: d56e9548-6686-4349-8c13-9114800d0638

package framework

import "os"

// Cleanup releases resources allocated for the test environment.
func (te *TestEnvironment) Cleanup() error {
	if te == nil {
		return nil
	}
	if te.TempDir != "" {
		if err := os.RemoveAll(te.TempDir); err != nil {
			return err
		}
	}
	return nil
}
