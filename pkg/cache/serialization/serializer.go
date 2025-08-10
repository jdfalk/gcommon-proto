// file: pkg/cache/serialization/serializer.go
// version: 1.0.0
// guid: 6f7a8b9c-0d1e-42f3-1a2b-3c4d5e6f7a8b

package serialization

// Serializer defines methods for serializing data before storage.
type Serializer interface {
	Marshal(v interface{}) ([]byte, error)
	Unmarshal(data []byte, v interface{}) error
}
