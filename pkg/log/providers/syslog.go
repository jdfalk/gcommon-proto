// file: pkg/log/providers/syslog.go
// version: 1.0.0
// guid: aac4e9e8-9788-4f54-9bcb-6e75d4a1d941

package providers

import (
	"context"
	"fmt"
	"io"
	"log/syslog"

	"github.com/jdfalk/gcommon/pkg/log"
)

// syslogProvider sends logs to the system syslog service.
type syslogProvider struct {
	writer *syslog.Writer
	level  log.Level
}

// init registers the syslog provider.
func init() {
	log.RegisterProvider("syslog", newSyslogProvider)
}

// newSyslogProvider creates a provider that writes to syslog.
func newSyslogProvider(cfg log.Config) (log.Provider, error) {
	w, err := syslog.New(syslog.LOG_INFO|syslog.LOG_USER, "gcommon")
	if err != nil {
		return nil, err
	}
	return &syslogProvider{writer: w, level: parseLevel(cfg.Level)}, nil
}

func (p *syslogProvider) Name() string { return "syslog" }

func (p *syslogProvider) Close() error { return p.writer.Close() }

func (p *syslogProvider) Sync() error { return nil }

func (p *syslogProvider) SetOutput(w io.Writer) {}

func (p *syslogProvider) AddHook(h log.Hook) error { return nil }

func (p *syslogProvider) log(level log.Level, msg string) {
	if p.level > level {
		return
	}
	switch level {
	case log.DebugLevel:
		_ = p.writer.Debug(msg)
	case log.InfoLevel:
		_ = p.writer.Info(msg)
	case log.WarnLevel:
		_ = p.writer.Warning(msg)
	case log.ErrorLevel:
		_ = p.writer.Err(msg)
	case log.FatalLevel:
		_ = p.writer.Crit(msg)
	}
}

func (p *syslogProvider) Debug(msg string, fields ...log.Field) {
	p.log(log.DebugLevel, formatSyslog(msg, fields))
}
func (p *syslogProvider) DebugContext(ctx context.Context, msg string, fields ...log.Field) {
	p.Debug(msg, fields...)
}
func (p *syslogProvider) Info(msg string, fields ...log.Field) {
	p.log(log.InfoLevel, formatSyslog(msg, fields))
}
func (p *syslogProvider) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	p.Info(msg, fields...)
}
func (p *syslogProvider) Warn(msg string, fields ...log.Field) {
	p.log(log.WarnLevel, formatSyslog(msg, fields))
}
func (p *syslogProvider) WarnContext(ctx context.Context, msg string, fields ...log.Field) {
	p.Warn(msg, fields...)
}
func (p *syslogProvider) Error(msg string, fields ...log.Field) {
	p.log(log.ErrorLevel, formatSyslog(msg, fields))
}
func (p *syslogProvider) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {
	p.Error(msg, fields...)
}
func (p *syslogProvider) Fatal(msg string, fields ...log.Field) {
	p.log(log.FatalLevel, formatSyslog(msg, fields))
}
func (p *syslogProvider) FatalContext(ctx context.Context, msg string, fields ...log.Field) {
	p.Fatal(msg, fields...)
}

func (p *syslogProvider) With(fields ...log.Field) log.Logger { return p }

func (p *syslogProvider) WithContext(ctx context.Context) log.Logger { return p }

func (p *syslogProvider) SetLevel(level log.Level) { p.level = level }

func (p *syslogProvider) GetLevel() log.Level { return p.level }

func formatSyslog(msg string, fields []log.Field) string {
	if len(fields) == 0 {
		return msg
	}
	s := msg
	for _, f := range fields {
		s += " " + f.Key + "=" + fmt.Sprint(f.Value)
	}
	return s
}
