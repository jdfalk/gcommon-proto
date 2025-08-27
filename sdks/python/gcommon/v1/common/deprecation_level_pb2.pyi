from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeprecationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPRECATION_LEVEL_UNSPECIFIED: _ClassVar[DeprecationLevel]
    DEPRECATION_LEVEL_SOFT: _ClassVar[DeprecationLevel]
    DEPRECATION_LEVEL_HARD: _ClassVar[DeprecationLevel]
    DEPRECATION_LEVEL_REMOVAL: _ClassVar[DeprecationLevel]

DEPRECATION_LEVEL_UNSPECIFIED: DeprecationLevel
DEPRECATION_LEVEL_SOFT: DeprecationLevel
DEPRECATION_LEVEL_HARD: DeprecationLevel
DEPRECATION_LEVEL_REMOVAL: DeprecationLevel
