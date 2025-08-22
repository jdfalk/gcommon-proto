from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BackoffStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKOFF_STRATEGY_UNSPECIFIED: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_FIXED: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_LINEAR: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_EXPONENTIAL: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_CUSTOM: _ClassVar[BackoffStrategy]
BACKOFF_STRATEGY_UNSPECIFIED: BackoffStrategy
BACKOFF_STRATEGY_FIXED: BackoffStrategy
BACKOFF_STRATEGY_LINEAR: BackoffStrategy
BACKOFF_STRATEGY_EXPONENTIAL: BackoffStrategy
BACKOFF_STRATEGY_CUSTOM: BackoffStrategy
