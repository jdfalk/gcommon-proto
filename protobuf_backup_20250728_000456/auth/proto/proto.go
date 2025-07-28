// file: pkg/auth/proto/proto.go

// Package authpb provides consolidated exports for auth protobuf types
package authpb

// Re-export types from various auth protobuf packages for backwards compatibility
import (
	authpb_requests "github.com/jdfalk/gcommon/pkg/auth/proto/requests"
	authpb_responses "github.com/jdfalk/gcommon/pkg/auth/proto/responses"
	authpb_services "github.com/jdfalk/gcommon/pkg/auth/proto/services"
)

// Request types
type (
	AuthenticateRequest  = authpb_requests.AuthenticateRequest
	CreateSessionRequest = authpb_requests.CreateSessionRequest
	ValidateTokenRequest = authpb_requests.ValidateTokenRequest
)

// Response types
type (
	AuthenticateResponse  = authpb_responses.AuthenticateResponse
	CreateSessionResponse = authpb_responses.CreateSessionResponse
	ValidateTokenResponse = authpb_responses.ValidateTokenResponse
)

// Service interfaces
type (
	AuthServiceClient          = authpb_services.AuthServiceClient
	AuthServiceServer          = authpb_services.AuthServiceServer
	SessionServiceClient       = authpb_services.SessionServiceClient
	SessionServiceServer       = authpb_services.SessionServiceServer
	AuthorizationServiceClient = authpb_services.AuthorizationServiceClient
	AuthorizationServiceServer = authpb_services.AuthorizationServiceServer
)
