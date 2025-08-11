// file: monitoring/collectors/logs_test.go
// version: 1.0.0
// guid: 8b821b4a-4e7a-4cf5-9d03-7bc9d95fbd11

package collectors

import (
	"context"
	"log"
	"testing"
	"time"
)

// TestLogsCollectorEmit verifies that subscribers receive emitted logs.
func TestLogsCollectorEmit(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	lc := NewLogsCollector(10)
	lc.Start(ctx)
	sub := lc.Subscribe(1)
	lc.Emit(LevelInfo, "hello", nil)
	select {
	case entry := <-sub:
		if entry.Message != "hello" {
			t.Fatalf("unexpected message: %s", entry.Message)
		}
	case <-time.After(time.Second):
		t.Fatalf("timeout waiting for log entry")
	}
	lc.Close()
}

// TestLogsCollectorStdLogger ensures standard logger output is captured.
func TestLogsCollectorStdLogger(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	lc := NewLogsCollector(10)
	lc.Start(ctx)
	sub := lc.Subscribe(1)
	logger := lc.StdLogger(LevelError, map[string]any{"component": "test"})
	logger.Print("failure")
	select {
	case entry := <-sub:
		if entry.Level != LevelError || entry.Message != "failure" {
			t.Fatalf("unexpected log entry: %+v", entry)
		}
	case <-time.After(time.Second):
		t.Fatalf("timeout")
	}
	lc.Close()
}

// TestLogsCollectorRedirectStandardLibrary confirms log package output is redirected.
func TestLogsCollectorRedirectStandardLibrary(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	lc := NewLogsCollector(10)
	lc.Start(ctx)
	sub := lc.Subscribe(1)
	lc.RedirectStandardLibrary(LevelWarn)
	log.Print("warning")
	select {
	case entry := <-sub:
		if entry.Level != LevelWarn || entry.Message != "warning" {
			t.Fatalf("unexpected entry: %+v", entry)
		}
	case <-time.After(time.Second):
		t.Fatalf("timeout")
	}
	lc.Close()
}
