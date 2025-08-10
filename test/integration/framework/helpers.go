// file: test/integration/framework/helpers.go
// version: 1.0.0
// guid: 6b4cfc4e-df9f-459f-8909-15e45041d645

package framework

import "path/filepath"

// TempFile returns a temporary file path within the test environment.
func (te *TestEnvironment) TempFile(name string) string {
	if te == nil {
		return ""
	}
	return filepath.Join(te.TempDir, name)
}

// Path returns a path within the test environment's temporary directory.
func (te *TestEnvironment) Path(name string) string {
	if te == nil {
		return ""
	}
	return filepath.Join(te.TempDir, name)
}
