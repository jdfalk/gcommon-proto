from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LoggerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGGER_STATUS_UNSPECIFIED: _ClassVar[LoggerStatus]
    LOGGER_STATUS_ACTIVE: _ClassVar[LoggerStatus]
    LOGGER_STATUS_INACTIVE: _ClassVar[LoggerStatus]
    LOGGER_STATUS_ERROR: _ClassVar[LoggerStatus]
LOGGER_STATUS_UNSPECIFIED: LoggerStatus
LOGGER_STATUS_ACTIVE: LoggerStatus
LOGGER_STATUS_INACTIVE: LoggerStatus
LOGGER_STATUS_ERROR: LoggerStatus
