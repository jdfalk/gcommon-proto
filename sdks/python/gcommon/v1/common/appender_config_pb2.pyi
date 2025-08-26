from gcommon.v1.common import appender_type_pb2 as _appender_type_pb2
from gcommon.v1.common import formatter_type_pb2 as _formatter_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppenderConfig(_message.Message):
    __slots__ = ("name", "type", "output", "formatter", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutputConfig(_message.Message):
        __slots__ = ("target", "options")
        class OptionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TARGET_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        target: str
        options: _containers.ScalarMap[str, str]
        def __init__(self, target: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class LogFormatterConfig(_message.Message):
        __slots__ = ("type", "pattern")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PATTERN_FIELD_NUMBER: _ClassVar[int]
        type: _formatter_type_pb2.FormatterType
        pattern: str
        def __init__(self, type: _Optional[_Union[_formatter_type_pb2.FormatterType, str]] = ..., pattern: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _appender_type_pb2.AppenderType
    output: AppenderConfig.OutputConfig
    formatter: AppenderConfig.LogFormatterConfig
    properties: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_appender_type_pb2.AppenderType, str]] = ..., output: _Optional[_Union[AppenderConfig.OutputConfig, _Mapping]] = ..., formatter: _Optional[_Union[AppenderConfig.LogFormatterConfig, _Mapping]] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...
