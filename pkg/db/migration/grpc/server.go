// file: pkg/db/migration/grpc/server.go
// version: 1.0.0
// guid: 9c73515b-63dc-4b9c-9d5a-7a7fd1c2c222

// Package grpc provides gRPC services for database migrations.
package grpc

import (
	"context"
	"fmt"
	"strconv"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/types/known/timestamppb"

	commonpb "github.com/jdfalk/gcommon/pkg/common/proto"
	"github.com/jdfalk/gcommon/pkg/db/migration"
	dbpb "github.com/jdfalk/gcommon/pkg/db/proto"
)

// MigrationServer implements MigrationServiceServer.
type MigrationServer struct {
	dbpb.UnimplementedMigrationServiceServer
	manager *migration.Manager
}

// NewMigrationServer creates a new MigrationServer.
func NewMigrationServer(mgr *migration.Manager) *MigrationServer {
	return &MigrationServer{manager: mgr}
}

// Register registers the service with the provided gRPC server.
func (s *MigrationServer) Register(server *grpc.Server) {
	dbpb.RegisterMigrationServiceServer(server, s)
}

// ApplyMigration applies all pending migrations using the manager.
func (s *MigrationServer) ApplyMigration(ctx context.Context, req *dbpb.RunMigrationRequest) (*dbpb.RunMigrationResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "nil request")
	}
	if err := s.manager.Migrate(ctx); err != nil {
		return &dbpb.RunMigrationResponse{Success: false, Error: &commonpb.Error{Message: err.Error()}}, nil
	}
	applied, err := s.manager.Exec.List(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "list applied: %v", err)
	}
	versions := make([]string, 0, len(applied))
	for _, m := range applied {
		versions = append(versions, fmt.Sprintf("%d", m.Version))
	}
	return &dbpb.RunMigrationResponse{Success: true, AppliedVersions: versions}, nil
}

// RevertMigration rolls back to the specified version.
func (s *MigrationServer) RevertMigration(ctx context.Context, req *dbpb.RevertMigrationRequest) (*dbpb.RevertMigrationResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "nil request")
	}
	target, err := strconv.Atoi(req.TargetVersion)
	if err != nil {
		return nil, status.Errorf(codes.InvalidArgument, "invalid target version: %v", err)
	}
	current, err := s.manager.Tracker.Current(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "current version: %v", err)
	}
	if target < 0 || target > current {
		return nil, status.Error(codes.InvalidArgument, "target version out of range")
	}
	steps := current - target
	if err := s.manager.Rollback(ctx, steps); err != nil {
		return &dbpb.RevertMigrationResponse{Success: false, Error: &commonpb.Error{Message: err.Error()}}, nil
	}
	return &dbpb.RevertMigrationResponse{Success: true, RevertedTo: req.TargetVersion}, nil
}

// GetMigrationStatus returns current, applied, and pending migration versions.
func (s *MigrationServer) GetMigrationStatus(ctx context.Context, req *dbpb.GetMigrationStatusRequest) (*dbpb.GetMigrationStatusResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "nil request")
	}
	current, err := s.manager.Tracker.Current(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "current version: %v", err)
	}
	migs, err := s.loadAll(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "load migrations: %v", err)
	}
	var applied, pending []string
	for _, m := range migs {
		v := fmt.Sprintf("%d", m.Version)
		if m.Version <= current {
			applied = append(applied, v)
		} else {
			pending = append(pending, v)
		}
	}
	return &dbpb.GetMigrationStatusResponse{
		CurrentVersion:  fmt.Sprintf("%d", current),
		AppliedVersions: applied,
		PendingVersions: pending,
	}, nil
}

// ListMigrations returns metadata for migrations with optional status filtering.
func (s *MigrationServer) ListMigrations(ctx context.Context, req *dbpb.ListMigrationsRequest) (*dbpb.ListMigrationsResponse, error) {
	if req == nil {
		return nil, status.Error(codes.InvalidArgument, "nil request")
	}
	current, err := s.manager.Tracker.Current(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "current version: %v", err)
	}
	migs, err := s.loadAll(ctx)
	if err != nil {
		return nil, status.Errorf(codes.Internal, "load migrations: %v", err)
	}
	infos := make([]*dbpb.MigrationInfo, 0, len(migs))
	for _, m := range migs {
		status := "pending"
		if m.Version <= current {
			status = "applied"
		}
		if req.StatusFilter != "" && status != req.StatusFilter {
			continue
		}
		var ts *timestamppb.Timestamp
		if status == "applied" {
			ts = timestamppb.Now()
		}
		infos = append(infos, &dbpb.MigrationInfo{
			Version:     fmt.Sprintf("%d", m.Version),
			Description: m.Name,
			AppliedAt:   ts,
		})
	}
	return &dbpb.ListMigrationsResponse{Migrations: infos}, nil
}

// loadAll aggregates migrations from manager sources.
func (s *MigrationServer) loadAll(ctx context.Context) ([]migration.Migration, error) {
	var all []migration.Migration
	for _, src := range s.manager.Sources {
		migs, err := src.Load(ctx)
		if err != nil {
			return nil, err
		}
		all = append(all, migs...)
	}
	migration.SortMigrations(all)
	return all, nil
}

// TODO: implement tracking of applied timestamps in VersionTracker.
