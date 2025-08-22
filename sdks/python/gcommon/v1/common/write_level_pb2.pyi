from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WriteLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WRITE_LEVEL_UNSPECIFIED: _ClassVar[WriteLevel]
    WRITE_LEVEL_ASYNC: _ClassVar[WriteLevel]
    WRITE_LEVEL_SYNC_ONE: _ClassVar[WriteLevel]
    WRITE_LEVEL_SYNC_QUORUM: _ClassVar[WriteLevel]
    WRITE_LEVEL_SYNC_ALL: _ClassVar[WriteLevel]
WRITE_LEVEL_UNSPECIFIED: WriteLevel
WRITE_LEVEL_ASYNC: WriteLevel
WRITE_LEVEL_SYNC_ONE: WriteLevel
WRITE_LEVEL_SYNC_QUORUM: WriteLevel
WRITE_LEVEL_SYNC_ALL: WriteLevel
