// file: pkg/db/migration/grpc/client.go
// version: 1.0.0
// guid: 0b3a0f34-8c2f-4d3f-9a73-6b1a63f99999

// Package grpc provides gRPC clients for database migration services.
package grpc

import (
	"context"

	"google.golang.org/grpc"

	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// MigrationClient wraps the generated MigrationServiceClient.
type MigrationClient struct {
	client dbpb.MigrationServiceClient
}

// NewMigrationClient creates a new MigrationClient using the provided connection.
func NewMigrationClient(conn grpc.ClientConnInterface) *MigrationClient {
	return &MigrationClient{client: dbpb.NewMigrationServiceClient(conn)}
}

// ApplyMigration runs pending migrations on the server.
func (c *MigrationClient) ApplyMigration(ctx context.Context, req *dbpb.RunMigrationRequest, opts ...grpc.CallOption) (*dbpb.RunMigrationResponse, error) {
	return c.client.ApplyMigration(ctx, req, opts...)
}

// RevertMigration requests rollback to a specific version.
func (c *MigrationClient) RevertMigration(ctx context.Context, req *dbpb.RevertMigrationRequest, opts ...grpc.CallOption) (*dbpb.RevertMigrationResponse, error) {
	return c.client.RevertMigration(ctx, req, opts...)
}

// GetMigrationStatus retrieves current migration status.
func (c *MigrationClient) GetMigrationStatus(ctx context.Context, req *dbpb.GetMigrationStatusRequest, opts ...grpc.CallOption) (*dbpb.GetMigrationStatusResponse, error) {
	return c.client.GetMigrationStatus(ctx, req, opts...)
}

// ListMigrations lists all migrations with optional filtering.
func (c *MigrationClient) ListMigrations(ctx context.Context, req *dbpb.ListMigrationsRequest, opts ...grpc.CallOption) (*dbpb.ListMigrationsResponse, error) {
	return c.client.ListMigrations(ctx, req, opts...)
}
