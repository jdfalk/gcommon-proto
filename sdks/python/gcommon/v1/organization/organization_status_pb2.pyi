from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORGANIZATION_STATUS_UNSPECIFIED: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_ACTIVE: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_INACTIVE: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_SUSPENDED: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_PENDING: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_ARCHIVED: _ClassVar[OrganizationStatus]
    ORGANIZATION_STATUS_DELETED: _ClassVar[OrganizationStatus]
ORGANIZATION_STATUS_UNSPECIFIED: OrganizationStatus
ORGANIZATION_STATUS_ACTIVE: OrganizationStatus
ORGANIZATION_STATUS_INACTIVE: OrganizationStatus
ORGANIZATION_STATUS_SUSPENDED: OrganizationStatus
ORGANIZATION_STATUS_PENDING: OrganizationStatus
ORGANIZATION_STATUS_ARCHIVED: OrganizationStatus
ORGANIZATION_STATUS_DELETED: OrganizationStatus
