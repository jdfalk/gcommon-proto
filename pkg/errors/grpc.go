// file: pkg/errors/grpc.go
// version: 1.0.0
// guid: 0f3e18ec-b74a-4e3f-b54e-6fc5c5abc123

package errors

import (
	"context"

	"google.golang.org/grpc"
	grpcCodes "google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

// ToGRPCStatus converts an internal Error to a gRPC status.Status.
func ToGRPCStatus(err Error) *status.Status {
	if err == nil {
		return status.New(grpcCodes.OK, "")
	}
	code := grpcCodes.Unknown
	switch err.Code() {
	case ErrCodeInvalidInput:
		code = grpcCodes.InvalidArgument
	case ErrCodeNotFound:
		code = grpcCodes.NotFound
	case ErrCodeAlreadyExists:
		code = grpcCodes.AlreadyExists
	case ErrCodeTimeout:
		code = grpcCodes.DeadlineExceeded
	case ErrCodeUnavailable:
		code = grpcCodes.Unavailable
	case ErrCodeUnauthorized:
		code = grpcCodes.Unauthenticated
	case ErrCodeForbidden:
		code = grpcCodes.PermissionDenied
	default:
		code = grpcCodes.Unknown
	}
	return status.New(code, err.Error())
}

// FromGRPCStatus converts a gRPC status.Status to an internal Error.
func FromGRPCStatus(st *status.Status) Error {
	if st == nil {
		return nil
	}
	var code ErrorCode
	switch st.Code() {
	case grpcCodes.InvalidArgument:
		code = ErrCodeInvalidInput
	case grpcCodes.NotFound:
		code = ErrCodeNotFound
	case grpcCodes.AlreadyExists:
		code = ErrCodeAlreadyExists
	case grpcCodes.DeadlineExceeded:
		code = ErrCodeTimeout
	case grpcCodes.Unavailable:
		code = ErrCodeUnavailable
	case grpcCodes.Unauthenticated:
		code = ErrCodeUnauthorized
	case grpcCodes.PermissionDenied:
		code = ErrCodeForbidden
	default:
		code = ErrCodeUnknown
	}
	return newBaseError(code, "grpc", "", st.Message())
}

// ErrorHandlingInterceptor is a unary interceptor converting Errors to gRPC statuses.
func ErrorHandlingInterceptor() grpc.UnaryServerInterceptor {
	return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
		resp, err := handler(ctx, req)
		if err != nil {
			if e, ok := err.(Error); ok {
				return nil, ToGRPCStatus(e).Err()
			}
			return nil, err
		}
		return resp, nil
	}
}

// ErrorHandlingStreamInterceptor is a stream interceptor converting Errors to gRPC statuses.
func ErrorHandlingStreamInterceptor() grpc.StreamServerInterceptor {
	return func(srv interface{}, ss grpc.ServerStream, info *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
		if err := handler(srv, ss); err != nil {
			if e, ok := err.(Error); ok {
				return ToGRPCStatus(e).Err()
			}
			return err
		}
		return nil
	}
}
