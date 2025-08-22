from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResolutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOLUTION_STRATEGY_UNSPECIFIED: _ClassVar[ResolutionStrategy]
    RESOLUTION_STRATEGY_LAST_WRITER_WINS: _ClassVar[ResolutionStrategy]
    RESOLUTION_STRATEGY_FIRST_WRITER_WINS: _ClassVar[ResolutionStrategy]
    RESOLUTION_STRATEGY_MERGE: _ClassVar[ResolutionStrategy]
    RESOLUTION_STRATEGY_CUSTOM: _ClassVar[ResolutionStrategy]
    RESOLUTION_STRATEGY_MULTI_VALUE: _ClassVar[ResolutionStrategy]
RESOLUTION_STRATEGY_UNSPECIFIED: ResolutionStrategy
RESOLUTION_STRATEGY_LAST_WRITER_WINS: ResolutionStrategy
RESOLUTION_STRATEGY_FIRST_WRITER_WINS: ResolutionStrategy
RESOLUTION_STRATEGY_MERGE: ResolutionStrategy
RESOLUTION_STRATEGY_CUSTOM: ResolutionStrategy
RESOLUTION_STRATEGY_MULTI_VALUE: ResolutionStrategy
