from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuditLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_LEVEL_UNSPECIFIED: _ClassVar[AuditLevel]
    AUDIT_LEVEL_NONE: _ClassVar[AuditLevel]
    AUDIT_LEVEL_MINIMAL: _ClassVar[AuditLevel]
    AUDIT_LEVEL_STANDARD: _ClassVar[AuditLevel]
    AUDIT_LEVEL_DETAILED: _ClassVar[AuditLevel]
    AUDIT_LEVEL_VERBOSE: _ClassVar[AuditLevel]
AUDIT_LEVEL_UNSPECIFIED: AuditLevel
AUDIT_LEVEL_NONE: AuditLevel
AUDIT_LEVEL_MINIMAL: AuditLevel
AUDIT_LEVEL_STANDARD: AuditLevel
AUDIT_LEVEL_DETAILED: AuditLevel
AUDIT_LEVEL_VERBOSE: AuditLevel
