from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetadataStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METADATA_STATUS_UNSPECIFIED: _ClassVar[MetadataStatus]
    METADATA_STATUS_ACTIVE: _ClassVar[MetadataStatus]
    METADATA_STATUS_INACTIVE: _ClassVar[MetadataStatus]
    METADATA_STATUS_DRAFT: _ClassVar[MetadataStatus]
    METADATA_STATUS_DEPRECATED: _ClassVar[MetadataStatus]
    METADATA_STATUS_DELETED: _ClassVar[MetadataStatus]
    METADATA_STATUS_ERROR: _ClassVar[MetadataStatus]

METADATA_STATUS_UNSPECIFIED: MetadataStatus
METADATA_STATUS_ACTIVE: MetadataStatus
METADATA_STATUS_INACTIVE: MetadataStatus
METADATA_STATUS_DRAFT: MetadataStatus
METADATA_STATUS_DEPRECATED: MetadataStatus
METADATA_STATUS_DELETED: MetadataStatus
METADATA_STATUS_ERROR: MetadataStatus
