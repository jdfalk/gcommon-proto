from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARAMETER_TYPE_UNSPECIFIED: _ClassVar[ParameterType]
    PARAMETER_TYPE_STRING: _ClassVar[ParameterType]
    PARAMETER_TYPE_INTEGER: _ClassVar[ParameterType]
    PARAMETER_TYPE_FLOAT: _ClassVar[ParameterType]
    PARAMETER_TYPE_BOOLEAN: _ClassVar[ParameterType]
    PARAMETER_TYPE_ENUM: _ClassVar[ParameterType]
    PARAMETER_TYPE_ARRAY: _ClassVar[ParameterType]
    PARAMETER_TYPE_OBJECT: _ClassVar[ParameterType]
    PARAMETER_TYPE_FILE: _ClassVar[ParameterType]
    PARAMETER_TYPE_URL: _ClassVar[ParameterType]
    PARAMETER_TYPE_EMAIL: _ClassVar[ParameterType]
    PARAMETER_TYPE_PASSWORD: _ClassVar[ParameterType]
    PARAMETER_TYPE_DATE: _ClassVar[ParameterType]
    PARAMETER_TYPE_TIME: _ClassVar[ParameterType]
    PARAMETER_TYPE_DATETIME: _ClassVar[ParameterType]

PARAMETER_TYPE_UNSPECIFIED: ParameterType
PARAMETER_TYPE_STRING: ParameterType
PARAMETER_TYPE_INTEGER: ParameterType
PARAMETER_TYPE_FLOAT: ParameterType
PARAMETER_TYPE_BOOLEAN: ParameterType
PARAMETER_TYPE_ENUM: ParameterType
PARAMETER_TYPE_ARRAY: ParameterType
PARAMETER_TYPE_OBJECT: ParameterType
PARAMETER_TYPE_FILE: ParameterType
PARAMETER_TYPE_URL: ParameterType
PARAMETER_TYPE_EMAIL: ParameterType
PARAMETER_TYPE_PASSWORD: ParameterType
PARAMETER_TYPE_DATE: ParameterType
PARAMETER_TYPE_TIME: ParameterType
PARAMETER_TYPE_DATETIME: ParameterType
