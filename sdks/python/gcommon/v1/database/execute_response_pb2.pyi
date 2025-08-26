from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.database import execute_stats_pb2 as _execute_stats_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteResponse(_message.Message):
    __slots__ = ("affected_rows", "generated_keys", "stats", "error")
    AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_KEYS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    affected_rows: int
    generated_keys: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    stats: _execute_stats_pb2.ExecuteStats
    error: _error_pb2.Error
    def __init__(self, affected_rows: _Optional[int] = ..., generated_keys: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., stats: _Optional[_Union[_execute_stats_pb2.ExecuteStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
