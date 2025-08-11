// file: pkg/log/monitoring/alerts_test.go
// version: 1.0.0
// guid: 7c2d5e1a-8f4b-4f17-a1b0-0de712fa3b11

package monitoring

import (
	"testing"
	"time"

	"github.com/jdfalk/gcommon/pkg/log"
)

// TestAlertManager triggers callback when error count exceeds threshold.
func TestAlertManager(t *testing.T) {
	fired := make(chan int64, 1)
	am := NewAlertManager(1, 10*time.Millisecond, func(c int64) { fired <- c })
	am.Notify(log.ErrorLevel)
	select {
	case c := <-fired:
		if c != 1 {
			t.Fatalf("expected count 1, got %d", c)
		}
	case <-time.After(time.Second):
		t.Fatalf("callback not triggered")
	}
}
