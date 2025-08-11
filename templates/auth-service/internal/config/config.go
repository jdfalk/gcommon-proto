// file: templates/auth-service/internal/config/config.go
// version: 1.0.0
// guid: f3aaad67-6134-489a-ab7a-40d541aaf1c8

package config

import (
	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

type AppConfig struct {
	HTTPPort string `yaml:"http_port"`
}

func NewFileSource(path string) config.ConfigSource {
	return sources.FileSource{Path: path, Decoder: formats.YAMLDecoder{}}
}

func MustLoad(m *config.Manager) *AppConfig {
	cfg := &AppConfig{HTTPPort: "8080"}
	if v, err := m.Get("http_port"); err == nil {
		if s, ok := v.(string); ok {
			cfg.HTTPPort = s
		}
	}
	return cfg
}
