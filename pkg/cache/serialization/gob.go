// file: pkg/cache/serialization/gob.go
// version: 1.0.0
// guid: 9c0d1e2f-3a4b-45c6-7d8e-9f0a1b2c3d4e

package serialization

import (
	"bytes"
	"encoding/gob"
)

// Gob implements Serializer using gob encoding.
type Gob struct{}

// Marshal serializes v using gob.
func (Gob) Marshal(v interface{}) ([]byte, error) {
	var buf bytes.Buffer
	if err := gob.NewEncoder(&buf).Encode(v); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

// Unmarshal deserializes gob data into v.
func (Gob) Unmarshal(data []byte, v interface{}) error {
	return gob.NewDecoder(bytes.NewReader(data)).Decode(v)
}
