from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_STATUS_UNSPECIFIED: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_ACTIVE: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_INACTIVE: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_PENDING: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_DELETED: _ClassVar[ResourceStatus]
    RESOURCE_STATUS_ERROR: _ClassVar[ResourceStatus]

RESOURCE_STATUS_UNSPECIFIED: ResourceStatus
RESOURCE_STATUS_ACTIVE: ResourceStatus
RESOURCE_STATUS_INACTIVE: ResourceStatus
RESOURCE_STATUS_PENDING: ResourceStatus
RESOURCE_STATUS_DELETED: ResourceStatus
RESOURCE_STATUS_ERROR: ResourceStatus
