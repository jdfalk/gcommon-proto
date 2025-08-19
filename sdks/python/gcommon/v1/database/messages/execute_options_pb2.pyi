from gcommon.v1.database.enums import isolation_level_pb2 as _isolation_level_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteOptions(_message.Message):
    __slots__ = ("timeout", "return_generated_keys", "isolation")
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETURN_GENERATED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_FIELD_NUMBER: _ClassVar[int]
    timeout: _duration_pb2.Duration
    return_generated_keys: bool
    isolation: _isolation_level_pb2.DatabaseIsolationLevel
    def __init__(self, timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., return_generated_keys: bool = ..., isolation: _Optional[_Union[_isolation_level_pb2.DatabaseIsolationLevel, str]] = ...) -> None: ...
