from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsQueryStats(_message.Message):
    __slots__ = ("total_queries", "avg_execution_time_ms", "failed_queries", "cache_hit_rate")
    TOTAL_QUERIES_FIELD_NUMBER: _ClassVar[int]
    AVG_EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FAILED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_RATE_FIELD_NUMBER: _ClassVar[int]
    total_queries: int
    avg_execution_time_ms: float
    failed_queries: int
    cache_hit_rate: float
    def __init__(self, total_queries: _Optional[int] = ..., avg_execution_time_ms: _Optional[float] = ..., failed_queries: _Optional[int] = ..., cache_hit_rate: _Optional[float] = ...) -> None: ...
