// file: pkg/cache/serialization/json.go
// version: 1.0.0
// guid: 7a8b9c0d-1e2f-43a4-5b6c-7d8e9f0a1b2c

package serialization

import "encoding/json"

// JSON implements Serializer using JSON encoding.
type JSON struct{}

// Marshal serializes v into JSON.
func (JSON) Marshal(v interface{}) ([]byte, error) {
	return json.Marshal(v)
}

// Unmarshal deserializes JSON data into v.
func (JSON) Unmarshal(data []byte, v interface{}) error {
	return json.Unmarshal(data, v)
}
