from gcommon.v1.common import hook_error_handling_pb2 as _hook_error_handling_pb2
from gcommon.v1.common import hook_type_pb2 as _hook_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateHook(_message.Message):
    __slots__ = ("name", "type", "command", "timeout_seconds", "working_directory", "environment", "conditions", "error_handling")
    class EnvironmentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ConditionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_HANDLING_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _hook_type_pb2.HookType
    command: str
    timeout_seconds: int
    working_directory: str
    environment: _containers.ScalarMap[str, str]
    conditions: _containers.ScalarMap[str, str]
    error_handling: _hook_error_handling_pb2.HookErrorHandling
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_hook_type_pb2.HookType, str]] = ..., command: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., working_directory: _Optional[str] = ..., environment: _Optional[_Mapping[str, str]] = ..., conditions: _Optional[_Mapping[str, str]] = ..., error_handling: _Optional[_Union[_hook_error_handling_pb2.HookErrorHandling, str]] = ...) -> None: ...
