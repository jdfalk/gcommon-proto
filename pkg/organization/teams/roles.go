// file: pkg/organization/teams/roles.go
// version: 1.0.0
// guid: f49f2012-5d35-4336-848b-e8203d626289

// Package teams defines team roles and utilities.
package teams

import "strings"

// Role defines a team role with associated permissions.
type Role string

const (
	// RoleMember represents standard team membership.
	RoleMember Role = "member"
	// RoleAdmin represents administrative team membership.
	RoleAdmin Role = "admin"
	// RoleOwner represents ownership of the team.
	RoleOwner Role = "owner"
)

// ParseRole converts a string to a Role value, normalizing case.
func ParseRole(r string) Role {
	switch strings.ToLower(r) {
	case "admin":
		return RoleAdmin
	case "owner":
		return RoleOwner
	default:
		return RoleMember
	}
}

// String returns the string representation of the role.
func (r Role) String() string { return string(r) }

// RolesEqual compares roles ignoring case.
func RolesEqual(a, b Role) bool {
	return strings.EqualFold(a.String(), b.String())
}
