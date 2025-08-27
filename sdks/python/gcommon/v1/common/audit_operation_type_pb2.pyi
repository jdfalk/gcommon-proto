from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuditOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_OPERATION_TYPE_UNSPECIFIED: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_CREATE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_UPDATE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_DELETE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_BULK_CREATE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_BULK_UPDATE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_BULK_DELETE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_IMPORT: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_EXPORT: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_BACKUP: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_RESTORE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_ROLLBACK: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_VALIDATE: _ClassVar[AuditOperationType]
    AUDIT_OPERATION_TYPE_SYNC: _ClassVar[AuditOperationType]

AUDIT_OPERATION_TYPE_UNSPECIFIED: AuditOperationType
AUDIT_OPERATION_TYPE_CREATE: AuditOperationType
AUDIT_OPERATION_TYPE_UPDATE: AuditOperationType
AUDIT_OPERATION_TYPE_DELETE: AuditOperationType
AUDIT_OPERATION_TYPE_BULK_CREATE: AuditOperationType
AUDIT_OPERATION_TYPE_BULK_UPDATE: AuditOperationType
AUDIT_OPERATION_TYPE_BULK_DELETE: AuditOperationType
AUDIT_OPERATION_TYPE_IMPORT: AuditOperationType
AUDIT_OPERATION_TYPE_EXPORT: AuditOperationType
AUDIT_OPERATION_TYPE_BACKUP: AuditOperationType
AUDIT_OPERATION_TYPE_RESTORE: AuditOperationType
AUDIT_OPERATION_TYPE_ROLLBACK: AuditOperationType
AUDIT_OPERATION_TYPE_VALIDATE: AuditOperationType
AUDIT_OPERATION_TYPE_SYNC: AuditOperationType
