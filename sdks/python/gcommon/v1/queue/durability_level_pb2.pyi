from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DurabilityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DURABILITY_LEVEL_UNSPECIFIED: _ClassVar[DurabilityLevel]
    DURABILITY_LEVEL_NONE: _ClassVar[DurabilityLevel]
    DURABILITY_LEVEL_MEMORY: _ClassVar[DurabilityLevel]
    DURABILITY_LEVEL_DISK_SYNC: _ClassVar[DurabilityLevel]
    DURABILITY_LEVEL_DISK_ASYNC: _ClassVar[DurabilityLevel]
    DURABILITY_LEVEL_REPLICATED: _ClassVar[DurabilityLevel]
DURABILITY_LEVEL_UNSPECIFIED: DurabilityLevel
DURABILITY_LEVEL_NONE: DurabilityLevel
DURABILITY_LEVEL_MEMORY: DurabilityLevel
DURABILITY_LEVEL_DISK_SYNC: DurabilityLevel
DURABILITY_LEVEL_DISK_ASYNC: DurabilityLevel
DURABILITY_LEVEL_REPLICATED: DurabilityLevel
