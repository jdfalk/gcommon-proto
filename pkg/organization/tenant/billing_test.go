// file: pkg/organization/tenant/billing_test.go
// version: 1.1.0
// guid: a6c070e9-ded4-42d6-a224-37abad83a389

package tenant

import (
	"context"
	"testing"
	"time"
)

// TestBillingManager_QuotaAndRecord verifies quota enforcement and record generation.
func TestBillingManager_QuotaAndRecord(t *testing.T) {
	// Setup
	ctx := context.Background()
	bm := NewBillingManager()
	quota := &Quota{CPUSeconds: 5}
	if err := bm.SetQuota(ctx, "t1", quota); err != nil {
		t.Fatalf("set quota: %v", err)
	}
	usage := &Usage{CpuSeconds: 10}

	// Exercise
	exceeded, err := bm.AddUsage(ctx, "t1", usage)
	if err != nil {
		t.Fatalf("add usage: %v", err)
	}
	if !exceeded {
		t.Fatalf("expected quota exceeded")
	}

	// Generate record
	rec, err := bm.GenerateRecord(ctx, "t1", time.Now())
	if err != nil {
		t.Fatalf("generate record: %v", err)
	}
	if rec.Usage.CpuSeconds != 10 {
		t.Fatalf("expected usage 10")
	}
}
