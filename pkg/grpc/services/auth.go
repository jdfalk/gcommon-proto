// file: pkg/grpc/services/auth.go
// version: 1.0.0
// guid: 0fb7f539-ddcf-4619-b13e-1f0a807112bd

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// AuthService defines the service interface placeholder.
type AuthService interface{}

// RegisterAuthService registers the auth service with the server registrar.
func RegisterAuthService(reg server.ServiceRegistrar, srv AuthService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
