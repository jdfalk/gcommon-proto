from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConsistencyValidation(_message.Message):
    __slots__ = ("enabled", "validation_interval_seconds", "validation_scope", "failure_actions", "timeout_ms")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    validation_interval_seconds: int
    validation_scope: str
    failure_actions: _containers.RepeatedScalarFieldContainer[str]
    timeout_ms: int
    def __init__(self, enabled: bool = ..., validation_interval_seconds: _Optional[int] = ..., validation_scope: _Optional[str] = ..., failure_actions: _Optional[_Iterable[str]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
