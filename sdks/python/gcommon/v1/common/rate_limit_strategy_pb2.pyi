from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RateLimitStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RATE_LIMIT_STRATEGY_UNSPECIFIED: _ClassVar[RateLimitStrategy]
    RATE_LIMIT_STRATEGY_TOKEN_BUCKET: _ClassVar[RateLimitStrategy]
    RATE_LIMIT_STRATEGY_FIXED_WINDOW: _ClassVar[RateLimitStrategy]
    RATE_LIMIT_STRATEGY_SLIDING_WINDOW: _ClassVar[RateLimitStrategy]
    RATE_LIMIT_STRATEGY_LEAKY_BUCKET: _ClassVar[RateLimitStrategy]
RATE_LIMIT_STRATEGY_UNSPECIFIED: RateLimitStrategy
RATE_LIMIT_STRATEGY_TOKEN_BUCKET: RateLimitStrategy
RATE_LIMIT_STRATEGY_FIXED_WINDOW: RateLimitStrategy
RATE_LIMIT_STRATEGY_SLIDING_WINDOW: RateLimitStrategy
RATE_LIMIT_STRATEGY_LEAKY_BUCKET: RateLimitStrategy
