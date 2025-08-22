from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFFSET_TYPE_UNSPECIFIED: _ClassVar[OffsetType]
    OFFSET_TYPE_EARLIEST: _ClassVar[OffsetType]
    OFFSET_TYPE_LATEST: _ClassVar[OffsetType]
    OFFSET_TYPE_CURRENT: _ClassVar[OffsetType]
    OFFSET_TYPE_COMMITTED: _ClassVar[OffsetType]
OFFSET_TYPE_UNSPECIFIED: OffsetType
OFFSET_TYPE_EARLIEST: OffsetType
OFFSET_TYPE_LATEST: OffsetType
OFFSET_TYPE_CURRENT: OffsetType
OFFSET_TYPE_COMMITTED: OffsetType
