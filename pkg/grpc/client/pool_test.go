// file: pkg/grpc/client/pool_test.go
// version: 1.0.0
// guid: 4dfb0a1c-977b-4062-8fcd-2345155c2ccd

package client

import (
	"context"
	"net"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"
)

// TestPoolGet uses round-robin to reuse connections.
func TestPoolGet(t *testing.T) {
	lis := bufconn.Listen(1024 * 1024)
	s := grpc.NewServer()
	go func() { _ = s.Serve(lis) }()
	dialer := func(context.Context, string) (net.Conn, error) { return lis.Dial() }

	res := NewResolver(nil)
	res.Update("svc", "buf")
	pool := NewPool(res, grpc.WithContextDialer(dialer), grpc.WithInsecure())

	ctx := context.Background()
	conn1, err := pool.Get(ctx)
	if err != nil {
		t.Fatalf("get1 failed: %v", err)
	}
	conn2, err := pool.Get(ctx)
	if err != nil {
		t.Fatalf("get2 failed: %v", err)
	}
	if conn1 != conn2 {
		t.Fatalf("expected same connection")
	}
	pool.Close()
	s.Stop()
}
