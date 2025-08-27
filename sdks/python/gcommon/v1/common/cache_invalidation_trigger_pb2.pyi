from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CacheInvalidationTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CACHE_INVALIDATION_TRIGGER_UNSPECIFIED: _ClassVar[CacheInvalidationTrigger]
    CACHE_INVALIDATION_TRIGGER_CHANGE: _ClassVar[CacheInvalidationTrigger]
    CACHE_INVALIDATION_TRIGGER_DELETE: _ClassVar[CacheInvalidationTrigger]
    CACHE_INVALIDATION_TRIGGER_EXPIRE: _ClassVar[CacheInvalidationTrigger]
    CACHE_INVALIDATION_TRIGGER_MANUAL: _ClassVar[CacheInvalidationTrigger]
    CACHE_INVALIDATION_TRIGGER_SCHEDULE: _ClassVar[CacheInvalidationTrigger]

CACHE_INVALIDATION_TRIGGER_UNSPECIFIED: CacheInvalidationTrigger
CACHE_INVALIDATION_TRIGGER_CHANGE: CacheInvalidationTrigger
CACHE_INVALIDATION_TRIGGER_DELETE: CacheInvalidationTrigger
CACHE_INVALIDATION_TRIGGER_EXPIRE: CacheInvalidationTrigger
CACHE_INVALIDATION_TRIGGER_MANUAL: CacheInvalidationTrigger
CACHE_INVALIDATION_TRIGGER_SCHEDULE: CacheInvalidationTrigger
