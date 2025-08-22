from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuditResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_RESULT_UNSPECIFIED: _ClassVar[AuditResult]
    AUDIT_RESULT_SUCCESS: _ClassVar[AuditResult]
    AUDIT_RESULT_FAILURE: _ClassVar[AuditResult]
    AUDIT_RESULT_PARTIAL: _ClassVar[AuditResult]
AUDIT_RESULT_UNSPECIFIED: AuditResult
AUDIT_RESULT_SUCCESS: AuditResult
AUDIT_RESULT_FAILURE: AuditResult
AUDIT_RESULT_PARTIAL: AuditResult
