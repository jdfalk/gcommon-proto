from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CacheStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CACHE_STRATEGY_UNSPECIFIED: _ClassVar[CacheStrategy]
    CACHE_STRATEGY_NONE: _ClassVar[CacheStrategy]
    CACHE_STRATEGY_MEMORY: _ClassVar[CacheStrategy]
    CACHE_STRATEGY_DISTRIBUTED: _ClassVar[CacheStrategy]
    CACHE_STRATEGY_CDN: _ClassVar[CacheStrategy]
CACHE_STRATEGY_UNSPECIFIED: CacheStrategy
CACHE_STRATEGY_NONE: CacheStrategy
CACHE_STRATEGY_MEMORY: CacheStrategy
CACHE_STRATEGY_DISTRIBUTED: CacheStrategy
CACHE_STRATEGY_CDN: CacheStrategy
