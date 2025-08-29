from gcommon.v1.common import appender_type_pb2 as _appender_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.common import output_config_pb2 as _output_config_pb2
from gcommon.v1.common import formatter_config_pb2 as _formatter_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _appender_type_pb2.AppenderType
    output: _output_config_pb2.OutputConfig
    formatter: _formatter_config_pb2.LogFormatterConfig
    properties: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_appender_type_pb2.AppenderType, str]] = ..., output: _Optional[_Union[_output_config_pb2.OutputConfig, _Mapping]] = ..., formatter: _Optional[_Union[_formatter_config_pb2.LogFormatterConfig, _Mapping]] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...
