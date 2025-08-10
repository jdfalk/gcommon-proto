// file: pkg/plugins/lifecycle.go
// version: 1.0.0
// guid: d5b274db-2bd5-4931-8a36-9e47f77581be

package plugins

import "context"

// Initialize configures a plugin before use.
func Initialize(p Plugin, cfg map[string]interface{}) error {
	return p.Initialize(cfg)
}

// Start activates the plugin.
func Start(ctx context.Context, p Plugin) error {
	return p.Start(ctx)
}

// Stop shuts down the plugin.
func Stop(ctx context.Context, p Plugin) error {
	return p.Stop(ctx)
}

// InitializeAll configures all plugins with the provided configs.
func InitializeAll(reg *Registry, configs map[string]map[string]interface{}) error {
	for name, p := range reg.plugins {
		if cfg, ok := configs[name]; ok {
			if err := Initialize(p, cfg); err != nil {
				return err
			}
		}
	}
	return nil
}
