// file: pkg/log/providers/zerolog.go
// version: 1.0.0
// guid: f2b0f0f2-91d2-4b9e-9c3f-4f3e7b2a1c6d

package providers

import (
	"context"
	"io"
	"os"

	"github.com/jdfalk/gcommon/pkg/log"
	"github.com/rs/zerolog"
)

// zerologProvider implements log.Provider using rs/zerolog.
type zerologProvider struct {
	logger *zerolog.Logger
	level  log.Level
}

// init registers the zerolog provider.
func init() {
	log.RegisterProvider("zerolog", newZeroLogProvider)
}

// newZeroLogProvider creates a zerolog-based provider.
func newZeroLogProvider(cfg log.Config) (log.Provider, error) {
	z := zerolog.New(os.Stdout).With().Timestamp().Logger()
	p := &zerologProvider{logger: &z, level: parseLevel(cfg.Level)}
	return p, nil
}

func (p *zerologProvider) Name() string { return "zerolog" }

func (p *zerologProvider) Close() error { return nil }

func (p *zerologProvider) Sync() error { return nil }

func (p *zerologProvider) SetOutput(w io.Writer) {
	l := zerolog.New(w).With().Timestamp().Logger()
	p.logger = &l
}

func (p *zerologProvider) AddHook(h log.Hook) error { return nil }

func (p *zerologProvider) log(level log.Level, msg string, fields []log.Field) {
	if p.level > level {
		return
	}
	e := p.logger.With()
	for _, f := range fields {
		e = e.Interface(f.Key, f.Value)
	}
	logger := e.Logger()
	switch level {
	case log.DebugLevel:
		logger.Debug().Msg(msg)
	case log.InfoLevel:
		logger.Info().Msg(msg)
	case log.WarnLevel:
		logger.Warn().Msg(msg)
	case log.ErrorLevel:
		logger.Error().Msg(msg)
	case log.FatalLevel:
		logger.Fatal().Msg(msg)
	}
}

func (p *zerologProvider) Debug(msg string, fields ...log.Field) { p.log(log.DebugLevel, msg, fields) }
func (p *zerologProvider) DebugContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.DebugLevel, msg, fields)
}
func (p *zerologProvider) Info(msg string, fields ...log.Field) { p.log(log.InfoLevel, msg, fields) }
func (p *zerologProvider) InfoContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.InfoLevel, msg, fields)
}
func (p *zerologProvider) Warn(msg string, fields ...log.Field) { p.log(log.WarnLevel, msg, fields) }
func (p *zerologProvider) WarnContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.WarnLevel, msg, fields)
}
func (p *zerologProvider) Error(msg string, fields ...log.Field) { p.log(log.ErrorLevel, msg, fields) }
func (p *zerologProvider) ErrorContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.ErrorLevel, msg, fields)
}
func (p *zerologProvider) Fatal(msg string, fields ...log.Field) { p.log(log.FatalLevel, msg, fields) }
func (p *zerologProvider) FatalContext(ctx context.Context, msg string, fields ...log.Field) {
	p.log(log.FatalLevel, msg, fields)
}

func (p *zerologProvider) With(fields ...log.Field) log.Logger {
	e := p.logger.With()
	for _, f := range fields {
		e = e.Interface(f.Key, f.Value)
	}
	np := *p
	l := e.Logger()
	np.logger = &l
	return &np
}

func (p *zerologProvider) WithContext(ctx context.Context) log.Logger { return p }

func (p *zerologProvider) SetLevel(level log.Level) { p.level = level }

func (p *zerologProvider) GetLevel() log.Level { return p.level }
