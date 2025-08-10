// file: pkg/config/sources/env.go
// version: 1.0.0
// guid: 99999999-aaaa-bbbb-cccc-dddddddddddd

package sources

import (
	"os"
	"strings"

	"github.com/jdfalk/gcommon/pkg/config"
)

// EnvSource reads configuration from environment variables with a prefix.
type EnvSource struct {
	Prefix string
}

// Load returns environment variables as configuration map.
func (e EnvSource) Load() (map[string]interface{}, error) {
	result := make(map[string]interface{})
	for _, kv := range os.Environ() {
		parts := strings.SplitN(kv, "=", 2)
		if len(parts) != 2 {
			continue
		}
		if strings.HasPrefix(parts[0], e.Prefix) {
			key := strings.TrimPrefix(parts[0], e.Prefix)
			result[strings.ToLower(key)] = parts[1]
		}
	}
	return result, nil
}

// TODO:
//  - Support nested keys using delimiters
//  - Allow customizing case transformation behavior
//  - Provide whitelist/blacklist for allowed variables
//  - Detect and warn about conflicting variables
//  - Support default values for missing variables
//  - Expose metrics for environment variable usage
//  - Document security implications of environment configs
//  - Add examples for docker-compose and Kubernetes setups
//  - Implement variable expansion for referencing other values
//  - Provide helper for generating sample env files
//  - Handle large numbers of environment variables efficiently
//  - Validate variables against schema or regex patterns
//  - Support dynamic updates via os.Environ replacement
//  - Offer CLI to audit environment configuration
//  - Add unit tests covering edge cases and Unicode keys
//  - Integrate with watcher to reload on env changes
//  - Provide context for cancellation and deadlines
//  - Support secrets management via env files
//  - Document cross-platform behavior differences
//  - Explore caching strategies for repeated loads

var _ config.ConfigSource = (*EnvSource)(nil)
