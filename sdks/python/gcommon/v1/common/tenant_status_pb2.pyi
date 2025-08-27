from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TenantStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TENANT_STATUS_UNSPECIFIED: _ClassVar[TenantStatus]
    TENANT_STATUS_ACTIVE: _ClassVar[TenantStatus]
    TENANT_STATUS_INACTIVE: _ClassVar[TenantStatus]
    TENANT_STATUS_SUSPENDED: _ClassVar[TenantStatus]
    TENANT_STATUS_PENDING: _ClassVar[TenantStatus]
    TENANT_STATUS_QUOTA_EXCEEDED: _ClassVar[TenantStatus]
    TENANT_STATUS_TRIAL: _ClassVar[TenantStatus]
    TENANT_STATUS_ARCHIVED: _ClassVar[TenantStatus]
    TENANT_STATUS_DELETED: _ClassVar[TenantStatus]

TENANT_STATUS_UNSPECIFIED: TenantStatus
TENANT_STATUS_ACTIVE: TenantStatus
TENANT_STATUS_INACTIVE: TenantStatus
TENANT_STATUS_SUSPENDED: TenantStatus
TENANT_STATUS_PENDING: TenantStatus
TENANT_STATUS_QUOTA_EXCEEDED: TenantStatus
TENANT_STATUS_TRIAL: TenantStatus
TENANT_STATUS_ARCHIVED: TenantStatus
TENANT_STATUS_DELETED: TenantStatus
