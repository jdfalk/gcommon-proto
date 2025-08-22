from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OrderingLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDERING_LEVEL_UNSPECIFIED: _ClassVar[OrderingLevel]
    ORDERING_LEVEL_NONE: _ClassVar[OrderingLevel]
    ORDERING_LEVEL_PARTIAL: _ClassVar[OrderingLevel]
    ORDERING_LEVEL_TOTAL: _ClassVar[OrderingLevel]
ORDERING_LEVEL_UNSPECIFIED: OrderingLevel
ORDERING_LEVEL_NONE: OrderingLevel
ORDERING_LEVEL_PARTIAL: OrderingLevel
ORDERING_LEVEL_TOTAL: OrderingLevel
