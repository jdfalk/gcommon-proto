// file: security/tools/crypto_test.go
// version: 1.0.0
// guid: c9a3c1ab-8c91-4e5c-9f33-8d68a99924d0

package tools

import "testing"

func TestEncryptDecrypt(t *testing.T) {
	key, err := GenerateKey()
	if err != nil {
		t.Fatalf("generate key: %v", err)
	}
	cipher, err := EncryptAES(key, []byte("secret"))
	if err != nil {
		t.Fatalf("encrypt: %v", err)
	}
	plain, err := DecryptAES(key, cipher)
	if err != nil {
		t.Fatalf("decrypt: %v", err)
	}
	if string(plain) != "secret" {
		t.Fatalf("expected secret, got %s", plain)
	}
}

func TestHashPassword(t *testing.T) {
	hash, err := HashPassword("password123!")
	if err != nil {
		t.Fatalf("hash: %v", err)
	}
	if !VerifyPassword(hash, "password123!") {
		t.Fatalf("password verification failed")
	}
}
