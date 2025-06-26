// file: pkg/log/std.go

package log

import (
	"context"
	"fmt"
	"io"
	stdlog "log"
	"os"
	"strings"
)

// stdProvider implements the Provider interface using the standard library logger.
type stdProvider struct {
	logger *stdlog.Logger
	level  Level
}

// NewStdProvider creates a new standard library logging provider.
func NewStdProvider(config Config) (Provider, error) {
	p := &stdProvider{
		logger: stdlog.New(os.Stdout, "", stdlog.LstdFlags),
		level:  parseLevel(config.Level),
	}
	return p, nil
}

func (p *stdProvider) Name() string          { return "std" }
func (p *stdProvider) Close() error          { return nil }
func (p *stdProvider) Sync() error           { return nil }
func (p *stdProvider) SetOutput(w io.Writer) { p.logger.SetOutput(w) }
func (p *stdProvider) AddHook(h Hook) error  { return nil }

func (p *stdProvider) logf(level Level, msg string, fields []Field) {
	if p.level > level {
		return
	}
	if len(fields) > 0 {
		msg = fmt.Sprintf("%s %s", msg, formatFields(fields))
	}
	p.logger.Printf("[%s] %s", level.String(), msg)
}

func (p *stdProvider) Debug(msg string, fields ...Field) { p.logf(DebugLevel, msg, fields) }
func (p *stdProvider) DebugContext(ctx context.Context, msg string, fields ...Field) {
	p.Debug(msg, fields...)
}
func (p *stdProvider) Info(msg string, fields ...Field) { p.logf(InfoLevel, msg, fields) }
func (p *stdProvider) InfoContext(ctx context.Context, msg string, fields ...Field) {
	p.Info(msg, fields...)
}
func (p *stdProvider) Warn(msg string, fields ...Field) { p.logf(WarnLevel, msg, fields) }
func (p *stdProvider) WarnContext(ctx context.Context, msg string, fields ...Field) {
	p.Warn(msg, fields...)
}
func (p *stdProvider) Error(msg string, fields ...Field) { p.logf(ErrorLevel, msg, fields) }
func (p *stdProvider) ErrorContext(ctx context.Context, msg string, fields ...Field) {
	p.Error(msg, fields...)
}
func (p *stdProvider) Fatal(msg string, fields ...Field) { p.logf(FatalLevel, msg, fields); os.Exit(1) }
func (p *stdProvider) FatalContext(ctx context.Context, msg string, fields ...Field) {
	p.Fatal(msg, fields...)
}
func (p *stdProvider) With(fields ...Field) Logger {
	return &stdProvider{logger: p.logger, level: p.level}
}
func (p *stdProvider) WithContext(ctx context.Context) Logger { return p }
func (p *stdProvider) SetLevel(level Level)                   { p.level = level }
func (p *stdProvider) GetLevel() Level                        { return p.level }

func formatFields(fields []Field) string {
	var b strings.Builder
	for i, f := range fields {
		if i > 0 {
			b.WriteByte(' ')
		}
		b.WriteString(f.Key)
		b.WriteByte('=')
		fmt.Fprint(&b, f.Value)
	}
	return b.String()
}

func parseLevel(l string) Level {
	switch strings.ToLower(l) {
	case "debug":
		return DebugLevel
	case "info":
		return InfoLevel
	case "warn", "warning":
		return WarnLevel
	case "error":
		return ErrorLevel
	case "fatal":
		return FatalLevel
	default:
		return InfoLevel
	}
}

func init() {
	RegisterProvider("std", NewStdProvider)
}
