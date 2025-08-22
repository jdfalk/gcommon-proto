from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.database import query_stats_pb2 as _query_stats_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryRowResponse(_message.Message):
    __slots__ = ("found", "columns", "values", "stats", "error")
    FOUND_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    found: bool
    columns: _containers.RepeatedScalarFieldContainer[str]
    values: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    stats: _query_stats_pb2.DatabaseQueryStats
    error: _error_pb2.Error
    def __init__(self, found: bool = ..., columns: _Optional[_Iterable[str]] = ..., values: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., stats: _Optional[_Union[_query_stats_pb2.DatabaseQueryStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
