import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NamespaceStats(_message.Message):
    __slots__ = ("total_keys", "memory_usage_bytes", "hit_rate_percent", "cache_hits", "cache_misses", "evictions", "avg_key_size_bytes", "avg_value_size_bytes", "last_access_time")
    TOTAL_KEYS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HIT_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
    EVICTIONS_FIELD_NUMBER: _ClassVar[int]
    AVG_KEY_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVG_VALUE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    total_keys: int
    memory_usage_bytes: int
    hit_rate_percent: float
    cache_hits: int
    cache_misses: int
    evictions: int
    avg_key_size_bytes: float
    avg_value_size_bytes: float
    last_access_time: _timestamp_pb2.Timestamp
    def __init__(self, total_keys: _Optional[int] = ..., memory_usage_bytes: _Optional[int] = ..., hit_rate_percent: _Optional[float] = ..., cache_hits: _Optional[int] = ..., cache_misses: _Optional[int] = ..., evictions: _Optional[int] = ..., avg_key_size_bytes: _Optional[float] = ..., avg_value_size_bytes: _Optional[float] = ..., last_access_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
