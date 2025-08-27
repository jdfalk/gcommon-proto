from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretAuditLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_AUDIT_LEVEL_UNSPECIFIED: _ClassVar[SecretAuditLevel]
    SECRET_AUDIT_LEVEL_NONE: _ClassVar[SecretAuditLevel]
    SECRET_AUDIT_LEVEL_MINIMAL: _ClassVar[SecretAuditLevel]
    SECRET_AUDIT_LEVEL_STANDARD: _ClassVar[SecretAuditLevel]
    SECRET_AUDIT_LEVEL_DETAILED: _ClassVar[SecretAuditLevel]
    SECRET_AUDIT_LEVEL_VERBOSE: _ClassVar[SecretAuditLevel]

SECRET_AUDIT_LEVEL_UNSPECIFIED: SecretAuditLevel
SECRET_AUDIT_LEVEL_NONE: SecretAuditLevel
SECRET_AUDIT_LEVEL_MINIMAL: SecretAuditLevel
SECRET_AUDIT_LEVEL_STANDARD: SecretAuditLevel
SECRET_AUDIT_LEVEL_DETAILED: SecretAuditLevel
SECRET_AUDIT_LEVEL_VERBOSE: SecretAuditLevel
