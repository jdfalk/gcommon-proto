// file: pkg/organization/tenant/billing.go
// version: 1.1.0
// guid: df9428d4-0a64-4f66-ae1c-97f16f56dcda

// Package tenant provides basic billing and quota tracking for tenants.
package tenant

import (
	"context"
	"errors"
	"sync"
	"time"
)

// Quota defines resource limits for a tenant.
type Quota struct {
	CPUSeconds   int64
	MemoryBytes  int64
	StorageBytes int64
	NetworkBytes int64
}

// BillingRecord captures usage and cost information for a billing period.
type BillingRecord struct {
	TenantID string
	Period   time.Time
	Usage    *Usage
	CostUSD  float64
}

// BillingManager tracks tenant quotas, usage and billing records.
type BillingManager struct {
	mu      sync.RWMutex
	quotas  map[string]*Quota
	usage   map[string]*Usage
	records map[string][]*BillingRecord
	pricing PricingModel
}

// PricingModel defines cost multipliers for usage metrics.
type PricingModel struct {
	CPUSecondUSD   float64
	MemoryByteUSD  float64
	StorageByteUSD float64
	NetworkByteUSD float64
}

// NewBillingManager returns an initialized BillingManager with default pricing.
func NewBillingManager() *BillingManager {
	return &BillingManager{
		quotas:  make(map[string]*Quota),
		usage:   make(map[string]*Usage),
		records: make(map[string][]*BillingRecord),
		pricing: PricingModel{
			CPUSecondUSD:   0.001,
			MemoryByteUSD:  0.0000001,
			StorageByteUSD: 0.00000005,
			NetworkByteUSD: 0.00000002,
		},
	}
}

// SetQuota sets resource limits for a tenant.
func (m *BillingManager) SetQuota(ctx context.Context, tenantID string, q *Quota) error {
	if tenantID == "" {
		return errors.New("missing tenant id")
	}
	if q == nil {
		return errors.New("missing quota")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	m.quotas[tenantID] = q
	if _, ok := m.usage[tenantID]; !ok {
		m.usage[tenantID] = &Usage{}
	}
	return nil
}

// AddUsage accumulates usage for the tenant and returns whether the quota has been exceeded.
func (m *BillingManager) AddUsage(ctx context.Context, tenantID string, u *Usage) (bool, error) {
	if u == nil {
		return false, errors.New("missing usage")
	}
	m.mu.Lock()
	defer m.mu.Unlock()
	current, ok := m.usage[tenantID]
	if !ok {
		current = &Usage{}
		m.usage[tenantID] = current
	}
	current.CpuSeconds += u.CpuSeconds
	current.MemoryBytes += u.MemoryBytes
	current.StorageBytes += u.StorageBytes
	current.NetworkBytes += u.NetworkBytes
	q, ok := m.quotas[tenantID]
	if !ok {
		return false, errors.New("quota not set")
	}
	exceeded := current.CpuSeconds > q.CPUSeconds ||
		current.MemoryBytes > q.MemoryBytes ||
		current.StorageBytes > q.StorageBytes ||
		current.NetworkBytes > q.NetworkBytes
	return exceeded, nil
}

// GenerateRecord finalizes current usage into a billing record and resets usage counters.
func (m *BillingManager) GenerateRecord(ctx context.Context, tenantID string, period time.Time) (*BillingRecord, error) {
	m.mu.Lock()
	defer m.mu.Unlock()
	usage, ok := m.usage[tenantID]
	if !ok {
		return nil, errors.New("usage not found")
	}
	// Calculate cost
	cost := float64(usage.CpuSeconds)*m.pricing.CPUSecondUSD +
		float64(usage.MemoryBytes)*m.pricing.MemoryByteUSD +
		float64(usage.StorageBytes)*m.pricing.StorageByteUSD +
		float64(usage.NetworkBytes)*m.pricing.NetworkByteUSD
	record := &BillingRecord{
		TenantID: tenantID,
		Period:   period,
		Usage:    usage,
		CostUSD:  cost,
	}
	m.records[tenantID] = append(m.records[tenantID], record)
	// Reset usage after generating record
	m.usage[tenantID] = &Usage{}
	return record, nil
}

// Records returns billing records for a tenant.
func (m *BillingManager) Records(ctx context.Context, tenantID string) ([]*BillingRecord, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	recs, ok := m.records[tenantID]
	if !ok {
		return nil, errors.New("no billing records")
	}
	result := make([]*BillingRecord, len(recs))
	copy(result, recs)
	return result, nil
}

// CurrentUsage returns the current accumulated usage for a tenant.
func (m *BillingManager) CurrentUsage(ctx context.Context, tenantID string) (*Usage, error) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	usage, ok := m.usage[tenantID]
	if !ok {
		return nil, errors.New("usage not found")
	}
	copy := *usage
	return &copy, nil
}

// Remove clears all billing information for a tenant.
func (m *BillingManager) Remove(ctx context.Context, tenantID string) {
	m.mu.Lock()
	defer m.mu.Unlock()
	delete(m.quotas, tenantID)
	delete(m.usage, tenantID)
	delete(m.records, tenantID)
}
