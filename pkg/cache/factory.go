// file: pkg/cache/factory.go
// version: 1.1.0
// guid: d54fe3da-43e0-4e13-8201-017a79499f05

package cache

import (
	"fmt"

	"github.com/jdfalk/gcommon/pkg/cache/policies"
	"github.com/jdfalk/gcommon/pkg/cache/providers"
)

// Known cache providers.
const (
	ProviderMemory      = "memory"
	ProviderRedis       = "redis"
	ProviderMemcached   = "memcached"
	ProviderDistributed = "distributed"
)

// New creates a cache provider by name.
func New(provider string) (Cache, error) {
	switch provider {
	case ProviderMemory:
		return providers.NewMemoryCache(0, policies.NewLRU()), nil
	case ProviderRedis:
		return providers.NewRedisCache(nil), nil
	case ProviderMemcached:
		return providers.NewMemcachedCache(nil), nil
	case ProviderDistributed:
		return providers.NewDistributedCache(nil), nil
	default:
		return nil, fmt.Errorf("unknown cache provider: %s", provider)
	}
}
