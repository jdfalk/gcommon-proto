from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LogSortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_SORT_FIELD_UNSPECIFIED: _ClassVar[LogSortField]
    LOG_SORT_FIELD_TIMESTAMP: _ClassVar[LogSortField]
    LOG_SORT_FIELD_LEVEL: _ClassVar[LogSortField]
    LOG_SORT_FIELD_LOGGER: _ClassVar[LogSortField]
    LOG_SORT_FIELD_MESSAGE: _ClassVar[LogSortField]
LOG_SORT_FIELD_UNSPECIFIED: LogSortField
LOG_SORT_FIELD_TIMESTAMP: LogSortField
LOG_SORT_FIELD_LEVEL: LogSortField
LOG_SORT_FIELD_LOGGER: LogSortField
LOG_SORT_FIELD_MESSAGE: LogSortField
