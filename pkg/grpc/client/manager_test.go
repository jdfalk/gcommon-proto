// file: pkg/grpc/client/manager_test.go
// version: 1.0.0
// guid: 661964dc-f1fb-4294-b2ec-180e2fb8df01

package client

import (
	"context"
	"net"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"
)

const bufSize = 1024 * 1024

func dialer() (*grpc.ClientConn, func(), error) {
	lis := bufconn.Listen(bufSize)
	s := grpc.NewServer()
	go func() { _ = s.Serve(lis) }()
	conn, err := grpc.DialContext(context.Background(), "", grpc.WithContextDialer(func(ctx context.Context, s string) (net.Conn, error) {
		return lis.Dial()
	}), grpc.WithInsecure())
	cleanup := func() {
		conn.Close()
		s.Stop()
	}
	return conn, cleanup, err
}

// TestManagerGet verifies connections are cached.
func TestManagerGet(t *testing.T) {
	_, cleanup, err := dialer()
	if err != nil {
		t.Fatalf("dialer setup failed: %v", err)
	}
	cleanup()

	ctx := context.Background()
	m := NewManager()
	conn1, err := m.Get(ctx, "example", grpc.WithInsecure(), grpc.WithContextDialer(func(ctx context.Context, s string) (net.Conn, error) {
		return bufconn.Listen(1).Dial()
	}))
	if err != nil {
		t.Fatalf("first get failed: %v", err)
	}
	conn2, err := m.Get(ctx, "example")
	if err != nil {
		t.Fatalf("second get failed: %v", err)
	}
	if conn1 != conn2 {
		t.Fatalf("expected cached connection")
	}
	if err := m.Close(); err != nil {
		t.Fatalf("close failed: %v", err)
	}
}
