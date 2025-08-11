// file: pkg/config/sources/env.go
// version: 1.1.1
// guid: 99999999-aaaa-bbbb-cccc-dddddddddddd

package sources

import (
	"os"
	"strings"

	"github.com/jdfalk/gcommon/pkg/config"
)

// EnvSource reads configuration from environment variables with a prefix.
//
// The source supports nested key construction using a configurable
// delimiter, key case transformation, allow/deny lists, default values, and
// simple variable expansion in values. These features make it suitable for
// complex deployment scenarios such as container orchestration where
// environment variables are the primary configuration mechanism.
//
// Examples:
//
//	APP_DB__HOST=localhost   -> {"db": {"host": "localhost"}}
//	APP_DB__PORT=5432        -> {"db": {"port": "5432"}}
//	APP_FEATURE=true         -> {"feature": "true"}
//
// Variable expansion uses the existing collected values and falls back to
// the process environment. For example, if `APP_PATH=/data` and
// `APP_LOG=${APP_PATH}/logs`, the resulting value for `log` will be
// `/data/logs`.
//
// NOTE: this implementation is intentionally simple and does not attempt to
// provide full shell-like expansion semantics.
type EnvSource struct {
	Prefix     string            // prefix to match (e.g. "APP_")
	Delimiter  string            // delimiter for nested keys (default "__")
	Case       string            // "lower", "upper", or "none"
	Allowlist  []string          // if non-empty, only these keys are allowed
	Denylist   []string          // keys to exclude
	Defaults   map[string]string // default values for missing keys
	ExpandVars bool              // perform variable expansion on values
}

// Load returns environment variables as a configuration map following the
// rules defined on EnvSource.
func (e EnvSource) Load() (map[string]interface{}, error) {
	if e.Delimiter == "" {
		e.Delimiter = "__"
	}
	lower := func(s string) string { return s }
	upper := func(s string) string { return s }
	switch strings.ToLower(e.Case) {
	case "lower", "":
		lower = strings.ToLower
		upper = strings.ToLower
	case "upper":
		lower = strings.ToUpper
		upper = strings.ToUpper
	}

	allow := make(map[string]struct{})
	if len(e.Allowlist) > 0 {
		for _, k := range e.Allowlist {
			allow[upper(k)] = struct{}{}
		}
	}
	deny := make(map[string]struct{})
	for _, k := range e.Denylist {
		deny[upper(k)] = struct{}{}
	}

	raw := make(map[string]string)
	result := make(map[string]interface{})
	for _, kv := range os.Environ() {
		parts := strings.SplitN(kv, "=", 2)
		if len(parts) != 2 {
			continue
		}
		key := parts[0]
		if !strings.HasPrefix(key, e.Prefix) {
			continue
		}
		trimmed := strings.TrimPrefix(key, e.Prefix)
		norm := upper(trimmed)
		if len(allow) > 0 {
			if _, ok := allow[norm]; !ok {
				continue
			}
		}
		if _, denied := deny[norm]; denied {
			continue
		}
		val := parts[1]
		raw[norm] = val
		if e.ExpandVars {
			val = os.Expand(val, func(v string) string {
				if rv, ok := raw[upper(v)]; ok {
					return rv
				}
				return os.Getenv(v)
			})
		}
		setNested(result, lower(trimmed), val, e.Delimiter)
	}

	for k, v := range e.Defaults {
		norm := upper(k)
		if _, ok := raw[norm]; ok {
			continue
		}
		setNested(result, lower(k), v, e.Delimiter)
	}
	return result, nil
}

// setNested inserts value into map using delimiter-separated keys, creating
// intermediate maps as necessary.
func setNested(m map[string]interface{}, key, value, delim string) {
	if delim == "" {
		m[key] = value
		return
	}
	parts := strings.Split(key, delim)
	for i, p := range parts {
		if i == len(parts)-1 {
			m[p] = value
			return
		}
		next, ok := m[p].(map[string]interface{})
		if !ok {
			next = make(map[string]interface{})
			m[p] = next
		}
		m = next
	}
}

// TODO:
//  - Detect and warn about conflicting variables
//  - Expose metrics for environment variable usage
//  - Document security implications of environment configs
//  - Add examples for docker-compose and Kubernetes setups
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
