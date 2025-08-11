// file: pkg/grpc/interceptors/recovery_stream.go
// version: 1.0.0
// guid: 99072d0c-2129-49ce-8325-6462b74a30b1

package interceptors

import (
	"fmt"

	"google.golang.org/grpc"
)

// RecoveryStream intercepts panics in stream handlers.
func RecoveryStream() grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) (err error) {
		defer func() {
			if r := recover(); r != nil {
				err = fmt.Errorf("panic: %v", r)
			}
		}()
		return handler(srv, ss)
	}
}
