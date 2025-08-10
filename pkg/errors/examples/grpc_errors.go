// file: pkg/errors/examples/grpc_errors.go
// version: 1.0.0
// guid: b2c3d4e5-f6a7-4890-abcd-2345678901bc

package examples

import (
	"context"
	"fmt"

	errpkg "github.com/jdfalk/gcommon/pkg/errors"
	"google.golang.org/grpc/status"
)

// ExampleGRPC demonstrates converting between internal errors and gRPC statuses.
func ExampleGRPC() {
	err := errpkg.NewError(context.Background(), errpkg.ErrCodeInvalidInput, "bad request")
	st := errpkg.ToGRPCStatus(err)
	fmt.Println(st.Code())
	restored := errpkg.FromGRPCStatus(status.New(st.Code(), st.Message()))
	fmt.Println(restored.Code())
	// Output:
	// InvalidArgument
	// ErrCodeInvalidInput
}
