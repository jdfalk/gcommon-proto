// file: pkg/cache/policies/policy.go
// version: 1.0.0
// guid: 5d4f2e1c-6a7b-4c9d-8e1f-2a3b4c5d6e7f

package policies

// Policy defines cache eviction behaviors.
type Policy interface {
	// OnGet records an access to the given key.
	OnGet(key string)
	// OnSet records an insertion or update of the given key.
	OnSet(key string)
	// OnDelete records removal of the given key.
	OnDelete(key string)
	// Evict returns the key that should be evicted next. Empty string if none.
	Evict() string
}
