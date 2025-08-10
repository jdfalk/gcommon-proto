// file: pkg/config/types.go
// version: 1.1.0
// guid: 2b2a1b3c-4d5e-678f-9012-abcdefabcdef

package config

// GlobalConfig holds shared configuration for all modules.
type GlobalConfig struct {
	Logger  LogConfig
	Metrics MetricsConfig
	Health  HealthConfig
	Server  ServerConfig
	// TODO: add tracing configuration
}

// ModuleConfigs contains configuration for each module.
type ModuleConfigs struct {
	Config       ConfigModuleConfig
	Queue        QueueModuleConfig
	Auth         AuthModuleConfig
	Web          WebModuleConfig
	Cache        CacheModuleConfig
	Organization OrganizationModuleConfig
	Notification NotificationModuleConfig
	// TODO: add additional modules as needed
}

// Placeholder configuration types for modules.
type (
	LogConfig struct {
		Level  string
		Format string
	}
	MetricsConfig struct {
		Endpoint string
		Enabled  bool
	}
	HealthConfig struct {
		Interval int
		Enabled  bool
	}
	ServerConfig struct {
		Address string
		Port    int
	}
	ConfigModuleConfig struct {
		Path string
	}
	QueueModuleConfig struct {
		Provider string
	}
	AuthModuleConfig struct {
		Provider string
	}
	WebModuleConfig struct {
		Host string
	}
	CacheModuleConfig struct {
		Size int
	}
	OrganizationModuleConfig struct {
		Enabled bool
	}
	NotificationModuleConfig struct {
		Provider string
	}
)
