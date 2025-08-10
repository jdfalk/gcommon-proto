// file: pkg/config/providers/env_test.go
// version: 1.0.0
// guid: 74e45086-560a-41ab-8605-cacc54926261

package providers

import (
	"os"
	"testing"
)

func TestEnvProvider_GetSet(t *testing.T) {
	t.Parallel()
	pIface, err := NewEnvProvider(nil)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	p := pIface.(*EnvProvider)
	if err := p.Set("TEST_KEY", "VALUE"); err != nil {
		t.Fatalf("set error: %v", err)
	}
	val, err := p.Get("TEST_KEY")
	if err != nil {
		t.Fatalf("get error: %v", err)
	}
	if val != "VALUE" {
		t.Fatalf("expected VALUE, got %v", val)
	}
	os.Unsetenv("TEST_KEY")
}
