// file: pkg/auth/policies/abac_test.go
// version: 1.0.0
// guid: b7b2f5c8-12a4-4c9d-8e88-5f9e6c7a8b1c

package policies

import (
	"testing"

	proto "github.com/jdfalk/gcommon/pkg/auth/proto"
)

func TestABACAuthorize(t *testing.T) {
	eng := NewABACEngine()
	req := &proto.AuthorizeRequest{}
	req.SetResource("res")
	req.SetAction("read")
	req.SetContext(map[string]string{"resource": "res", "action": "read"})
	resp, err := eng.Authorize(nil, req)
	if err != nil {
		t.Fatalf("authorize: %v", err)
	}
	if !resp.GetAuthorized() {
		t.Fatalf("expected authorized")
	}
}
