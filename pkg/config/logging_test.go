// file: pkg/config/logging_test.go
// version: 1.0.0
// guid: f5706d15-ade4-4b62-a335-d331cdd894a4

package config

import (
	"context"
	"fmt"
	"testing"

	configpb "github.com/jdfalk/gcommon/pkg/config/proto"
	"github.com/jdfalk/gcommon/pkg/log/testlogger"
)

// stubProvider is a simple in-memory provider for testing.
type stubProvider struct {
	store map[string]interface{}
}

func (s *stubProvider) Get(key string) (interface{}, error)          { return s.store[key], nil }
func (s *stubProvider) Set(key string, value interface{}) error      { s.store[key] = value; return nil }
func (s *stubProvider) Watch(key string, cb func(interface{})) error { return nil }
func (s *stubProvider) Close() error                                 { return nil }

// stubService implements ConfigService using a Provider.
type stubService struct{ p Provider }

func (s *stubService) Get(ctx context.Context, req *configpb.GetConfigRequest) (*configpb.GetConfigResponse, error) {
	return &configpb.GetConfigResponse{}, nil
}
func (s *stubService) Set(ctx context.Context, req *configpb.SetConfigRequest) (*configpb.SetConfigResponse, error) {
	return &configpb.SetConfigResponse{}, nil
}
func (s *stubService) Watch(req *configpb.WatchConfigRequest, stream configpb.ConfigService_WatchServer) error {
	return nil
}

func TestLoggedProvider_GetSet(t *testing.T) {
	p := &stubProvider{store: map[string]interface{}{"a": "1"}}
	tl := testlogger.New()
	lp := NewLoggedProvider(p, tl)

	if _, err := lp.Get("a"); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if err := lp.Set("b", "2"); err != nil {
		t.Fatalf("unexpected set error: %v", err)
	}

	entries := tl.Entries()
	if len(entries) != 4 {
		t.Fatalf("expected 4 entries, got %d", len(entries))
	}
	if entries[0].Message != "config get" || entries[2].Message != "config set" {
		t.Fatalf("unexpected messages: %+v", entries)
	}
}

func TestLoggedConfigService_GetSet(t *testing.T) {
	p := &stubProvider{store: map[string]interface{}{"a": "1"}}
	svc := &stubService{p: p}
	tl := testlogger.New()
	ls := NewLoggedConfigService(svc, tl)

	if _, err := ls.Get(context.Background(), &configpb.GetConfigRequest{}); err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if _, err := ls.Set(context.Background(), &configpb.SetConfigRequest{}); err != nil {
		t.Fatalf("unexpected set error: %v", err)
	}

	entries := tl.Entries()
	if len(entries) != 4 {
		t.Fatalf("expected 4 entries, got %d", len(entries))
	}
	if entries[0].Message != "config service get" || entries[2].Message != "config service set" {
		t.Fatalf("unexpected messages: %+v", entries)
	}
}

// errProvider returns errors for all methods.
type errProvider struct{}

func (errProvider) Get(key string) (interface{}, error)          { return nil, fmt.Errorf("fail") }
func (errProvider) Set(key string, value interface{}) error      { return fmt.Errorf("fail") }
func (errProvider) Watch(key string, cb func(interface{})) error { return fmt.Errorf("fail") }
func (errProvider) Close() error                                 { return fmt.Errorf("fail") }

// errService wraps a Provider but returns errors.
type errService struct{ p Provider }

func (e errService) Get(ctx context.Context, req *configpb.GetConfigRequest) (*configpb.GetConfigResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (e errService) Set(ctx context.Context, req *configpb.SetConfigRequest) (*configpb.SetConfigResponse, error) {
	return nil, fmt.Errorf("fail")
}
func (e errService) Watch(req *configpb.WatchConfigRequest, stream configpb.ConfigService_WatchServer) error {
	return fmt.Errorf("fail")
}

func TestLoggedProvider_Error(t *testing.T) {
	tl := testlogger.New()
	lp := NewLoggedProvider(errProvider{}, tl)
	if _, err := lp.Get("x"); err == nil {
		t.Fatalf("expected error")
	}
	if err := lp.Set("x", "1"); err == nil {
		t.Fatalf("expected error")
	}
	if err := lp.Watch("x", func(interface{}) {}); err == nil {
		t.Fatalf("expected error")
	}
	if err := lp.Close(); err == nil {
		t.Fatalf("expected error")
	}
	entries := tl.Entries()
	if len(entries) != 8 {
		t.Fatalf("expected 8 entries, got %d", len(entries))
	}
}

func TestLoggedConfigService_Error(t *testing.T) {
	tl := testlogger.New()
	ls := NewLoggedConfigService(errService{}, tl)
	if _, err := ls.Get(context.Background(), &configpb.GetConfigRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if _, err := ls.Set(context.Background(), &configpb.SetConfigRequest{}); err == nil {
		t.Fatalf("expected error")
	}
	if err := ls.Watch(&configpb.WatchConfigRequest{}, nil); err == nil {
		t.Fatalf("expected error")
	}
	entries := tl.Entries()
	if len(entries) != 6 {
		t.Fatalf("expected 6 entries, got %d", len(entries))
	}
}
