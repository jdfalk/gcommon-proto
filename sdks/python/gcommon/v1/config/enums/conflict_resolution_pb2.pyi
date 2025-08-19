from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigConflictResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFLICT_RESOLUTION_UNSPECIFIED: _ClassVar[ConfigConflictResolution]
    CONFLICT_RESOLUTION_SOURCE_WINS: _ClassVar[ConfigConflictResolution]
    CONFLICT_RESOLUTION_TARGET_WINS: _ClassVar[ConfigConflictResolution]
    CONFLICT_RESOLUTION_MERGE: _ClassVar[ConfigConflictResolution]
    CONFLICT_RESOLUTION_MANUAL: _ClassVar[ConfigConflictResolution]
    CONFLICT_RESOLUTION_TIMESTAMP: _ClassVar[ConfigConflictResolution]
CONFLICT_RESOLUTION_UNSPECIFIED: ConfigConflictResolution
CONFLICT_RESOLUTION_SOURCE_WINS: ConfigConflictResolution
CONFLICT_RESOLUTION_TARGET_WINS: ConfigConflictResolution
CONFLICT_RESOLUTION_MERGE: ConfigConflictResolution
CONFLICT_RESOLUTION_MANUAL: ConfigConflictResolution
CONFLICT_RESOLUTION_TIMESTAMP: ConfigConflictResolution
