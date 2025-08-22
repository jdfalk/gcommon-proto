from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEMA_FORMAT_UNSPECIFIED: _ClassVar[SchemaFormat]
    SCHEMA_FORMAT_JSON_SCHEMA: _ClassVar[SchemaFormat]
    SCHEMA_FORMAT_AVRO: _ClassVar[SchemaFormat]
    SCHEMA_FORMAT_PROTOBUF: _ClassVar[SchemaFormat]
    SCHEMA_FORMAT_XML_SCHEMA: _ClassVar[SchemaFormat]
    SCHEMA_FORMAT_CUSTOM: _ClassVar[SchemaFormat]
SCHEMA_FORMAT_UNSPECIFIED: SchemaFormat
SCHEMA_FORMAT_JSON_SCHEMA: SchemaFormat
SCHEMA_FORMAT_AVRO: SchemaFormat
SCHEMA_FORMAT_PROTOBUF: SchemaFormat
SCHEMA_FORMAT_XML_SCHEMA: SchemaFormat
SCHEMA_FORMAT_CUSTOM: SchemaFormat
