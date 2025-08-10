// file: pkg/queue/security.go
// version: 1.0.0
// guid: 8c99f5a8-e7a1-4b44-9d58-5e330c1a1b79

package queue

import (
	"crypto/hmac"
	"crypto/sha256"
	"errors"

	"github.com/jdfalk/gcommon/security/tools"
)

// EncryptMessage encrypts payload using repository crypto tools.
func EncryptMessage(key, payload []byte) (string, error) {
	return tools.EncryptAES(key, payload)
}

// DecryptMessage decrypts payload using repository crypto tools.
func DecryptMessage(key []byte, cipherText string) ([]byte, error) {
	return tools.DecryptAES(key, cipherText)
}

// AuthorizeQueueAccess checks if user role is permitted to interact with queue.
func AuthorizeQueueAccess(roles map[string]bool, role string) bool {
	allowed, ok := roles[role]
	return ok && allowed
}

// SignMessage computes HMAC of message for integrity.
func SignMessage(key, msg []byte) string {
	mac := hmac.New(sha256.New, key)
	mac.Write(msg)
	return string(mac.Sum(nil))
}

// VerifyMessage ensures message integrity.
func VerifyMessage(key, msg []byte, signature string) bool {
	mac := hmac.New(sha256.New, key)
	mac.Write(msg)
	expected := mac.Sum(nil)
	return hmac.Equal([]byte(signature), expected)
}

// RouteMessageSecure validates routing key before sending.
func RouteMessageSecure(route string, allowed []string) error {
	for _, a := range allowed {
		if route == a {
			return nil
		}
	}
	return errors.New("unauthorized route")
}
