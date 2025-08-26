import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryStatistics(_message.Message):
    __slots__ = ("execution_time", "data_points_processed", "metrics_examined", "series_returned", "memory_used_bytes", "storage_backends_used", "cache_hit_rate", "query_time")
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_POINTS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    METRICS_EXAMINED_FIELD_NUMBER: _ClassVar[int]
    SERIES_RETURNED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BACKENDS_USED_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_RATE_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIME_FIELD_NUMBER: _ClassVar[int]
    execution_time: _duration_pb2.Duration
    data_points_processed: int
    metrics_examined: int
    series_returned: int
    memory_used_bytes: int
    storage_backends_used: _containers.RepeatedScalarFieldContainer[str]
    cache_hit_rate: float
    query_time: _timestamp_pb2.Timestamp
    def __init__(self, execution_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., data_points_processed: _Optional[int] = ..., metrics_examined: _Optional[int] = ..., series_returned: _Optional[int] = ..., memory_used_bytes: _Optional[int] = ..., storage_backends_used: _Optional[_Iterable[str]] = ..., cache_hit_rate: _Optional[float] = ..., query_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
