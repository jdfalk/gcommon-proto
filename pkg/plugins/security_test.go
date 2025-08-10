// file: pkg/plugins/security_test.go
// version: 1.0.0
// guid: 2c4f8448-5a94-49f1-aea5-c372ac4a3eab

package plugins

import (
	"context"
	"testing"
)

type permPlugin struct{ Base string }

func (p *permPlugin) Name() string                            { return "perm" }
func (p *permPlugin) Version() string                         { return "v1" }
func (p *permPlugin) Initialize(map[string]interface{}) error { return nil }
func (p *permPlugin) Start(context.Context) error             { return nil }
func (p *permPlugin) Stop(context.Context) error              { return nil }
func (p *permPlugin) Health() HealthStatus                    { return HealthStatus{OK: true} }

func TestDefaultCheckerValidate(t *testing.T) {
	p := &permPlugin{}
	md := Metadata{Name: "perm", Permissions: []Permission{PermissionRead}}
	wp := WithMetadata(p, md)
	checker := DefaultChecker{}
	policy := Policy{Permissions: []Permission{PermissionRead, PermissionWrite}}
	if err := checker.Validate(wp, policy); err != nil {
		t.Fatalf("validate: %v", err)
	}
}

func TestDefaultCheckerMissingPermission(t *testing.T) {
	p := &permPlugin{}
	md := Metadata{Name: "perm", Permissions: []Permission{PermissionWrite}}
	wp := WithMetadata(p, md)
	checker := DefaultChecker{}
	policy := Policy{Permissions: []Permission{PermissionRead}}
	if err := checker.Validate(wp, policy); err == nil {
		t.Fatalf("expected error")
	}
}
