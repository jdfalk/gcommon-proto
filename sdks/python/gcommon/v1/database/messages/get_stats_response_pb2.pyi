from gcommon.v1.common.messages import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheGetStatsResponse(_message.Message):
    __slots__ = ("total_items", "cache_hits", "cache_misses", "hit_ratio", "memory_usage", "memory_limit", "evicted_items", "success", "error")
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
    HIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EVICTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    total_items: int
    cache_hits: int
    cache_misses: int
    hit_ratio: float
    memory_usage: int
    memory_limit: int
    evicted_items: int
    success: bool
    error: _error_pb2.Error
    def __init__(self, total_items: _Optional[int] = ..., cache_hits: _Optional[int] = ..., cache_misses: _Optional[int] = ..., hit_ratio: _Optional[float] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., evicted_items: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
