// file: monitoring/collectors/logs_extended_test.go
// version: 1.0.0
// guid: d4e2c3b1-7a8f-49b2-9c3d-4e5f6a7b8c9d

package collectors

import (
	"context"
	"testing"
	"time"
)

// TestMultipleSubscribers ensures all subscribers receive logs.
func TestMultipleSubscribers(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	lc := NewLogsCollector(10)
	lc.Start(ctx)
	sub1 := lc.Subscribe(1)
	sub2 := lc.Subscribe(1)
	lc.Emit(LevelInfo, "message", nil)
	for i, ch := range []<-chan LogEntry{sub1, sub2} {
		select {
		case <-ch:
		case <-time.After(time.Second):
			t.Fatalf("subscriber %d did not receive log", i)
		}
	}
	lc.Close()
}

// TestCloseBehavior ensures subscribers are closed when collector closes.
func TestCloseBehavior(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	lc := NewLogsCollector(10)
	lc.Start(ctx)
	sub := lc.Subscribe(1)
	lc.Close()
	if _, ok := <-sub; ok {
		t.Fatalf("subscriber channel should be closed")
	}
}
