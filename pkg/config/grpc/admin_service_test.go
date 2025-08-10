// file: pkg/config/grpc/admin_service_test.go
// version: 1.0.0
// guid: 05050505-0505-0505-0505-050505050505

package grpc

import (
	"context"
	"testing"

	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"github.com/jdfalk/gcommon/pkg/config/providers"
)

// TestBackupConfig ensures backup call returns non-nil
func TestBackupConfig(t *testing.T) {
	p, _ := providers.NewEnvProvider("B_")
	svc := &ConfigAdminServiceServer{Provider: p}
	resp, err := svc.BackupConfig(context.Background(), &configpb.BackupConfigRequest{})
	if err != nil || resp == nil {
		t.Fatalf("unexpected response: %v %v", resp, err)
	}
}

// TODO: Add tests for RestoreConfig

// EOF
