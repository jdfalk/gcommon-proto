from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_TYPE_UNSPECIFIED: _ClassVar[ValueType]
    VALUE_TYPE_STRING: _ClassVar[ValueType]
    VALUE_TYPE_INT: _ClassVar[ValueType]
    VALUE_TYPE_DOUBLE: _ClassVar[ValueType]
    VALUE_TYPE_BOOL: _ClassVar[ValueType]
    VALUE_TYPE_BYTES: _ClassVar[ValueType]
    VALUE_TYPE_JSON: _ClassVar[ValueType]
    VALUE_TYPE_YAML: _ClassVar[ValueType]
VALUE_TYPE_UNSPECIFIED: ValueType
VALUE_TYPE_STRING: ValueType
VALUE_TYPE_INT: ValueType
VALUE_TYPE_DOUBLE: ValueType
VALUE_TYPE_BOOL: ValueType
VALUE_TYPE_BYTES: ValueType
VALUE_TYPE_JSON: ValueType
VALUE_TYPE_YAML: ValueType
