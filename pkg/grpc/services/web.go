// file: pkg/grpc/services/web.go
// version: 1.0.0
// guid: 8819127a-b305-4a64-9828-5312b3335f41

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// WebService defines the service interface placeholder.
type WebService interface{}

// RegisterWebService registers the web service with the server registrar.
func RegisterWebService(reg server.ServiceRegistrar, srv WebService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
