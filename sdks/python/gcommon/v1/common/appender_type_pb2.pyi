from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPENDER_TYPE_UNSPECIFIED: _ClassVar[AppenderType]
    APPENDER_TYPE_CONSOLE: _ClassVar[AppenderType]
    APPENDER_TYPE_FILE: _ClassVar[AppenderType]
    APPENDER_TYPE_ROLLING_FILE: _ClassVar[AppenderType]
    APPENDER_TYPE_SYSLOG: _ClassVar[AppenderType]
    APPENDER_TYPE_NETWORK: _ClassVar[AppenderType]
    APPENDER_TYPE_DATABASE: _ClassVar[AppenderType]
APPENDER_TYPE_UNSPECIFIED: AppenderType
APPENDER_TYPE_CONSOLE: AppenderType
APPENDER_TYPE_FILE: AppenderType
APPENDER_TYPE_ROLLING_FILE: AppenderType
APPENDER_TYPE_SYSLOG: AppenderType
APPENDER_TYPE_NETWORK: AppenderType
APPENDER_TYPE_DATABASE: AppenderType
