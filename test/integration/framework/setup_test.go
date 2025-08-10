// file: test/integration/framework/setup_test.go
// version: 1.1.0
// guid: 13d5981e-69a9-42a1-9376-211505425c21

package framework

import (
	"path/filepath"
	"testing"
)

func TestSetupAndCleanup(t *testing.T) {
	env, err := SetupTestEnvironment()
	if err != nil {
		t.Fatalf("SetupTestEnvironment returned error: %v", err)
	}
	if env == nil {
		t.Fatalf("expected non-nil environment")
	}
	if err := LoadFixtures(env); err != nil {
		t.Fatalf("LoadFixtures returned error: %v", err)
	}
	p := env.TempFile("sample.txt")
	if filepath.Dir(p) != env.TempDir {
		t.Fatalf("TempFile returned path outside temp dir: %s", p)
	}
	if err := env.Cleanup(); err != nil {
		t.Fatalf("Cleanup returned error: %v", err)
	}
}
