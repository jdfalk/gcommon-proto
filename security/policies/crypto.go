// file: security/policies/crypto.go
// version: 1.1.0
// guid: c0e5b18f-c75b-4d6b-8641-50b6e535e720

package policies

import "errors"

// CryptoPolicy outlines cryptographic standards.
type CryptoPolicy struct {
	AllowedAlgorithms []string
	MinKeyLength      int
	RequireRSA        bool
}

// Validate ensures cryptographic standards are met.
func (p CryptoPolicy) Validate(algorithm string, keyLength int) error {
	allowed := false
	for _, a := range p.AllowedAlgorithms {
		if a == algorithm {
			allowed = true
			break
		}
	}
	if !allowed {
		return errors.New("algorithm not permitted by policy")
	}
	if keyLength < p.MinKeyLength {
		return errors.New("key length below policy minimum")
	}
	if p.RequireRSA && algorithm != "RSA" {
		return errors.New("RSA required by policy")
	}
	return nil
}
