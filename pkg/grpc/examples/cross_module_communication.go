// file: pkg/grpc/examples/cross_module_communication.go
// version: 1.0.0
// guid: 4e83c4f5-4a25-43f5-a205-1ca1fa5b62d4

package examples

import (
	"context"
	"log"
	"net"
	"time"

	"github.com/jdfalk/gcommon/pkg/grpc/client"
	"github.com/jdfalk/gcommon/pkg/grpc/interceptors"
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"
)

// CrossModuleCommunicationExample demonstrates client/server with retry and circuit breaking.
func CrossModuleCommunicationExample() error {
	// Setup in-memory server for example purposes
	lis := bufconn.Listen(1024 * 1024)
	s := server.NewServer("bufnet")
	go func() { _ = s.Start(context.Background()) }()
	dialer := func(context.Context, string) (net.Conn, error) { return lis.Dial() }

	// Configure client utilities
	res := client.NewResolver(nil)
	res.Update("example", "bufnet")
	pool := client.NewPool(res, grpc.WithContextDialer(dialer), grpc.WithInsecure())

	// Combine interceptors
	cb := client.NewCircuitBreaker()
	retry := client.UnaryRetryInterceptor(client.RetryOptions{BackoffStrategy: client.ConstantBackoff{Delay: time.Millisecond}})
	auth := interceptors.AuthUnary(func(ctx context.Context) error { return nil })
	conn, err := pool.Get(context.Background())
	if err != nil {
		return err
	}
	_ = cb
	_ = retry
	_ = auth
	_ = conn

	// Normally we would make RPC calls here using generated stubs.
	log.Println("example setup complete")
	return nil
}
