// file: pkg/cache/serialization/protobuf.go
// version: 1.0.0
// guid: 8b9c0d1e-2f3a-44b5-6c7d-8e9f0a1b2c3d

package serialization

import (
	"errors"

	"google.golang.org/protobuf/proto"
)

// Protobuf implements Serializer using protobuf encoding.
type Protobuf struct{}

// Marshal serializes v using protobuf.
func (Protobuf) Marshal(v interface{}) ([]byte, error) {
	m, ok := v.(proto.Message)
	if !ok {
		return nil, errors.New("not proto message")
	}
	return proto.Marshal(m)
}

// Unmarshal deserializes data into the provided message.
func (Protobuf) Unmarshal(data []byte, v interface{}) error {
	m, ok := v.(proto.Message)
	if !ok {
		return errors.New("not proto message")
	}
	return proto.Unmarshal(data, m)
}
