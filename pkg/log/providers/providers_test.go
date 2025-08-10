// file: pkg/log/providers/providers_test.go
// version: 1.0.0
// guid: b4c3d2e1-f0a9-48b7-9c6d-1234567890fa

package providers

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/log"
)

// TestNewProviderRegistration verifies that all providers register correctly with the factory.
func TestNewProviderRegistration(t *testing.T) {
	cases := []struct {
		name     string
		provider string
	}{
		{name: "zap", provider: "zap"},
		{name: "logrus", provider: "logrus"},
		{name: "zerolog", provider: "zerolog"},
		{name: "syslog", provider: "syslog"},
	}

	for _, c := range cases {
		c := c
		t.Run(c.name, func(t *testing.T) {
			t.Parallel()
			p, err := log.NewProvider(log.Config{Provider: c.provider, Level: "info"})
			if c.provider == "syslog" && err != nil {
				t.Skip("syslog not available")
			}
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}
			if p.Name() != c.provider {
				t.Fatalf("expected %s, got %s", c.provider, p.Name())
			}
		})
	}
}
