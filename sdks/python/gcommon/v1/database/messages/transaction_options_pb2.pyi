from gcommon.v1.database.enums import isolation_level_pb2 as _isolation_level_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionOptions(_message.Message):
    __slots__ = ("isolation", "timeout", "read_only")
    ISOLATION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    isolation: _isolation_level_pb2.DatabaseIsolationLevel
    timeout: _duration_pb2.Duration
    read_only: bool
    def __init__(self, isolation: _Optional[_Union[_isolation_level_pb2.DatabaseIsolationLevel, str]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., read_only: bool = ...) -> None: ...
