// file: security/policies/network.go
// version: 1.1.0
// guid: cfd8a049-0703-4c93-99b6-f8e90dee48ef

package policies

import (
	"net"
)

// NetworkPolicy defines network security requirements.
type NetworkPolicy struct {
	AllowedCIDRs []string
}

// IsAllowed determines if the given IP is within allowed ranges.
func (p NetworkPolicy) IsAllowed(ip string) bool {
	addr := net.ParseIP(ip)
	if addr == nil {
		return false
	}
	for _, cidr := range p.AllowedCIDRs {
		_, network, err := net.ParseCIDR(cidr)
		if err != nil {
			continue
		}
		if network.Contains(addr) {
			return true
		}
	}
	return false
}
