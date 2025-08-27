from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PriorityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUE_PRIORITY_LEVEL_UNSPECIFIED: _ClassVar[PriorityLevel]
    QUEUE_PRIORITY_LEVEL_LOW: _ClassVar[PriorityLevel]
    QUEUE_PRIORITY_LEVEL_MEDIUM: _ClassVar[PriorityLevel]
    QUEUE_PRIORITY_LEVEL_HIGH: _ClassVar[PriorityLevel]
    QUEUE_PRIORITY_LEVEL_CRITICAL: _ClassVar[PriorityLevel]

QUEUE_PRIORITY_LEVEL_UNSPECIFIED: PriorityLevel
QUEUE_PRIORITY_LEVEL_LOW: PriorityLevel
QUEUE_PRIORITY_LEVEL_MEDIUM: PriorityLevel
QUEUE_PRIORITY_LEVEL_HIGH: PriorityLevel
QUEUE_PRIORITY_LEVEL_CRITICAL: PriorityLevel
