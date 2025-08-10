// file: security/policies/access.go
// version: 1.1.0
// guid: 4a15af98-c89d-4baa-8ce3-519aae7a2f9a

package policies

import "sync"

// AccessPolicy defines role based access control rules.
type AccessPolicy struct {
	mu    sync.RWMutex
	roles map[string][]string
}

// NewAccessPolicy creates an empty policy.
func NewAccessPolicy() *AccessPolicy {
	return &AccessPolicy{roles: map[string][]string{}}
}

// AddRole adds a role with associated permissions.
func (p *AccessPolicy) AddRole(role string, perms []string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.roles[role] = perms
}

// RemoveRole removes a role from the policy.
func (p *AccessPolicy) RemoveRole(role string) {
	p.mu.Lock()
	defer p.mu.Unlock()
	delete(p.roles, role)
}

// Allow checks whether a role has permission to perform an action.
func (p *AccessPolicy) Allow(role, perm string) bool {
	p.mu.RLock()
	defer p.mu.RUnlock()
	perms, ok := p.roles[role]
	if !ok {
		return false
	}
	for _, p := range perms {
		if p == perm {
			return true
		}
	}
	return false
}
