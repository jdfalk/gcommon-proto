// file: pkg/config/config_data.go
// version: 1.0.0
// guid: 6b3f8f5e-24d7-4f4d-b8ac-10e1e0f5d0e5

package config

import (
	"encoding/json"
	"fmt"
	"strings"
)

// ConfigData implements the Config interface using strongly typed
// structures for global and module configurations. The structure can be
// used to construct hierarchical configuration values and to expose them
// through the Config interface expected by the Manager.
//
// The design keeps the structure lightweight while providing a convenient
// `ToMap` helper for flattening configuration into a simple key/value map
// where keys are represented as `section.key` (for example,
// `global.logger.level`).
//
// Additional modules can be added by expanding the `ModuleConfigs` struct
// defined in types.go.
//
// TODO: Consider generating these mappings using reflection to reduce
// maintenance as modules grow.

type ConfigData struct {
	Global  GlobalConfig
	Modules ModuleConfigs
}

// NewConfig constructs a ConfigData instance from global and module
// configurations.
func NewConfig(global GlobalConfig, modules ModuleConfigs) *ConfigData {
	return &ConfigData{Global: global, Modules: modules}
}

// GetModuleConfig returns configuration for the requested module.
func (c *ConfigData) GetModuleConfig(module string) (ModuleConfig, error) {
	switch strings.ToLower(module) {
	case "config":
		return c.Modules.Config, nil
	case "queue":
		return c.Modules.Queue, nil
	case "auth":
		return c.Modules.Auth, nil
	case "web":
		return c.Modules.Web, nil
	case "cache":
		return c.Modules.Cache, nil
	case "organization":
		return c.Modules.Organization, nil
	case "notification":
		return c.Modules.Notification, nil
	default:
		return nil, fmt.Errorf("unknown module %s", module)
	}
}

// SetModuleConfig updates configuration for the specified module.
func (c *ConfigData) SetModuleConfig(module string, cfg ModuleConfig) error {
	switch strings.ToLower(module) {
	case "config":
		v, ok := cfg.(ConfigModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Config = v
	case "queue":
		v, ok := cfg.(QueueModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Queue = v
	case "auth":
		v, ok := cfg.(AuthModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Auth = v
	case "web":
		v, ok := cfg.(WebModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Web = v
	case "cache":
		v, ok := cfg.(CacheModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Cache = v
	case "organization":
		v, ok := cfg.(OrganizationModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Organization = v
	case "notification":
		v, ok := cfg.(NotificationModuleConfig)
		if !ok {
			return fmt.Errorf("invalid type for module %s", module)
		}
		c.Modules.Notification = v
	default:
		return fmt.Errorf("unknown module %s", module)
	}
	return nil
}

// GetGlobalConfig returns the global configuration block.
func (c *ConfigData) GetGlobalConfig() (GlobalConfig, error) {
	return c.Global, nil
}

// toMap converts a structure into a map with the provided prefix. It
// marshals the structure to JSON and then unmarshals into a
// map[string]interface{} for generic processing. Each resulting key is
// prefixed with the provided prefix.
func toMap(prefix string, v interface{}, dst map[string]interface{}) {
	b, err := json.Marshal(v)
	if err != nil {
		return
	}
	var m map[string]interface{}
	if err := json.Unmarshal(b, &m); err != nil {
		return
	}
	flatten(prefix, m, dst)
}

// flatten recursively flattens nested maps into dot-separated keys.
func flatten(prefix string, m map[string]interface{}, dst map[string]interface{}) {
	for k, val := range m {
		key := strings.ToLower(k)
		if prefix != "" {
			key = prefix + "." + key
		}
		if sub, ok := val.(map[string]interface{}); ok {
			flatten(key, sub, dst)
			continue
		}
		dst[key] = val
	}
}

// ToMap flattens the configuration into a map where keys are prefixed
// with their section names. This helper is primarily used by Manager
// during merge operations.
func (c *ConfigData) ToMap() map[string]interface{} {
	result := make(map[string]interface{})
	toMap("global", c.Global, result)
	toMap("config", c.Modules.Config, result)
	toMap("queue", c.Modules.Queue, result)
	toMap("auth", c.Modules.Auth, result)
	toMap("web", c.Modules.Web, result)
	toMap("cache", c.Modules.Cache, result)
	toMap("organization", c.Modules.Organization, result)
	toMap("notification", c.Modules.Notification, result)
	return result
}

var _ Config = (*ConfigData)(nil)
