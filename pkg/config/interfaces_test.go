// file: pkg/config/interfaces_test.go
// version: 1.0.0
// guid: eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee

package config_test

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/providers"
)

// TestProviderInterface ensures EnvProvider implements Provider
// TODO: Expand tests for other providers
func TestProviderInterface(t *testing.T) {
	p, err := providers.NewEnvProvider("APP_")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, ok := interface{}(p).(config.Provider); !ok {
		t.Fatalf("EnvProvider does not implement Provider")
	}
}

// TODO: Add tests for ConfigService interface once implementations exist
// TODO: Add benchmark tests
// TODO: Improve coverage with error scenarios

// EOF
