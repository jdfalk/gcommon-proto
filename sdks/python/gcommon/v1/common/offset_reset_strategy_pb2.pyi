from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetResetStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFFSET_RESET_STRATEGY_UNSPECIFIED: _ClassVar[OffsetResetStrategy]
    OFFSET_RESET_STRATEGY_EARLIEST: _ClassVar[OffsetResetStrategy]
    OFFSET_RESET_STRATEGY_LATEST: _ClassVar[OffsetResetStrategy]
    OFFSET_RESET_STRATEGY_NONE: _ClassVar[OffsetResetStrategy]
    OFFSET_RESET_STRATEGY_TIMESTAMP: _ClassVar[OffsetResetStrategy]

OFFSET_RESET_STRATEGY_UNSPECIFIED: OffsetResetStrategy
OFFSET_RESET_STRATEGY_EARLIEST: OffsetResetStrategy
OFFSET_RESET_STRATEGY_LATEST: OffsetResetStrategy
OFFSET_RESET_STRATEGY_NONE: OffsetResetStrategy
OFFSET_RESET_STRATEGY_TIMESTAMP: OffsetResetStrategy
