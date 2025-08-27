from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConflictStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFLICT_STRATEGY_UNSPECIFIED: _ClassVar[ConflictStrategy]
    CONFLICT_STRATEGY_TIMESTAMP: _ClassVar[ConflictStrategy]
    CONFLICT_STRATEGY_VECTOR_CLOCK: _ClassVar[ConflictStrategy]
    CONFLICT_STRATEGY_CAUSAL: _ClassVar[ConflictStrategy]

CONFLICT_STRATEGY_UNSPECIFIED: ConflictStrategy
CONFLICT_STRATEGY_TIMESTAMP: ConflictStrategy
CONFLICT_STRATEGY_VECTOR_CLOCK: ConflictStrategy
CONFLICT_STRATEGY_CAUSAL: ConflictStrategy
