from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LogFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILTER_TYPE_UNSPECIFIED: _ClassVar[LogFilterType]
    FILTER_TYPE_LEVEL: _ClassVar[LogFilterType]
    FILTER_TYPE_LOGGER: _ClassVar[LogFilterType]
    FILTER_TYPE_MESSAGE: _ClassVar[LogFilterType]
    FILTER_TYPE_FIELD: _ClassVar[LogFilterType]
FILTER_TYPE_UNSPECIFIED: LogFilterType
FILTER_TYPE_LEVEL: LogFilterType
FILTER_TYPE_LOGGER: LogFilterType
FILTER_TYPE_MESSAGE: LogFilterType
FILTER_TYPE_FIELD: LogFilterType
