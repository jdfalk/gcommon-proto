from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import query_stats_pb2 as _query_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsGetStatsResponse(_message.Message):
    __slots__ = ("stats", "error")
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    stats: _query_stats_pb2.MetricsQueryStats
    error: _error_pb2.Error
    def __init__(self, stats: _Optional[_Union[_query_stats_pb2.MetricsQueryStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
