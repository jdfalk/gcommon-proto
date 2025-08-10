// file: pkg/errors/types_test.go
// version: 1.1.0
// guid: fb48d36d-d03f-42e1-af17-86e43f1eeef2

package errors

import (
	"context"
	"fmt"
	"testing"
)

// TestNewError verifies that NewError creates an Error with expected fields.
func TestNewError(t *testing.T) {
	err := NewError(context.Background(), ErrCodeInternal, "message")
	e, ok := err.(*BaseError)
	if !ok {
		t.Fatalf("expected *BaseError, got %T", err)
	}
	if e.Code() != ErrCodeInternal {
		t.Fatalf("expected code %v, got %v", ErrCodeInternal, e.Code())
	}
	if e.Component() != "" || e.Operation() != "" {
		t.Fatalf("unexpected component or operation")
	}
}

// TestWrapWithCode verifies that wrapping preserves the cause and code.
func TestWrapWithCode(t *testing.T) {
	base := fmt.Errorf("root cause")
	wrapped := WrapWithCode(base, ErrCodeTimeout, "comp", "op")
	if wrapped.Cause() != base {
		t.Fatalf("expected cause to be preserved")
	}
	if wrapped.Code() != ErrCodeTimeout {
		t.Fatalf("expected code %v, got %v", ErrCodeTimeout, wrapped.Code())
	}
	if wrapped.Component() != "comp" || wrapped.Operation() != "op" {
		t.Fatalf("component or operation not set")
	}
}

// TestWrapWithDetails verifies that details are merged into the error.
func TestWrapWithDetails(t *testing.T) {
	base := fmt.Errorf("failure")
	wrapped := WrapWithDetails(base, map[string]interface{}{"k": "v"})
	if wrapped.Details()["k"] != "v" {
		t.Fatalf("expected detail to be present")
	}
}

// TestSpecificErrors ensures specialized error constructors populate fields.
func TestSpecificErrors(t *testing.T) {
	ce := NewConfigError(ErrCodeConfigInvalid, "key", "val", "bad config")
	if ce.ConfigKey != "key" || ce.ConfigValue != "val" {
		t.Fatalf("config fields not set")
	}
	qe := NewQueueError(ErrCodeQueueFull, "main", "id1", "full")
	if qe.QueueName != "main" || qe.MessageID != "id1" {
		t.Fatalf("queue fields not set")
	}
	ae := NewAuthError(ErrCodeUnauthorized, "u1", "res", "act", "unauth")
	if ae.UserID != "u1" || ae.Resource != "res" || ae.Action != "act" {
		t.Fatalf("auth fields not set")
	}
	me := NewMetricsError(ErrCodeMetricInvalid, "cpu", "bad metric")
	if me.MetricName != "cpu" {
		t.Fatalf("metric name not set")
	}
	cache := NewCacheError(ErrCodeCacheMiss, "k", "miss")
	if cache.Key != "k" {
		t.Fatalf("cache key not set")
	}
	we := NewWebError(ErrCodeRouteNotFound, "/path", "missing")
	if we.Route != "/path" {
		t.Fatalf("web route not set")
	}
	de := NewDBError(ErrCodeDBQuery, "SELECT", "db err")
	if de.Query != "SELECT" {
		t.Fatalf("db query not set")
	}
	le := NewLogError(ErrCodeLogWriteFailed, "main", "log err")
	if le.Logger != "main" {
		t.Fatalf("logger not set")
	}
}
