// file: pkg/grpc/examples/client_usage.go
// version: 1.0.0
// guid: f044b36e-ee3d-453d-9b8f-5c3f02833dc7

package examples

import (
	"context"

	"github.com/jdfalk/gcommon/pkg/grpc/client"
)

// ClientUsageExample demonstrates dialing a service.
func ClientUsageExample(ctx context.Context) error {
	mgr := client.NewManager()
	conn, err := mgr.Get(ctx, "localhost:50051")
	if err != nil {
		return err
	}
	defer mgr.Close()
	_ = conn
	return nil
}
