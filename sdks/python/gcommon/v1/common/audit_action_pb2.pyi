from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuditAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_ACTION_UNSPECIFIED: _ClassVar[AuditAction]
    AUDIT_ACTION_LOGIN: _ClassVar[AuditAction]
    AUDIT_ACTION_LOGOUT: _ClassVar[AuditAction]
    AUDIT_ACTION_LOGIN_FAILED: _ClassVar[AuditAction]
    AUDIT_ACTION_ACCESS_GRANTED: _ClassVar[AuditAction]
    AUDIT_ACTION_ACCESS_DENIED: _ClassVar[AuditAction]
    AUDIT_ACTION_USER_CREATED: _ClassVar[AuditAction]
    AUDIT_ACTION_USER_UPDATED: _ClassVar[AuditAction]
    AUDIT_ACTION_USER_DELETED: _ClassVar[AuditAction]
    AUDIT_ACTION_USER_SUSPENDED: _ClassVar[AuditAction]
    AUDIT_ACTION_ROLE_ASSIGNED: _ClassVar[AuditAction]
    AUDIT_ACTION_ROLE_REMOVED: _ClassVar[AuditAction]
    AUDIT_ACTION_ROLE_CREATED: _ClassVar[AuditAction]
    AUDIT_ACTION_ROLE_UPDATED: _ClassVar[AuditAction]
    AUDIT_ACTION_ROLE_DELETED: _ClassVar[AuditAction]
    AUDIT_ACTION_PERMISSION_GRANTED: _ClassVar[AuditAction]
    AUDIT_ACTION_PERMISSION_REVOKED: _ClassVar[AuditAction]
    AUDIT_ACTION_SESSION_CREATED: _ClassVar[AuditAction]
    AUDIT_ACTION_SESSION_TERMINATED: _ClassVar[AuditAction]
    AUDIT_ACTION_CONFIG_UPDATED: _ClassVar[AuditAction]
    AUDIT_ACTION_SYSTEM_BACKUP: _ClassVar[AuditAction]
    AUDIT_ACTION_SYSTEM_RESTORE: _ClassVar[AuditAction]

AUDIT_ACTION_UNSPECIFIED: AuditAction
AUDIT_ACTION_LOGIN: AuditAction
AUDIT_ACTION_LOGOUT: AuditAction
AUDIT_ACTION_LOGIN_FAILED: AuditAction
AUDIT_ACTION_ACCESS_GRANTED: AuditAction
AUDIT_ACTION_ACCESS_DENIED: AuditAction
AUDIT_ACTION_USER_CREATED: AuditAction
AUDIT_ACTION_USER_UPDATED: AuditAction
AUDIT_ACTION_USER_DELETED: AuditAction
AUDIT_ACTION_USER_SUSPENDED: AuditAction
AUDIT_ACTION_ROLE_ASSIGNED: AuditAction
AUDIT_ACTION_ROLE_REMOVED: AuditAction
AUDIT_ACTION_ROLE_CREATED: AuditAction
AUDIT_ACTION_ROLE_UPDATED: AuditAction
AUDIT_ACTION_ROLE_DELETED: AuditAction
AUDIT_ACTION_PERMISSION_GRANTED: AuditAction
AUDIT_ACTION_PERMISSION_REVOKED: AuditAction
AUDIT_ACTION_SESSION_CREATED: AuditAction
AUDIT_ACTION_SESSION_TERMINATED: AuditAction
AUDIT_ACTION_CONFIG_UPDATED: AuditAction
AUDIT_ACTION_SYSTEM_BACKUP: AuditAction
AUDIT_ACTION_SYSTEM_RESTORE: AuditAction
