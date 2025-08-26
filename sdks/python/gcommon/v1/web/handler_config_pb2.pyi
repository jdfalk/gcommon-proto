from gcommon.v1.common import handler_type_pb2 as _handler_type_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HandlerConfig(_message.Message):
    __slots__ = ("type", "config", "target", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    type: _handler_type_pb2.HandlerType
    config: _any_pb2.Any
    target: str
    options: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_handler_type_pb2.HandlerType, str]] = ..., config: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., target: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
