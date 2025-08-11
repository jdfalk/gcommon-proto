// file: perf/benchmarks/auth_bench.go
// version: 1.1.0
// guid: fd0f1fb4-c2b0-4ffe-877a-3ec930f5fa3c

package benchmarks

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"strings"
	"sync"
	"testing"
)

var secret = []byte("secret")

// mockToken creates a simple JWT-like token for benchmarking.
func mockToken() string {
	header := base64.RawURLEncoding.EncodeToString([]byte(`{"alg":"HS256"}`))
	payload := base64.RawURLEncoding.EncodeToString([]byte(`{"sub":"user"}`))
	mac := hmac.New(sha256.New, secret)
	mac.Write([]byte(header + "." + payload))
	sig := base64.RawURLEncoding.EncodeToString(mac.Sum(nil))
	return strings.Join([]string{header, payload, sig}, ".")
}

// BenchmarkTokenValidation measures token validation speed.
func BenchmarkTokenValidation(b *testing.B) {
	tok := mockToken()
	parts := strings.Split(tok, ".")
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		mac := hmac.New(sha256.New, secret)
		mac.Write([]byte(parts[0] + "." + parts[1]))
		_ = mac.Sum(nil)
	}
}

// BenchmarkAuthDecision measures authorization decision latency.
func BenchmarkAuthDecision(b *testing.B) {
	roles := map[string]bool{"admin": true}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = roles["admin"]
	}
}

// BenchmarkConcurrentAuthRequests measures concurrent authentication requests.
func BenchmarkConcurrentAuthRequests(b *testing.B) {
	tok := mockToken()
	parts := strings.Split(tok, ".")
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			mac := hmac.New(sha256.New, secret)
			mac.Write([]byte(parts[0] + "." + parts[1]))
			_ = mac.Sum(nil)
		}
	})
}

// BenchmarkPolicyEvaluation measures policy evaluation performance.
func BenchmarkPolicyEvaluation(b *testing.B) {
	policies := map[string]bool{"read": true, "write": false}
	var mu sync.RWMutex
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		mu.RLock()
		_ = policies["read"]
		mu.RUnlock()
	}
}
