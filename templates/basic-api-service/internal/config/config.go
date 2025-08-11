// file: templates/basic-api-service/internal/config/config.go
// version: 1.0.0
// guid: 4941f8fc-4db8-41cf-9f0d-d074d17cf397

// Package config defines the application configuration structures and helpers
// for the basic API service template. It demonstrates loading configuration
// using the gcommon configuration manager and YAML file source.
package config

import (
	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

// AppConfig contains runtime configuration for the service.
type AppConfig struct {
	HTTPPort    string `yaml:"http_port"`
	MetricsPort string `yaml:"metrics_port"`
}

// NewFileSource constructs a configuration file source with YAML decoding.
func NewFileSource(path string) config.ConfigSource {
	return sources.FileSource{Path: path, Decoder: formats.YAMLDecoder{}}
}

// MustLoad loads configuration from the manager and returns an AppConfig. If
// configuration is missing, sensible defaults are returned. In production code,
// applications should handle errors explicitly rather than relying on defaults.
func MustLoad(m *config.Manager) *AppConfig {
	cfg := &AppConfig{HTTPPort: "8080", MetricsPort: "9090"}
	if v, err := m.Get("http_port"); err == nil {
		if s, ok := v.(string); ok {
			cfg.HTTPPort = s
		}
	}
	if v, err := m.Get("metrics_port"); err == nil {
		if s, ok := v.(string); ok {
			cfg.MetricsPort = s
		}
	}
	return cfg
}
