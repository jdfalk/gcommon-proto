from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BufferOverflowStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUFFER_OVERFLOW_STRATEGY_UNSPECIFIED: _ClassVar[BufferOverflowStrategy]
    BUFFER_OVERFLOW_STRATEGY_DROP_OLDEST: _ClassVar[BufferOverflowStrategy]
    BUFFER_OVERFLOW_STRATEGY_DROP_NEWEST: _ClassVar[BufferOverflowStrategy]
    BUFFER_OVERFLOW_STRATEGY_BLOCK: _ClassVar[BufferOverflowStrategy]
    BUFFER_OVERFLOW_STRATEGY_ERROR: _ClassVar[BufferOverflowStrategy]

BUFFER_OVERFLOW_STRATEGY_UNSPECIFIED: BufferOverflowStrategy
BUFFER_OVERFLOW_STRATEGY_DROP_OLDEST: BufferOverflowStrategy
BUFFER_OVERFLOW_STRATEGY_DROP_NEWEST: BufferOverflowStrategy
BUFFER_OVERFLOW_STRATEGY_BLOCK: BufferOverflowStrategy
BUFFER_OVERFLOW_STRATEGY_ERROR: BufferOverflowStrategy
