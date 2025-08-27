from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RetryDelayStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RETRY_DELAY_STRATEGY_UNSPECIFIED: _ClassVar[RetryDelayStrategy]
    RETRY_DELAY_STRATEGY_FIXED: _ClassVar[RetryDelayStrategy]
    RETRY_DELAY_STRATEGY_LINEAR: _ClassVar[RetryDelayStrategy]
    RETRY_DELAY_STRATEGY_EXPONENTIAL: _ClassVar[RetryDelayStrategy]
    RETRY_DELAY_STRATEGY_CUSTOM: _ClassVar[RetryDelayStrategy]
RETRY_DELAY_STRATEGY_UNSPECIFIED: RetryDelayStrategy
RETRY_DELAY_STRATEGY_FIXED: RetryDelayStrategy
RETRY_DELAY_STRATEGY_LINEAR: RetryDelayStrategy
RETRY_DELAY_STRATEGY_EXPONENTIAL: RetryDelayStrategy
RETRY_DELAY_STRATEGY_CUSTOM: RetryDelayStrategy
