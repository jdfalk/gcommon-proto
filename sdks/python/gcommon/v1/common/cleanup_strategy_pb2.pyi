from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CleanupStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLEANUP_STRATEGY_UNSPECIFIED: _ClassVar[CleanupStrategy]
    CLEANUP_STRATEGY_IMMEDIATE: _ClassVar[CleanupStrategy]
    CLEANUP_STRATEGY_GRACEFUL: _ClassVar[CleanupStrategy]
    CLEANUP_STRATEGY_BACKGROUND: _ClassVar[CleanupStrategy]
    CLEANUP_STRATEGY_SCHEDULED: _ClassVar[CleanupStrategy]
CLEANUP_STRATEGY_UNSPECIFIED: CleanupStrategy
CLEANUP_STRATEGY_IMMEDIATE: CleanupStrategy
CLEANUP_STRATEGY_GRACEFUL: CleanupStrategy
CLEANUP_STRATEGY_BACKGROUND: CleanupStrategy
CLEANUP_STRATEGY_SCHEDULED: CleanupStrategy
