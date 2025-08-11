// file: templates/event-driven-service/internal/config/config.go
// version: 1.0.0
// guid: 63258fac-399c-450d-abdd-97a8153e0c6b

package config

import (
	"github.com/jdfalk/gcommon/pkg/config"
	"github.com/jdfalk/gcommon/pkg/config/formats"
	"github.com/jdfalk/gcommon/pkg/config/sources"
)

type AppConfig struct {
	QueueName   string `yaml:"queue_name"`
	MetricsPort string `yaml:"metrics_port"`
}

func NewFileSource(path string) config.ConfigSource {
	return sources.FileSource{Path: path, Decoder: formats.YAMLDecoder{}}
}

func MustLoad(m *config.Manager) *AppConfig {
	cfg := &AppConfig{QueueName: "events", MetricsPort: "9090"}
	if v, err := m.Get("queue_name"); err == nil {
		if s, ok := v.(string); ok {
			cfg.QueueName = s
		}
	}
	if v, err := m.Get("metrics_port"); err == nil {
		if s, ok := v.(string); ok {
			cfg.MetricsPort = s
		}
	}
	return cfg
}
