from gcommon.v1.common import log_level_pb2 as _log_level_pb2
from gcommon.v1.common import appender_config_pb2 as _appender_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoggerConfig(_message.Message):
    __slots__ = ("level", "appenders", "inherit_appenders", "propagate", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    APPENDERS_FIELD_NUMBER: _ClassVar[int]
    INHERIT_APPENDERS_FIELD_NUMBER: _ClassVar[int]
    PROPAGATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    level: _log_level_pb2.LogLevel
    appenders: _containers.RepeatedCompositeFieldContainer[_appender_config_pb2.AppenderConfig]
    inherit_appenders: bool
    propagate: bool
    properties: _containers.ScalarMap[str, str]
    def __init__(self, level: _Optional[_Union[_log_level_pb2.LogLevel, str]] = ..., appenders: _Optional[_Iterable[_Union[_appender_config_pb2.AppenderConfig, _Mapping]]] = ..., inherit_appenders: bool = ..., propagate: bool = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...
