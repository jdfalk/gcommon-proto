import datetime

from gcommon.v1.common import cache_policy_pb2 as _cache_policy_pb2
from gcommon.v1.common import cache_strategy_pb2 as _cache_strategy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebCacheConfig(_message.Message):
    __slots__ = ("strategy", "policy", "ttl", "enabled", "cache_name")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CACHE_NAME_FIELD_NUMBER: _ClassVar[int]
    strategy: _cache_strategy_pb2.CacheStrategy
    policy: _cache_policy_pb2.CachePolicy
    ttl: _duration_pb2.Duration
    enabled: bool
    cache_name: str
    def __init__(self, strategy: _Optional[_Union[_cache_strategy_pb2.CacheStrategy, str]] = ..., policy: _Optional[_Union[_cache_policy_pb2.CachePolicy, _Mapping]] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., enabled: _Optional[bool] = ..., cache_name: _Optional[str] = ...) -> None: ...
