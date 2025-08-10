// file: pkg/queue/security_test.go
// version: 1.0.0
// guid: 6b8207a4-f251-4c06-83a7-1a9b1a0d3f7e

package queue

import (
	"testing"

	"github.com/jdfalk/gcommon/security/tools"
)

func TestEncryptVerify(t *testing.T) {
	key, _ := tools.GenerateKey()
	enc, err := EncryptMessage(key, []byte("msg"))
	if err != nil {
		t.Fatalf("encrypt: %v", err)
	}
	dec, err := DecryptMessage(key, enc)
	if err != nil {
		t.Fatalf("decrypt: %v", err)
	}
	if string(dec) != "msg" {
		t.Fatalf("expected msg, got %s", dec)
	}
	sig := SignMessage(key, dec)
	if !VerifyMessage(key, dec, sig) {
		t.Fatalf("signature invalid")
	}
}
