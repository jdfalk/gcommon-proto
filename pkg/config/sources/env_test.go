// file: pkg/config/sources/env_test.go
// version: 1.0.0
// guid: 12345678-90ab-cdef-1234-567890abcdef

package sources

import (
	"testing"
)

// TestEnvSourceBasic verifies loading with nested keys, expansion, allow/deny lists and defaults.
func TestEnvSourceBasic(t *testing.T) {
	t.Setenv("APP_DB__HOST", "localhost")
	t.Setenv("APP_DB__PORT", "5432")
	t.Setenv("APP_PATH", "/data")
	t.Setenv("APP_LOG", "${APP_PATH}/logs")
	t.Setenv("APP_SECRET", "ignore")

	src := EnvSource{
		Prefix:     "APP_",
		ExpandVars: true,
		Denylist:   []string{"SECRET"},
		Defaults:   map[string]string{"missing": "42"},
	}

	cfg, err := src.Load()
	if err != nil {
		t.Fatalf("Load failed: %v", err)
	}

	db, ok := cfg["db"].(map[string]interface{})
	if !ok {
		t.Fatalf("expected db map, got %T", cfg["db"])
	}
	if db["host"] != "localhost" {
		t.Fatalf("unexpected host: %v", db["host"])
	}
	if db["port"] != "5432" {
		t.Fatalf("unexpected port: %v", db["port"])
	}
	if cfg["log"] != "/data/logs" {
		t.Fatalf("unexpected log: %v", cfg["log"])
	}
	if cfg["secret"] != nil {
		t.Fatalf("secret should be denied, got %v", cfg["secret"])
	}
	if cfg["missing"] != "42" {
		t.Fatalf("default not applied: %v", cfg["missing"])
	}
}

// TestEnvSourceAllowlist ensures only allowed keys are included when allowlist is set.
func TestEnvSourceAllowlist(t *testing.T) {
	t.Setenv("APP_FOO", "1")
	t.Setenv("APP_BAR", "2")
	src := EnvSource{Prefix: "APP_", Allowlist: []string{"BAR"}}
	cfg, err := src.Load()
	if err != nil {
		t.Fatalf("Load failed: %v", err)
	}
	if _, ok := cfg["foo"]; ok {
		t.Fatalf("foo should not be included")
	}
	if cfg["bar"] != "2" {
		t.Fatalf("bar not loaded: %v", cfg["bar"])
	}
}
