// file: pkg/metrics/exporters/grpc_test.go
// version: 1.0.0
// guid: 607189ab-cdef-0123-4567-89abcdef0123

package exporters

import (
	"context"
	"testing"
	"time"
)

// TestGRPCExporter_StartStop verifies that the gRPC exporter can be started and
// stopped without error. Real metrics streaming is not yet implemented.
func TestGRPCExporter_StartStop(t *testing.T) {
	exp := NewGRPCExporter("127.0.0.1:0")
	if err := exp.Start(context.Background()); err != nil {
		t.Fatalf("start error: %v", err)
	}
	stopCtx, cancel := context.WithTimeout(context.Background(), time.Millisecond)
	defer cancel()
	if err := exp.Stop(stopCtx); err != nil {
		t.Fatalf("stop error: %v", err)
	}
}

// TODO: add tests for real RPC interactions once exporter is complete.
