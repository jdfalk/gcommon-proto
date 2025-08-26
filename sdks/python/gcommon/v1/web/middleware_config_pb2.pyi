from gcommon.v1.common import middleware_type_pb2 as _middleware_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MiddlewareConfig(_message.Message):
    __slots__ = ("type", "enabled", "priority", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    type: _middleware_type_pb2.MiddlewareType
    enabled: bool
    priority: int
    options: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_middleware_type_pb2.MiddlewareType, str]] = ..., enabled: _Optional[bool] = ..., priority: _Optional[int] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...
