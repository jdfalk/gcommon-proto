// file: pkg/config/merger.go
// version: 1.0.0
// guid: 44444444-5555-6666-7777-888888888888

package config

// Merger combines multiple configuration maps following precedence.
type Merger struct {
	order []map[string]interface{}
}

// NewMerger creates a Merger with given configs ordered from lowest to highest precedence.
func NewMerger(configs ...map[string]interface{}) *Merger {
	return &Merger{order: configs}
}

// Merge produces a single configuration map applying precedence.
func (m *Merger) Merge() map[string]interface{} {
	result := make(map[string]interface{})
	for _, cfg := range m.order {
		for k, v := range cfg {
			result[k] = v
		}
	}
	return result
}
