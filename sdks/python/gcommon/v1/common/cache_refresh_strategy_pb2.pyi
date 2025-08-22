from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CacheRefreshStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CACHE_REFRESH_STRATEGY_UNSPECIFIED: _ClassVar[CacheRefreshStrategy]
    CACHE_REFRESH_STRATEGY_TTL: _ClassVar[CacheRefreshStrategy]
    CACHE_REFRESH_STRATEGY_LAZY: _ClassVar[CacheRefreshStrategy]
    CACHE_REFRESH_STRATEGY_PROACTIVE: _ClassVar[CacheRefreshStrategy]
    CACHE_REFRESH_STRATEGY_BACKGROUND: _ClassVar[CacheRefreshStrategy]
CACHE_REFRESH_STRATEGY_UNSPECIFIED: CacheRefreshStrategy
CACHE_REFRESH_STRATEGY_TTL: CacheRefreshStrategy
CACHE_REFRESH_STRATEGY_LAZY: CacheRefreshStrategy
CACHE_REFRESH_STRATEGY_PROACTIVE: CacheRefreshStrategy
CACHE_REFRESH_STRATEGY_BACKGROUND: CacheRefreshStrategy
