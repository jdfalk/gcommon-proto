// file: pkg/log/providers/zap.go
// version: 1.0.0
// guid: c5c6b9d1-27e2-4f9f-aeaa-7c68e7b1c1a1

package providers

import (
	"context"
	"io"

	"github.com/jdfalk/gcommon/pkg/log"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

// zapProvider implements the log.Provider interface using Uber's zap logger.
type zapProvider struct {
	logger *zap.Logger
	level  log.Level
}

// init registers the zap provider with the logging factory.
func init() {
	log.RegisterProvider("zap", newZapProvider)
}

// newZapProvider creates a zap-based logging provider.
func newZapProvider(cfg log.Config) (log.Provider, error) {
	zapCfg := zap.NewProductionConfig()
	if cfg.Format == "console" {
		zapCfg.Encoding = "console"
	}
	l, err := zapCfg.Build()
	if err != nil {
		return nil, err
	}
	p := &zapProvider{logger: l, level: parseLevel(cfg.Level)}
	return p, nil
}

func (p *zapProvider) Name() string { return "zap" }

// Close flushes any buffered log entries.
func (p *zapProvider) Close() error {
	return p.logger.Sync()
}

// Sync ensures all logs are written to the underlying writer.
func (p *zapProvider) Sync() error {
	return p.logger.Sync()
}

// SetOutput changes the destination for log entries.
func (p *zapProvider) SetOutput(w io.Writer) {
	core := zapcore.NewCore(zapcore.NewJSONEncoder(zap.NewProductionEncoderConfig()), zapcore.AddSync(w), zapcore.DebugLevel)
	p.logger = zap.New(core)
}

// AddHook attaches a hook to the logger. zap does not support hooks directly so this is a no-op.
func (p *zapProvider) AddHook(h log.Hook) error { return nil }

// log logs a message with the specified level and fields.
func (p *zapProvider) log(level log.Level, msg string, fields []log.Field) {
	if p.level > level {
		return
	}
	switch level {
	case log.DebugLevel:
		p.logger.Debug(msg, convertFields(fields)...)
	case log.InfoLevel:
		p.logger.Info(msg, convertFields(fields)...)
	case log.WarnLevel:
		p.logger.Warn(msg, convertFields(fields)...)
	case log.ErrorLevel:
		p.logger.Error(msg, convertFields(fields)...)
	case log.FatalLevel:
		p.logger.Fatal(msg, convertFields(fields)...)
	}
}

// Debug logs a debug-level message.
func (p *zapProvider) Debug(msg string, fields ...log.Field) { p.log(log.DebugLevel, msg, fields) }

// DebugContext logs a debug-level message with context.
func (p *zapProvider) DebugContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.DebugLevel, msg, fields)
}

// Info logs an info-level message.
func (p *zapProvider) Info(msg string, fields ...log.Field) { p.log(log.InfoLevel, msg, fields) }

// InfoContext logs an info-level message with context.
func (p *zapProvider) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.InfoLevel, msg, fields)
}

// Warn logs a warning-level message.
func (p *zapProvider) Warn(msg string, fields ...log.Field) { p.log(log.WarnLevel, msg, fields) }

// WarnContext logs a warning-level message with context.
func (p *zapProvider) WarnContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.WarnLevel, msg, fields)
}

// Error logs an error-level message.
func (p *zapProvider) Error(msg string, fields ...log.Field) { p.log(log.ErrorLevel, msg, fields) }

// ErrorContext logs an error-level message with context.
func (p *zapProvider) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.ErrorLevel, msg, fields)
}

// Fatal logs a fatal-level message.
func (p *zapProvider) Fatal(msg string, fields ...log.Field) { p.log(log.FatalLevel, msg, fields) }

// FatalContext logs a fatal-level message with context.
func (p *zapProvider) FatalContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.FatalLevel, msg, fields)
}

// With returns a new logger with additional structured fields.
func (p *zapProvider) With(fields ...log.Field) log.Logger {
	l := p.logger.With(convertFields(fields)...)
	return &zapProvider{logger: l, level: p.level}
}

// WithContext returns a new logger associated with the context.
func (p *zapProvider) WithContext(ctx context.Context) log.Logger {
	return p
}

// SetLevel sets the minimum level for this logger.
func (p *zapProvider) SetLevel(level log.Level) { p.level = level }

// GetLevel returns the current logging level.
func (p *zapProvider) GetLevel() log.Level { return p.level }

// convertFields converts log.Field values into zap fields.
func convertFields(fields []log.Field) []zap.Field {
	zs := make([]zap.Field, len(fields))
	for i, f := range fields {
		zs[i] = zap.Any(f.Key, f.Value)
	}
	return zs
}

// parseLevel converts a string level into a log.Level.
func parseLevel(l string) log.Level {
	switch l {
	case "debug":
		return log.DebugLevel
	case "info":
		return log.InfoLevel
	case "warn":
		return log.WarnLevel
	case "error":
		return log.ErrorLevel
	case "fatal":
		return log.FatalLevel
	default:
		return log.InfoLevel
	}
}
