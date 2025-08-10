// file: pkg/log/providers/logrus.go
// version: 1.0.0
// guid: d7c6ed52-9f8c-4cb6-8b67-5dcd5ef16e21

package providers

import (
	"context"
	"io"

	"github.com/jdfalk/gcommon/pkg/log"
	logrus "github.com/sirupsen/logrus"
)

// logrusProvider implements log.Provider using the logrus library.
type logrusProvider struct {
	logger *logrus.Logger
	level  log.Level
}

// init registers the logrus provider.
func init() {
	log.RegisterProvider("logrus", newLogrusProvider)
}

// newLogrusProvider creates a new logrus-based provider.
func newLogrusProvider(cfg log.Config) (log.Provider, error) {
	l := logrus.New()
	if cfg.Format == "json" {
		l.SetFormatter(&logrus.JSONFormatter{})
	}
	p := &logrusProvider{logger: l, level: parseLevel(cfg.Level)}
	return p, nil
}

func (p *logrusProvider) Name() string { return "logrus" }

// Close closes the logger; logrus has no close operation.
func (p *logrusProvider) Close() error { return nil }

// Sync flushes logs; logrus does not buffer, so this is a no-op.
func (p *logrusProvider) Sync() error { return nil }

// SetOutput sets the destination for logs.
func (p *logrusProvider) SetOutput(w io.Writer) { p.logger.SetOutput(w) }

// AddHook adds a logrus hook.
func (p *logrusProvider) AddHook(h log.Hook) error { return nil }

func (p *logrusProvider) log(level log.Level, msg string, fields []log.Field) {
	if p.level > level {
		return
	}
	entry := p.logger.WithFields(convertToLogrus(fields))
	switch level {
	case log.DebugLevel:
		entry.Debug(msg)
	case log.InfoLevel:
		entry.Info(msg)
	case log.WarnLevel:
		entry.Warn(msg)
	case log.ErrorLevel:
		entry.Error(msg)
	case log.FatalLevel:
		entry.Fatal(msg)
	}
}

func (p *logrusProvider) Debug(msg string, fields ...log.Field) { p.log(log.DebugLevel, msg, fields) }
func (p *logrusProvider) DebugContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.DebugLevel, msg, fields)
}
func (p *logrusProvider) Info(msg string, fields ...log.Field) { p.log(log.InfoLevel, msg, fields) }
func (p *logrusProvider) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.InfoLevel, msg, fields)
}
func (p *logrusProvider) Warn(msg string, fields ...log.Field) { p.log(log.WarnLevel, msg, fields) }
func (p *logrusProvider) WarnContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.WarnLevel, msg, fields)
}
func (p *logrusProvider) Error(msg string, fields ...log.Field) { p.log(log.ErrorLevel, msg, fields) }
func (p *logrusProvider) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.ErrorLevel, msg, fields)
}
func (p *logrusProvider) Fatal(msg string, fields ...log.Field) { p.log(log.FatalLevel, msg, fields) }
func (p *logrusProvider) FatalContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.FatalLevel, msg, fields)
}

func (p *logrusProvider) With(fields ...log.Field) log.Logger {
	c := p.logger.WithFields(convertToLogrus(fields))
	np := *p
	np.logger = c.Logger
	return &np
}

func (p *logrusProvider) WithContext(ctx context.Context) log.Logger { return p }

func (p *logrusProvider) SetLevel(level log.Level) {
	p.level = level
	p.logger.SetLevel(toLogrusLevel(level))
}

func (p *logrusProvider) GetLevel() log.Level { return p.level }

func convertToLogrus(fields []log.Field) logrus.Fields {
	lf := logrus.Fields{}
	for _, f := range fields {
		lf[f.Key] = f.Value
	}
	return lf
}

func toLogrusLevel(level log.Level) logrus.Level {
	switch level {
	case log.DebugLevel:
		return logrus.DebugLevel
	case log.InfoLevel:
		return logrus.InfoLevel
	case log.WarnLevel:
		return logrus.WarnLevel
	case log.ErrorLevel:
		return logrus.ErrorLevel
	case log.FatalLevel:
		return logrus.FatalLevel
	default:
		return logrus.InfoLevel
	}
}
