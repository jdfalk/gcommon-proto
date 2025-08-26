from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheStats(_message.Message):
    __slots__ = ("total_items", "cache_hits", "cache_misses", "hit_ratio", "memory_usage", "memory_limit", "evicted_items", "expired_items", "avg_access_time_ms", "last_reset", "uptime_seconds")
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
    HIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EVICTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    AVG_ACCESS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_RESET_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    total_items: int
    cache_hits: int
    cache_misses: int
    hit_ratio: float
    memory_usage: int
    memory_limit: int
    evicted_items: int
    expired_items: int
    avg_access_time_ms: float
    last_reset: _timestamp_pb2.Timestamp
    uptime_seconds: int
    def __init__(self, total_items: _Optional[int] = ..., cache_hits: _Optional[int] = ..., cache_misses: _Optional[int] = ..., hit_ratio: _Optional[float] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., evicted_items: _Optional[int] = ..., expired_items: _Optional[int] = ..., avg_access_time_ms: _Optional[float] = ..., last_reset: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uptime_seconds: _Optional[int] = ...) -> None: ...
