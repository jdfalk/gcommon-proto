from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaCompatibilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEMA_COMPATIBILITY_MODE_UNSPECIFIED: _ClassVar[SchemaCompatibilityMode]
    SCHEMA_COMPATIBILITY_MODE_STRICT: _ClassVar[SchemaCompatibilityMode]
    SCHEMA_COMPATIBILITY_MODE_LENIENT: _ClassVar[SchemaCompatibilityMode]
    SCHEMA_COMPATIBILITY_MODE_NONE: _ClassVar[SchemaCompatibilityMode]

SCHEMA_COMPATIBILITY_MODE_UNSPECIFIED: SchemaCompatibilityMode
SCHEMA_COMPATIBILITY_MODE_STRICT: SchemaCompatibilityMode
SCHEMA_COMPATIBILITY_MODE_LENIENT: SchemaCompatibilityMode
SCHEMA_COMPATIBILITY_MODE_NONE: SchemaCompatibilityMode
