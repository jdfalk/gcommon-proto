// file: pkg/grpc/services/organization.go
// version: 1.0.0
// guid: af24d9f3-e842-42e1-aaf9-8c0934f4e96c

package services

import (
	"github.com/jdfalk/gcommon/pkg/grpc/server"
	"google.golang.org/grpc"
)

// OrganizationService defines the service interface placeholder.
type OrganizationService interface{}

// RegisterOrganizationService registers the organization service with the server registrar.
func RegisterOrganizationService(reg server.ServiceRegistrar, srv OrganizationService, desc *grpc.ServiceDesc) {
	if reg == nil || srv == nil || desc == nil {
		return
	}
	reg.RegisterService(desc, srv)
}
