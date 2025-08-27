from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.database import query_stats_pb2 as _query_stats_pb2
from gcommon.v1.database import result_set_pb2 as _result_set_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryResponse(_message.Message):
    __slots__ = ("result_set", "stats", "error")
    RESULT_SET_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result_set: _result_set_pb2.ResultSet
    stats: _query_stats_pb2.DatabaseQueryStats
    error: _error_pb2.Error
    def __init__(self, result_set: _Optional[_Union[_result_set_pb2.ResultSet, _Mapping]] = ..., stats: _Optional[_Union[_query_stats_pb2.DatabaseQueryStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
