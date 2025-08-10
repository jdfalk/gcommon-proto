// file: pkg/plugins/examples/integration/analytics/analytics_test.go
// version: 1.0.0
// guid: 04a5f24e-973b-4d5a-8320-e82bb00d6bbd

package analytics

import (
	"context"
	"testing"
)

func TestAnalyticsConnect(t *testing.T) {
	p := New()
	if err := p.Connect(context.Background()); err != nil {
		t.Fatalf("connect: %v", err)
	}
}
