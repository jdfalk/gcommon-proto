from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ReadLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    READ_LEVEL_UNSPECIFIED: _ClassVar[ReadLevel]
    READ_LEVEL_EVENTUAL: _ClassVar[ReadLevel]
    READ_LEVEL_STRONG: _ClassVar[ReadLevel]
    READ_LEVEL_BOUNDED_STALENESS: _ClassVar[ReadLevel]
    READ_LEVEL_SESSION: _ClassVar[ReadLevel]

READ_LEVEL_UNSPECIFIED: ReadLevel
READ_LEVEL_EVENTUAL: ReadLevel
READ_LEVEL_STRONG: ReadLevel
READ_LEVEL_BOUNDED_STALENESS: ReadLevel
READ_LEVEL_SESSION: ReadLevel
