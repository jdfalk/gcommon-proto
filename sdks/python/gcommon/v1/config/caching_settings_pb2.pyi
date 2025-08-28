from gcommon.v1.common import cache_invalidation_trigger_pb2 as _cache_invalidation_trigger_pb2
from gcommon.v1.common import cache_refresh_strategy_pb2 as _cache_refresh_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CachingSettings(_message.Message):
    __slots__ = ("enabled", "ttl_seconds", "refresh_strategy", "triggers", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ttl_seconds: int
    refresh_strategy: _cache_refresh_strategy_pb2.CacheRefreshStrategy
    triggers: _containers.RepeatedScalarFieldContainer[_cache_invalidation_trigger_pb2.CacheInvalidationTrigger]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., ttl_seconds: _Optional[int] = ..., refresh_strategy: _Optional[_Union[_cache_refresh_strategy_pb2.CacheRefreshStrategy, str]] = ..., triggers: _Optional[_Iterable[_Union[_cache_invalidation_trigger_pb2.CacheInvalidationTrigger, str]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
