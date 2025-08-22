from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConflictResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMON_CONFLICT_RESOLUTION_UNSPECIFIED: _ClassVar[ConflictResolution]
    COMMON_CONFLICT_RESOLUTION_MERGE: _ClassVar[ConflictResolution]
    COMMON_CONFLICT_RESOLUTION_OVERWRITE: _ClassVar[ConflictResolution]
    COMMON_CONFLICT_RESOLUTION_FAIL: _ClassVar[ConflictResolution]
COMMON_CONFLICT_RESOLUTION_UNSPECIFIED: ConflictResolution
COMMON_CONFLICT_RESOLUTION_MERGE: ConflictResolution
COMMON_CONFLICT_RESOLUTION_OVERWRITE: ConflictResolution
COMMON_CONFLICT_RESOLUTION_FAIL: ConflictResolution
