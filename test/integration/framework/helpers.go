// file: test/integration/framework/helpers.go
// version: 0.1.0
// guid: 04337e78-7f34-43c3-9bba-b2f34f9b67f5

package framework

import "path/filepath"

// Path returns a path within the test environment's temporary directory.
func (te *TestEnvironment) Path(name string) string {
	if te == nil {
		return ""
	}
	return filepath.Join(te.TempDir, name)
}
