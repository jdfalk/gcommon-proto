from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorActionConfig(_message.Message):
    __slots__ = ("error_pattern", "action", "action_params")
    class ActionParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ERROR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    error_pattern: str
    action: str
    action_params: _containers.ScalarMap[str, str]
    def __init__(self, error_pattern: _Optional[str] = ..., action: _Optional[str] = ..., action_params: _Optional[_Mapping[str, str]] = ...) -> None: ...
