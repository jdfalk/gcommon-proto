from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SerializationFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERIALIZATION_FORMAT_UNSPECIFIED: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_PROTOBUF: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_JSON: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_MSGPACK: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_AVRO: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_BINARY: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_TEXT: _ClassVar[SerializationFormat]
    SERIALIZATION_FORMAT_XML: _ClassVar[SerializationFormat]

SERIALIZATION_FORMAT_UNSPECIFIED: SerializationFormat
SERIALIZATION_FORMAT_PROTOBUF: SerializationFormat
SERIALIZATION_FORMAT_JSON: SerializationFormat
SERIALIZATION_FORMAT_MSGPACK: SerializationFormat
SERIALIZATION_FORMAT_AVRO: SerializationFormat
SERIALIZATION_FORMAT_BINARY: SerializationFormat
SERIALIZATION_FORMAT_TEXT: SerializationFormat
SERIALIZATION_FORMAT_XML: SerializationFormat
