// file: pkg/plugins/sdk/base_test.go
// version: 1.0.0
// guid: 1f38a3c8-5bd6-4e56-b1a2-f3c1c46c7fd4

package sdk

import (
	"testing"

	"github.com/jdfalk/gcommon/pkg/plugins"
)

func TestGenerateDocumentation(t *testing.T) {
	md := plugins.Metadata{Name: "doc", Version: "1.0", Description: "test", Permissions: []plugins.Permission{plugins.PermissionRead}}
	doc := GenerateDocumentation(md)
	if len(doc) == 0 {
		t.Fatalf("no documentation generated")
	}
}
